def compute_PPV(sensitivity, specificity, incidence):
    PPV = (incidence*sensitivity)/(incidence*sensitivity + (1-incidence)*(1-specificity))
    print("PPV = ", PPV)

def main():
    sensitivity = int(input(""))
    specificity = int(input(""))
    incidence = int(input(""))

    compute_PPV(sensitivity, specificity, incidence)


if __name__ == "__main__":
    main()