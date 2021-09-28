from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class PublicationDetail:
    id: str
    title: str
    date: str
    journal: str
    source:str

