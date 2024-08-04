import math
def main():
    mass = int(input("m: "))
    energy = Einstein(mass)
    print(energy)

def Einstein(m):
    c = 300000000
    e = m * c**2
    return e

main()
