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

from matplotlib import pyplot
from mathlib.functions.general import generate_function
from mathlib.output.ConsolePrinter import ConsolePrinter


def plot(*args, glob_vars={}):
    func_str, unknowns = generate_function(*args, glob_vars=glob_vars, printer=ConsolePrinter())

    ylabel = ''
    for arg in args:
        ylabel += " "+arg
    ylabel = ylabel.strip()
    pyplot.ylabel(ylabel)

    if len(unknowns) == 0:
        print("Plotting '{}' with no variables...".format(ylabel))
        x = [-10,10]
        try:
            y = eval(func_str)
            pyplot.plot(x, [y, y])
            pyplot.grid(True)
            pyplot.show()
            return True
        except:
            print("Cannot evaluate expresssion. Aborting plot...")

    if len(unknowns) == 1:
        unknown = unknowns[0]
        print("Plotting '{}' with variable '{}'...".format(ylabel, unknown))
        glob_vars[unknown] = 0
        y = []
        x = []
        evaluation_failures = 0
        for x_scaled in range(-100, 100, 1):
            glob_vars[unknown] = x_scaled/10
            try:
                s = eval(func_str)
                x.append(glob_vars[unknown])
                y.append(s)
                evaluation_failures = 0
            except:
                print("Failed evaluating function for {}={}. (Singularity?)".format(unknown, glob_vars[unknown]))
                evaluation_failures += 1
                if evaluation_failures > 10:
                    print("There were 10 evaluation failures in a row. "
                          "Assuming function is not plottable. Aborting plot...")
                    del glob_vars[unknown]
                    return False

        pyplot.plot(x, y)
        pyplot.xlabel(unknown)
        pyplot.grid(True)

        pyplot.show()

        del glob_vars[unknown]
        return True

    print("Too many unknown variables. Only up to one dimensional functions can be plotted.")
    print("Unknown variables are:", unknowns)
    return False
