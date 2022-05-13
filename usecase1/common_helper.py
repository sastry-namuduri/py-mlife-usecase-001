# from distutils.command.config import config
import os, json

def read_config():
    configFile = "static_variables.json"
    config_file = open(configFile)
    json_config_file = json.load(config_file)
    return json_config_file


def get_env_from_filename(filename) -> str: 
    """
    Arguments: 
            type : str
                Environment file to read
    Description: 
            Derive environment value from the file name passed as input
            filenames would be in either “<environment> ##.csv” format or “<environment>.csv”, 
            where “<enviroment>” is a string that might contain alphabetic characters and/or spaces
    Return: 
            type : str
                derived environment value
    """               
    # remove extension, remove word after last space
    split_file_nm = " ".join(filename.strip(".csv").split(" ")[:-1])
    # if filename has no spaces, return the file name without extension
    # or return the above derived file name
    return filename.strip(".csv") if split_file_nm == "" else split_file_nm

