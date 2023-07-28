# Complex numbers implementation in Python

## In few words

I created this project solely to learn how to work with Git and to train OOP in python. It allows to do some basic arithmetic using complex numbers, convert the cardinal(if that's the name) form to Trig and Euler forms. It contains also some usefull(hopefully) methods. I hope I can convert this funny code into working module in the future :)

It should be basis for my project In PyTQ5 or TKTinker - complex and dual calculators.

## Classes

### ComplexNumber

Takes two arguments Re - for real part and Im - for imaginary part. User can multiply, divide, add, subtract, take absolute value and print those numbers like normal floats or ints - thanks to the __dunder__ methods.

Methods:
* toTrig() - converts the ComplexNumber object to TrigForm object, which allows user to use new funcionalities - like method called roots() - which returns the list of all possible roots.

* conjugate() - returns conjugate of given number
