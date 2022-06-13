import configparser

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class ReadConfig:

    @staticmethod
    def get_logs_path():
        return config.get('common', 'logs_path')
