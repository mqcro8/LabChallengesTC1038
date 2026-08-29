def main():
    price = int(input())
    quantity = int(input())
    tax_product = int(input())

    subtotal = price*quantity
    print("Subtotal :", subtotal)

    tax = (subtotal*tax_product)/100
    print("Tax :", tax)

    total = subtotal + tax
    print("Total :", total)

    average = total / quantity
    print("Average :", average)
    
if __name__ == "__main__":
    main()