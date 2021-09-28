from src.infrastructure.config_parser import parse_config

def test_parse_config():
    return parse_config("./config.ini")['log']['level'] == "INFO"  