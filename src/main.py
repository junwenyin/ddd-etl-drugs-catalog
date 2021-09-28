import logging
import argparse

from application.pipeline import ETLPipeline
from infrastructure.config import Config 


if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", dest="date", type=str, required=True, help="date to extract: YYYY-mm-dd"
    )
    parser.add_argument(
        "-s", dest="sources", type=str, required=True, help="pubmed or clinical_trials or all"
    )
    args = parser.parse_args()

    config = Config(args)
    
    logging.basicConfig(
        level = config.log_level,
        format = "%(asctime)s;%(levelname)s;%(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
    )

    pipeline = ETLPipeline(config)
    pipeline.run()