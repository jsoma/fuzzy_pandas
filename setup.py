from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fuzzy_pandas',
    version='0.1',
    description='Fuzzy matching in pandas using csvmatch',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/jsoma/fuzzy_pandas',
    author='Jonathan Soma',
    author_email='jonathan.soma@gmail.com',
    license='MIT',
    packages=['fuzzy_pandas'],
    install_requires=[
        'pandas',
        'csvmatch'
    ],
    keywords='fuzzy matching pandas',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities'
    ]
)
