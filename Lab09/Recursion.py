def product_of_digits(x):
    if x < 0:
        x *= -1
    if x < 10:
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)
    
def array_to_string(a, index=0):
    if index == len(a):
        return ""
    elif index == len(a) - 1:
        return str(a[index])
    else:
         return str(a[index]) + "," + array_to_string(a, index + 1)
    
def log(base, value):
    if value <= 0 or base <= 1:
        raise ValueError("Invalid input: value must be greater than 0 and base must be greater than 1")
    if value < base:
        return 0
    else:
        return 1 + log(base, value // base)


def main():
    print(product_of_digits(1234))
    print(product_of_digits(232))
    print(array_to_string([1, 2, 3, 4, 5]))
    print(log(10, 4567))
main()