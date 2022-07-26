# 최대공약수와 최소공배수

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# A와 B를 비교해 큰 수를 작은 수로 나눈다.
# 두 수를 나누어서 나머지가 0이면 작은 수가 최대공약수이다.
# 두 수를 나누어서 나머지가 0이면 큰 수가 최소공배수이다.

def gcd(a,b):
    if a<b:
        a,b=b,a
    c=a%b
    if c==0:
        return c
    else:
        return gcd(b,c)

def lcm(a,b):
    if a<b:
        a,b=b,a
    c=a%b
    if c==0:
        return a
    else:
        return gcd(a,b)*(a/gcd(a,b)*b/gcd(a,b))