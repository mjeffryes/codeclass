## Week 2 Vocab

**computationally hard**: a problem that takes a long time to compute the answer for

**top-down design**: breaking down a problem/system by assuming a solution (sometimes referred to as a black box) for one or more sub-problems/systems. The overall solution/design can be completed before working on the sub-problems. Contrast with: bottom-up design; where a design/solution is constructed by starting with the smallest components.

**first-class citizen**: a first-class citizen (also type, object, entity, or value) in a given programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, modified, and assigned to a variable.

**predicate**: a function which returns a boolean value. If the predicate returns true for a given input we say the predicate “matches” the input (or sometimes “matches against” the input).

**anonymous function**: a (usually short lived) function that is not given a name; sometimes called a “lambda” or a “lambda function” (especially in python which literally uses the word “lambda” in its syntax for creating anonymous functions)

**higher-order function**: a function that takes a function as an argument and/or returns a function as a result

**filter**: a higher-order function that returns a list containing only the elements in the input list for which the predicate matches.

**map**: a higher-order function that returns a list constructed by applying an input function to each element of an input list

**reduce**: a higher-order function that applies a function of two arguments cumulatively to the items of list, from left to right, so as to reduce the list to a single value.

**list-comprehension**: a special bit of python syntax that makes it quick to map and filter lists.

**function composition**: a way of combining functions such that the output of the first function becomes the input of the next function. Composition can be used to build complex functions out of simpler components.

**multiple assignment**: a syntax for assigning multiple values in a single line. Eg `x, y = 1, 2` nb. The expressions on the right hand side (to the right of the `=`) are evaluated completely before any variables are assigned. So `x, y = y, x` is roughly equivalent to:

    ```

    temporary = y, x

             x = temporary[0]

             y = temporary[1]

             ```

**principle of generalization**: When building lots of similar things, look for opportunities to build something more generic that can handle all the cases.

**refactoring**: the process of restructuring existing computer code without changing its external behavior. Refactoring is intended to improve nonfunctional aspects of software, eg. code readability, reduced complexity, better maintainability, or improved extensibility.

**rule of three**: a rule of thumb to decide when similar pieces of code should be refactored (or generalized) to avoid duplication. It states that two instances of similar code don't require refactoring, but when similar code is used three times, it should be extracted into a new procedure.

**“idiomatic”/”pythonic”**: Exploiting the features of the Python language to produce code that is clear, concise and maintainable. Pythonic means code that doesn't just get the syntax right but that follows the conventions of the Python community and uses the language in the way it is intended to be used. (https://stackoverflow.com/questions/25011078/what-does-pythonic-mean) The phase “idiomatic python” has a similar meaning.

**edge case**: Input values that may require special handling in an algorithm. Eg. for algorithm that operates on a number, very large numbers, 0, 1, and negative numbers are come common edge cases. When testing, it’s a good idea to make sure you “cover” (ie test) all the edge cases.

**helper function:** A function that handles a smaller piece of the work required for the overall function/program.

**git**: Git is an open source program for tracking changes in text files. (aka a “version control system“ a tool that helps a software team manage changes to source code over time)

**repository**: A repository contains all of the project files (including documentation), and stores each file's revision history.

**commit**: A commit, or "revision", is an individual change to a file (or set of files). It's like when you _save_ a file, except with Git, every time you save it creates a unique ID (a.k.a. the "SHA" or "hash") that allows you to keep a record of what changes were made when and by who. Commits usually contain a commit message which is a brief description of what changes were made.

**diff**: A diff is the _difference_ in changes between two commits, or saved changes. The diff will visually describe what was added or removed from a file since its last commit.

**branch**: A branch represents an independent line of development. You can think of them as a way to request a brand new working directory, and project history. New commits are recorded in the history for the current branch. (which means that the history of a file can be different on different branches)

**master**: The primary branch of all repositories. All committed and accepted changes should be on the master branch. You can work directly from the master branch, or create other branches.

**checkout:** update one or more files in the working directory to match the version stored in a particular  commit or branch. The `git checkout` command is most commonly used to switch branches in a repository. `git checkout testing-el` would take you to the _testing-el_ branch whereas `git checkout master` would drop you back into master.

**Working directory:** The working directory is a single checkout of one version of the project.

**Fetch**: Fetching refers to getting the latest changes from an online repository without merging them in. Once these changes are fetched you can compare them to your local branches (the code residing on your local machine).

**Merge**: Merging takes the changes from one branch (in the same repository or from a fork), and applies them into another. A “merge conflict” is an event that occurs when Git is unable to automatically resolve differences in code between two commits.

**Pull**: Pull refers to when you are fetching _in_ changes _and_ merging them. For instance, if someone has edited the remote version of a file you're both working on, you'll want to _pull_ in those changes to your local copy so that it's up to date.

**Push**: Pushing refers to sending your committed changes to a remote repository, such as a repository hosted on GitHub. For instance, if you change something locally, you'd want to then _push_ those changes so that others may access them.

