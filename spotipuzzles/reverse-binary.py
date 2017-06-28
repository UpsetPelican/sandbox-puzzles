n = raw_input()
n = int(n)
n = bin(n)[2:]
n = str(n)
n = n[::-1]
n = int(n,2)
print n