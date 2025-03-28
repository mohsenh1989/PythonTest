from  Utility import Color, Person



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

       print(Color.Yellow + "======================================" + Color.End)
       print(Color.Cyan+ 'Hi' + Color.End)
       print(Color.Red + "======================================" + Color.End)

       print(Color.Cyan + "Name: {}, Age: {}.".format(Person.name, Person.age)+ Color.End)
       print(Color.Green + "======================================" + Color.End)
       print(Color.Red + "======================================" + Color.End)

