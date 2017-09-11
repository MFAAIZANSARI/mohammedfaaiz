g=int(input("enter an integer:"))
print("the divisors of the number are as follow:")
i=1
for i in range(1,g):
    if(g%i==0):
        print(i)
    else:
        i=i+1
