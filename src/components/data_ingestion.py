# all the input data like working in team it has big data like collecteing data and storing like in mongo db firstly we have to read 
# lets take it from local
import os
import sys
from src.exception import CustomException
from src.logger import logging 
import pandas as pd

from sklearn.model_selection import train_test_split  
from dataclasses import dataclass


# where i have to store the data 
@dataclass # define directly class variable 
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv') ## inputs giving to data ingestino component 
    raw_data_path: str=os.path.join('artifacts','data.csv') # now it knows where to store the data 

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  

    def initiate_data_ingestion(self): # if data is stored in some databases the code to read it 
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("notebook\data\stud.csv") # change this line and able to read from api or mongo db
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            # path is known like artifacts lets create a folder using dtest train and raw
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path # this information is required for data trainsformation  i am just passing it so that data transformation is able to grab the info
            )

             
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
