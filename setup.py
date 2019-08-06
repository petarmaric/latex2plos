from setuptools import find_packages, setup


setup(
    name='latex2plos',
    version='1.0.1',
    url='https://bitbucket.org/petar/latex2plos',
    license='BSD',
    author='Petar Maric',
    author_email='petarmaric@uns.ac.rs',
    description='Console app and Python API for automated preparation of your '\
                'LaTeX paper for submission in PLOS journals',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'latex2plos=latex2plos.shell:main',
        ],
    },
    install_requires=[
        'friendly_name_mixin~=1.0',
        'simple_plugins~=1.0',
        'wand~=0.5.0',
    ],
    extras_require={
        'dev': [
            'pylint~=1.9',
        ],
    },
)
