import math
p=3
q=5
n=p*q
print("n:",n)
quotient=(p-1)*(q-1)
print("quotient:",quotient)
#finding e
e=2
while(e<quotient):
    if(math.gcd(e,quotient)==1):
        break
    else:
        e=e+1
print("e:",e)
finding d
d=2
while(d<quotient):
    if((d*e)%quotient):
        break
    else:
        d=d+1
print("d:",d)
#public and private key
print(f"public key:{e},{n}")
print(f"private key:{d},{n}")
#encryption
message=10
encrypt=(message**e)%n
print("encrypted message:",encrypt)
#decryption
decrypt=(encrypt**d)%n
print("decrypted message:",decrypt)
