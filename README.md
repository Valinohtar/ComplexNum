# Complex numbers implementation in Python

## In few words

I created this project solely to learn how to work with Git and to train OOP in python. It allows to do some basic arithmetic using complex numbers, convert the Rectangular Form to Polar and Euler forms. It contains also some usefull (hopefully) methods. I hope I can convert this funny code into working module in the future :)

It should be basis for my project In PyTQ5 or Tkinker - complex and dual calculators.

## Classes

### ComplexNumber

Takes two arguments Re - for real part and Im - for imaginary part. User can multiply, divide, add, subtract, take absolute value and print those numbers like normal floats or ints - thanks to the __dunder__ methods.

Methods:
* toTrig() - converts the ComplexNumber object to TrigForm object, which allows user to use new funcionalities - like method called roots() - which returns the list of all possible roots.

* conjugate() - returns conjugate of given number

### PolarForm

Takes two arguments Arg - for argument and abs_val for modulus. User can multiply, divide take roots or raise the to power(works for floats but generates only one root). Using toComplex method can be converted into rectangular form.

Methods:
* pow(power) - takes the numer to the power, returns PolarForm object.

* roots(root) - returns a list of PolarForm objects - the roots of root power.

* print_roots(root): - prints a list of PolarForm objects and returns it.

* print_rectangular_roots(root) - prints a list of ComplexNumber objects - returns None
