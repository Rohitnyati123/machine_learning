# from distutils.core import setup
from setuptools import setup, find_packages
from typing import List

PROJECT_NAME="Machine Learning Project"
VERSION="0.0.1"
DESCRIPTION="This is our machine learning project in modular coding"
AUTHOR_NAME="Rohit Nyati"
AUTHOR_EMAIL="rohit.nyati@gmail.com"

REQUIREMENTS_FILE_NAME="requirements.txt"


HYPHEN_E_DOT="-e ."
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requiremnt_file:
        requirement_list=requiremnt_file.readlines()
        requirement_list=[requirements_name.replace("\n","") for requirements_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list



setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list() 
     )