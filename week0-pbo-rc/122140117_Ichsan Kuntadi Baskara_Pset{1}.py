t=int(input("Triangle Height : "))
for i in range(1, t+1):
    s=" "*(t-i)
    b="*"*(i*2-1)
    print(s+b)