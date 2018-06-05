def fizzbuzz():
    number = raw_input("input a number for fizzbuzz:")
    number = int(number)
    for num in range(1,number):
            if num % 15 == 0:
                print(str(num) + ':fizzbuzz')
            elif num % 3 == 0:
                print(str(num) + ':fizz')
            elif num % 5 == 0:
                print(str(num) + ':buzz')
            else:
                print(str(num) + ":")

if __name__ == "__main__":
    fizzbuzz()
