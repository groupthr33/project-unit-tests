import unittest
from auth import Auth


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()

    def test_authenticate(self):
        # put user with username jdoe and password password in storage

        actual_response = self.auth.authenticate("jdoe", "password")
        expected_response = True

        self.assertEqual(expected_response, actual_response)

    def test_authenticate_wrong_password(self):
        # put user with username jdoe and password password in storage

        actual_response = self.auth.authenticate("jdoe", "wrong")
        expected_response = False

        self.assertEqual(expected_response, actual_response)

    def test_is_authenticated(self):
        # put user with username jdoe and password password in storage
        # set current user to jdoe

        actual_response = self.auth.is_authenticated()
        expected_response = True

        self.assertEqual(expected_response, actual_response)

    def test_is_authorized_true(self):
        # put user with username jdoe and password password in storage
        # set current user to jdoe with auth_string 0xC

        command_auth_string = 0x08

        actual_response = self.auth.is_authorized(command_auth_string)
        expected_response = True

        self.assertEqual(expected_response, actual_response)

    def test_is_authorized_false(self):
        # put user with username jdoe and password password in storage
        # set current user to jdoe with auth_string 0x1

        command_auth_string = 0x08

        actual_response = self.auth.is_authorized(command_auth_string)
        expected_response = False

        self.assertEqual(expected_response, actual_response)
