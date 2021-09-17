

import setuptools

REQUIRED_PACKAGES = [
    'tensorflow==1.12.0',
    'tensorflow-hub==0.2.0',
    'tensorflow-transform==0.11.0']

setuptools.setup(
    name='etl_pipeline',
    version='0.0.1',
    author='anonymous',
    author_email='anonymous@google.com',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages()
)
