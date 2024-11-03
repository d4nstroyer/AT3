# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:54:24 2024

@author: Danny
"""

import PyPDF2
from getpass import getpass

# Function to Merge PDF files
def merge_pdf(pdf_list, output):
    merger = PyPDF2.PdfMerger()
    try:
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write(output)
        print(f"Merged PDFs into '{output}' successfully.")
    finally:
        merger.close()

# Function to rotate a page in PDF
def rotate_pdf(input_file, output_file, page_number, rotation):
    with open(input_file, 'rb') as infile: # open the input PDF in read-binary mode
        reader = PyPDF2.PdfReader(infile) # read the input PDF
        writer = PyPDF2.PdfWriter() # create a new PDF writer object

        # Copy pages and rotate the specified page
        for i in range(len(reader.pages)): # loop through all pages in the PDF
            page = reader.pages[i] # get the current page by index
            if i == page_number: # check if this is the page to rotate
                page.rotate(rotation) # rotate the page clockwise
            writer.add_page(page) # add the page to the writer

        with open(output_file, 'wb') as outfile: #'wb' for write mode and binary mode, used when creating non-text files
            writer.write(outfile) # Write the contents to the output file
            print(f"Rotated page {page_number + 1} by {rotation}° in '{input_file}'.")

# Encrypt PDF
def encrypt_pdf(input_file, output_file, password):
    reader = PyPDF2.PdfReader(input_file)
    writer = PyPDF2.PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    with open(output_file, 'wb') as outfile: 
        writer.write(outfile) 
        print(f"Encrypted '{input_file}' successfully.")

# Decrypt PDF
def decrypt_pdf(input_file, output_file, password):
    reader = PyPDF2.PdfReader(input_file)

    if reader.is_encrypted:
        reader.decrypt(password)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_file, 'wb') as outfile: 
            writer.write(outfile) 
            print(f"Decrypted '{input_file}' successfully.")
    else:
        print("The file is now decrypted.")

# Function to input PDF files
def get_pdf_list():
    pdf_list = []
    while True:
        pdf_name = input("Enter PDF file name (or 'done' to finish): ")
        if pdf_name.lower() == 'done':
            break
        if not pdf_name.endswith('.pdf'):
            pdf_name += '.pdf'
        pdf_list.append(pdf_name)
    return pdf_list

def main():
    while True:
        print("\nPDF Manager - Choose an option:")
        print("1. Merge PDFs")
        print("2. Rotate a PDF Page")
        print("3. Encrypt a PDF")
        print("4. Decrypt a PDF")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
    
        if choice == '1':
                pdf = get_pdf_list()
                output = input("Enter output PDF file name: ")
                if not output.endswith('.pdf'):
                    output += '.pdf'
                merge_pdf(pdf, output)
    
        elif choice == '2':
            input_file = input("Enter input PDF file: ")
            if not input_file.endswith('.pdf'):
                input_file += '.pdf'
            output = input("Enter output PDF file: ")
            if not output.endswith('.pdf'):
                output += '.pdf'
            page_number = int(input("Enter the page number to rotate: ")) - 1
            rotation = int(input("Enter the rotation angle (90, 180, 270): "))
            rotate_pdf(input_file, output, page_number, rotation)
        
        elif choice == '3':
            input_file = input("Enter input PDF file: ")
            if not input_file.endswith('.pdf'):
                input_file += '.pdf'
            output = input("Enter output PDF file: ")
            if not output.endswith('.pdf'):
                output += '.pdf'
            password = getpass("Enter password to encrypt: ")
            encrypt_pdf(input_file, output, password)
        
        elif choice == '4':
            input_file = input("Enter input PDF file: ")
            if not input_file.endswith('.pdf'): 
                input_file += '.pdf'
            output = input("Enter output PDF file: ")
            if not output.endswith('.pdf'):
                output += '.pdf'
            password = getpass("Enter password to decrypt: ")
            decrypt_pdf(input_file, output, password)
            
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
