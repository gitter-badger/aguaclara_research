"""
Setup script.
"""

from distutils.core import Command
from setuptools import setup


class Coverage(Command):
    """
    Coverage setup.
    """

    description = (
        "Run test suite against single instance of"
        "Python and collect coverage data."
    )
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import coverage
        import unittest

        cov = coverage.coverage(config_file='.coveragerc')
        cov.erase()
        cov.start()

        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(start_dir='tests')
        unittest.TextTestRunner().run(test_suite)

        cov.stop()
        cov.save()
        cov.report()
        cov.html_report()


setup(
    author='AguaClara',
    author_email='aguaclara@cornell.edu',
    description='aguaclara_research',
    download_url='',
    cmdclass={
        'coverage': Coverage,
    },
    install_requires=['aide_design'],
    license='Apache License (2.0)',
    name='aguaclara_research',
    packages=[
        'aguaclara_research',
    ],
    scripts=[],
    test_suite='tests',
    tests_require=[
        'codecov>=2.0.3,<3.0.0',
        'coverage>=4.0.3,<5.0.0',
        'Sphinx>=1.4.1,<2.0.0',
        'tox>=2.3.1,<3.0.0',
        'virtualenv>=15.0.1,<16.0.0'
    ],
    include_package_data=True,
    url='https://github.com/AguaClara/aguaclara_research',
    version='1.0.6'
)
