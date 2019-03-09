import unittest
import testFileSystemCourseDaoImpl, testFileSystemLabSectionDaoImpl, testFileSystemUserDaoImpl
import testUserService, testCourseService, testLabService

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(testFileSystemUserDaoImpl.TestFileSystemUserDaoImpl))
suite.addTest(unittest.makeSuite(testFileSystemLabSectionDaoImpl.TestfileSystemLabSectionDaoImpl))
suite.addTest(unittest.makeSuite(testFileSystemCourseDaoImpl.TestFileSystemCourseDaoImpl))
suite.addTest(unittest.makeSuite(testUserService.TestUserService))
suite.addTest(unittest.makeSuite(testCourseService.TestCourseService))
suite.addTest(unittest.makeSuite(testLabService.TestLabService))

runner = unittest.TextTestRunner()
runner.run(suite)
