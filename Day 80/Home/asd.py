
def comparisons():
    a = 10
    b = 20
    print(f"a = {a}, b = {b}")
    print("a == b :", a == b)
    print("a != b :", a != b)
    print("a >  b :", a > b)
    print("a <  b :", a < b)
    print("a >= b :", a >= b)
    print("a <= b :", a <= b)

def sign_check():
    s = input("განათავსეთ რიცხვი (Enter-ით დაადასტურეთ): ").strip()
    try:
       
        n = float(s) if ('.' in s or 'e' in s or 'E' in s) else int(s)
    except ValueError:
        print("არასწორი შეყვანა: გთხოვთ ჩაწეროთ რიცხვი.")
        return

    if n > 0:
        print("რიცხვი დადებითი.")
    elif n < 0:
        print("რიცხვი უარყოფითი.")
    else:
        print("რიცხვი ნულოვანი.")

def main():
    comparisons()
    print()  
    sign_check()

if __name__ == "__main__":
    main()