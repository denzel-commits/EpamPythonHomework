import requests
from requests.adapters import HTTPAdapter, Retry
from utilities.logger import LogGen


class RssParser:
    feed = None
    title = None
    date = None
    link = None

    def __init__(self, verbose, limit, json):
        self.verbose = verbose
        self.limit = limit
        self.json = json
        self.logger = LogGen.log_gen(self.verbose)

    def make_request(self, url):
        self.logger.info("Requesting {url}".format(url=url))

        s = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))

        s.get("https://httpstat.us/503")

    def get_news(self):
        pass

    def get_title(self):
        pass
