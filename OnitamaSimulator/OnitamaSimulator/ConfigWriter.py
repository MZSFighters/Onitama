from configparser import ConfigParser

config = ConfigParser()

config["DefaultGame"] = {
    "GameString" : "N02000103044240414344NNNNN"
    # Could add more game info to the section(dictionary) if needed
    # e.g
    # "P1master" : "0,2",
    # "P1pawn1" : "0,0",
    # "P1pawn2" : "0,1",
    # .
    # .
    # .

}

with open("save_game_config.ini", "w") as configfile:
    config.write(configfile)