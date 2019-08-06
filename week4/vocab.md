## Week 4 Vocab

**data mining**: Data mining is the process of discovering patterns in large data sets

**imperative programming**: a programming paradigm that uses statements that change a program's state. In much the same way that the imperative mood in natural languages expresses commands, an imperative program consists of commands for the computer to perform. Imperative programming focuses on describing _how_ a program operates.

**iteration**: running the same instructions/statements in a program multiple times (using a loop) OR a single execution of the statements in a loop

**loop**: a program statement or series of statements that executes multiple times

**body of a loop**: the statements that are run on each iteration of a loop

**for-loop**: a loop that executes “for” a certain number of iterations

**while-loop**: a loop that executes “while” a condition is true (Note: all for loops can be written as while loops)

**unrolling** **a** **loop**: writing the body of the loop out a specific number of times in a program rather than using a for loop. (This is sometimes done intentionally by compilers for performance reasons; it’s generally a bad idea to do it as a programmer except maybe for instruction purposes.)

**accumulator**: a variable that is updated on each iteration of a loop, accumulating results from each iteration into a final result

**infinite** **loop**: a loop that never ends

**mutable/immutable**: mutable data can have its value changed (eg. adding/removing/overwriting elements in a list), immutable data cannot have it’s value changed once it is written to memory.

**reference**: the address in memory where a variable’s data is stored

**value**: the data to which a variable refers

**linear time algorithm**: An algorithm whose runtime scales linearly with the size of its inputs.

**quadratic time algorithm**: An algorithm whose runtime scales quadratically with the size of its inputs.

**exponential time algorithm**: An algorithm whose runtime scales exponentially with the size of its inputs.

**array**: A collection of items of the same type that are stored consecutively in memory. They are efficient for “random access” (reading or writing the value at a particular index), but expensive to resize (eg. adding or removing an element) because it generally requires copying the whole array.

**2D array**: An array that itself contains arrays of data. This can be extended to 3D array, 4D array, etc. although in practice it’s rare to encounter more than 3D. (It’s hard to think about arrays of arrays of arrays of arrays…)

**dictionary**: A python data type that contains a mapping between pieces of (immutable) data (the keys) and other pieces of data (the values).
