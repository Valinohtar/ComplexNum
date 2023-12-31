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
            return f'{round(self.Re, 10)} + {round(self.Im, 10)}i'
        else:
            return f'{round(self.Re, 10)} - {abs(round(self.Im, 10))}i'
    
    def conjugate(self):
        return(ComplexNumber(self.Re, -1*self.Im))
    
    def toPolar(self):
        return PolarForm(self.Arg, abs(self))

class PolarForm:
    def __init__(self, Arg, abs_val):
        self.Arg = Arg 
        self.abs_val = abs_val

    def __str__(self):
        return f'{round(self.abs_val,3)} ⋅ (cos {round(self.Arg, 3)}° + i ⋅ sin {round(self.Arg, 3)}°)'
    
    def toComplex(self):
        return ComplexNumber(cos(self.Arg*pi/180)*self.abs_val, sin(self.Arg*pi/180)*self.abs_val)

    def __mul__(self, other):
        return PolarForm(self.Arg + other.Arg, self.abs_val*other.abs_val)
    
    def __truediv__(self, other):
        return PolarForm(self.Arg - other.Arg, self.abs_val/other.abs_val)
    
    def pow(self, power):
        return PolarForm(self.Arg*power, self.abs_val ** power)
    
    #i think I'll just add separate methods for printing and returning/done
    def roots(self, root):
        '''Returns a list of PolarForm objects - the roots of root power'''
        rad_Arg = (self.Arg/180)*pi
        root_list = [(rad_Arg + i*2*pi)/root for i in range(root)]
        root_absval = self.abs_val**(1/root)
        final = []
        for root_item in root_list:
            new_root = PolarForm(root_item*180/pi, root_absval)
            final.append(new_root)

        return final
    
    def print_roots(self, root):
        '''Prints a list of PolarForm objects and returns it'''
        final = self.roots(root)
        for root_item in final:
            print(root_item)

        return final

    def print_rectangular_roots(self, root):
        final = self.roots(root)
        for root_item in final:
            print(root_item.toComplex())

 
         



#z1 = ComplexNumber(3,-1)
#z2 = ComplexNumber(2,5)

z1 = ComplexNumber(16,0)
z1 = z1.toPolar()
z1.print_rectangular_roots(8)

