# exercise 1.5

def sum_all(a, b):
    """This function adds integers between a and b
    """
    sum_numbers = 0
    summable = a
    while summable <= b:
        sum_numbers += summable
        summable += 1
    return sum_numbers


print(sum_all(5, 8))


# exercise 1.6
def sum_all1(a, b):
    """This function returns add integers between a and b if a < b, and
    integers between b and a, if b < a, and 0, if a == b
    """
    sum_numbers = 0
    if a == b:
        return sum_numbers
    elif a < b:
        summable = a
        while summable <= b:
            sum_numbers += summable
            summable += 1
    else:
        summable = b
        while summable <= a:
            sum_numbers += summable
            summable += 1
    return sum_numbers


print(sum_all1(12, 10))


# exercise 1.7
def pow(base, exp):
    """ this function returns the exp power of the base number
    """
    if base == 0 and exp < 0:
        return None
    elif exp == 0:
        return 1
    elif exp > 0:
        return base ** exp
    else:
        return 1 / base ** (-exp)


print(pow(5, 3))


# exercise 1.8
def abs(n):
    if n > 0:
        return n
    return -n


def guess_enough(value, target):
    if abs(value ** 3 - target) < 0.0001:
        return True
    return False


def improve(root, target):
    return (target / (root ** 2) + 2 * root) / 3


def cube(n):
    """This function returns the approximated cube root of number n
    """
    root = 1
    while not guess_enough(root, n):
        root = improve(root, n)
    return root


print(cube(2))


# exercise 1.9
def inc(a):
    return a + 1


def dec(a):
    return a - 1


def add1(a, b):
    if a == 0:
        return b
    else:
        return inc(add1(dec(a), b))


def add2(a, b):
    if a == 0:
        return b
    else:
        return add2(dec(a), inc(b))


# add1(4, 5) -> inc(add1(3, 5)) -> inc(inc(add1(add1(2, 5)))) -> inc(inc(inc(add1(1, 5)))) ->
# -> inc(inc(inc(inc(add(0, 5))))) -> inc(inc(inc(inc(5)))) -> inc(inc(inc(6))) -> inc(inc(7)) -> inc(8) -> 9
# There is a chain of operations, so add1 function is a recursion

# add2(4, 5) -> add2(3, 6) -> add2(2, 7) -> add2(1, 8) -> add2(0, 9) -> 9
# There isn't a chain of operations, that is, the program needs to remember only the last result returned by the cycle
# add2 function is a tail recursion function


# exercise 1.10
def ackermann(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return ackermann(x - 1, ackermann(x, y - 1))


# ackermann(1, 5) -> ackermann(0, ackermann(1, 4)) -> ackermann(0, ackermann(0, ackermann(1, 3))) ->
# ackermann(0, ackermann(0, ackermann(0, ackermann(1, 2)))) ->
# ackermann(0, ackermann(0, ackermann(0, ackermann(0, ackermann(1, 1))))) ->
# ackermann(0, ackermann(0, ackermann(0, ackermann(0, 2)))) -> ackermann(0, ackermann(0, ackermann(0, 4))) ->
#  -> ackermann(0, ackermann(0, 8)) -> ackermann(0, 16) -> 32


print(ackermann(2, 4))
print(ackermann(3, 3))

