from . import constants as c
from .parser import NaiveLaTeXParser


def latex2plos(input_filename, build_dir=c.DEFAULT_BUILD_DIR, export_dir=c.DEFAULT_EXPORT_DIR):
    parser = NaiveLaTeXParser(input_filename, build_dir, export_dir)
    parser.parse()
