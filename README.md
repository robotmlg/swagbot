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

## Generating some finger-lickin good insults - Matthew Lee
One of the tasks I was assigned was to design an insult generator for the bot. There are some interesting design choices when it comes to generating insults. It is easy to just string together a bunch of harsh words and come out with a crude insult that barely inflicts any pain. In my quest for quality insults I've found that often the most amusing insults comes from combinations of words that seem random but also flow together nicely. In order to do this you must not have a word repertoire that consists only of words such as stinky, grimy, terrible etc. Instead, you must throw in what I like to call "Game Changers". For example, when you have a linking verb such as "Fascinating" in an insult it leads to some amazingly funny insults. 

For example, "Ah, you must be a fascinating trollop" throws a whole new spin on the insult game. If that fascinating were replaced with disgusting the insult could easily be disregarded as some barbarian joke not fitting of the Swagbot. But instead it leaves the person wondering about the suttle undertone of the Swagbot's intentions. It shrouds the insult in mystique and makes the Swagbot seem even more omnipotent. These types of insults can  truly lead to some serious emotional damage and I think the insult generator has been one of the crowning accomplishments of our Swagbot Project. 

##Wikipedia - Thanassi Natsis

My role in the programming of the chatbot was to allow it to be able to pull information from Wikipedia.
The goal was to allow it to give summary information about a person or topic and to give birth and death dates.
In order to obtain summary information, it was simply a task of giving the name to the Wikipedia API and then any information in parentheses was filtered out because it was usually about pronunciation.
For the birth and death information, the url was needed and used to obtain the html of the page.
The html was parsed for the birth and death dates and filtered out any unnecessary html or other information.

Sample input: Who is Euler?
Sample Output: Leonhard Euler was a pioneering Swiss mathematician and physicist. He made important discoveries in fields as diverse as infinitesimal calculus and graph theory. 

Sample input: When was Euler born?
Sample Output: 1707-04-15