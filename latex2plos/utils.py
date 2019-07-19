import fnmatch
import os


def find_filenames(path, filename_pattern):
    file_list = sorted(os.listdir(path))
    for name in fnmatch.filter(file_list, filename_pattern):
        yield os.path.join(path, name)
