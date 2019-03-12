import unittest
from commandLineController import CommandLineController

# TODO: only listen() is a public method, so maybe the others dont need to be tested, and listen() is hard to test too


class TestCommandLineController(unittest.TestCase):

    def setUp(self):
        self.commandLineController = CommandLineController()

    def test_read_command(self):
        self.commandLineController.read_command()

    def test_parse_command(self):
        self.commandLineController.parse_command("course CS417 'Intro to software'")

    def test_execute_command(self):
        self.commandLineController.execute_command({'command': 'course', 'name': 'myclass'})

    def test_report_outcome(self):
        self.commandLineController.report_outcome("it worked")

    def test_listen(self):
        self.commandLineController.listen()

