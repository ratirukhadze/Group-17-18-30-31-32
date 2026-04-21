

def main():
    try:
        a = float(input("პირველი რიცხვი: "))
        b = float(input("მეორე რიცხვი: "))
    except ValueError:
        print("გთხოვთ შეიყვანოთ ლეგალური რიცხვები.")
        return

    print(f"ჯამი: {a + b}")
    print(f"სხვაობა (a - b): {a - b}")
    print(f"ნამრავლი: {a * b}")
    if b != 0:
        print(f"განაყოფი (a / b): {a / b}")
    else:
        print("განაყოფი: შეცდომა — ცდომიერი: გამყოფი 0-ია.")

    
    print(f"5^2 = {5 ** 2}")
    print(f"5^3 = {5 ** 3}")

   
    print(f"17-ში რამდენჯერ შედის 5 (17 // 5): {17 // 5}")
    print(f"17-ში ნაშთი 5-ით (17 % 5): {17 % 5}")


if __name__ == "__main__":
    main()