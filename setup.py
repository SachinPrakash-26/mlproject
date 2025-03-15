from setuptools import find_packages, setup
from typing import List
import os

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found!")
        return requirements  # Return an empty list if file is missing
    
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]  # Remove newlines and empty lines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sachin',
    author_email='sachinprakash2698@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
