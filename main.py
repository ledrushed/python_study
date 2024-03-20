def increase(person):
    person['age'] += 1
    return person

person_one = {
    'name': 'Bob',
    'age': 21
}

increase(person_one)
print(person_one['age'])
print(type(person_one))