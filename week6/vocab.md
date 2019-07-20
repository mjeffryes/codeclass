Week 6 Vocab
------------

**halt checker**: A theoretical program that could determine whether any other program will
eventually complete (ie. halt) or run forever.

**turing machine**: A Turing machine is a mathematical model of computation that defines an
abstract machine, which manipulates symbols on a strip of tape according to a table of rules.
Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating
 that algorithm's logic can be constructed.

**runtime analysis**: Determining how the execution time of an algorithm will vary as the size of
its input changes.

**space analysis**: Determining how the memory usage of an algorithm will vary as the size of its
input changes.

**Big-O analysis/notation**: A notation that describes the worst case growth of the (space or time)
requirements of an algorithm as the size of its input increases.

**P**: A category of algorithms that run in polynomial time on a Turing equivalent computer.

**NP**: A category of algorithms that would run in polynomial time on a Non-deterministic Turing
machine. Note: We don't have a reliable way to build such a machine today; the best equivalent
algorithms on *deterministic* turing machines (ie. real computers) are exponential.

**NP-hard**: Problems that are at least as hard as the hardest problems in NP. (NP-Hard problems
are not necessarily in NP)

**NP-complete**: Problems that are in NP and NP-hard

**approximation algorithm**: An algorithm that runs fast (in polynomial time) and finds solutions
 that are guaranteed to be within a certain percentage of the best possible solution.

**heuristic**: A "rule-of-thumb" for solving a problem; no guarantees are made about how close the
heuristic will come to the optimal solution, but some can be "good enough" for "most" inputs.

**array**: An array is a list of data of a consistent size that is arranged consecutively in memory.
An array supports constant time random access and updates, but cannot change size without copying the
entire structure. A basic data type used to construct other data types.

**linked-list**: A linked list is a list of data elements "linked" together by references from one
element to the next element in the list. A basic data type that is used to construct other data types.

**doubly-linked-list**: A linked list where each element has both a reference to the next
element and a reference to the previous element in the list.

**stack**: A data structure containing an ordered list of elements where data is inserted into or
removed from one end only. A stack is LIFO (Last in, First out), it does not support random access.

**queue**: A data structure containing an ordered list of elements where data is inserted into one end
and removed from the other. A queue is FIFO (First in, First out), it does not support random access.

**tree**: A data structure where each element (aka. node) contains a reference to zero, one or more
 "child" elements. In a tree each "child" element can have only one "parent" element that holds a
 reference to it.

**binary tree**: A tree where each element holds a reference to a maximum of two "child" elements.

**root node**: the entry point of the tree. No other elements contain a reference to this node.

**leaf node**: An element in a tree with no children.

**graph**: A data structure where each element (aka. node) contains a reference to zero, one or more
other elements. Unlike a tree, a graph has no restrictions on how the elements many reference one
annother.

**hash table/hash map**: A hash table, or a hash map, is a data structure that associates keys with
 values. The primary operation it supports efficiently is a lookup:
given a key, find the corresponding value. (eg. Python dictionaries are a hash map)

**map**: Another name for a dictionary or hash map.

**set**: A data structure that contains an un-ordered collection of elements. Usually supports
efficient tests of whether and element is in the set.

