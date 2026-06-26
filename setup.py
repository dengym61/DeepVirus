"""
VIRUS
A tool to fit mechanistic models to deep mutational scanning data
"""
import sys
from setuptools import setup, find_packages

short_description = "A tool to fit mechanistic models to deep mutational scanning data".split("\n")[0]


try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = None

setup(
    name='deepvirus',
    author='Yamin Deng',
    author_email=' dengym61@163.com',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
     version='0.1.0', 
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
        scripts=[
        'deepvirus/bin/run_virus.py', 
        'deepvirus/bin/demo_virus.py'],
    package_data={'deepvirus': [
        'data/model_design.txt',
   
        'data/VIRUS_input_format.RData']},
)
