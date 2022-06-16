import argparse
import sys
from http_client.http_client import HttpClient
from rss_parser.rss_parser import RssParser
from requests.exceptions import RetryError
from utilities.validator import Validator
from exceptions.limit_error_exception import LimitIsNotIntegerError
from utilities.logger import LogGen
from utilities.read_properties import ReadConfig


def main():
    parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
    parser.add_argument("source", type=str, help="RSS URL")
    parser.add_argument("--version", action="version",
                        version="%(prog)s {version}".format(version=ReadConfig.get_version()),
                        help="Print version info")
    parser.add_argument("--json", default=False, action="store_true", help="Print result as JSON in stdout")
    parser.add_argument("--verbose", default=False, action="store_true", help="Outputs verbose status messages")
    parser.add_argument("--limit", help="Limit news topics if this parameter provided")

    args = parser.parse_args()
    # raise custom exception on 404 error
    # raise custom exception on page not accessible
    # raise custom exception on page is not rss

    logger = LogGen.log_gen(args.verbose)
    client = HttpClient(args.source, logger)

    try:
        Validator.validate_limit(args.limit)
    except LimitIsNotIntegerError:
        logger.error("Limit is not integer, please provide integer value for limit")
        sys.exit(1)

    try:
        response = client.make_request()
        rss_parser = RssParser(response.text, args.limit, args.json, logger)
        rss_parser.parse()
        # printer print json or text
    except KeyboardInterrupt:
        logger.info("Shutdown requested...exiting")
    except RetryError as err:
        logger.error("Failed to open source url, check if it is correct or try again later. {error}".format(error=err))
        sys.exit(1)


if __name__ == "__main__":
    main()
