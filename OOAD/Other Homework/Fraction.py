from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ZeroDivisionError("Denominator can't be zero.")
    
        greatest_common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // greatest_common_divisor
        self.denominator = denominator // greatest_common_divisor
        
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self) -> str:
        return f"Fraction({self.numerator},{self.denominator})"
    
    def __add__(self, other: 'Fraction') -> 'Fraction':
        new_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)

        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other: 'Fraction') -> 'Fraction':
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self,other: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)
    
    def __truediv__(self,other: 'Fraction') -> 'Fraction':
        
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
    
        return Fraction(new_numerator,new_denominator)
    def __eq__(self, other: 'Fraction') -> bool:
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False
    def __eq__(self, other: 'Fraction') -> bool:
        if self.numerator != other.numerator or self.denominator != other.denominator:
            return False
        return True
    def __lt__(self,other: 'Fraction') -> bool:
        one = self.numerator/self.denominator
        two = other.numerator/other.denominator
        if one < two:
            return True
        return False
    def __gt__(self,other: 'Fraction') -> bool:
        one = self.numerator/self.denominator
        two = other.numerator/other.denominator
        if one > two:
            return True
        return False
    def __le__(self,other: 'Fraction') -> bool:
        one = self.numerator/self.denominator
        two = other.numerator/other.denominator
        if one <= two:
            return True
        return False
    def __ge__(self,other: 'Fraction') -> bool:
        one = self.numerator/self.denominator
        two = other.numerator/other.denominator
        if one >= two:
            return True
        return False
    def __hash__(self) -> int:
        return hash((self.numerator,self.denominator))
    
    def __float__(self) -> float:
        return self.numerator / self.denominator
    def __int__(self) -> int:
        return self.numerator // self.denominator
    def __neg__(self) -> 'Fraction':
        self.numerator *= -1
        return Fraction(self.numerator, self.denominator)
    def Mixed_Number_Representation(self) -> str:
        if abs(self.numerator) >= self.denominator:
            whole_part = self.numerator // self.denominator
            new_numerator = abs(self.numerator) % self.denominator
            if new_numerator == 0:
                return f"{whole_part}"
            return f"{whole_part} {new_numerator}/{self.denominator}"
        return f"{self.numerator}/{self.denominator}"

    def __iadd__(self, other: 'Fraction') -> 'Fraction':
        new_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(new_numerator, new_denominator)
ob = Fraction(7, 4)
ob2 = Fraction(1, 4)
print(ob)
print(ob.Mixed_Number_Representation())
ob+=ob2
print(ob)

