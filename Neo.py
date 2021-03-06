from Interpreter.Interpreter import Interpreter
from Lexer.Lexer import Lexer
from Parser.Parser import Parser
from Lexer.Source import SourceFile, SourceString

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Pass path to Neo program to interpret", type=str)
args = parser.parse_args()

# source_string = """
# m = [[1, 2, 3][4, 5, 6][7, 8, 8]];
# m = m.transposed;

# print(m);
# print(m.det);
# """

# source = SourceString(source_string)
source = SourceFile(args.filename)
lexer = Lexer(source)
parser = Parser(lexer)

parsed_program = parser.parse_program()
interpreter = Interpreter(parsed_program)

interpreter.run()