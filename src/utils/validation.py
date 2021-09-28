from typing import List
from src.utils.date_utils import try_parsing_date

def is_valid_pub_line(line: List[str]) -> bool: 
    is_valid_length = (len(line) == 4)
    is_valid = is_valid_length and is_valid_date(str(line[2])) and is_valid_value(str(line[1])) and is_valid_value(str(line[0]))
    return is_valid

def is_valid_drug_line(line: List[str]) -> bool: 
    is_valid_length = (len(line) == 2)
    is_valid = is_valid_length and is_valid_value(str(line[1])) and is_valid_value(str(line[0]))
    return is_valid

def is_valid_date(date: str)-> bool: 
    return try_parsing_date(date) != None

def is_valid_value(value: str)-> bool: 
    return len(value.strip()) > 0
    