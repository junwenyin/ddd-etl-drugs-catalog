import os 
from infrastructure import config_parser
from utils.date_utils import get_no_event_from_date
import logging


class Config:
    """
    Parameters class.

    This file centralizes anything that can be 
    parametrized in the code.

    """

    def __init__(self, args):
        """
        read config file and add it to parameters
        """

        cfg = config_parser.parse_config(os.path.abspath('./config.ini'))
        self.log_level = cfg['log']['level']

        self.date = args.date
        no_event = get_no_event_from_date(self.date)

        self.drugs_format = str(cfg['input']['drugs_format'])
        self.drugs_path = str(cfg['input']['drugs_path']) + '.' + self.drugs_format

        self.pubmed_format = str(cfg['input']['pubmed_format'])
        self.pubmed_path = str(cfg['input']['pubmed_path']).format(no_event = no_event) + '.' + self.pubmed_format

        self.clinical_trials_format = str(cfg['input']['clinical_trials_format'])
        self.clinical_trials_path = str(cfg['input']['clinical_trials_path']).format(no_event = no_event) + '.' + self.clinical_trials_format

        self.staging_catalog_path = str(cfg['staging']['staging_catalog_path']).format(no_event = no_event)

        self.catalog_path = str(cfg['output']['catalog_path']).format(no_event = no_event)

        all_sources = ["pubmed", "clinical_trials"]
        
        if args.sources == 'all':
            self.sources = all_sources
        elif args.sources in all_sources:
            self.sources = [args.sources]
        else:
            raise Exception("invalid params sources type, it should be one of pubmed or clinical_trials or all")





	
