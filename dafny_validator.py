import sys
from antlr4 import *

from DafnyLexer import DafnyLexer
from DafnyParser import DafnyParser
from valid_file_listener import DafnyValidatorListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DafnyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DafnyParser(stream)
    tree = parser.translation_unit()

    dafnyValidatorListener = DafnyValidatorListener()
    tree.enterRule(dafnyValidatorListener)


if __name__ == '__main__':
    main(sys.argv)