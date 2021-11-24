from collections import OrderedDict

from dpctl.terraform import Terraform
from dpctl.cf import CF
from dpctl.helm import Helm


class Workflow(object):

    def __init__(self, config):
        self.clients = OrderedDict()
        tf_config = config.get('providers', {}).get('terraform')
        helm_config = config.get('providers', {}).get('helm')
        cf_config = config.get('providers', {}).get('cf')
        if tf_config:
            self.clients['terraform'] = Terraform(tf_config)
        if cf_config:
            self.clients['cf'] = CF(cf_config)
        if helm_config:
            self.clients['helm'] = Terraform(helm_config)

    def apply(self):
        results = []
        for k, v in self.clients.items():
            results.append(v.apply())
        return results
