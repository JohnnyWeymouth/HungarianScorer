import setuptools
import os
from _version import __version__ as version

with open("README.md", "r", encoding="utf-8") as fh:
    longDescription = fh.read()

requirements = ""
with open("HungarianScorer/requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

requirements = requirements.split("\n")

def listFolders(directory: str) -> list:
    """Creates a list of all the folders in a directory.

    Args:
        directory (str): the directory to search

    Returns:
        list: A list of all the folders in the directory
    """
    folders = []
    for item in os.listdir(directory):
        itemPath = os.path.join(directory, item)
        if os.path.isdir(itemPath) and item != "__pycache__":
            folders.append(itemPath)
    otherFolders = [listFolders(itemPath) for itemPath in folders]
    for folder in otherFolders:
        folders.extend(folder)
    return folders

folderPath = "HungarianScorer"
folders = listFolders(folderPath)
folders.append("HungarianScorer")
print(folders)

setuptools.setup(
    name='HungarianScorer',
    version=version,
    author='Johnny Weymouth',
    author_email='johnnycweymouth@gmail.com',
    description='This package makes finding optimal combinations using the hungarian algorithm dead simple.',
    long_description=longDescription,
    long_description_content_type="text/markdown",
    url='https://github.com/johnnyweymouth/HungarianScorer.git',
    project_urls = {
        "Bug Tracker": "https://github.com/johnnyweymouth/HungarianScorer/issues"
    },
    packages=folders,
    install_requires=requirements,
    package_data={"": ["*.json", "*.txt"]},
)