'''
Project: uas
Created: Wed, 21st Dec 2022 3:47:14 PM
Author : F. Waskito
'''

import os
import shutil
import tkinter
from tkinter import filedialog as fd

def open_file():
    """Sebuah fungsi untuk membuka file melalui popup dialog

    Args:

    Returns:
        str: sumber path
    """
    root = tkinter.Tk()
    root.wm_withdraw()
    curr_directory = os.getcwd()            # current working directory
    source_path = fd.askopenfilename(
                        initialdir=curr_directory, 
                        title="Select Image", 
                        filetypes=[('Image Files', '*.jpg')])
    root.destroy()                          # force close the root dialog
    return source_path

def upload_file():
    """Sebuah fungsi untuk mengunggah file--menyalin file dari path 
    sumber ke path destinasi.

    Args:

    Returns:
        str: nama file yang telah diunggah pada path destinasi
    """
    curr_directory = os.getcwd()
    source_path = open_file()
    uploaded_file_name = os.path.basename(source_path)
    uploaded_path = os.path.join(curr_directory, uploaded_file_name)
    shutil.copyfile(source_path, uploaded_path)
    os.chdir(curr_directory)
    return uploaded_file_name

uploaded_file_name = upload_file()
print(f"Uploaded file name: {uploaded_file_name}\n")
for file in os.listdir(os.getcwd()):
    print(file)
