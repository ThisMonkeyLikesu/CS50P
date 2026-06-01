def main():
    mass = int(input("What`s mass? "))
    print(count_energy(mass))


def count_energy(mass:int)->int:
    return mass * pow(300000000,2)

main()