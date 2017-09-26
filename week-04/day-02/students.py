
# Create a Person class with the following fields:

# name: the name of the person
# age: the age of the person (whole number)
# gender: the gender of the person (male / female)
# And the following methods:

class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm", self.name, self.age, "year old", self.gender)
    
    def get_goal(self):
        print("My goal is: Live for the moment!")

person1 = Person("Jane Doe", "30", "female")
person1.introduce()
person1.get_goal()

# Student

class Student(object):

    def __init__(self, previous_organization, skipped_days):
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print("Be a junior software developer.")

    def introduce(self):
        print( "Hi, I'm", self.name, self.age, "year old", self.gender, "from", self.previous_organization,  who skipped skipped_days days from the course already.")
# Create a Student class that has the same fields and methods as the Person class, and has the following additional

# fields:
# previous_organization: the name of the student’s previous company / school
# skipped_days: the number of days skipped from the course
# methods:
# get_goal(): prints out "Be a junior software developer."
# introduce(): "Hi, I'm name, a age year old gender from previous_organization who skipped skipped_days days from the course already."
# skip_days(number_of_days): increases skipped_days by number_of_days
# The Student class has the following constructors:

# Student(name, age, gender, previous_organization): beside the given parameters, it sets skipped_days to 0
# Student(): sets name to Jane Doe, age to 30, gender to female, previous_organization to The School of Life, skipped_days to 0
# Mentor

# Create a Mentor class that has the same fields and methods as the Personclass, and has the following additional

# fields:
# level: the level of the mentor (junior / intermediate / senior)
# methods:
# get_goal(): prints out "Educate brilliant junior software developers."
# introduce(): "Hi, I'm name, a age year old gender level mentor."
# The Mentor class has the following constructors:

# Mentor(name, age, gender, level)
# Mentor(): sets name to Jane Doe, age to 30, gender to female, level to intermediate
# Sponsor

# Create a Sponsor class that has the same fields and methods as the Person class, and has the following additional

# fields:
# company: name of the company
# hired_students: number of students hired
# method:
# introduce(): "Hi, I'm name, a age year old gender who represents company and hired hired_students students so far."
# hire(): increase hired_students by 1
# get_goal(): prints out "Hire brilliant junior software developers."
# The Sponsor class has the following constructors:

# Sponsor(name, age, gender, company): beside the given parameters, it sets hired_students to 0
# Sponsor(): sets name to Jane Doe, age to 30, gender to female, company to Google and hired_students to 0
# Result

# Your program should result this output if you run it with this input