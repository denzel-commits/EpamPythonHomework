from bs4 import BeautifulSoup


class RssParser:

    def __init__(self, xml, limit, json, logger):
        self.limit = int(limit)
        self.json = json
        self.logger = logger
        self.soup = BeautifulSoup(xml, features="xml")

        self.feed_title = self.get_feed_title()
        self.feed_link = self.get_feed_link()
        self.entries = self.get_entries_list()

        self.feed = {"Title": self.feed_title, "Link": self.feed_link, "Entries": self.entries}

    def parse(self):
        if not self.limit or self.limit > len(self.entries):
            limit = len(self.entries)
        else:
            limit = self.limit

        for i in range(0, limit):
            print(self.entries[i])  # format to human-readable or json

        # return raw_data and give it to formatter/printer

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
            "Description": self.get_description(item),
            "Links": self.get_links(item),
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
            is_permalink = item.find("guid", isPermaLink=True)
            if is_permalink == "false":
                link = self.feed_link+'/'+item.find("guid").get_text()
            elif is_permalink == "true":
                link = item.find("guid").get_text()

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

    def get_description(self, item):
        """ Parse feed entry description """
        if item.find("description"):
            return item.find("description").get_text()

        return 'no description'

    def get_author(self, item):
        """ Parse feed entry author """
        if item.find("author"):
            return item.find("author").get_text()

        return 'no author'

    def get_links(self, item):
        """ Parse feed entry links """
        links = [
            {"link": self.get_feed_link(), "type": "link"},
            {"link": self.get_media(item), "type": "image"},
            {"link": self.get_source(item), "type": "link"},
        ]

        return links

    def get_source(self, item):
        """ Parse feed source """
        source = item.find("source")["url"]

        return source

    def get_media(self, item):
        """ Parse feed entry media """
        media_content = item.find("content")

        return media_content

    def get_link_type(self, element):
        pass

    def get_feed_title(self):
        """ Parse feed title """
        return self.soup.title.string

    def get_feed_link(self):
        """ Parse feed link """
        return self.soup.link.string

    def get_feed_items(self):
        """ Parse feed items """
        return self.soup.find_all("item")



