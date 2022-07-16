# new code, now the numbers are completely random
import random
list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 4, 5, 6, 7, 8]

a = (random.choice(list1))
c = (random.choice(list2)) # c before b, because c will always be half of b
b = c + c

print("a + b =", a+b)
print("b = ", "c + c")
print("c =", c)

answer=float(input("What is A? (Type a Number) : "))
if answer == a:
    print("Correct answer!")
else: print("Incorrect answer. A was", (random.choice(list1)))
