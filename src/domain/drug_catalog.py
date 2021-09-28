from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class StagingDrugCatalog:
    drug_id: str
    drug_name: str
    date_mention: str
    publication_id: str
    publication_titile: str
    journal_name: str
    source:str

@dataclass_json
@dataclass
class DrugCatalog:
    drug_id: str
    drug_name: str
    publications: List[StagingDrugCatalog]