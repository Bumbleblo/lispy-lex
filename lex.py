import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str

r"(?P<token>[\(\)])|(?P<symbol>[a-zA-Z]\w*)|(?P<number>\d+(?:\.\d+)?)"

tokens = [
    "\'",
    "\".*\"",
    "\.{3}",
    "\.\.\.",
    "[a-zA-Z+-\.\/<=>!?:$%_&~\^][a-zA-Z+-\.\/<=>!?:$%_&~\^0-9]*",
    "[\/+-]",
]

def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    # symbol : regex
    patterns = {
        'n-comentario': ';.*$',
        'LPAR': r'\(',
        'RPAR': r'\)',
        'STRING': r'\".*\"',
        'BOOL': r'#[tf]',
        'CHAR': r'#\\[\w\\]+',
        'NUMBER': r'(?:#[eibodx])?[+-]?\d+(?:\.\d+)?',
        'NAME': rf"{'|'.join(tokens)}",
    }

    pattern = ''

    for key, value in patterns.items():

        if re.match('n\-\w+', key):
            pattern += f'(?:{value})|'
        else:
            pattern += f'(?P<{key}>{value})|'

    pattern = pattern[:-1]
    pattern = re.compile(pattern)


    result = [ ]

    for each in pattern.finditer(code):
        if each.lastgroup != None:
            result.append(Token(each.lastgroup, each.group()))

    return result


if __name__ == '__main__': 

    # Just for try some tests besides pytest
    with open('code.scheme') as code:

        for line in code.readlines():

            tokenized_code = lex(line)

            [print(token) for token in tokenized_code]
