# config_utils.py
import yaml

def load_openai_key(filepath="./secret.yml"):
    with open(filepath, "r") as file:
        config = yaml.safe_load(file)
    return config["OPENAI_KEY"]
