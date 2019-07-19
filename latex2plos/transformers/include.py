import os

from ..utils import find_filenames
from .base import BaseTransformer


class BaseFileIncludeTransformer(BaseTransformer):
    append_extension_to_file = ''
    header = ''
    footer = ''

    def filenames(self, parser, line):
        return [
            os.path.join(
                parser.input_dir,
                self.marker_match(line).group(1) + self.append_extension_to_file
            ),
        ]

    def transform_line(self, parser, line):
        for filename in self.filenames(parser, line):
            with open(filename, 'r') as fp_in:
                parser.input_lines.appendleft(self.footer)

                # Feed the parser with lines from the included file, placing
                # them at the start of its input deque/stack.
                # Recursive file inclusion then no longer requires a recursive
                # parser, and a simple iterative parser will suffice instead.
                parser.input_lines.extendleft(reversed(fp_in.readlines()))

                parser.input_lines.appendleft(self.header)

        return '' # Removes the original "file inclusion" line


class IncludeTransformer(BaseFileIncludeTransformer):
    marker = 'include'
    append_extension_to_file = '.tex'


class InputTransformer(BaseFileIncludeTransformer):
    marker = 'input'
    append_extension_to_file = '.tex'


class VerbatimInputTransformer(BaseFileIncludeTransformer):
    marker = 'verbatiminput'
    header = '\\begin{verbatim}\n'
    footer = '\\end{verbatim}\n'


class BibliographyTransformer(BaseFileIncludeTransformer):
    marker = 'bibliography'

    def filenames(self, parser, line):
        return find_filenames(parser.build_dir, '*.bbl')
