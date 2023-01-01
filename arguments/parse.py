import sys
from argparse import Namespace

from arguments.TargsArgumentParser import TargsArgumentParser


class Parser:
    @staticmethod
    def parse_args() -> Namespace:
        # Configure parser
        parser = TargsArgumentParser(usage="%(prog)s [options] [-- utility [argument ...]]")
        parser.add_argument("--width", type=int, default=2)
        parser.add_argument("--height", type=int, default=2)
        parser.add_argument("-I", metavar="replstr", dest="replstr", type=str)

        return parser.parse_args()

    @staticmethod
    def parse_stdin(delimiter="\n") -> list[str]:
        # Read stdin, skipping blank lines
        inputs: list[str] = sys.stdin.read().split(delimiter)
        inputs = [cmd for cmd in inputs if cmd != ""]

        if len(inputs) == 0:
            exit()

        return inputs
