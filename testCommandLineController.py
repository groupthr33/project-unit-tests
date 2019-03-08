import unittest
from commandLineController import CommandLineController

# TODO: only listen() is a public method, so maybe the others dont need to be tested, and listen() is hard to test too


class TestCommandLineController(unittest.TestCase):

    def setUp(self):
        self.commandLineController = CommandLineController()

    def test_read_command(self):
        pass

    def test_parse_command(self):
        pass

    def test_execute_command(self):
        pass

    def test_report_outcome(self):
        pass

    def test_listen(self):
        pass

