class FormatData:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def prepare(self):
        # use self.data
        output = ""
        output = "Feed: {feed_title} \n\n".format(feed_title=feed_title)

        for i in range(0, len(titles)):
            output += "Title: {title}".format(title=titles[i]
            output += "Date: {date}".format(date=dates[i]) # format date Sun, 20 Oct 2019 04:21:44 +0300
            output += "Link: {link} \n".format(link=links[i])
            output += "\n\nLinks:"
            # collect all links media and urls
            output += "[1]{link}".format(link=links[i])
            output += "[2]{link} \n".format(link=media[i])
            output += "\n\n"

        return output

    def prepare_json(self):
        pass