# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:55:44 2024

@author: Danny
"""

import unittest
import PyPDF2
import os
import tempfile
from pdf_manager import merge_pdf, rotate_pdf, encrypt_pdf, decrypt_pdf

class TestPDFManager(unittest.TestCase):
    
    def setUp(self):
        # Create temporary PDF files for testing
        self.temp_files = []
        
        # Create a sample PDF file for merging and rotating
        for i in range(2):
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
            self.temp_files.append(temp_file.name)
            writer = PyPDF2.PdfWriter()
            # Corrected line to create a blank page
            writer.add_page(PyPDF2.PageObject.create_blank_page(width=200, height=200))
            with open(temp_file.name, 'wb') as f:
                writer.write(f)
        
        # Create a password for testing encryption/decryption
        self.password = 'testpassword'
    
    def tearDown(self):
        # Remove temporary files after tests
        for temp_file in self.temp_files:
            os.remove(temp_file)

    def test_merge_pdf(self):
        output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf').name
        merge_pdf(self.temp_files, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_rotate_pdf(self):
        input_file = self.temp_files[0]
        output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf').name
        rotate_pdf(input_file, output_file, 0, 90)  # Rotate the first page
        with open(output_file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            self.assertEqual(reader.pages[0].get('/Rotate'), 90)  # Check if rotation was applied
        os.remove(output_file)  # Clean up

    def test_encrypt_pdf(self):
        input_file = self.temp_files[0]
        output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf').name
        encrypt_pdf(input_file, output_file, self.password)
        self.assertTrue(os.path.exists(output_file))  # Check if output file exists

        # Check if the file is encrypted
        reader = PyPDF2.PdfReader(output_file)
        self.assertTrue(reader.is_encrypted)

        os.remove(output_file)

    def test_decrypt_pdf(self):
        # First encrypt the file
        encrypted_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf').name
        encrypt_pdf(self.temp_files[0], encrypted_file, self.password)

        # try to decrypt it
        decrypted_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf').name
        decrypt_pdf(encrypted_file, decrypted_file, self.password)
        self.assertTrue(os.path.exists(decrypted_file))  # Check if output file exists

      
        reader = PyPDF2.PdfReader(decrypted_file)
        self.assertFalse(reader.is_encrypted)

        os.remove(encrypted_file)
        os.remove(decrypted_file)

if __name__ == '__main__':
    unittest.main()
