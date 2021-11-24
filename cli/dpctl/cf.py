from dpctl import config
from dpctl.config import Config


class CF(object):

    def __init__(self, config):
        self.config = config

    def apply(self):
        if self.config.get('path'):
            return f'cf push {self.config.get("path")}'
        if self.config.get('templatePath') and \
            self.config.get("varsPath"):
            return (
                f'cf push {self.config.get("templatePath")} '
                f'and {self.config.get("varsPath")}'
            )
        return "Error"
