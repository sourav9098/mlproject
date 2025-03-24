import sys
from dataclasses import dataclass  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
sys.path.append(os.path.abspath("src"))
from mlprojects.logger import logging
from mlprojects.exception import CustomException
from mlprojects.utils import save_object

@dataclass


class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    def get_data_transformer_object(self):
        """"this function is responsible for data tranmsformation"""
        try:
            numerical=['reading_score', 'writing_score']   
            catagorical=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course'] 
            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scalar",StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ]) 
            logging.info(f"catagorical columns:{catagorical}")
            logging.info(f"numerical columns:{numerical}")   
            preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical),
                ("cat_pipeline",cat_pipeline,catagorical)
            ])
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("reading the train test file")
            preprocessing_obj=self.get_data_transformer_object()
            target_col_name="math_score"
            numerical=["writing_score","reading_score"]
            input_features_train_df=train_df.drop(columns=[target_col_name],axis=1)
            target_features_train_df=train_df[target_col_name]
            input_features_test_df=test_df.drop(columns=[target_col_name],axis=1)
            target_features_test_df=test_df[target_col_name]
            logging.info("applying preprocessing in train test dataset")
            input_features_train_arr=preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr=preprocessing_obj.transform(input_features_test_df)
            train_arr=np.c_[input_features_train_arr,np.array(target_features_train_df)]
            test_arr=np.c_[input_features_test_arr,np.array(target_features_test_df)]
            logging.info(f"save preprocessing object")
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocessing_obj)
            return(train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path)
        except Exception as e:
            raise CustomException(e,sys)    
            
            
                