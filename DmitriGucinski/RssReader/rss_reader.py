import argparse
import sys
from rss_parser.rss_parser import RssParser
from requests.exceptions import RetryError

parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
parser.add_argument("source", type=str, help="RSS URL")
parser.add_argument("--version", action="version", version="%(prog)s 1.0", help="Print version info")
parser.add_argument("--json", default=False, action="store_true", help="Print result as JSON in stdout")
parser.add_argument("--verbose", default=False, action="store_true", help="Outputs verbose status messages")
parser.add_argument("--limit", help="Limit news topics if this parameter provided")

args = parser.parse_args()

# validate limit - it should be positive integer
# raise custom exception on error
# Validator::validate_int(args.limit)
print(args.limit.isdigit())
# raise custom exception on 404 error
# raise custom exception on page not accessible
# raise custom exception on page is not rss

parser = RssParser(args.verbose, args.limit, args.json)
try:
    parser.get_news(
        parser.make_request(args.source)
        )
except KeyboardInterrupt:
    print("Shutdown requested...exiting")
except RetryError as err:
    print("Failed to open source url. {error}".format(error=err))
    print("Please see if given url is correct or try again later")
    sys.exit(1)
