import re


__version__ = '1.0.2'


# Based on `django.db.models.options.get_verbose_name`
class FriendlyNameFromClassMixin(object):
    _name_re = re.compile('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z0-9]|$)))')

    @property
    def name(self):
        if not hasattr(self, '_name'):
            class_name = self.__class__.__name__
            self._name = self._name_re.sub(r' \1', class_name).strip()

        return self._name

