def my_name():
    print("my name is jana")

def my_meal(food,drink):
    print(f"i like to eat {food} and while drinking {drink}")
my_name()
my_meal("rice ", "water")


def cube(number):
    return(number**3)

print(cube(13))
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(by_three(15)) 
    