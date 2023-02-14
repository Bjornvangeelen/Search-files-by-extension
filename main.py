import os
import shutil
import logging

logging.basicConfig(
    filename='Search_files.log',
    filemode='w',
    format='%(asctime)s, %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)

source = input('Input the directory u want to search for specifically files extensions: ')
ext = input('Input the extension that u want to search (.jpg, .dng, .docx): ')
destination = input('Input destination u want to copy the files to: ')

def make_destination_dir():
    if os.path.exists(destination):
        pass
        logging.debug(f'Destination "{destination}" already exists, continuing script.')
    else:
        os.chdir(source)
        os.mkdir(destination)
        logging.debug(f'Destination folder "{destination}" is created ')

def search_by_ext2():
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith(ext):
                shutil.copy(os.path.join(root, file), os.path.join(file, destination))
    logging.debug(f'All files with the extension "{ext}" where copied to "{destination}". ')

make_destination_dir()
search_by_ext2()


