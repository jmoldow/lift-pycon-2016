#!/usr/bin/env python3.5
# coding: utf-8

from __future__ import absolute_import, division, generator_stop, print_function, unicode_literals

import argparse
import sys
import traceback


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


__program_notice__ = """
jmoldow-lift-pycon-2016: Solution to Lift Challenge (codelift.org).

jmoldow-lift-pycon-2016  Copyright (C) 2016  Jordan Moldow <jmoldow@alum.mit.edu>
This program comes with ABSOLUTELY NO WARRANTY; for details run
`jmoldow-lift-pycon-2016 -w'.
This is free software, and you are welcome to redistribute it
under certain conditions; run
`jmoldow-lift-pycon-2016 -c' for details.
"""


__program_name__ = 'jmoldow-lift-pycon-2016'
__program_warranty__ = __doc__
__version__ = '0.0.1'


with open('COPYING') as license_file:
    __license__ = license_file.read()


def construct_parser():
    parser = argparse.ArgumentParser(
        prog=__program_name__,
        description=__program_notice__,
        formatter_class=type(
            '_FormatterClass',
            (
                argparse.RawTextHelpFormatter,
                argparse.ArgumentDefaultsHelpFormatter,
                argparse.MetavarTypeHelpFormatter,
            ),
            {},
        ),
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=__version__,
    )
    parser.add_argument(
        '-w', '--warranty',
        action='store_true',
        help="show program's warranty and exit",
    )
    parser.add_argument(
        '-c', '--conditions',
        action='store_true',
        help="show program's conditions and exit",
    )
    return parser


parser = construct_parser()
__doc__ = parser.format_help()


def jmoldow_lift_pycon_2016():
    """Solution to Lift Challenge (codelift.org)."""
    pass


def main(*args):
    args = parser.parse_args(args)
    if args.warranty:
        print(__program_warranty__)
        return 0
    if args.conditions:
        print(__license__)
        return 0
    result = jmoldow_lift_pycon_2016()
    return 0


main.__doc__ = __doc__


def console_script_main():
    try:
        sys.exit(main(*sys.argv[1:]) or 0)
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    console_script_main()
