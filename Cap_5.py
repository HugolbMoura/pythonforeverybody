largest = None
smallest = None
itervar = float
value = float
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        numm = int(num)
    except:
        print ('Invalid input')
        continue
def max(value):
    largest = None
    for value in [numm]:
        if largest is None or value > largest:
            largest = value
            return largest
p = max(value)
print("Maximum is", p)
def min(itervar):
    smallest = None
    for itervar in [numm]:
        if smallest is None or itervar < smallest:
            smallest = itervar
            return smallest
s = min(itervar)
print('Minimum is', s)

