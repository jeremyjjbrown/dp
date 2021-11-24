import unittest
import os

from dpctl.config import YamlReader, Config


class TestConfig(unittest.TestCase):

    config_file = os.path.join(
        os.path.dirname(__file__),
        'data/dpctl.yaml'
    )

    def test_reader(self):
        yr = YamlReader()
        self.assertIsInstance(yr.data, dict)

    def test_config(self):
        c = Config(configPath=TestYamlReader.config_file)
        self.assertIsInstance(c, dict)
        self.assertTrue(c['configPath'].endswith('data/dpctl.yaml'))
        self.assertIsNotNone(c.get('providers'))


if __name__ == '__main__':
    unittest.main()
