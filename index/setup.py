

from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['annoy==1.15.0', 'google-api-python-client']

setup(
    name='embeds-index-builder',
    version='v0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description=''
)
