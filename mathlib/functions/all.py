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
import numpy

from mathlib.functions import general, plotting, imaging, barcoding

commands = {
    "exit": general._exit,
    "print": general._print,
    "echo": general._print,
    "return": general.save_eval,
    "let": general.let,
    "eval": general.save_eval,
    "plot": plotting.plot,
    "help": general.help,
    "load": imaging.load,
    "execute": general.execute,
    "blur": barcoding.convolute,
    "mmult": barcoding.mmult,
    "vmult": barcoding.vmult,
    "disturb": barcoding.disturb,
    "#": general.comment,
    "//": general.comment,
    "vars": general.vars,
    "del": general._del,
}

import math


def binarize(x, threshold):
    res = []
    for val in x:
        if val < threshold:
            res.append(0)
        else:
            res.append(1)
    return numpy.array(res)

glob_vars = {
    "ans": None,
    "sin": math.sin,
    "cos": math.cos,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "asin": math.asin,
    "acos": math.acos,
    "asinh": math.asinh,
    "acosh": math.acosh,
    "exp": math.exp,
    "e": math.e,
    "pi": math.pi,
    "pow": pow,
    "blur_matrix": barcoding.blur_matrix,
    "img_blur_matrix": barcoding.ext_blur_matrix,
    "ones": numpy.ones,
    "zeros": numpy.zeros,
    "eye": numpy.eye,
    "eps": numpy.finfo(float).eps,
    "svd": lambda x, compute_uv=False: numpy.linalg.svd(numpy.matrix(x), compute_uv=compute_uv),
    "len": lambda x: len(x),
    "shape": lambda x: numpy.matrix(x).shape,
    "transpose": lambda x: numpy.matrix(x).transpose(),
    "average": lambda x: numpy.average(x),
    "binarize": binarize,
    "condition": lambda val: numpy.linalg.cond(numpy.matrix(val)),
    "invert": lambda x: numpy.matrix(x).I
}
