import yaml

import importlib.resources as pkg_resources
from dpctl import defaults


class Config(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
        d = YamlReader()
        self.__dict__.update(d.data)
        c = YamlReader(path=kwargs.get('configPath'))
        # TODO we will likely need a proper recursive function to merge configs
        self.__dict__.update(c.data)


class YamlReader(object):

    def __init__(self, path=None):
        if not path:
            f = pkg_resources.open_text(
                defaults,
                'defaults.yaml'
            )
        else:
            f = open(path, 'r')
        self.data = yaml.safe_load(f.read())
