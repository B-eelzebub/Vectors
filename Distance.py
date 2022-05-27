# Shortest distance calculator
print("Enter line in the form of a tuple (a1, a2, a3, b1, b2, b3)")
l1 = eval(input("Enter line 1: "))
l2 = eval(input("Enter line 2: "))

# Converting to workable form
a1 = l1[:3]
b1 = l1[3:]
a2 = l2[:3]
b2 = l2[3:]

# A = a2 - a1
# B = b1 x b2

A = []
for i in range(3):
    A.append(a2[i] - a1[i])


# Cross product
def cross(v1, v2):
    B = []
    n = len(v1)
    for i in range(n):
        n1 = (i + 1) % n
        n2 = ((n1 + 1) % n) % n
        B.append(v1[n1] * v2[n2] - v2[n1] * v1[n2])
    return B


# Dot product
def dot(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i] * v2[i]
    return sum


# Vector magnitude
def mod(vec):
    sum = 0
    for i in vec:
        sum += i ** 2
    return sum ** (1 / 2)


# Distance
B = cross(b1, b2)

print("Distance as a float")
d = abs(dot(B, A)) / mod(B)
print(d)

print("Distance as a fraction")
Mod = mod(B)
if Mod.is_integer():
    print(str(abs(dot(B, A))) + "/" + str(Mod))
else:
    print(str(abs(dot(B, A))) + "/√" + str(int(Mod**2)))
