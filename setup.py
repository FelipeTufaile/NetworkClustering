from setuptools import setup, find_packages

setup(
    name='smoalib',
    version='0.1.0',
    description='Utility function for data practioners',
    author='Felipe Tufaile',
    author_email='TufaileFelipeM@JohnDeere.com',
    url='https://githubcloud.deere.com/JDFSalesMarketingOperationalAnalytics/smoafun',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'DateTime==5.1',
        'python-dateutil==2.8.2',
    ],
    classifiers=[
        'Intended Audience :: SMOA Data Practioners',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)