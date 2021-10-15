#!/usr/bin/python3
## @file

#
#    khoca/__init__.py --- Part of khoca, a knot homology calculator
#
# Copyright (C) 2021 Sebastian Oehms <seb.oehms@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# The file to be run by the user.
# The main work is done by pui.pyx via run_commandline, which is called
# by this file.

from .khoca import run_commandline


class InteractiveCalculator:
    r"""
    Class to allow the usage of *Khoca* interactively in a Python session.

    EXAMPLES::

        >>> from khoca import InteractiveCalculator
        >>> KH = InteractiveCalculator('0', '0.0', '0')
        >>> KH('braidaBaB', 'calc0')
        Frobenius algebra: Z[X] / (1*X^2).
        [[[-2, 4, 0, 1], [-1, 2, 0, 1], [0, 0, 0, 1], [1, -2, 0, 1], [2, -4, 0, 1],
          [-2, 4, 0, 0], [-1, 4, 0, 0], [-1, 2, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0],
          [1, 0, 0, 0], [1, -2, 0, 0], [2, -2, 0, 0]], [[-2, 3, 0, 1], [-2, 5, 0, 1],
          [-1, 1, 0, 1], [-1, 3, 0, 1], [0, -1, 0, 1], [0, 1, 0, 1], [1, -3, 0, 1],
          [1, -1, 0, 1], [2, -5, 0, 1], [2, -3, 0, 1], [-1, 3, 2, 1], [-2, 3, 0, -1],
          [-1, 3, 0, -1], [-2, 5, 0, 0], [-1, 5, 0, 0], [-1, 1, 0, 0], [0, 1, 0, 0],
          [-1, 3, 0, 0], [0, 3, 0, 0], [0, -1, 0, 0], [1, -1, 0, 0], [0, 1, 0, 0],
          [1, 1, 0, 0], [2, -3, 2, 1], [1, -3, 0, -1], [2, -3, 0, -1], [1, -1, 0, 0],
          [2, -1, 0, 0]]]
        >>> res, mess = KH('braidaaa', 'calc0', print_messages=True); mess
        ['Result:', 'Reduced Homology:', 'Non-equivariant homology:',
         't^-3q^8 + t^-2q^6 + t^0q^2', 'Unreduced Homology:',
         'Non-equivariant homology:', 't^-3q^9 + t^-2q^5 + t^0q^1 + t^0q^3 + t^-2q^7[2]']
    """
    def __init__(self, coefficient_ring, frobenius_algebra, root):
        r"""
        Constructor

        INPUT:

            - ``coefficient_ring`` -- coefficient ring of the homology 

        EXAMPLES::
        """
        if type(coefficient_ring) == int:
            self._coefficient_ring = '%s' %coefficient_ring
        elif type(coefficient_ring) == str:
            self._coefficient_ring = coefficient_ring
        else:
            raise TypeError('Coefficient ring must be declared by an integer or string')
        if type(frobenius_algebra) in  (tuple, list):
            self._frobenius_algebra = '%s' %list(frobenius_algebra)
        elif type(frobenius_algebra) == str:
            self._frobenius_algebra = frobenius_algebra
        else:
            raise TypeError('Frobenius algebra must be declared by a tuple, list or string')
        if type(root) == int:
            self._root = '%s' %root
        elif type(root) == str:
            self._root = root
        else:
            raise TypeError('Root must be declared by an integer or string')

    def __call__(self, link, command, print_messages=False):
        r"""
        Instance call to apply the calculator to a link with
        respect to a certain command.

        INPUT:

            - ``link`` -- the link as a string in Khoca input form.

        ..NOTE:

            Stack operations are not supported at the moment.
        """
        # Todo: allow Python type inputs like tuples ..
        arg_list = [None]
        arg_list.append(self._coefficient_ring)
        arg_list.append(self._frobenius_algebra)
        arg_list.append(self._root)
        arg_list.append(link)
        arg_list.append(command)
        print_output = []
        def no_print(s):
            print_output.append(s)
        res = run_commandline(arg_list, no_print, 0)
        if print_messages:
            return res, print_output
        return res
