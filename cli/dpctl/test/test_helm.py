import unittest
import os

from dpctl.config import Config
from dpctl.helm import Helm


class TestCF(unittest.TestCase):

    def setUp(self):
        self.config = Config(
            configPath=os.path.join(
                os.path.dirname(__file__),
                'data/dpctl.yaml'
            )
        )

    def test_helm_apply(self):
        helm = Helm(self.config.get('providers', {}).get('helm'))
        self.assertEqual(
            'helm install --values helm/values.yaml helm',
            helm.apply()
        )


if __name__ == '__main__':
    unittest.main()
