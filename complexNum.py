#complex numbers implementation
from math import sqrt, atan2, pi, sin, cos

class ComplexNumber:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
        if abs(self):
            self.Arg = atan2(self.Im, self.Re)*180/pi
        else:
            self.Arg = 0
    
    def __abs__(self):
        return sqrt(self.Re**2 + self.Im**2)
    
    def __add__(self, other_complex):
        return ComplexNumber(self.Re + other_complex.Re, self.Im + other_complex.Im)
    
    def __mul__(self, other_complex):
        return ComplexNumber(self.Re*other_complex.Re-self.Im*other_complex.Im, self.Im*other_complex.Re+self.Re*other_complex.Im)
    
    def __sub__(self, other_complex):
        return ComplexNumber(self.Re - other_complex.Re, self.Im - other_complex.Im)
    
    def __truediv__(self, other_complex):
        return ComplexNumber((self.Re * other_complex.Re + self.Im*other_complex.Im)/(other_complex.Re**2 + other_complex.Im**2),(self.Im*other_complex.Re - self.Re*other_complex.Im)/(other_complex.Re**2 + other_complex.Im**2))
    
    def __str__(self):
        if self.Im >= 0:
            return f'{self.Re} + {self.Im}i'
        else:
            return f'{self.Re} - {abs(self.Im)}i'
    
    def conjugate(self):
        return(ComplexNumber(self.Re, -1*self.Im))
    
    def toTrig(self):
        return TrigForm(self.Arg, abs(self))

class TrigForm:
    def __init__(self, Arg, abs_val):
        self.Arg = Arg 
        self.abs_val = abs_val

    def __str__(self):
        return f'{round(self.abs_val,3)} ⋅ (cos {round(self.Arg, 3)}° + i ⋅ sin {round(self.Arg, 3)}°)'
    
    def toComplex(self):
        return ComplexNumber(cos(self.Arg*pi/180)*self.abs_val, sin(self.Arg*pi/180)*self.abs_val)

    def __mul__(self, other):
        return TrigForm(self.Arg + other.Arg, self.abs_val*other.abs_val)
    
    
         



#z1 = ComplexNumber(3,-1)
#z2 = ComplexNumber(2,5)

z1 = TrigForm(30, 2)
z2 = TrigForm(90, 3)
print(z1, z2,'=', z1*z2)
z3 = (z1*z2).toComplex()
print(z3)
print(z3.toTrig().toComplex().toTrig())
#print(z3.Re)
