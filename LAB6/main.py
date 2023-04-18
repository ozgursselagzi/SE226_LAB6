from math import factorial

# QUESTION1
 power = lambda base, exponent: base ** exponent
 fact = lambda num: factorial(num)
 sum_terms = lambda n, x: sum([power(n, i) / fact(i) for i in range(x + 1)])

 n = int(input("Enter a value for n: "))
 x = int(input("Enter a value for x: "))

 e_n = 1 + sum_terms(n, x)

 print("e^n = ", e_n)

# QUESTION2
sum = 0

def sum_recursive(n):
    global sum

    if n == 1:
        sum += 1
        return

    else:
        sum_recursive(n - 1)
        sum += ((-1) ** (n + 1)) / n
        return


n = int(input("Enter a value for n: "))
sum_recursive(n)

print("The sum of the given equation is:", sum)
