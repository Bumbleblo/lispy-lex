import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str

r"(?P<token>[\(\)])|(?P<symbol>[a-zA-Z]\w*)|(?P<number>\d+(?:\.\d+)?)"


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    # symbol : regex
    patterns = {
        'n-comentario': ';;.*$',
        'LPAR': r'\(',
        'RPAR': r'\)',
        'STRING': r'\".*\"',
        'BOOL': '#[tf]',
        'CHAR': '#\\\\\w+',
        'NUMBER': r'[+-]?\d+(?:\.\d+)?',
        'NAME': r"\'|\".*\"|\.{3}|[a-zA-Z\.\%][\w\-\?\>!]*|[\/+-]",
    }

    print(f"Code: {code}")

    pattern = ''
    for key, value in patterns.items():

        if re.match('n\-\w+', key):
            pattern += f'(?:{value})|'
        else:
            pattern += f'(?P<{key}>{value})|'

    pattern = pattern[:-1]

    print(pattern)

    pattern = re.compile(pattern)

    result = [ ]

    for each in pattern.finditer(code):

        if each.lastgroup != None:
            result.append(Token(each.lastgroup, each.group()))
        #print(each.lastgroup)
        #print(each)

    print(result)
    return result
    #return [Token('INVALIDA', 'valor inválido')]
