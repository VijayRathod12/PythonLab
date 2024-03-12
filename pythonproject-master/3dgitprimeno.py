# to print 3 digit prime number
isprime=True
for i in range(100,1000):
    for j in range(2,i//2):
        if i%j==0:
            isprime=False
            break
    if isprime==True:
        print(i)
    isprime=True


print("by using function ")

def isprime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
    
def print_prime(s,e):
    for i in range(s,e):
        if isprime(i):
            print(i)
print_prime(100,999)