import os
import yaml
import logging

# folder to load config file
CONFIG_PATH = "../"

# Function to load yaml configuration file
def load_config(config_name):
    """
    Sets the configuration file path
    Args:
    config_name: Name of the configuration file in the directory
    Returns:
    Configuration file
    """
    with open(os.path.join(CONFIG_PATH, config_name), encoding="utf-8") as conf:
        config = yaml.safe_load(conf)
    return config