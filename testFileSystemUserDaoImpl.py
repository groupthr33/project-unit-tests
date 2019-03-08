import unittest
from fileSystemUserDaoImpl import FileSystemUserDaoImpl as UserDao
from user import User
from unittest.mock import mock_open, patch

# TODO: create actual mocked text, instantiate Users correctly, test cases when pythons file operations throw exceptions


class TestFileSystemUserDaoImpl(unittest.TestCase):

    def setUp(self):
        self.mocked_user_data = 'hello'
        self.userDao = UserDao()

    def test_get_by_id(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user_id = 'mrwatts'

            expected_user = User()

            actual_user = self.userDao.get_by_id(user_id)

            self.assertEqual(expected_user, actual_user)

    def test_get_by_id_does_not_exist(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user_id = 'mrwatts2'

            with self.assertRaises(Exception):
                self.userDao.get_by_id(user_id)

    def test_get_all(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            expected_users = [User(), User()]

            actual_users = self.userDao.get_all()

            self.assertEqual(expected_users, actual_users)

    def test_update(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user = User()  # use id of user that IS in mock fs object

            expected_response = user
            actual_response = self.userDao.update(user)

            self.assertEqual(expected_response, actual_response)

    def test_update_does_not_exist(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user = User()  # use id of user that is NOT in mock fs object

            with self.assertRaises(Exception):
                self.userDao.update(user)

    def test_delete(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user = User()  # use id of user that IS in mock fs object

            expected_response = user

            actual_response = self.userDao.delete(user)

            self.assertEqual(expected_response, actual_response)

    def test_delete_does_not_exist(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user = User()  # use id of user that is NOT in mock fs object

            with self.assertRaises(Exception):
                self.userDao.delete(user)

    def test_save(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user = User()  # use id of user that is NOT in mock fs object

            expected_response = user

            actual_response = self.userDao.save(user)

            self.assertEqual(expected_response, actual_response)

    def test_save_already_exists(self):
        with patch('fileSystemUserDaoImpl.open', mock_open(read_data=self.mocked_user_data), create=True) as m:
            user = User()  # use id of user that IS in mock fs object

            with self.assertRaises(Exception):
                self.userDao.save(user)
