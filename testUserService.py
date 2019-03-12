import unittest
from userService import UserService
from user import User

# TODO: other cases besides happy path, there will need to be another mock that throws exceptions or returns bad data, etc.

class MockedUserDao:
    def get_by_id(self, username):
        return User("joe", "jbarney")

    def get_all(self):
        return [User("joe", "jdoe"), User("joe", "jbarney")]

    def update(self, user):
        return User()

    def delete(self, user):
        return User()

    def save(self, user):
        return User()


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.userService = UserService(MockedUserDao())

    def test_create_account(self):
        username = 'jbarney'
        name = 'Joe'
        roles = ['admin', 'ta']

        expected_response = "Account for user jbarney successfully created with roles admin, ta."
        actual_response = self.userService.create_account(username, name, roles)

        self.assertEqual(expected_response, actual_response)

    def test_delete_account(self):
        username = 'jbarney'

        expected_response = "Account for user jbarney successfully deleted."
        actual_response = self.userService.delete_account(username)

        self.assertEqual(expected_response, actual_response)

    def test_edit_account(self):
        username = 'jbarney'
        updates = {'password': 'newpassword'}

        expected_response = "password has been successfully updated for user jbarney"
        actual_response = self.userService.edit_account(username, updates)

        self.assertEqual(expected_response, actual_response)

    def edit_contact_info(self):
        username = 'jbarney'
        updates = {'address': 'newpassword'}

        expected_response = "address has been successfully updated for user jbarney"
        actual_response = self.userService.edit_contact_info(username, updates)

        self.assertEqual(expected_response, actual_response)

    def test_get_all_contact_info(self):
        expected_response = "Joe jbarney@uwm.edu\nAmy aymee@uwm.edu"
        actual_response = self.userService.get_all_contact_info()

        self.assertEqual(expected_response, actual_response)

    def test_get_contact_info(self):
        username = 'jbarney'

        expected_response = "Joe jbarney@uwm.edu"
        actual_response = self.userService.get_contact_info(username)

        self.assertEqual(expected_response, actual_response)

    def test_notify(self):
        subject = 'Important Things'
        content = 'You guys are late.'
        users = ['jbarney', 'aymee']

        expected_response = "Users jbarney and aymee have been notified."
        actual_response = self.userService.notify(subject, content, users)

        self.assertEqual(expected_response, actual_response)
