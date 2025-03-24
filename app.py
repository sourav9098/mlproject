import sys
import os

sys.path.append(os.path.abspath("src"))
from mlprojects.logger import logging
from mlprojects.exception import CustomException
from mlprojects.components.data_ingestion import DataIngestion
from mlprojects.components.data_ingestion import DataIngestionConfig
from mlprojects.components.data_transformation import DataTransformation,DataTransformationConfig
from mlprojects.components.model_trainer import ModelTrainerConfig,ModelTrainer




try:
    data_ingestion=DataIngestion()
    train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
    data_ingestion_config=DataIngestionConfig()
    data_ingestion.initiate_data_ingestion()
    data_transformation_config=DataTransformationConfig()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)    




if __name__=="__main__":
    logging.info("the excution has started")
    
