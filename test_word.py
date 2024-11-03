# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:40:57 2024

@author: Danny
"""

import os
import unittest
from word_manager import create_file, get_full_text 

class TestWordDocumentManager(unittest.TestCase):

    def setUp(self):
        self.filename = "test_document.docx"
        create_file(self.filename)  # Create the test document

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_document_creation(self):
        self.assertTrue(os.path.exists(self.filename))

    def test_get_full_text(self):
        expected_text = (
            "Heading 1\n"
            "Subheading under Heading 1\n"
            "This is a paragraph under Heading 1.\n"
            "Heading 2\n"
            "Subheading under Heading 2\n"
            "This is a paragraph under Heading 2."
        )
        full_text = get_full_text(self.filename)
        self.assertEqual(full_text.strip(), expected_text.strip())

if __name__ == "__main__":
    unittest.main()
