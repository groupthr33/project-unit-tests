import unittest
from fileSystemCourseDaoImpl import FileSystemCourseDaoImpl as CourseDao
from course import Course
from unittest.mock import mock_open, patch

# TODO create actual mocked text, instantiate Courses correctly


class TestFileSystemCourseDaoImpl(unittest.TestCase):

    def setUp(self):
        self.mocked_course_data = 'hello'
        self.courseDao = CourseDao()

    def test_get_by_id(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course_id = 'CS361'

            expected_course = Course()

            actual_course = self.courseDao.get_by_id(course_id)

            self.assertEqual(expected_course, actual_course)

    def test_get_by_id_does_not_exist(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course_id = 'CS1000'

            with self.assertRaises(Exception):
                self.userDao.get_by_id(course_id)

    def test_get_all(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            expected_courses = [Course(), Course()]

            actual_courses = self.courseDao.get_all()

            self.assertEqual(expected_courses, actual_courses)

    def test_update(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course = Course()  # use id of course that IS in mock fs object

            expected_response = course
            actual_response = self.courseDao.update(course)

            self.assertEqual(expected_response, actual_response)

    def test_update_does_not_exist(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course = Course()  # use id of course that is NOT in mock fs object

            with self.assertRaises(Exception):
                self.courseDao.update(course)

    def test_delete(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course = Course()  # use id of course that IS in mock fs object

            expected_response = course

            actual_response = self.courseDao.delete(course)

            self.assertEqual(expected_response, actual_response)

    def test_delete_does_not_exist(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course = Course()  # use id of course that is NOT in mock fs object

            with self.assertRaises(Exception):
                self.courseDao.delete(course)

    def test_save(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course = Course()  # use id of course that is NOT in mock fs object

            expected_response = course

            actual_response = self.courseDao.save(course)

            self.assertEqual(expected_response, actual_response)

    def test_save_already_exists(self):
        with patch('fileSystemCourseDaoImpl.open', mock_open(read_data=self.mocked_course_data), create=True) as m:
            course = Course()  # use id of course that IS in mock fs object

            with self.assertRaises(Exception):
                self.courseDao.save(course)
