people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
#normal func mode
def f(person):
    return person["name"]
people.sort(key=f)

print(people)
#lambda func

people.sort(key=lambda person:person["name"])
print(people)
