class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    new_people = []
    for person in people:
        Person.people[person["name"]] = Person(person["name"], person["age"])
    for person in people:
        inst_person = Person.people[person["name"]]
        if person.get("wife") is not None:
            inst_person.wife = Person.people.get(person.get("wife"))
        if person.get("husband") is not None:
            inst_person.husband = Person.people.get(person.get("husband"))
        new_people.append(inst_person)

    return new_people
