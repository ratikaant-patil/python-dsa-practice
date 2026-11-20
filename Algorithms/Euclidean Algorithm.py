# The Euclidean Algorithm is a method for efficiently calculating the greatest common divisor ( GCD ) of two integers
# It is also used for Highest Common Factor ( HCL )

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b) 
# gcd (b, a % b ) This is Euclidean Formula

print(gcd(5,50))

