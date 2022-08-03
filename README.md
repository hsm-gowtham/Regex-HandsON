# Regex-HandsON
##Raw Strings
String prefix with r, it tells python not to handle back slashes(\)


## MetaCharacters (needs to escaped):
. ^ $ * + ? { } [ ] \ | ( )

## Most Used
```bash
.          -  Any Character Except New Line
\d         -  Digit (0-9)
\D         -  NOT a Digit (0-9)
\w         -  Word Character (a-z, A-Z, 0-9, _)
\s         -  WhiteSpace (space, tab, newline)
\S         -  NOT a WhiteSpace (space, tab, newline)

\b         -  Word Boundary
\B         -  NOT a Word Boundary
^          -  Beginning of a String
$          -  Ending of a String
[]         -  Matches Characters in brackets
[^ ]       -  Matches Characters NOT in brackets
|          -  Either Or
```

## Quantifiers
```bash
*          -  0 or More
+          -  1 or More
?          -  0 or One
{3}        -  Exact Number
{3,4}      -  Range of Numbers (Minimum, Maximum)
```

### Quick Example
```bash
'''
Ms. Marvel
Mr. Sensei Hang
Mrs. Sensei
Mr.Bang
'''
pattern to match above words:  M(s|r|rs)\.?\s?[A-Z]\w*
```
#### Explanation:
1. M to match 1st letter
2. Using group to match s or r or rs
3. matching 0 or 1 dot
4. matching 0 or 1 space
5. matching 1 capital letter
6. matching 0 or More Words


# Regex Using Python
### re module
re.compile method allows us to separate out our patterns to variables and  also make it easier to make use of that variable to perform variable searches


