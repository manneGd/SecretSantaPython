import random


def set_chosen(perso1, perso2):
    if perso1.chosen is ""\
            and perso1.name != perso2.name\
            and not perso2.isChosen\
            and perso1.restriction != perso2.name:
        perso1.chosen = perso2.name
        perso2.isChosen = True


def set_chosen_random(list_persons):
    x = list_persons.copy()
    random.shuffle(x, random.random)
    for p in list_persons:
        for p2 in x:
            set_chosen(p, p2)


def check_empty_chosen(list_person):
    for is_chosen in list_person:
        if is_chosen.chosen is "":
            for p in list_person:
                p.chosen = ""
                p.isChosen = False
            return False
    return True


def solver(list_person):
    while not check_empty_chosen(list_person):
        set_chosen_random(list_person)
