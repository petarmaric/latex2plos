from nose.tools import eq_
from friendly_name_mixin import FriendlyNameFromClassMixin


def test_friendly_name_from_class_mixin():
    class IsHTML5BetterThanFlash11OrIsItMe(FriendlyNameFromClassMixin):
        answer = 'yes'
    
    eq_(
        IsHTML5BetterThanFlash11OrIsItMe().name,
        'Is HTML5 Better Than Flash11 Or Is It Me'
    )
