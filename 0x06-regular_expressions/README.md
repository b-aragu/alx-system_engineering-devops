---
banner: "https://www.oreilly.com/content/wp-content/uploads/sites/2/2019/06/email-regex_crop-ae942dc427c8cebd3a83c52d17389123.jpg"
sticker: lucide//regex
---

-   It is a sequence of characters that define a search pattern.
-   It is mainly used in pattern matching with strings, or string matching (i.e operates like a "find and replace")
-   **Meta characters** : `\`, `^`, `$`, `.`, `|`, `?`, `*`, `+`, `(`, `)`, `[`, `{` have speacial meaning in regex and are errors when used alone.
-   To use one of the metacharacters as a litteral in regex, you need to escape them with a backslash eg to match `1+1 = 2`, the correct regex is `1\+1 = 2`

**Character class or Character sets**
- a character class matches only one out of several characters, e.g to match an a or an e , use `[ae]` in gr`[ae]`y to match either gray or grey
- A character class matches only a single character gr`[ae]`y does not match graey or graay or any such thing
- You can use a hyphen inside a character class to specify a range of characters e.g \`\[0-9\]

**Shorthand character classes**
- `\d` matches a single character that is a digit, `\w`matches a word character, `\s` matches a whitespace character

**The **`.`** matches (almost) any character**
- The dot matches a single character, except line break characters
- e.g. gr`.`y matches gray , grey , gr%y e.t.c

**Anchor**
- They don't match any character, they match a position.
- `^` matches at the start of string, `$` matches at the end of a string, `\b` matches at the word boundary.

**Alternation**
- regex equivalent of "all".
- `cat|dog` matches cat in About cats and dogs. If the regex is applied again, it matches dog. You can add as many alternatives as you want: `cat|dog|mouse|fish`
- Alternation has the lowest precedence of all regex operators. `cat|dog food` matches cat or dog food. To create a regex that matches cat food or dog food, you need to group the alternatives:`(cat|dog) food`.

**Repetition**
- The question mark makes the preceding token in regex optional
- colou`?`r matches colour or color.
- The asterisk `*` tells the engine to attempt to match the preceding token zero or more times.
- The plus `+` tells the engine to attempt to match preceding token one or more time
- Use curly braces to specify a specific amount of repetition. Use `\b[1-9][0-9]{3}\b `to match a number between 1000 and 9999. `\b[1-9][0-9]{2,4}\b` matches a number between 100 and 99999.
