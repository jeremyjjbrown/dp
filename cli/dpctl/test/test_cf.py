import unittest
import os

from dpctl.config import Config
from dpctl.cf import CF


class TestCF(unittest.TestCase):

    def setUp(self):
        self.config = Config(
            configPath=os.path.join(
                os.path.dirname(__file__),
                'data/dpctl.yaml'
            )
        )

    def test_cf_apply(self):
        cf = CF(self.config.get('providers', {}).get('cf'))
        self.assertEqual('cf push cf/manifest.yml', cf.apply())


if __name__ == '__main__':
    unittest.main()
