import math
class AdvancedArithmetic(object):
    def divisorSum(self,n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors = []
        for i in range(1+int(math.floor(math.sqrt(n)))):
            if i==0:
                continue
            if n%i==0:
                divisors.append(i)
                if pow(i,2)!=n:
                    divisors.append(int(n/i))
        print(divisors)
        return sum(divisors)

s = Calculator()
s.divisorSum(1)
s.divisorSum(6)
# n = int(input())
# my_calculator = Calculator()
# s = my_calculator.divisorSum(n)
# print("I implemented: " + type(my_calculator).__bases__[0].__name__)
# print(s)