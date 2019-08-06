## Week 1 Vocab

**abstraction**: the idea that when designing one part of a program, we can ignore the inessential details of other parts of the program as long as we have a high level understanding of what they do. OR A simplified representation/model of the behavior of a complex system that emphasizes relevant details by excluding irrelevant details.

**algorithm**: An algorithm is a precise sequence of steps for carrying out a task.

**syntax**: The syntax of a computer language is the set of rules that defines the combinations of symbols that are considered to be a correctly structured document or fragment in that language.

**state**: The current condition of a computer system/what the computer is currently doing. OR The internal information that describes the current condition of the computer/what the computer is doing.

**wildcard**: A symbol used to replace or represent one or more characters, indicating that it does not matter which specific character(s) occur in that position. Common wildcard symbols are `.`, `*`, `_`, `%`, and `?`

**operator**: Operators are special symbols in Python that carry out arithmetic or logical computation. The value(s) that the operator operates on is called the operand(s). Common operators include +, - , >, <, =, ==, etc.

**mod/modulo/modulus**: the **modulo** operation finds the remainder after division of one number by another. Eg. `52 mod 10 = 2`, `33 mod 8 = 1`

**edit distance**: the smallest number of operations needed to change one string into another. (operations may vary by context, but typically include insertion, deletion and substitution.)

**type/data type**: A class of values; The data type defines the operations that can be done on the data, the meaning of the data, and the way values of that type can be stored.

**value**: some entity that can be manipulated by a program.

**variable**: a named storage location for a value.

**integer**: Generally, a number that can be written without a fractional component. In most programming languages integers also have a defined minimum and maximum value, typically -2^31 to 2^32 -1 (a “signed integer”) or 0 to 2^32 (an “unsigned integer”). (These constraints are a product of the amount of memory used to store the value.) (A kind of data type)

**float**: A number with a fractional component; typically stored as a fixed number of significant digits and an exponent (similar to “scientific notation”). (A kind of data type)

**string**: a sequence of symbols/characters (A kind of data type)

**list**: In python, a list is an ordered collection of values. (A kind of data type)

**polymorphism**: the provision of a single interface to entities of different data types. Eg. in python, a list may contain strings, integers, other lists, etc. A function accepts a value of any type as its argument and may return a value of any type.

**concatenation**: an operation joining two values of an ordered collection in sequence. Eg. `“s” + “pam” = “spam”`, `[a,b,c] + [d,e] = [a,b,c,d,e]`

**function**: A program unit that takes some data as arguments, processes that data in some way, and then returns some data as a result. (Functions are also a kind of data type in some languages including python.)

**argument**: A value passed to a function as input. Related term: Parameter. Sometimes used interchangeably, but technically the _argument_ is the actual input passed/supplied to a function in the invocation/call, whereas the _parameter_ is the variable inside the implementation of the function.

**function call**: (aka. “invocation”) the expression that “invokes” or “calls” a function, instructing the computer to run the function with the supplied arguments and return the result.

**comments**: explanatory text or information embedded in the source code of a computer program that is not interpreted as instructions for the computer

**statement**:a syntactic unit of a programming language that expresses some action to be carried out. (statements generally are not considered to evaluate to a value).

**boolean**: a data type that has two possible values (usually denoted _true_ and _false_).

**boolean expression**: An expression that has a value of True or False.

**Expression**: a fragment of a programming language that evaluates to a value. Contrast with statement

conditional statement: a statement which performs different computations/actions depending on whether a specified boolean _condition_ evaluates to true or false

**recursive** **function**: A function that calls itself within its own definition. Related: Recursion: a problem solving strategy that utilizes recursive functions. OR The process of executing a recursive function.

**base** **case**: a set of inputs to a recursive function that does not require recursion to produce an answer; thus terminating the recursion.

**recursive** **step**: the solution to a smaller version of the problem, computed by calling the function with a smaller or simpler argument. This solution to the smaller problem is then used in some way to solve the original problem.

**stack**: a data structure that stores information about the active functions of a computer program. When a function call is encountered, the variables that are in the current scope are stored onto a new “stack frame” so that they will not be affected by the execution of the function, when the function completes/returns the values of the variables are restored from the stack.

**scope**: The scope of a variable is the region of a computer program where that variable can be used. Eg. a variable defined inside a function definition can only be used with in the definition of that function. (sometimes this is referred to as the “local scope”) If you try to use a variable somewhere outside of it’s scope we say that it is “out of scope” or “not in scope”

**“Use it or lose it”**: A technique for breaking a problem down recursively by observing that any solution must either include a given element (“use it”) or exclude that element (“lose it”). This technique is especially common in optimization problems (minimize/maximize X given constraint Y).

**functional programming**: a programming paradigm—a style of building the structure and elements of computer programs—that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. Programming is done with expressions or declarations<sup> </sup>instead of statements.

**editor/text editor**: a program for editing plain text files. Contrast with: word processors (eg. MS Word, or OSX’s TextEdit) which focus on editing formatted documents (eg. for printing). Related: Integrated Development Environment or IDE, an IDE always includes an editor, but it is bundled with many other features that are commonly used when programming. (The line between an editor and an IDE can be somewhat fuzzy, but an IDE will generally be targeted at one or more specific programming languages, whereas an editor tries to be more or less equally useful for editing any text file or program.)

**terminal**: A terminal is a serial computer interface for text entry and display. A terminal window allows the user access to a terminal and all its applications, especially the CLI/shell.

**GUI**: Graphical User Interface

**CLI**: Command Line Interpreter Also referred to as the “shell”

A quick note on the vocab lists: I'm compiling words, mostly from our reading, that have specialized meaning in a computer science/programming context. I'm not going to be quizzing you on any of this, but your goal should be to be able to read and use these words fluently in context. This will help you to "sound like a programmer" and also give you the foundation to be able to learn from a wide variety of programming/CS sources. You can use whatever method works best for you to study them (paper flashcards, [anki](https://apps.ankiweb.net/), [supermemo](https://www.supermemo.com/), reading wikipedia, [search google books for usage examples](https://www.google.com/search?tbm=bks&ei=6TABXZ6bPIew0PEP0_686A4&q=boolean+expression+subject%3A%22software%22&oq=boolean+expression+subject%3A%22software%22&gs_l=psy-ab.3...3109.5131.0.5308.8.8.0.0.0.0.77.496.8.8.0....0...1c.1.64.psy-ab..0.0.0....0.5BV81AjVDjA), etc).
