# re for humans


## Introduction

### We seem to want a more "human" alternative to the regex syntax

`re` package is a powerful string-matching tool, conveniently included in Python standard library.
You could say that especially with
[f-strings and verbose multiline regular expressions](https://death.andgravity.com/f-re), they can
even be somewhat readable and maintainable.

But, most of us do not use `re` daily, and using it is always a bit of a struggle, requiring a visit
to Stack Overflow. `re` is not broken, but there is certainly an itch to make it easier. Over the
years many have scratched that itch, and it seems that there is another "regular expressions for
humans" package on PyPI every month.

### Look before you leap

Instead of writing my own, I wanted to take a look at what is already there.

I started with awesome lists, but to my surprise the awesome lists I visited did not have a separate 
section for regular expressions, even if by numbers they would certainly warrant one.

A consequent search through PyPI and Github resulted in the list here, compiling my opinionated
research notes on the main options.

If you are:
- Looking for a tool: Check the list to get a quick idea of the "look and feel" of each package.
- Thinking about building a tool: Check the list for alternative approaches, and maybe consider if
  contributing to an existing package might be a better way to get what you need.
- Building a tool, or already have one: Use the list to clarify and communicate what the main
  differences and strengths of your solution will be.

### Types

I have divided the packages I found into the following non-scientific and possibly overlapping
categories:


#### 1. Regular expression generation

Examples:
[PythonVerbalExpressions](https://github.com/VerbalExpressions/PythonVerbalExpressions),
[pregex](https://github.com/manoss96/pregex), [humre](https://github.com/asweigart/humre),
[edify](https://github.com/luciferreeves/edify), [mre](https://github.com/alvarofpp/mre),
[regularize](https://github.com/georgepsarakis/regularize),
[objective_regex](https://github.com/VRGhost/objective_regex),
[re_patterns](https://github.com/Nagidal/re_patterns),
[reggie-dsl](https://github.com/romilly/reggie-dsl),
[gekkota](https://github.com/courage-tci/gekkota), etc.

This seems to be the category with most examples, by far. Basic idea here is that instead of
`compile(r"\d+")`, you have e.g. `one_or_more(digit)`, and thus something that is easier to read and
easier to maintain, even if much more verbose.

The challenge is that you still need to be a "regex expert" to build expressions that
actually do what you thought they would do. But if you are lucky, though, you can find something
like `email()` in one these, all ready and matching your use case.


#### 2. String parsing

Examples: [parse](https://github.com/r1chardj0n3s/parse),
[simplematch](https://github.com/tfeldmann/simplematch),
[pygrok](https://github.com/garyelephant/pygrok)

These packages focus on having a very clear and simple syntax for the pattern string, at the cost of
versatility.


#### 3. Alternate syntax

Examples: [kleenex](https://github.com/sonoflilit/kleenexp),
[reb](https://github.com/workingenius/reb),
[abnormal-expressions](https://github.com/Buscedv/abnormal-expressions)

These packages focus on providing an alternative syntax that is intended to be comparable and in
some way superior to the regular expression syntax, with a similar level of completeness and
generality. Simplicity is probably not your main driver for picking one of these.


## Packages

Following tables show examples of several packages per category. To get a quick impression of what 
each looks like in use, we use the same simple matcher that in `re` would be:

```regexp
r"r"(?P<title>.+) (\(|\[)(?P<key>[A-Z]+)-(?P<number>\d+)(\)|\])""
```

matching e.g. `"This is a title [KEY-123]"`.

Issues or PRs are very welcome, if you want to fix or expand the list.


### 1. Regular expression generation


### PythonVerbalExpressions [➚](https://github.com/VerbalExpressions/PythonVerbalExpressions)

Partial Python implementation of a cross-language concept.

Example:
```python
pattern = (
    VerEx().
    anything().
    then(" ").
    then("[").
    OR("(").
    anything().
    then("-").
    anything().
    then("]").
    OR(")")
)
```

Notes:
- 1.6k stars but last commit in 2020.
- Version exists for [almost any language](http://verbalexpressions.github.io), polyglots can in
  theory transfer their knowledge.
- Python documentation is missing, had to consult the JSVerbalExpressions docs for capture
  group syntax, and then look at the code to see that the Python version did not support it.
- No type hinting means that IDE could not offer completions after the first dot.


### pregex [➚](https://github.com/manoss96/pregex)

Comprehensive implementation that can support both additive and flow styles.

Example:
```python
pattern = (
    Capture(OneOrMore(Any()), name="title") +
    " " +
    Either("(", "[") +
    Capture(OneOrMore(AnyUppercaseLetter()), name="key") +
    "-" +
    Capture(OneOrMore(AnyDigit()), name="number") +
    Either(")", "]")
)
```

Or using the functional/flow syntax:


Notes:
- 600 stars, very recent and active.
- Supports both plus-style and functional/flow style of building patterns.
- Has much more verbose imports when compared to other packages sampled here, which means you might
  need to use many * imports to get help from code completion.
- Even though the example above shows named capture groups, the API seems to currently miss a match
  method that would return the groups in a dict, with keys.
- Comprehensive documentation, need to use the search function if code completion is not enough.
  Missing a cheat sheet for quick look-up, I think.
- Some international support like `AnyGreekLetter()`.
- Nice package of
  [essentials](https://pregex.readthedocs.io/en/latest/documentation/modules/meta/essentials.html)
  or pre-made regexs.


### humre [➚](https://github.com/asweigart/humre)

Straight-forward regexp construction.

Example:
```python
pattern = (
    group(SOMETHING) +
    " " +
    noncap_group(either(OPEN_PARENTHESIS, OPEN_BRACKET)) +
    group(one_or_more(LETTER)) +
    "-" +
    group(one_or_more(DIGIT)) +
    noncap_group(either(CLOSE_PARENTHESIS, CLOSE_BRACKET))
)
```

Notes:
- 250 stars, very recent and well publicized.
- Seems well suited if you are used to writing a `re` regex and just write `humre` instead, as the
  conversion seems quite natural. On the flipside, I managed to write a non-compiling regex with
  humre, something I did not manage with the other packages here.
- Nice cheat sheets for quick function lookup.
- No support for named capture groups.
- Took the most time for me fighting with this to get the result I wanted.


### 2. String parsing

### parse [➚](https://github.com/r1chardj0n3s/parse)

"`parse()` is the opposite of `format()`"

Example:
```python
"{title} [{key:l}-{id:d}]"
```

Notes:
- 1.5k stars, last commits in early 2021.
- Ideal if you are already a power user of the [format specification mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language).
- Format specifiers mean that matching values are returned already converted to the right format
  (`id` in the example is returned as an `int`).
- There seems to be no support for matching "either this or that".
- If there is no match, nothing is returned, and there is no regex to print out to determine what
  went wrong.

### simplematch [➚](https://github.com/tfeldmann/simplematch)

As simple as it gets.

Example:
```python
"{title} ({key}-{id:int})"
```

Notes:
- Delivers on the promised simplicity, you probably do not need to reach for the docs when using it.
- Return value is just a dictionary, so no need to wonder how to get the actual matches out of the
  return value.
- Downside of the focus on simplicity is that there is no support for matching "either this or
  that", optional or a specific number of characters, or for searching several matches within a
  string.
- But there is support for defining specific format matchers as regexes (which seems a bit ironic
  to me).

### pygrok [➚](https://github.com/garyelephant/pygrok)

For those who grok grok?

Could be something like:
```python
"%{GREEDYDATA:title} [%{WORD:key}-%{NUMBER:id}]"
```

Notes:
- ... but I could not make it work, getting a re compiling error.
- Which is probably because pygrok had last commits in 2016.
- Includes a large [library](https://github.com/garyelephant/pygrok/tree/master/pygrok/patterns) of
  regular expressions as reusable patterns.
