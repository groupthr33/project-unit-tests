import unittest
from fileSystemLabSectionDaoImpl import FileSystemLabSectionDaoImpl as LabSectionDao
from labSection import LabSection
from unittest.mock import mock_open, patch

# TODO create actual mocked text, instantiate LabSections correctly


class TestfileSystemLabSectionDaoImpl(unittest.TestCase):

    def setUp(self):
        self.mocked_lab_section_data = 'hello'
        self.labSectionDao = LabSectionDao()

    def test_get_by_id(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section_id = '001'

            expected_lab_section = LabSection()

            actual_lab_section = self.labSectionDao.get_by_id(lab_section_id)

            self.assertEqual(expected_lab_section, actual_lab_section)

    def test_get_by_id_does_not_exist(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section_id = '999'

            with self.assertRaises(Exception):
                self.labSectionDao.get_by_id(lab_section_id)

    def test_get_all(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            expected_lab_sections = [LabSection(), LabSection()]

            actual_lab_sections = self.labSectionDao.get_all()

            self.assertEqual(expected_lab_sections, actual_lab_sections)

    def test_update(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section = LabSection()  # use id of LabSection that IS in mock fs object

            expected_response = lab_section
            actual_response = self.labSectionDao.update(lab_section)

            self.assertEqual(expected_response, actual_response)

    def test_update_does_not_exist(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section = LabSection()  # use id of LabSection that is NOT in mock fs object

            with self.assertRaises(Exception):
                self.labSectionDao.update(lab_section)

    def test_delete(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section = LabSection()  # use id of LabSection that IS in mock fs object

            expected_response = lab_section

            actual_response = self.labSectionDao.delete(lab_section)

            self.assertEqual(expected_response, actual_response)

    def test_delete_does_not_exist(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section = LabSection()  # use id of LabSection that is NOT in mock fs object

            with self.assertRaises(Exception):
                self.labSectionDao.delete(lab_section)

    def test_save(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section = LabSection()  # use id of LabSection that is NOT in mock fs object

            expected_response = lab_section

            actual_response = self.labSectionDao.save(lab_section)

            self.assertEqual(expected_response, actual_response)

    def test_save_already_exists(self):
        with patch('fileSystemLabSectionDaoImpl.open', mock_open(read_data=self.mocked_lab_section_data), create=True) as m:
            lab_section = LabSection()  # use id of LabSection that IS in mock fs object

            with self.assertRaises(Exception):
                self.labSectionDao.save(lab_section)
