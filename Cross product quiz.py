from random import randint as rand


# Generate random arguments
def Gen():
    l = []
    for i in range(6):
        if rand(0, 20) == 0:
            temp = (-1) ** (rand(0, 1)) * rand(5, 9)
            l.append(temp)
        else:
            temp = (-1) ** (rand(0, 1)) * rand(0, 5)
            l.append(temp)
    return l


# Compute cross product
def cross(v1, v2):
    B = []
    n = len(v1)
    for i in range(n):
        n1 = (i + 1) % n
        n2 = ((n1 + 1) % n) % n
        B.append(v1[n1] * v2[n2] - v2[n1] * v1[n2])
    return B


# Cleanly display the vectors in the form of a list with equal spacing
def disp(a):
    print("|", end="")
    for i in a:
        if i >= 0:
            print(" " + str(i), end=" ")
        else:
            print(str(i), end=" ")
    print("\b |")


# Actual code
print("Determinant calculation marathon")
q_num = 1
ans = True

while ans:
    try:
        print("Question " + str(q_num) + ":")
        q_num += 1
        l = Gen()
        a = l[:3]
        b = l[3:]
        print("| i  j  k |")
        disp(a)
        disp(b)
        out = cross(a, b)
        ans = list(eval(input("Cross product: ")))
        if ans == out:
            print("Correct")
        else:
            print("Incorrect")
            print(out)
        print()
    except:
        break
