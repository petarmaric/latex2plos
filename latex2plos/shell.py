import argparse
import logging

from . import __version__
from . import constants as c
from .main import latex2plos


def main():
    # Setup command line option parser
    parser = argparse.ArgumentParser(
        description='Automated preparation of your LaTeX paper for submission in PLOS journals',
    )
    parser.add_argument(
        'input_filename',
        help='Filename of the main LaTeX document',
    )
    parser.add_argument(
        '-b',
        '--build-dir',
        metavar='DIRECTORY',
        default=c.DEFAULT_BUILD_DIR,
        help="DIRECTORY where the main LaTeX document has successfully been built, '%s' by default" % c.DEFAULT_BUILD_DIR,
    )
    parser.add_argument(
        '-e',
        '--export-dir',
        metavar='DIRECTORY',
        default=c.DEFAULT_EXPORT_DIR,
        help="Export to selected DIRECTORY, '%s' by default" % c.DEFAULT_EXPORT_DIR,
    )
    parser.add_argument(
        '-q',
        '--quiet',
        action='store_const',
        const=logging.WARN,
        dest='verbosity',
        help='Be quiet, show only warnings and errors',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_const',
        const=logging.DEBUG,
        dest='verbosity',
        help='Be very verbose, show debug information',
    )
    parser.add_argument(
        '--version',
        action='version',
        version="%(prog)s " + __version__,
    )
    args = parser.parse_args()

    # Configure logging
    log_level = args.verbosity or logging.INFO
    logging.basicConfig(level=log_level, format="[%(levelname)s] %(message)s")

    latex2plos(args.input_filename, args.build_dir, args.export_dir)

if __name__ == '__main__':
    main()
