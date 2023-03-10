try:
    a = int(input("First number is: "))
    b = int(input("Second number is: "))
    print(a / b)
except ValueError:
    print("Please enter a valid number next time! ")
except ZeroDivisionError:
    print("Cannot divide by 0!")
    b = 1
    print(a / b)
finally:
    print("Done chiki done done..") # For closing a stream


def some_func():
    if True:
        raise ValueError("Something went terribly wrong")


# some_func()

x = 1000
y = 20
# assert(x < y)


width = 5
for num in range(5,12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

