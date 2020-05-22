#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
def factor(number):
    factors = []
    small = [2,3]

    for divisor in small:
        while number%divisor == 0:
            number = number // divisor
            factors.append(divisor)

    divisor = 5
    while True:
        if number%divisor == 0:
            number = number // divisor
            factors.append(divisor)
        divisor += 2
        if divisor * divisor > number:
            break
    factors.append(number)
    return factors

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 600851475143

    print(factor(number))PyEuler3.
