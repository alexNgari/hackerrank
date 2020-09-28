#Write your code here
class NPNegativeError(Exception):
    pass

class Calculator:
    def power(self, base, exponent):
        if base<0 or exponent<0:
            raise NPNegativeError("n and p should be non-negative")
        else:
            return pow(base, exponent)


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   