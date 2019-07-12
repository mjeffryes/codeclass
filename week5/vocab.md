Week 5 Vocab
-----------

**object-oriented programming**: A programming paradigm based on the concept of "objects",
which can contain data, in the form of attributes, and code, in the form of methods.

**class**: A class defines a new data type by describing the methods (functions) and data (attributes)

**object**: A self-contained entity that consists of both data and procedures to manipulate the data.

**instance**: An object that has the methods and attributes defined by a class. (usage: "x is an instance of class C")

**instantiate/construct**: To create a new instance of a class (ie a new object with the methods and attributes
defined by that class).

**constructor**: a functions that constructs/instantiates an instance of a class (ie. an object with
the methods and attributes defined by that class.

**attribute**: data belonging to/contained by an object. (aka. member, property, field, or instance variable)

**method**: a function that belongs to/is contained by an object.

**constructor method**: A method that is used for creating(constructing/instantiating)
 an instance of a class. (Constructors are usually defined using special syntax or method names.)

**operator overloading**: defining a method that is called/invoked when an operator is used with
a specific type.

**inheritance**: A mechanism of basing once class on another in order to reuse some of its
 implementation and extend its interface.

**composition**: Using instances of one class within the implementation of another either as
attributes or in the body of a method.

**superclass/subclass**: If class A inherits form class B, A is a subclass of B and B is a
superclass of A.

**override**: Defining a method in a subclass with the same name as a method in the super class in
order to change its behavior.

**encapsulation**: Bundling data with the methods that operate on that data. Encapsulation is used to
limit access to values or state of data inside a class, in order to make it easier to reason about
how that data may be used/modified.

**interface**: The external semantics of the methods defined by a class. (Ie. what methods does this
class have, how can I call them and what will they return/do.)

**implementation/implmentation details**: How the methods of a class do what they are supposed to do.
Implementation details can be changed without affecting the external semantics of the class.

**private vs public**: The public methods of a class are intended to be called
 outside of the methods of the class. The private methods/attributes of the class are only intended
to be accessed/called by other methods within the class. Put another way: public methods are a part
 of the interface of the class, while private methods/attributes are only part of the implementation
