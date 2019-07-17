from collections import deque
import logging
import os
import re

from .transformers import BaseTransformer


class NaiveLaTeXParser(object):
    comment_re = re.compile(r'^\s*%')

    def __init__(self, input_filename, build_dir, export_dir):
        self.input_filename = input_filename
        self.input_dir = os.path.dirname(self.input_filename)
        with open(self.input_filename, 'r') as fp_in:
            self.input_lines = deque(fp_in)

        self.build_dir = build_dir

        self.export_dir = export_dir
        self.export_filename = os.path.join(
            self.export_dir,
            os.path.basename(self.input_filename)
        )

        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)

    def parse(self):
        transformers = BaseTransformer.plugins.instances_sorted_by_id

        with open(self.export_filename, 'w') as fp_out:
            while self.input_lines:
                line = self.input_lines.popleft()

                if self.comment_re.search(line):
                    # This line contains a commented-out LaTeX command, keep it as is
                    fp_out.write(line)
                    continue

                for transformer in transformers:
                    if transformer.has_marker(line):
                        logging.debug("%s will be applied to the line '%s'", transformer, line.strip())
                        fp_out.write(transformer(self, line))

                        break # Skip other transformers
                else:
                    # No transformers can be applied to this line, keep it as is
                    fp_out.write(line)
