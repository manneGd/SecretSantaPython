import json


class Human:
    def __init__(self, data):
        self.__dict__ = data
        self.isChosen = False

    # def __init__(self, name, email, restriction, chosen):
    #     self.name = name
    #     self.email = email
    #     self.restriction = restriction
    #     self.chosen = chosen
    #     self.isChosen = False


def from_json(file):
    humans = list()
    with open(file, "r") as json_file:
        list_human = json.load(json_file)
    for human in list_human:
        humans.append(Human(human))
    json_file.close()
    return humans
