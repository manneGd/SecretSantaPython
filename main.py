import choice
import email_sending
import human

if __name__ == "__main__":
    test_list = human.from_json("liste_test.json")
    choice.solver(test_list)
    file = open("2019_test.txt", "w")
    for x in test_list:
        buf = x.name + " must do a present to " + x.chosen + " & can't have:" + x.restriction + "\n"
        file.write(buf)
        email_sending.send_email(x)
    file.close()

