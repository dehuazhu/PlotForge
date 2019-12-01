#####################################
# Module importPics
# Description: imports
# Author: Martina Buck
##################################


# import packages
import os
from zipfile import ZipFile


# classes and functions


def extractZips(base_dir, rel_dir, bandwidths):
    """
    A parsing function for zip-files with images of the structure:
    1) extract zip-files from a relative directory (contained in a base directory) in a folder unzipped/bandwidths[i]
    2) expected names of the files contained in the zip-files:
        String + bandwidths[i] + ".tiff"
    """
    # Scan through the directory and record the files
    lister = os.listdir(base_dir + rel_dir)

    for i in range(len(lister)):
        zipF = ZipFile(base_dir + rel_dir + lister[i], 'r')
        for tiffName in zipF.namelist():
            for bandwidth in bandwidths:
                if tiffName.endswith(bandwidth + '.tiff'):
                    zipF.extract(tiffName, base_dir + "unzipped/" + bandwidth)

    return base_dir + "unzipped"


def whatDoesntWork():
    print("The import of the package works.")

# main function for testing
