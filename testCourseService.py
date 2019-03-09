import unittest

class MockedCourseDao:
    def get_by_id(self, id):
        return Course()

    def get_all(self):
        return [Course(), Course()]

    def update(self, course):
        return Course()

    def delete(self, course):
        return Course()

    def save(self, course):
        return Course()

class TestCourseService(unittest.TestCase):

    def setUp(self):
        self.courseService = CourseService(MockedCourseDao())

    def test_create_course(self):
        id = "CS 361"
        name = "Intro to Software Engineering"

        expected_response = "Course for CS 361 Intro to Software Engineering has been created."
        actual_response = self.courseService.create_course(id, name)

        assertEqual(actual_response, expected_response)

    def test_assign_instructor(self):
        instructorUserName = "jdoe"
        id = "CS 361"

        expected_response = "User jdoe has been assigned as the instructor for course CS 361"
        actual_response = self.courseService.assign_instructor(instructorUserName, id)

        assertEqual(actual_response, expected_response)

    def test_view_course_assignments(self):
        #User is jdoe and is assigned to CS 361 and CS 537

        expected_response = "User jdoe was been assigned to courses CS 361 and CS 537"
        actual_response = self.courseService.view_course_assignments()

        assertEqual(actual_response, expected_response)