class RssParser:
    feed = None
    title = None
    date = None
    link = None

    def __init__(self, limit, json, logger):
        self.limit = limit
        self.json = json
        self.logger = logger

    def get_date(self):
        pass

    def get_title(self):
        pass
