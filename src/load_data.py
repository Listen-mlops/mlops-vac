import os
import yaml
import pandas as pd
import numpy as np
import argparse
from pkgutil import get_data 
from get_data import get_data,read_param

def load_save_data(config_path):
    config = read_param(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ","_") for col in df.columns]
    raw_data_path = config["load_data"]["cleaned_data"]
    df.to_csv(raw_data_path,sep=',',index=False,header=new_cols)
    print("Data Loaded and Saved: ",raw_data_path)
    return load_save_data

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.getenv("CONFIG_PATH", "params.yml")
    args.add_argument("--config",default=default_config_path)
    parsed_args = args.parse_args()
    load_save_data(config_path=parsed_args.config)