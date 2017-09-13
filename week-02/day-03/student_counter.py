students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

def candies():
    allcandies = 0
    for i in students:
        allcandies += i['candies']
    print(allcandies)


def studentscandies():
    candies = 0
    for i in students:
        name = i['name']
        candies = i['candies']
        print(name, candies) 
       

candies()
studentscandies()

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def peopleage():
    sumage = 0
    for i in students:
        if i['candies'] < 5:
            sumage += i['age']
    print(sumage)

peopleage()