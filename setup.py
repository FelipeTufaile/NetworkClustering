from setuptools import setup, find_packages

setup(
    name='NetworkClustering',
    version='0.1.0',
    description='Utility function for clustering a network of sub-clusters that have common elements between each other',
    author='Felipe Tufaile',
    author_email='f.tufaile@Jgmail.com',
    url='https://github.com/FelipeTufaile/NetworkClustering',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'times==0.7',
        'os-sys==2.1.4',
    ],
    classifiers=[
        'Intended Audience :: Public in general',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
