import logging
from utilities.read_properties import ReadConfig


class LogGen:
    logs_path = ReadConfig.get_logs_path()

    @classmethod
    def log_gen(cls):
        logger = logging.getLogger('rss reader')
        logger.setLevel(logging.INFO)

        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(cls.logs_path + 'rss_reader.log')

        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.INFO)

        c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        return logger
