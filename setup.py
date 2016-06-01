#!/usr/bin/env python3.5
# coding: utf-8

from __future__ import absolute_import, division, generator_stop, print_function, unicode_literals

__doc__ = """
jmoldow-lift-pycon-2016: Solution to Lift Challenge (codelift.org).
Copyright (C) 2016  Jordan Moldow <jmoldow@alum.mit.edu>

This file is part of jmoldow-lift-pycon-2016.

jmoldow-lift-pycon-2016 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

jmoldow-lift-pycon-2016 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with jmoldow-lift-pycon-2016.  If not, see <http://www.gnu.org/licenses/>.
"""

from os.path import dirname, join
import sys

from setuptools import setup

import jmoldow_lift_pycon_2016


def main():
    base_dir = dirname(__file__)
    setup(
        name=jmoldow_lift_pycon_2016.__program_name__,
        version=jmoldow_lift_pycon_2016.__version__,
        description=(
            'My solution to the Lift Challenge (codelift.org) for PyCon 2016,'
            ' using github.com/kingsawyer/python_lift_api.'
        ),
        long_description=open(join(base_dir, 'README.md'), encoding='utf-8').read(),
        author='Jordan Moldow',
        author_email='jmoldow@alum.mit.edu',
        url='https://github.com/jmoldow/lift-pycon-2016',
        py_modules=['jmoldow_lift_pycon_2016'],
        install_requires=['websocket-client'],
        license='GNU General Public License, Version 3 or any later version, http://www.gnu.org/licenses/',
        entry_points={
            'console_scripts': [
                'jmoldow-lift-pycon-2016=jmoldow_lift_pycon_2016:console_script_main',
            ],
        },
    )


if __name__ == '__main__':
    main()
