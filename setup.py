from setuptools import setup, find_packages

from typing import List
hyphen_dot='-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)
    return requirements
setup(
    name="ml_project1",
    version="0.1",
    author="Vishwajeet",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)