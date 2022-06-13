import argparse
import requests

parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
parser.add_argument("source", type=str, help="RSS URL")
parser.add_argument("--version", action="version", version="%(prog)s 1.0", help="Print version info")
parser.add_argument("--json", default=False, action="store_true", help="Print result as JSON in stdout")
parser.add_argument("--verbose", default=False, action="store_true", help="Outputs verbose status messages")
parser.add_argument("--limit", help="Limit news topics if this parameter provided")

args = parser.parse_args()

# validate limit - it should be positive integer
# raise custom exception on error

# raise custom exception on 404 error
# raise custom exception on page not accessible
# raise custom exception on page is not rss

x = requests.get(args.source)
print(x.status_code)
