# LOOPS
scores = [10, 11, 22, 19, 10, 8]
## for
for num in scores:
    print(f"The current item is: {num}")

## while
it = 0
while it < len(scores):
    print(f"This item in the while loop is {scores[it]}")
    it += 1

## list creation using list comprehension
### starting with a value create a list of the next 20 values in increments of 3 eg. x = 10, => [13, 16, 19, 22, 25, ... , 70]
gen_sequence = []
c = 1
start = 10
while c < 20:
    start += 3
    gen_sequence.append(start)
    c += 1

x_start = 20
x_sequence = [ x_start + i + 3 for i in range(20)]

square_sequence = [ (i+1)*(i+1) for i in range(20) ]
print(f"squares: {square_sequence}")

print(f"Sequence: {gen_sequence}")
print(f"x-Sequence: {x_sequence}")


# Conditional Statements => selection statements / error handlers
## if/else => selection statement
age = 19
if age < 19:
    print("You are too young")
elif age > 70:
    print("You are supposed to be sleeping")
else:
    print("Old enough here")

## try/except => error handler statement
def divide(num1, num2):
    try:
        q = num1 / num2
        print(f"The quotient is: {q}")
    except (TypeError, ZeroDivisionError) as exc:
        print(f"The exception that arose was: {type(exc)}")
        # print("You are trying to perform an illegal math op.")
    finally:
        print("This runs regardless")

divide(10, 2)


# Classes and Objects
## Class
class Animal:
    def __init__(self, name, lifespan, isColdBlooded):
        self.name = name
        self.lifespan = lifespan,
        self.isColdBlooded =  isColdBlooded
    
    def introduce(self):
        print(f"My name is {self.name} and I live for {self.lifespan} years. Before I forget, I am cold blooded- {self.isColdBlooded}")

## Instance/Object
dog = Animal("Dog", 10, False)
croc = Animal("Crocodile", 35, True)

dog.introduce()
croc.introduce()