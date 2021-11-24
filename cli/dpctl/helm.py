from dpctl import config
from dpctl.config import Config


class Helm(object):

    def __init__(self, config):
        self.config = config

    def apply(self):
        if self.config.get('path') and \
            self.config.get("values"):
            return (
                f'helm install --values {self.config.get("values")}'
                f' {self.config.get("path")}'
            )
        return "Error"
