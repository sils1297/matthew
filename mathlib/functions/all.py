__author__ = 'lasse'

from mathlib.functions import general

commands = {
    "exit": general._exit,
    "print": general._print,
    "return": general._return,
    "let": general.let,
    "eval": general.save_eval
}
