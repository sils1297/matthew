"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from mathlib.output.ColorPrinter import ColorPrinter
from mathlib.output.LogPrinter import LogPrinter


class NullPrinter(LogPrinter, ColorPrinter):
    def __init__(self):
        ColorPrinter.__init__(self)
        LogPrinter.__init__(self)

    def _print_uncolored(self, output, **kwargs):
        pass

    def _print_colored(self, output, color=None, **kwargs):
        pass
