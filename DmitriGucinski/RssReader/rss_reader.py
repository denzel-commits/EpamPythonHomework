import argparse
import sys
from http_client.http_client import HttpClient
from rss_parser.rss_parser import RssParser
from requests.exceptions import RetryError
from utilities.logger import LogGen

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


logger = LogGen.log_gen(args.verbose)
client = HttpClient(args.source, logger)
parser = RssParser(args.limit, args.json, logger)

try:
    client.make_request()
except KeyboardInterrupt:
    logger.info("Shutdown requested...exiting")
except RetryError as err:
    logger.error("Failed to open source url, check if it is correct or try again later. {error}".format(error=err))
    sys.exit(1)
