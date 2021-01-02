import glob
import os
from pathlib import Path

def list_files_in_dir(directory,ext=""):
    """recursively list all files in a directory with a particular exention
    e.g. directory= /home/user/datasets, ext=".jpeg"
    """
    files = glob.glob(directory + '/**/*'+ext, recursive=True)
    files.sort()
    return files

def getDirectory(fileName):
    """Returns the directory name for the given filename
    e.g.
    fileName = "/foo/bar/foobar.txt"
    return value is "bar"
    Not much error checking though
    """
    dirName = os.path.dirname(fileName)
    return os.path.basename(dirName)


def ensurePath(path):
    """Make sure that the given path exists"""
    if not path:
        return
    if not os.path.isdir(path):
        os.makedirs(path)

def create_default_file_struct(base_dir,dataset_name):
# Create a default directory to store the new dataset format
    # DEFAULT TARGET DATASET FORMAT
    # └── dataset name
    #     ├── gt
    #     │   ├── test
    #     │   ├── train
    #     │   └── val
    #     ├── images
    #     │   ├── test
    #     │   ├── train
    #     │   └── val
    #     └── image_sets
    #         ├── test.txt
    #         ├── trn.txt
    #         └── val.txt
    base_dir_dataset=os.path.join(base_dir,dataset_name+"_standardized")
    for folder in ['gt','images']:
        for subfolder in ['val','train','test']:
            dir= os.path.join(base_dir_dataset,folder,subfolder)
            Path(dir).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(base_dir_dataset,'image_sets')).mkdir(parents=True, exist_ok=True)