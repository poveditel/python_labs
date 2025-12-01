import pandas as pd
import os

def json_to_csv(json_path, csv_path):
    df = pd.read_json(json_path)
    df.to_csv(csv_path, index=False)

def csv_to_json(csv_path, json_path):
    df = pd.read_csv(csv_path)
    df.to_json(json_path, orient='records', indent=4)