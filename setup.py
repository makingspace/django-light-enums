# coding=utf-8
import os
import sys

from setuptools import setup, Command, find_packages


class RunTests(Command):

    """
    RunTests class borrowed from django-celery project
    """
    description = 'Run the django test suite from the tests dir.'
    user_options = []
    extra_args = []

    def run(self):
        from django.core.management import execute_from_command_line
        settings_module_name = 'tests.settings'
        os.environ['DJANGO_SETTINGS_MODULE'] = os.environ.get(
            'DJANGO_SETTINGS_MODULE',
            settings_module_name)
        prev_argv = sys.argv[:]

        this_dir = os.getcwd()
        testproj_dir = os.path.join(this_dir, 'tests')
        os.chdir(testproj_dir)
        sys.path.append(testproj_dir)

        try:
            sys.argv = [__file__, 'test'] + self.extra_args
            execute_from_command_line(argv=sys.argv)
        finally:
            sys.argv[:] = prev_argv

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass
setup(
    name="django-light-enums",
    version="0.1.2",
    author="MakeSpace Labs, Inc.",
    author_email="dhites@makespace.com",
    description="django-light-enums is a ligthweigth implementation of enums for Django.",
    url="https://github.com/makingspace/django-light-enums",
    license="Revised BSD",
    packages=find_packages(),
    install_requires=[
        "Django>=1.8",
        "six==1.10.0",
    ],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Database",
    ],
    cmdclass={'test': RunTests},
)
