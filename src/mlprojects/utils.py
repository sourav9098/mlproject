import os
import sys
import pickle
import numpy as np
import pandas as pd
sys.path.append(os.path.abspath("src"))
from mlprojects.logger import logging
from mlprojects.exception import CustomException
import pymysql
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("reading sql dataset")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established",mydb)
        df=pd.read_sql_query('select * from student1',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)
    
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True) 
        with open(file_path,"wb")as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)           
