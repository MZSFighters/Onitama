import configparser
import pathlib

config = configparser.ConfigParser()

config["DEFAULT"] = {
    "AIDifficulty": "Easy",
    "Sound": "On" 
}

with open("main_menu_terminal.ini", "w") as f:
    config.write(f)
