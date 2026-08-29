def main():
    amount = int(input())

    fivehundreds = amount // 500
    print("500: ",fivehundreds)

    twohundrerds = (amount % 500) // 200
    print("200: ",twohundrerds)

    onehundreds = ((amount % 500) % 200) // 100
    print("100: ",onehundreds)

    fifties = (((amount % 500) % 200) % 100) // 50
    print("50: ",fifties)

    twenties = ((((amount % 500) % 200) % 100) % 50) // 20
    print("20: ",twenties)

    remaining = ((((amount % 500) % 200) % 100) % 50) % 20
    print("Remaining: ",remaining)

if __name__ == "__main__":
    main()