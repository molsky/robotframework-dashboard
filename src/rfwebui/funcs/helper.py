import configparser
import os


SETTINGS_FILE_PATH = "../app_configs/settings.ini"


def ConfigSectionMap(section):
    Config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), SETTINGS_FILE_PATH)
    Config.read(config_file)

    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


def read_settings():
    working_dir = ""

    if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/" + SETTINGS_FILE_PATH):
        working_dir = ConfigSectionMap("FILES")['path']

    settings_dict = {"test_file_dir": working_dir}

    return settings_dict


def save_settings(dir_path):
    config = configparser.ConfigParser()
    if not dir_path.endswith('/'):
        dir_path += '/'
    config['FILES'] = {'Path': dir_path}
    with open(os.path.join(os.path.dirname(__file__), SETTINGS_FILE_PATH), 'w+') as configfile:
        config.write(configfile)
