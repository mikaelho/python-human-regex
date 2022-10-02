# re for humans


## Introduction

### We do seem to want more "human" alternatives to the regex syntax

`re` package is a powerful string-matching tool, conveniently included in Python standard library.
You could say that especially with
[f-strings and verbose multiline regular expressions](https://death.andgravity.com/f-re), they can
even be somewhat readable and maintainable.

But, most of us do not use `re` daily, and using it is always a bit of a struggle, requiring a visit
to Stack Overflow. `re` is not broken, but there is certainly an itch to make it easier. Over the
years many have scratched that itch, and it seems that there is another "regular expressions for
humans" package on PyPI every month.

### Look before you leap

I wanted to understand what is available, but a plain web search was not very successful, partly
because any related search came up with ~10 regexp tutorials for every relevant hit. Neither was
awesome list browsing very helpful - I expected to find a whole section dedicated to these regexp
helpers, but found very few listed overall. 

A consequent search through PyPI and Github resulted in the list below. The list does not cover all
packages found on PyPI - several packages were left out, either because they were too raw (no
documentation) or likely dead (last activity more than 3 years ago).

The list could be useful to you if you are:
- *Looking for a tool*: Check the list to get a quick idea of the "look and feel" of each package.
- *Thinking about building a tool*: Check the list for alternative approaches, and maybe consider if
  contributing to an existing package might be a better way to get what you need.
- *Building a tool, or already have one*: Use the list to clarify and communicate what the main
  differences and strengths of your solution are.

## Packages

Please see below for quick samples of the packages I found, divided into non-scientific groups based
on overall style or goals.

Asterisks link to additional notes after the list.


#### 1. Flow-style regular expression generation

Functional/fluent style of dotted function chains.

| Package                     | Github                                                            | Sample                                                                                     | Notes                           |
|-----------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------|
| **PythonVerbalExpressions** | [➚](https://github.com/VerbalExpressions/PythonVerbalExpressions) | `VerEx().anything().then(" ").then("[").OR("(").anything()`                                | [***](#pythonverbalexpressions) |
| **edify**                   | [➚](https://github.com/luciferreeves/edify)                       | `RegexBuilder().optional().string("0x").capture().exactly(4).range("A", "F")`              |                                 |
| **mre**                     | [➚](https://github.com/alvarofpp/mre)                             | `Regex(Set(Regex("0-9")).quantifier(5), Regex("-").quantifier(0, 1)`                       |                                 |
| **regularize**              | [➚](https://github.com/georgepsarakis/regularize)                 | `pattern().literal('application.').any_number().quantify(minimum=1).case_insensitive()`    |                                 |
| **re_patterns**             | [➚](https://github.com/Nagidal/re_patterns)                       | `Rstr("Isaac").not_followed_by("Newton").named("non_newtonians")`                          |                                 |

#### 2. Plus-style regular expression generation

Building the regex with adding string or overloaded `+`, `|` and/or `[:]`.

| Package             | Github                                          | Sample                                                                          | Notes                  |
|---------------------|-------------------------------------------------|---------------------------------------------------------------------------------|------------------------|
| **pregex**          | [➚](https://github.com/manoss96/pregex)         | `Capture(OneOrMore(AnyUppercaseLetter())) + " " + Either("(", "[")`             | [***](#pregex)         |
| **humre**           | [➚](https://github.com/asweigart/humre)         | `group(SOMETHING) + " " + noncap_group(either(OPEN_PARENTHESIS, OPEN_BRACKET))` | [***](#humre)          |
| **bourbaki.regex**  | [➚](https://github.com/bourbaki-py/regex)       | `"hello" + L(",").optional + Whitespace[1:] + "world" + L("!").optional`        | [***](#bourbaki-regex) |
| **objective_regex** | [➚](https://github.com/VRGhost/objective_regex) | `Text("hello").times.any() + Raw("\s").times(5) + Text("world!").times.many()`  |                        |
| **reggie-dsl**      | [➚](https://github.com/romilly/reggie-dsl)      | `dd = multiple(digit, 2, 2); name(dd + slash + dd + slash + year, 'date')`      |                        |
| **reb**             | [➚](https://github.com/workingenius/reb)        | `"n(nic(':/?#'), 1) + ':' + n01('//' + n(nic('/?#'))) + n(nic('?#'))"`          |                        |

#### 3. Format strings

Focus on simple matching on sections of input, rather than full `re` functionality.

| Package         | Github                                        | Sample                                                                 | Notes               |
|-----------------|-----------------------------------------------|------------------------------------------------------------------------|---------------------|
| **scanf**       | [➚](https://github.com/joshburnett/scanf)     | `"Power: %f [%], %s, temp: %f"`                                        | [***](#scanf)       |
| **parse**       | [➚](https://github.com/r1chardj0n3s/parse)    | `"To get {amount:d} {item:w}, meet me at {time:tg}"`                   | [***](#parse)       |
| **simplematch** | [➚](https://github.com/tfeldmann/simplematch) | `"To get {amount:int} {item}, meet me at {time}"`                      | [***](#simplematch) |
| **pygrok**      | [➚](https://github.com/garyelephant/pygrok)   | `"To get %{NUMBER:amount} %{WORD:item}, meet me at %{DATESTAMP:time}"` | [***](#pygrok)      |
| **qre**         | [➚](https://github.com/mikaelho/qre)          | `"Value: [quantitative:float]&vert;[qualitative]"`                     |                     |

#### 4. Full re syntax replacements

Packages with a stated goal of expanding or completely replacing the `re` syntax.

| Package                  | Github                                               | Sample                                                       | Notes            |
|--------------------------|------------------------------------------------------|--------------------------------------------------------------|------------------|
| **regex**                | [➚](https://github.com/mrabarnett/mrab-regex)        | `"(?(DEFINE)(?P<quant>\d+)(?P<item>\w+))(?&quant) (?&item)"` | [***](#regex)    |
| **kleenexp**             | [➚](https://github.com/sonoflilit/kleenexp)          | `"[#open=['('] #close=[')'] #open [0+ not #close] #open]"`   | [***](#kleenexp) |
| **abnormal-expressions** | [➚](https://github.com/Buscedv/abnormal-expressions) | `'{[w "._-"]1++} "@" {[w "."]1++}'`                          |                  |

## And the winner is...

... with the disclaimers that I a) use `re` only intermittently in production contexts, and b) have
never really used any of the packages in the list:

For everyday casual use, my two picks for from this pack are `simplematch` and `kleenexp`.
`simplematch` because of the utter simplicity that should cover basic needs without reaching for the
manual, and `kleenexp` because of a syntax that feels to me like a pretty good balance between
conciseness and readability.

Overall, it is highly probable that we will never converge on any of these packages in a big way,
because the definitions of "easy", "intuitive", "clear" and "productive" are highly subjective, and
it only takes 200-300 lines of code to roll your own.

## Research notes

What follows are my opinionated notes, compiled while trying out simple examples on each of the
packages I found most interesting. To make the examples comparable and easier to understand, each
tries to match the following simple `re` pattern:

```regexp
r"(?P<title>.+) (\(|\[)(?P<key>[A-Z]+)-(?P<number>\d+)(\)|\])"
```

... matching e.g. `"This is a title [KEY-123]"`.

All the example patterns in this section are tested. See
[examples.py](https://github.com/mikaelho/python-human-regex/blob/main/examples.py) if you want a
quick copy-paste start on using a package.

The star counts mentioned for some of the packages are probably not the only things on this page
that will soon prove incorrect. Issues or PRs are highly welcome.

### PythonVerbalExpressions

Unfinished Python implementation of a cross-language concept.

Example:
```python
pattern = (
    VerEx().anything().then(" ").then("[").OR("(").anything().then("-").anything().then("]").OR(")")
)
```

Notes:
- 1.6k stars but last commit in 2020.
- Version exists for [almost any language](http://verbalexpressions.github.io), polyglots can in
  theory transfer their knowledge.
- Python documentation is missing, had to consult the JSVerbalExpressions docs for capture
  group syntax, and then look at the code to see that the Python version did not support it.
- No type hinting means that IDE could not offer completions after the first dot.


### pregex

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


### humre

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
- 250 stars, very recent.
- Seems well suited if you are used to writing a `re` regex and just write `humre` instead, as the
  conversion seems quite natural. On the flipside, I managed to write a non-compiling regex with
  humre, something I did not manage with the other packages here.
- Nice cheat sheets for quick function lookup.
- No support for named capture groups.
- Took the most time for me fighting with this to get the result I wanted.


### bourbaki.regex

Comprehensive and powerful, with the option to use some of the `regex` package features as well

Example:
```python
pattern = (
    ANYCHAR[1:] ("title") +
    " [" +
    C["A":"Z"][1:] ("key") +
    "-" +
    Digit[1:] ("number") +
    "]"
)
```

Notes:
- Supports both additive and flow/fluent styles and terse/verbose modes. E.g. the use of slice
  notation to indicate ranges and multiplicity can be replaced with more verbose options.
- Supports all advanced constructs from the `re` module, including back-references, lookahead, and
  local sub-pattern compilation flags (e.g. ignore case for only part of the pattern).
- Optional features from `regex`: variable-length lookbehind assertions and atomic groups.
- Static validation of patterns with nice error messages, and behind-the-scenes performance
  optimizations.

### scanf

Python version of [scanf](http://en.wikipedia.org/wiki/Scanf).

Example:
```python
"%s [%s-d]"
```

Notes:
- One of the top 1% PyPI critical packages by downloads, so has wide adoption for its use case 
  despite not having been updated since 2018.
- Focused on picking numbers out of the input. In our example case, I could not find a way to match
  the full varying-length title part of the example (`%s` matches single words).
- Ideal if you already know scanf by heart.

### parse

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

### simplematch

As simple as it gets.

Example:
```python
"{title} ({key}-{id:int})"
```

Notes:
- Just `*` for anything and `{}` for the matching groups, this package delivers on the promised
  simplicity. You probably do not need to reach for the docs when using it.
- Return value is just a dictionary, so no need to remember how to get the actual matches out of the
  return value.
- But, simple is simple: there is no support for matching "either this or that", optional characters
  or a specific number of characters, or for searching several matches within a string. New matchers
  (within the braces) can be defined with a regex, so you could in theory fall back to the full
  syntax of re when needed.

### pygrok

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

### regex

Same but better.

Example:
```python
r"(?P<title>.+) (\(|\[)(?P<key>[A-Z]+)-(?P<number>\d+)(\)|\])"
```

Notes:
- Arguably not part of this compilation as it does not actively attempt to be "easier" version of
  the `re`, just "better".
- Referred to in the `re` documentation.
- Takes the standard library `re` and improves it in different ways, including full unicode case
  folding, nested sets and set operations etc.
- Has two versions, where the first is backwards compatible with `re` and the second pushes the
  boundaries.

### kleenexp

Package with ambition.

Example:
```python
"[capture:title 1+ #any] ['(' | '['][capture:key 1+ #letter]-[capture:id 1+ #digit][')' | ']']"
```

Notes:
- "This is a serious attempt to fix something that is broken in the software ecosystem and has been
  broken since before we were born."
- Generates a standard regex.
- Thoroughly documented.
