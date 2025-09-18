import yaml


def load_config(config: str):
    with open(config, "r") as f:
        config = yaml.safe_load(f)
    return config
