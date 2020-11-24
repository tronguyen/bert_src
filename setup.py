from setuptools import setup, find_packages

setup_info = dict(
    name='bertsrc',
    version='1.0',
    url='https://github.com/tronguyen/bert_src.git',
    author='Trong Nguyen',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "tqdm >= 4.27",
        "torch==1.6.0",
        "torchvision==0.7.0"
    ],
    description='Modules for graph embedding model',
    long_description=open('README.md').read(),
)

setup(**setup_info)
