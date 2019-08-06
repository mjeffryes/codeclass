
## Week 3 Vocab

**transistor**: A transistor is a semiconductor device used to amplify or switch electronic signals and electrical power. It is the fundamental building block of modern electronic devices; it’s ability to switch electronic signals on and off allows for the construction of logic gates

**logic** **gate**: an idealized or physical device implementing a Boolean function; that is, it performs a logical operation on one or more binary inputs and produces a single binary output

**radix**/**base** :the number of unique digits, including the digit zero, used to represent numbers in a positional numeral system. For example, for the decimal/denary system (the most common system in use today) the radix (base number) is ten, because it uses the ten digits from 0 through 9.

**binary**: a number expressed in the binary numeral system, uses only two symbols: typically "0" and "1". Each digit is referred to as a bit. Because of its straightforward implementation in digital electronic circuitry using logic gates, the binary system is used by almost all modern computers and computer-based devices.

**bit**: a single digit in a binary number. The name is a portmanteau of binary digit

**byte**: a unit of data that (almost always) consists of eight bits; it is the smallest addressable unit of memory in many computer architectures.

**word**: a word is the natural unit of data used by a particular processor design. A word is a fixed-sized piece of data handled as a unit by the instruction set or the hardware of the processor. In modern general-purpose computers usually use a 32 or 64 bit word.

**encoding**: a system of representing some data in binary numbers so that it can be manipulated by the computer.

**ASCII**: a character encoding standard. ASCII codes represent text in computers, telecommunications equipment, and other devices.

**Unicode**:  computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems. Unicode comes in a few different variants, most common are UTF-8 and UTF-16. UTF-8 uses the same representation as ASCII for the 128 symbols in ASCII, so any ASCII encoding string is also valid UTF-8.

**two’s complement representation**: an encoding for representing positive and negative numbers in binary. It has the useful property that adding positive and negative values can be done with simple bitwise addition.

**boolean algebra**: a branch of algebra in which the values of the variables are _true_ and _false_, usually denoted 1 and 0 respectively. The basic operations of boolean algebra are conjunction (AND), disjunction (OR) and negation (NOT).

**truth table**: A truth table shows how a logic circuit's output responds to various combinations of the inputs, using logic 1 for true and logic 0 for false.

**minterm expansion principle**: a rule for converting a truth table into a boolean expression.

**half adder**: an logic circuit that performs the addition of numbers. The half adder is able to add two single binary digits and provide the output plus a carry value. (A full adder is typically constructed from two half adders, hence the name.)

**full adder**: a logic circuit that performs addition. A full adder adds three one-bit binary numbers, two operands and a carry bit. The adder outputs two numbers, a sum and a carry bit.

**ripple-carry adder**: a logic circuit that can add multiple bits, constructing by connecting the carry output of each full adder to the carry input of the full adder for the next bit/digit.

latch: (aka a “flip-flop”) a logic circuit that holds a value until it is reset.

**RAM**: Random Access Memory. The storage that holds most of the data and programs the computer is using running.

**page fault**: If all the programs and data the computer is using do not fit into RAM; Some of the data will be copied off to a larger storage device like the hard drive. Data is loaded from/stored to this device in “pages”. If the data the CPU needs to access in not loaded into RAM, it triggers a “page fault”  where the CPU pauses what it is doing to load the page it needs into memory “swapping” it for a page that it does not expect to use again soon.

**CPU**: Central Processing Unit. The CPU reads instructions out of memory and executes them. The most common instructions a CPU can execute are basic mathematical operations (on the values in the registers), copying between main memory and the registers and testing if the value in a register is equal (usually to 0 or to the value in another register).

**registers**: small bits of memory in the CPU, that contain the values it is operating on right now.

**program counter**: a register that holds the address in memory of the next instruction to execute. By changing the program counter a program can choose to execute different instructions for different data.

**instruction register**: a register holding the instruction the CPU is currently executing.

**cache**: because the main memory is slow to access (relative to the speed of the CPU), the CPU often has one or more smaller memory units on the same bit of silicon as the processor. Data from the main memory is copied into the cache.

**cache hit/cache miss**: When the CPU loads data from memory, it first tries to read it from the cache. If it finds the data it need there, it’s called a “cache hit” if it does not find it, it’s called a “cache miss”

**Von Neumann Architecture**: a computer design that consists of: 1) A processing unit that contains an arithmetic logic unit and processor registers, 2) A control unit that contains an instruction register and program counter, and 3) Memory that stores data and instructions. Pretty much all modern computers use this design.

**opcode**: the binary encoding of an instruction to be performed. Most instructions consist of an opcode, plus some data to operate on (identifiers for registers, an address in memory or raw data)

**assembly language**: a language where each machine instruction gets a friendlier textual representation.

**assembler**: a program which turns assembly language into raw binary instructions that the computer can process.

**stack pointer**: the address of the stack in memory, traditionally stored in the highest numbered register.

**push/pop**: when we add something to a stack we say we are “pushing it onto the stack” when we remove something from the stack we “pop it of the stack”

**compiler**: a program that translates a program written in a programming language (like python) into instructions a computer can execute.

**interpreter**: a program that translates instructions in a programming language (like python) into instructions the computer can execute. As opposed to a compiler, an interpreter performs this translation “on-the-fly” when the program is run.
