import csv
import json
import logging
from domain.publication_detail import PublicationDetail
from domain.drug_catalog import StagingDrugCatalog,DrugCatalog
from domain.drug_detail import DrugDetail
from utils.validation import is_valid_drug_line, is_valid_pub_line
from utils.date_utils import try_parsing_date
from typing import List

logger = logging.getLogger()

def read_pub_from_csv(file:str, source:str)-> List[PublicationDetail]:
    logger.info("read from file " + file)

    with open(file, 'r') as csvfile:
        res = []
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)
        for row in reader:
            if is_valid_pub_line(row):
                pub = PublicationDetail(id=str(row[0]), title=str(row[1]), date=try_parsing_date(row[2]), journal=str(row[3]), source=source)
                res.append(pub)
            else:
                pass
        return res   

def read_pub_from_json(file:str, source:str)-> List[PublicationDetail]:
    pass

def read_drug_from_csv(file:str)-> List[DrugDetail]:
    logger.info("read from file " + file)
    
    with open(file, 'r') as csvfile:
        res = []
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)
        for row in reader:
            if is_valid_drug_line(row):
                drug = DrugDetail(id=str(row[0]), name=str(row[1]))
                res.append(drug)
            else:
                pass
        return res   

def write_staging_catalogs_to_json_file(staging_catalogs: List[StagingDrugCatalog],file:str)-> None:
    logger.info("write staging_catalogs to file " + file)
    
    json_data = StagingDrugCatalog.schema().dumps(staging_catalogs, many=True) 
    with open(file, "w") as f:
        f.write(json_data)      

def write_catalogs_to_json_file(staging_catalogs: List[DrugCatalog],file:str)-> None:
    logger.info("write catalogs to file " + file)
    
    json_data = DrugCatalog.schema().dumps(staging_catalogs, many=True) 
    with open(file, "w") as f:
        f.write(json_data)                 