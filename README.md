# Swagbot
A chatbot that does math (or at least tries to)

## Parsing math text

An important part of Swagbot is parsing math sentences in English into symbolic
notation.  First, the verb is found in the sentence.  A rough order of operations
is indicated by the order in which the verbs are processed: "multiply," then
"divide," then "add," then "subtract," then the corressponding infix versions of
each operation.  For the prefix verbs, the preposition in the middle of the 
sentence is located and then the operands extracted from around it.  For the infix
verbs, the operands are extracted from either side.  Then the operands are recursively
parsed for their own subexpressions.  Numeric words are converted into numbers
and parentheses are placed around the subexpressions.

```
>>> mathparse.make_arith_string("divide fourteen times seventy three by five minus two")
'(14*73)/(5-2)'
```
