
from aws_profile_manager._version import __version__
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='aws-profile-manager',
    version=__version__,
    description='This util allows you to manager your AWS profiles like add, remove, update and switch default AWS CLI profile',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/99stealth/aws-profile-manager',
    author='Roman Banakh',
    author_email='banakh.ri@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(exclude=['aws-profile-manager.tests']),
    include_package_data=True,
    install_requires=['configparser', 'argparse', 'click', 'boto3'],
    entry_points={
        'console_scripts': [
            'aws-profile-manager=aws_profile_manager.cli:cli'
        ]
    }
)