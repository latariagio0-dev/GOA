#vaketebt kalkulators
def calculator():
    print("აირჩიეთ ოპერაცია:")
    print("1. მიმატება (+)")
    print("2. გამოკლება (-)")
    print("3. გამრავლება (*)")
    print("4. გაყოფა (/)")

    choice = input("შეიყვანეთ არჩევანი (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("შეიყვანეთ პირველი ციფრი: "))
        num2 = float(input("შეიყვანეთ მეორე ციფრი: "))

        if choice == '1':
            print(f"შედეგი: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"შედეგი: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"შედეგი: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"შედეგი: {num1} / {num2} = {num1 / num2}")
            else:
                print("შეცდომა: ნულზე გაყოფა არ შეიძლება ბრატ")
    else:
        print("არ ხარ ბრატ მართალი არჩევანი!")

if __name__ == "__main__":
    calculator()