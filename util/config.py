import os
import configparser

config = configparser.ConfigParser()
ini_path = os.path.join(os.path.dirname(__file__), '../', 'config.ini')
config.read(ini_path)
# config.read('../config.ini') # relative path cannot be caculated like this

# print(config.sections())