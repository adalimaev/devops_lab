from setuptools import setup, find_packages

setup(
    name='watcher',
    packages=find_packages(),
    version='0.1',
    author='Aliaksandr Dalimayeu',
    author_email='aliaksandr_dalimayeu@epam.com',
    description='Gets common system information '
                'every given time interval and writes to the txt|json file.',
    license="MIT"
)
