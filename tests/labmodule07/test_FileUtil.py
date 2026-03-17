import logging
import unittest
import tempfile
import os

from typing import List

from ipp.exercises.labmodule07.FileUtil import FileUtil

class FileUtilTest(unittest.TestCase):
    TEST_PATH = tempfile.gettempdir()
    TEST_FILE = "IppTestFile.txt"

    @classmethod
    def setUpClass(self):
        logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
        logging.info("Testing FileUtil class...")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # --- Helper Methods ---

    def _createTestFileName(self) -> str:
        fileName = os.path.join(tempfile.gettempdir(), FileUtilTest.TEST_FILE)
        return fileName

    def _createTestData(self) -> str:
        testData = "Test data only. Nothing to see here."
        return testData

    # --- Test Methods ---

    def testReadFile(self):
        fileName = self._createTestFileName()
        testData = self._createTestData()

        # write the file first to make sure it exists
        FileUtil.writeTextFile(fileName = fileName, content = testData)

        # load the data
        loadedData = FileUtil.readTextFile(fileName = fileName)

        # check if it matches the data just written
        self.assertEqual(loadedData, testData)

    def testWriteFile(self):
        fileName = self._createTestFileName()
        testData = self._createTestData()

        self.assertTrue(FileUtil.writeTextFile(fileName = fileName, content = testData))

        loadedData = FileUtil.readTextFile(fileName = fileName)

        self.assertEqual(loadedData, testData)

    def testDoesFileExist(self):
        fileName = self._createTestFileName()

        # write the file first to make sure it's there
        self.testWriteFile()

        self.assertTrue(FileUtil.fileExists(fileName = fileName))

    def testDoesPathExist(self):
        dirName = tempfile.gettempdir()

        self.assertTrue(FileUtil.directoryExists(dirName = dirName))