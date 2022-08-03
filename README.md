# Regex-HandsON
##Raw Strings
String prefix with r, it tells python not to handle back slashes(\)


## MetaCharacters (needs to escaped):
. ^ $ * + ? { } [ ] \ | ( )

## Most Used
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

# Regex Using Python
### re module
re.compile method allows us to separate out our patterns to variables and  also make it easier to make use of that variable to perform variable searches


