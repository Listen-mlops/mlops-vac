import os
import yaml
import pandas as pd
import numpy as np
import argparse
from pkgutil import get_data 
from get_data import get_data,read_param
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.linear_model import ElasticNet
import joblib
import json
import mlflow
from urllib.parse import urlparse
from split_data import split_data

def train_and_eval(config_path):
    config = read_param(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    raw_data_path = config["load_data"]["cleaned_data"]
    split_data = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_path"]

    alpha = ["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = ["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = config["base"]["target_col"]
    train=pd.read_csv(train_data_path)
    test=pd.read_csv(test_data_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="C:/Users/Sarthak/OneDrive/Documents/Desktop/VAC-MLOPS/params.yml")
    parsed_args = args.parse_args()
    train_and_eval(config_path=parsed_args.config)