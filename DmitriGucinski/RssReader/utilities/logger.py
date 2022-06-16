import logging
from utilities.read_properties import ReadConfig


class LogGen:
    logs_path = ReadConfig.get_logs_path()

    @classmethod
    def log_gen(cls, verbose):
        logger = logging.getLogger('rss reader')
        logger.setLevel(logging.INFO)

        if verbose:
            c_handler = logging.StreamHandler()
            c_handler.setLevel(logging.INFO)
            c_format = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
            c_handler.setFormatter(c_format)
            logger.addHandler(c_handler)
        else:
            f_handler = logging.FileHandler(cls.logs_path + 'rss_reader.log')
            f_handler.setLevel(logging.INFO)

            f_format = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
            f_handler.setFormatter(f_format)

            logger.addHandler(f_handler)

        return logger
