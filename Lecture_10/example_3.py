x=0

def increment():
    global x
    for _ in range (1000000):
        x += 1

def main():
    global x
    x=0

    increment()
    increment()

for i in range(10):
    main()
    print("Iteration: ", i, " x: ", x)