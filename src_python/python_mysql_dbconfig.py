import os
from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # Get the directory of the project
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the absolute path to the config.ini file
    config_path = os.path.join(project_dir, 'Files', 'config', filename)

    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(config_path)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db
