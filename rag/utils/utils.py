import json
import yaml
from pprint import pprint

def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

def load_yaml_file(path):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

if __name__ == "__main__":
    pprint(load_yaml_file("config.yaml")['resume_file_path'])