import logging
import json
from typing import List
from itertools import groupby

from domain.drug_catalog import StagingDrugCatalog, DrugCatalog
from domain.drug_detail import DrugDetail
from domain.publication_detail import PublicationDetail
from infrastructure.repositories import FilePubRepository,FileDrugRepository,FileCatalogRepository
from infrastructure.config import Config
from utils.nltk_helper import get_tokens_from_sentence

logger = logging.getLogger()

def extract_durg_keywords_from_pub(pub:PublicationDetail, drugs:List[DrugDetail]) -> List[DrugDetail]:
    """
    find the list of keywords which are mentioned by the title
    """
    word_tokens = get_tokens_from_sentence(pub.title)
    drugs_mentioned = [w for w in drugs if w.name.lower() in word_tokens]
    return drugs_mentioned  

def key_func(staging:StagingDrugCatalog):
    return (staging.drug_id, staging.drug_name)

def generate_final_catalog(staging_catalogs: List[StagingDrugCatalog]) -> List[DrugCatalog]:
    """
    find the list of keywords which are mentioned by the title
    """
    res = []
    sorted_staging_catalogs = sorted(staging_catalogs, key=key_func)
    for key, value in groupby(sorted_staging_catalogs, key_func):
        pubs = []
        for pub in value:
            pubs.append(pub)
        catalog = DrugCatalog(key[0], key[1], pubs)
        res.append(catalog)
    print(res[0])    
    return res   


class ETLPipeline:
    def __init__(self, config:Config) -> None:
        self.config = config
        self.pub_repo = FilePubRepository(config)
        self.drug_repo = FileDrugRepository(config)
        self.catalog_repo = FileCatalogRepository(config)
        self.drugs_data = []
        self.pub_data = []
        self.staging_catalog_data = []
        self.catalog_data = []

    def _extract(self) -> None:
        self.drugs_data = self.drug_repo.get_by_path_format(self.config.drugs_path, self.config.drugs_format)
        for source in self.config.sources:
            if source == 'pubmed':
                self.pub_data.extend(self.pub_repo.get_by_path_format(self.config.pubmed_path, self.config.pubmed_format, source))
            elif source == 'clinical_trials':
                self.pub_data.extend(self.pub_repo.get_by_path_format(self.config.clinical_trials_path, self.config.clinical_trials_format, source))

    def _enrich(self) -> None:
        for pub in self.pub_data:
            drugs = extract_durg_keywords_from_pub(pub, self.drugs_data)
            for drug in drugs:
                staging_catalog = StagingDrugCatalog(drug.id, drug.name, pub.date, pub.id,pub.title, pub.journal, pub.source)
                self.staging_catalog_data.append(staging_catalog)

        self.catalog_repo.save_to_path(self.staging_catalog_data)

    def _transform(self) -> None:
        self.catalog_data = generate_final_catalog(self.staging_catalog_data)

    def _load(self) -> None:
        self.catalog_repo.save_to_path(self.catalog_data)


    def run(self) -> None:
        self._extract()
        self._enrich()
        self._transform()
        self._load()

        
