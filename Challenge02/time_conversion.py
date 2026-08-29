def main():
    t = int(input("Enter the time in seconds: "))

    hours = t // 3600
    print(hours)

    minutes = (t%3600) // 60
    print(minutes)

    seconds = (t%3600) % 60
    print(seconds)

    
    
if __name__ == "__main__":
    main()