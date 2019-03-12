import unittest
from labSection import LabSection
from labService import LabService


class MockedLabSectionDao:
    def get_by_id(self, id):
        return LabSection()

    def get_all(self):
        return [LabSection(), LabSection()]

    def update(self, labSection):
        return LabSection()

    def delete(self, labSection):
        return LabSection()

    def save(self, labSection):
        return LabSection()

class TestLabService(unittest.TestCase):

    def setUp(self):
        self.labService = LabService(MockedLabSectionDao())

    def test_add_lab_to_course(self):
        id = "801"
        courseId = "CS 361"

        expected_response = "Lab section 801 has been added to course CS 361."
        actual_response = self.labService.add_lab_to_course(id, courseId)

        self.assertEqual(actual_response, expected_response)

    def test_assign_TA_without_sectionId(self):
        taUserName = "jbarney"
        courseId = "CS 361"

        expected_response = "User jbarney has been assigned as a TA for course CS 361."
        actual_response = self.labService.assign_TA(taUserName, courseId, None)

        self.assertEqual(actual_response, expected_response)

    def test_assign_TA_with_sectionId(self):
        taUserName = "jbarney"
        courseId = "CS 361"
        sectionId = "801"

        expected_response = "User jbarney has been assigned as a TA for lab section 801 of course CS 361."
        actual_response = self.labService.assign_TA(taUserName, courseId, sectionId)

        self.assertEqual(actual_response, expected_response)
