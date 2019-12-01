#####################################
# Module importPics
# Description: imports
# Author: Martina Buck
##################################


# import packages
from zipfile import ZipFile


# classes and functions


# parsing function for zip-files with images of the structure:
# Year + "-" + Month + "-" + Day + ", " + SateliteType + ", " + Bandwith + ".tiff"
def readPics(base_dir, rel_dir):
    with ZipFile('base_dir + rel_path', 'r') as zipF:
        zipTitle = ZipFile.namelist()
    for fileName in ZipFile.namelist():
        if fileName.endswith("B02.tiff"):
            zipF.extract(fileName, "B02")
        if fileName.endswith("B03.tiff"):
            zipF.extract(fileName, "B03")
        if fileName.endswith("B04.tiff"):
            zipF.extract(fileName, "B04")
        if fileName.endswith("B08.tiff"):
            zipF.extract(fileName, "B08")

def whatDoesntWork()
    print("The import of the package works.")

# main function for testing
