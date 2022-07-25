def main():
    costNight: int = 1
    costDay: int = 2
    costEvening: int = 3

    print("Enter used power: ")
    power = int(input())

    print("Enter finished time (hours): ")
    hours = int(input())

    if hours >= 0 and hours < 8:
        result = power * costNight
    elif hours >= 8 and hours < 16:
        result = power * costDay
    elif hours >= 16 and hours < 24:
        result = power * costEvening
    else: 
        print("The time is specified incorrectly")

    print("Total price: $", result)

if __name__ == "__main__":
    main()