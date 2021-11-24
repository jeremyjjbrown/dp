from dpctl.config import Config


class Terraform(object):

    def __init__(self, config):
        self.config = config

    def apply(self):
        if self.config.get('path') and \
            self.config.get("vars"):
            return (
                f'tf push {self.config.get("path")} '
                f'and {self.config.get("vars")}'
            )
        return "Error"
