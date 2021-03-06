from trakt.client import TraktClient
from trakt.helpers import has_attribute

__version__ = '0.6.1-beta'


class TraktMeta(type):
    def __getattr__(self, name):
        if has_attribute(self, name):
            return super(TraktMeta, self).__getattribute__(name)

        if self.client is None:
            self.construct()

        return getattr(self.client, name)

    def __setattr__(self, name, value):
        if has_attribute(self, name):
            return super(TraktMeta, self).__setattr__(name, value)

        if self.client is None:
            self.construct()

        setattr(self.client, name, value)

    def __getitem__(self, key):
        if self.client is None:
            self.construct()

        return self.client[key]


class Trakt(object):
    __metaclass__ = TraktMeta

    client = None

    @classmethod
    def construct(cls):
        cls.client = TraktClient()
