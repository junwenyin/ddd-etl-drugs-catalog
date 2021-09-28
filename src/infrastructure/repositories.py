from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from domain.repositories import Repository
from domain.publication_detail import PublicationDetail
from domain.drug_catalog import DrugCatalog, StagingDrugCatalog
from domain.drug_detail import DrugDetail
from infrastructure.config import Config 
from infrastructure.file_handler import read_pub_from_json, read_pub_from_csv, read_drug_from_csv, write_staging_catalogs_to_json_file,write_catalogs_to_json_file




class FilePubRepository(Repository):
    """Class for a gcs repository with CRUD operations"""

    def __init__(self, config:Config) -> None:
        self.config = config
    
    def get_by_path_format(self, path:str, format:str, source:str) -> List[PublicationDetail]:
        if format == 'csv':
            return read_pub_from_csv(path, source)
        elif format == 'json':
            return read_pub_from_json(path, source)
        else:
            raise Exception("invalid format")


class AzurePubRepository(Repository):
    """Class for a Azure repository with CRUD operations"""

    def __init__(self, az_client) -> None:
        pass
    
    def get_by_path_format(self, source:str, path:str, format:str) -> List[PublicationDetail]:
        pass

class FileDrugRepository(Repository):
    """Class for file drugs repository with CRUD operations"""

    def __init__(self, config:Config) -> None:
        self.config = config
    
    def get_by_path_format(self, path:str, format:str) -> List[DrugDetail]:
        if format == 'csv':
            return read_drug_from_csv(path)
        else:
            raise Exception("invalid format")

class FileStagingCatalogRepository(Repository):
    """Class for file catalog repository with CRUD operations"""

    def __init__(self, config:Config) -> None:
        self.config = config
    
    def save_to_path(self,  data: List[StagingDrugCatalog]) -> None:
        write_staging_catalogs_to_json_file(data, self.config.staging_catalog_path)

class FileCatalogRepository(Repository):
    """Class for file catalog repository with CRUD operations"""

    def __init__(self, config:Config) -> None:
        self.config = config
    
    def save_to_path(self,  data: List[DrugCatalog]) -> None:
        write_catalogs_to_json_file(data, self.config.catalog_path)        