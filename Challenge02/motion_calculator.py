def main():
    x0 = int(input())
    v0 = int(input())
    a = int(input())
    t = int(input())

    x = x0 + v0*t + (1/2)*a*t**2
    v = v0 + a*t
    d = x - x0

    print()
    
if __name__ == "__main__":
    main()