def main():
    total=0
    number=int(input("Enter a positive integer or enter a negative integer to quit: "))
    while(number>0):
        total+=number
        number=int(input("Enter a positive interger or enter a negative integer to quit: "))
    display(total)

def display(total):
    print('Total: ',format(total,'.2f'))

main()
