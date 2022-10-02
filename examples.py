import re

import humre
import ke
import simplematch
from bourbaki.regex import ANYCHAR
from bourbaki.regex import C
from bourbaki.regex import Digit
from humre import CLOSE_BRACKET
from humre import CLOSE_PARENTHESIS
from humre import DIGIT
from humre import LETTER
from humre import OPEN_BRACKET
from humre import OPEN_PARENTHESIS
from humre import SOMETHING
from humre import either
from humre import group
from humre import noncap_group
from humre import one_or_more
from parse import parse
from pregex.core.classes import Any
from pregex.core.classes import AnyDigit
from pregex.core.classes import AnyUppercaseLetter
from pregex.core.groups import Capture
from pregex.core.operators import Either
from pregex.core.quantifiers import OneOrMore
from scanf import scanf
from verbalexpressions import VerEx

STRING_TO_MATCH = "This is a title [KEY-123]"
STRING_NO_MATCH = "[KEY-123]"

# re

pattern = re.compile(r"(?P<title>.+) (\(|\[)(?P<key>[A-Z]+)-(?P<number>\d+)(\)|\])")
match = pattern.match(STRING_TO_MATCH)
no_match = pattern.match(STRING_NO_MATCH)

assert match
assert match.groupdict() == {"title": "This is a title", "key": "KEY", "number": "123"}
assert not no_match

# PythonVerbalExpressions

pattern = VerEx().anything().then(" ").then("[").OR("(").anything().then("-").anything().then("]").OR(")")
match = pattern.match(STRING_TO_MATCH)
no_match = pattern.match(STRING_NO_MATCH)

assert match
assert not no_match

# prerex

pattern = (
    Capture(OneOrMore(Any()), name="title") +
    " " +
    Either("(", "[") +
    Capture(OneOrMore(AnyUppercaseLetter()), name="key") +
    "-" +
    Capture(OneOrMore(AnyDigit()), name="number") +
    Either(")", "]")
)

captures = pattern.get_captures(STRING_TO_MATCH)
no_captures = pattern.get_captures(STRING_NO_MATCH)

assert captures == [('This is a title', 'KEY', '123')]
assert no_captures == []

# humre

pattern = (
    group(SOMETHING) +
    " " +
    noncap_group(either(OPEN_PARENTHESIS, OPEN_BRACKET)) +
    group(one_or_more(LETTER)) +
    "-" +
    group(one_or_more(DIGIT)) +
    noncap_group(either(CLOSE_PARENTHESIS, CLOSE_BRACKET))
)

compiled = humre.compile(pattern)
match = compiled.match(STRING_TO_MATCH)
no_match = compiled.match(STRING_NO_MATCH)

assert match.groups() == ('This is a title', 'KEY', '123')
assert not no_match

# bourbaki.regex

pattern = (
    ANYCHAR[1:] ("title") +
    " [" +
    C["A":"Z"][1:] ("key") +
    "-" +
    Digit[1:] ("number") +
    "]"
)

result = pattern.match(STRING_TO_MATCH)
result_no_match = pattern.match(STRING_NO_MATCH)

assert result
assert not result_no_match

# scanf

pattern = "%s [%s-%d]"

result = scanf(pattern, STRING_TO_MATCH)
result_no_parse = parse(pattern, STRING_NO_MATCH)

assert result == ("title", "KEY", 123)
assert not result_no_parse

# parse

pattern = "{title} [{key:l}-{id:3d}]"

result = parse(pattern, STRING_TO_MATCH)
result_no_parse = parse(pattern, STRING_NO_MATCH)

assert result.named == {'title': 'This is a title', 'key': 'KEY', 'id': 123}
assert not result_no_parse

# simplematch

pattern = "{title} [{key}-{id:int}]"

match = simplematch.match(pattern, STRING_TO_MATCH)
no_match = simplematch.match(pattern, STRING_NO_MATCH)

assert match == {'title': 'This is a title', 'key': 'KEY', 'id': 123}, match
assert not no_match

# grok

pattern = "%{GREEDYDATA:title} [%{WORD:key}-%{NUMBER:id}]"

# grok = Grok(pattern)
# match = grok.match(STRING_TO_MATCH)
# no_match = grok.match(STRING_NO_MATCH)
#
# assert match == {'title': 'This is a title', 'key': 'KEY', 'id': 123}, match
# assert not no_match

# kleenexp

pattern = "[capture:title 1+ #any] ['(' | '['][capture:key 1+ #letter]-[capture:id 1+ #digit][')' | ']']"

match = ke.match(pattern, STRING_TO_MATCH)
no_match = ke.match(pattern, STRING_NO_MATCH)
assert match.groupdict() == {"title": "This is a title", "key": "KEY", "id": "123"}
assert not no_match
