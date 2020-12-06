# token.py
from enum import Enum, auto


class Type(Enum):
    EOF = auto()
    UNIDENTIFIED = auto()
    IDENTIFIER = auto()
    VAR_DECLARATION = auto()

    SCALAR = auto()
    BOOL = auto()
    MATRIX = auto()
    STRING = auto()

    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUAL_TO = auto()
    NOT_EQUAL_TO = auto()

    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()

    OP_ROUND_BRACKET = auto()
    CL_ROUND_BRACKET = auto()
    OP_SQUARE_BRACKET = auto()
    CL_SQUARE_BRACKET = auto()
    OP_CURLY_BRACKET = auto()
    CL_CURLY_BRACKET = auto()
    OP_ANGLE_BRACKET = auto()
    CL_ANGLE_BRACKET = auto()

    LESS_THAN = auto()
    GREATER_THAN = auto()
    LESS_OR_EQUAL_TO = auto()
    GREATER_OR_EQUAL_TO = auto()

    AND = auto()
    OR = auto()
    NOT = auto()
    FUNCTION = auto()
    RETURN = auto()


class Symbol:
    special_characters = {
        '(': Type.OP_ROUND_BRACKET,
        ')': Type.CL_ROUND_BRACKET,
        '[': Type.OP_SQUARE_BRACKET,
        ']': Type.CL_SQUARE_BRACKET,
        '{': Type.OP_CURLY_BRACKET,
        '}': Type.CL_CURLY_BRACKET,
        '<': Type.OP_ANGLE_BRACKET,
        '>': Type.CL_ANGLE_BRACKET,
        '*': Type.MULTIPLY,
        '/': Type.DIVIDE,
        '+': Type.PLUS,
        '-': Type.MINUS,
        ';': Type.SEMICOLON,
        ',': Type.COMMA,
        '.': Type.DOT,
        '!': Type.NOT,
        '=': Type.ASSIGN
    }

    double_operators = {
        '<=': Type.LESS_OR_EQUAL_TO,
        '>=': Type.GREATER_OR_EQUAL_TO,
        '==': Type.EQUAL_TO,
        '!=': Type.NOT_EQUAL_TO
    }

    special_words = {
        'and': Type.AND,
        'or': Type.OR,
        'var': Type.VAR_DECLARATION,
        'true': Type.BOOL,
        'false': Type.BOOL,
        'return': Type.RETURN,
        'function': Type.FUNCTION,
    }


class Token:
    def __init__(self, token_type=Type.IDENTIFIER, value="", line=None, column=None):
        self.token_type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"{self.token_type}\t\tvalue={self.value}\t\tposition=({self.line}, {self.column})"
