# Swagbot
A chatbot that does math (or at least tries to)

## Parsing math text - Matt Goldman

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

Given more time, we would like to make this function capable of parsing more complex
math expressions, such as "to the power of" and "square root of."

## Solving equations - Roland Gorzkowski

An important part of the project was implementing a method that turned a standard polynomial input into something that sympi would understand. It required replacing any exponent symbols with two asterisks (the python symbol for exponentiation) and also putting any multiplication symbols between two variables or a variable and a number if there isn't already an operation there. The first implementation of it had an oversight for if there were two variables but this was very easily patched.
