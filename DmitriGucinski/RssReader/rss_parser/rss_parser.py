from bs4 import BeautifulSoup


class RssParser:

    def __init__(self, xml, limit, json, logger):
        self.limit = limit
        self.json = json
        self.logger = logger
        self.soup = BeautifulSoup(xml, features="xml")

        self.feed_title = self.get_feed_title()
        self.feed_link = self.get_feed_link()
        self.entries = self.get_entries_list()

    def parse(self):
        print(self.entries)

    def get_entries_list(self):
        """ Combine feed entries list """
        items = self.get_feed_items()
        entries = []
        for item in items:
            entries.append(
                self.get_entry(item)
            )

        return entries

    def get_entry(self, item):
        """ Combine feed entry fields """
        return {
            "Title": self.get_title(item),
            "Link": self.get_link(item),
            "Date": self.get_date(item),
            "Description": 'description',
            "Links": 'all links media and urls',
        }

    def get_title(self, item):
        """ Parse feed entry title """
        if item.find("title"):
            return item.find("title").get_text()

        return 'Untitled'

    def get_link(self, item):
        """ Parse feed entry link """
        link = ''
        if item.find("link"):
            link = item.find("link").get_text()

        if link == '' and item.find("guid"):
            self.feed_link+'/'+item.find("guid").get_text()

        if link:
            return link

        return "no link found"
        # raise exception print no link found

    def get_date(self, item):
        """ Parse feed entry publish date """
        if item.find("pubDate"):
            return item.find("pubDate").get_text()

        return 'no date'

        # if not found search in other place

        # raise exception print no date found

    def get_feed_title(self):
        """ Parse feed title """
        return self.soup.title.string

    def get_feed_link(self):
        """ Parse feed link """
        return self.soup.link.string

    def get_feed_items(self):
        """ Parse feed items """
        return self.soup.find_all("item")

    def get_item_media(self):
        return [item.find("media:content", url=True) for item in self.items]

