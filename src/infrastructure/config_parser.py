import configparser

def parse_config(conf_file):
    """
    Load configurations from given file .

    Parameters
    ----------
    conf_file : str
        full path of conf file

    Returns
    -------
    ConfigParser

    """
    config_parser = configparser.ConfigParser()
    config_parser.read(conf_file)
    return config_parser
