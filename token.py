
from enum import Enum


class TokenType(Enum):
    # vtype
    VTYPE = 'vtype'

    INTEGER = 'int'
    CHAR = 'char'
    BOOLEAN = 'boolean'
    STRING = 'String'

    # Boolean String
    TRUE = 'true'
    FALSE = 'false'

    # Identifier
    ID = 'identifier'

    # Special statements
    IF = 'if'
    ELSE = "else"
    WHILE = 'while'
    CLASS = 'class'
    RETURN = 'return'

    # Arithmetic operators
    OP = 'operator'

    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'

    # Assignment operator
    ASSIGN = '='

    # Comparison operators
    LT = '<'
    GT = '>'
    EQ = '=='
    NE = '!='
    LE = '<='
    GE = '>='

    # Symbols
    SEMI = ';'
    LBLACE = '{'
    RBLACE = '}'
    LPAREN = '('
    RPAREN = ')'
    LBRACKET = '['
    RBRACKET = ']'
    COMMA = ','


# 토큰 인자 -> 이름, 값(string) 저장
class Token:
    def __init__(self, t_type, t_value):
        self.type = t_type
        self.value = t_value

