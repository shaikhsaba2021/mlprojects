from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'

##the function get_requirements takes a single argument file_path, which should be a string. The function is expected to return a list of strings. The purpose of this function is likely to read the specified file and extract a list of requirements, which could be anything from software dependencies to project specifications, depending on the context in which this function is used.
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    reuirements=[]
    with open(file_path) as file_obj:
        reuirements=file_obj.readlines()
        reuirements=[req.replace("\n","") for req in reuirements]

        if HYPEN_E_DOT in reuirements:
            reuirements.remove(HYPEN_E_DOT)

    return reuirements            





setup(
    name='mlproject',
    version='0.0.1',
    author='Saba'
    author_email='shaikhsaba903@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(requirement.txt)
)