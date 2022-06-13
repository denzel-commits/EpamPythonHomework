import requests
from requests.adapters import HTTPAdapter, Retry


class HttpClient:
    def __init__(self, endpoint, logger):
        self.endpoint = endpoint
        self.logger = logger
        self.response = None

    def make_request(self):
        """
        Executes HTTP GET request with retries using the endpoint defined upon client creation.
        """
        self.logger.info("Requesting {url}".format(url=self.endpoint))

        http = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        http.mount('https://', HTTPAdapter(max_retries=retries))

        response = http.get("https://httpstat.us/503")  # self.endpoint
        self.response = response
