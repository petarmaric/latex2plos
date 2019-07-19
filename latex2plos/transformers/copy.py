import logging
import os
import shutil

from .base import BaseTransformer


class BaseFileCopyTransformer(BaseTransformer):
    filename_prefix = ''
    append_extension_to_file = ''
    prepend_counter_to_exported_filename = True # Avoids overwriting when basename is the same
    comment_out_the_line = False

    def __init__(self):
        self.counter = 1

    def transform_from_filename(self, filename):
        return filename

    def transform_to_filename(self, filename):
        return filename

    def transform_file(self, from_filename, to_filename):
        shutil.copy(from_filename, to_filename)

    def transform_line(self, parser, line):
        path = self.marker_match(line).group(1)
        basename = os.path.basename(path)

        maybe_comment = '%' if self.comment_out_the_line else ''

        if self.prepend_counter_to_exported_filename:
            basename = "%s%02d-%s" % (self.filename_prefix, self.counter, basename)

            self.counter += 1

        from_filename = self.transform_from_filename(os.path.join(
            parser.input_dir,
            path + self.append_extension_to_file
        ))
        to_filename = self.transform_to_filename(os.path.join(
            parser.export_dir,
            basename + self.append_extension_to_file
        ))
        self.transform_file(from_filename, to_filename)
        logging.info("Copied file %s to %s", from_filename, to_filename)

        return maybe_comment + line.replace(path, os.path.basename(to_filename))


class InputListingTransformer(BaseFileCopyTransformer):
    marker = 'lstinputlisting'
    filename_prefix = 'lst'
