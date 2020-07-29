from aws_profile_switcher._version import __version__
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='aws-profile-switcher',
    version=__version__,
    description='This util allows you to switch default AWS CLI profile',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/99stealth/aws-profile-switcher',
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
    ],
    packages=find_packages(exclude=['aws-profile-switcher.tests']),
    include_package_data=True,
    install_requires=['configparser', 'argparse'],
    entry_points={
        'console_scripts': [
            'aws-profile-switcher=aws_profile_switcher.run:main'
        ]
    }
)