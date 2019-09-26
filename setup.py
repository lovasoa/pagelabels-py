from setuptools import setup, find_packages

VERSION = '1.0.2'

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Intended Audience :: End Users/Desktop',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Text Processing',
    'Topic :: Utilities'
]

setup(
    name='pagelabels',
    version=VERSION,
    description='Python library to manipulate PDF page numbers and labels.',
    long_description=open("pagelabels/README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author='Ophir LOJKINE',
    author_email='pere.jobs@gmail.com',
    url='https://github.com/lovasoa/pagelabels-py',
    keywords=['pdf', 'page labels', 'page numbers', 'title page'],
    classifiers=CLASSIFIERS,
    install_requires=['pdfrw']
)
