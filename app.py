import sys
import os

sys.path.append(os.path.abspath("src"))
from mlprojects.logger import logging
from mlprojects.exception import CustomException
from mlprojects.components.data_ingestion import DataIngestion
from mlprojects.components.data_ingestion import DataIngestionConfig




try:
    data_ingestion=DataIngestion()
    data_ingestion_config=DataIngestionConfig()
    data_ingestion.initiate_data_ingestion()
except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)    




if __name__=="__main__":
    logging.info("the excution has started")
    
