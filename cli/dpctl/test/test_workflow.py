import unittest
import os

from unittest.mock import Mock
from collections import OrderedDict

from dpctl.config import Config
from dpctl.workflow import Workflow


class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.config = Config(
            configPath=os.path.join(
                os.path.dirname(__file__),
                'data/dpctl.yaml'
            )
        )

    def test_tf_apply(self):
        wf = Workflow(self.config)
        mock_client = Mock()
        mock_clients = OrderedDict()
        mock_clients['terraform'] = mock_client
        mock_clients['cf'] = mock_client
        mock_client.apply.return_value = "Success"
        wf.clients = mock_clients
        results = wf.apply()
        self.assertEqual(["Success", "Success"], results)
        self.assertEqual(2, mock_client.apply.call_count)


if __name__ == '__main__':
    unittest.main()
