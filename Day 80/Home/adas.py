

def comparisons(a, b):
    print(f"a = {a}, b = {b}")
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b: ", a > b)
    print("a < b: ", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)

def check_sign(n):
    if n > 0:
        return "დადებითი"   
    elif n < 0:
        return "უარყოფითი"  
    else:
        return "ნული"        

if __name__ == "__main__":
   
    a, b = 10, 20
    comparisons(a, b)

    
    try:
        s = input("\nშეიყვანეთ რიცხვი: ")
        num = float(s)
    except ValueError:
        print("ტყუილი შეყვანა: გთხოვთ შეიყვანოთ რიცხვი.")
    else:
        print("რიცხვის მდგომარეობა:", check_sign(num))