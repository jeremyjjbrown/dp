import unittest
import os

from dpctl.config import Config
from dpctl.terraform import Terraform


class TestTerraform(unittest.TestCase):

    def setUp(self):
        self.config = Config(
            configPath=os.path.join(
                os.path.dirname(__file__),
                'data/dpctl.yaml'
            )
        )

    def test_tf_apply(self):
        tf = Terraform(self.config.get('providers', {}).get('terraform'))
        self.assertEqual('tf push terraform/ and infra-vars/', tf.apply())


if __name__ == '__main__':
    unittest.main()
