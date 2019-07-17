import re

from friendly_name_mixin import FriendlyNameFromClassMixin
from simple_plugins import PluginMount


class BaseTransformer(FriendlyNameFromClassMixin):
    marker = None

    __metaclass__ = PluginMount

    class Meta:
        id_field = 'name'
        id_field_coerce = str

    def __str__(self):
        return self.name

    @property
    def marker_regex(self):
        if not hasattr(self, '_marker_regex'):
            latex_command = r"\\%s(?:\[.*\])?{(.+)}" % self.marker
            self._marker_regex = re.compile(latex_command)

        return self._marker_regex

    def marker_match(self, line):
        return self.marker_regex.search(line)

    def has_marker(self, line):
        return bool(self.marker_match(line))

    def transform_line(self, parser, line):
        raise NotImplementedError

    def __call__(self, parser, line):
        return self.transform_line(parser, line)
