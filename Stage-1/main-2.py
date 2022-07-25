from cmath import cos


def main():
    cost: int = 5
    sale: float = 20

    print("Enter the weight:")
    x: int = int(input())

    res: float = x * cost - ((x - cost) * (sale / 100))
    print("Result:", res)

if __name__ == "__main__":
    main()