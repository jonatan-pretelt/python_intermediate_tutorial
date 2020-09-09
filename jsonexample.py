import json

person = {'name':'john', 'age': 31, 'city':'Tampa', 'hasChildren': False}

personJSON = json.dumps(person)  #dumps to dump to string
print(personJSON)


with open('person.json', 'w') as file:
    json.dump(person,file)  #dump to file


#to convert json to python dict
person = json.loads(personJSON)
print(person)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
######################################

#custom code to jsonify a class

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# to decode back to dict
user = json.loads(userJSON)
print(user)

#############################################################################

