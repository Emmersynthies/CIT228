import json

def menu():
    selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("Error, please try again")
        selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    return selection

def print_menu():
    selection = int(input("1-word and definition, 2-word, 3-definition  "))
    while selection!=1 and selection!=2 and selection!=3:
        print("Error, please try again")
        selection = int(input("1-word and definition, 2-word, 3-definition  "))
    return selection

def create(object):
    overwrite = input("You are creating a new file, existing data will be erased (q to quit, any key to continue) ")
    if overwrite !="q":
        with open("Chapter10/glossary.json", "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def append(new_item):
    with open("Chapter10/glossary.json", "r+") as add_file:
        glossaryDictionary = json.load(add_file)
        glossaryDictionary.update(new_item)
        add_file.seek(0)
        json.dump(glossaryDictionary, add_file, indent=4, sort_keys=True)
        print("Info has been added to glossary.json")

def read():
    try:
        with open("Chapter10/glossary.json") as read_file:
            glossaryDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in glossaryDictionary.items():
            print(key.title(), "  means ", value)

def get_key():
    term=input("What is your word? ")
    return term

def get_value():
    definition=input("Enter your definition ")
    return definition

glossaryDictionary={
    "key-value": "a set of values associated with each other.",
    "boolean-value": "is either true or false.",
    "boolean-expression": "is just another name for a conditional test.",
    "equality operator": "return true if the value on the left and right side of the operator match and false if they don't match.",
    "conditional test": "An expression in every heart of an if statement that can be evaluated as true or false.",

}
choice=menu()
while choice != 4:
    if choice == 1:
        create(glossaryDictionary)
    elif choice == 2:
        read()
    elif choice == 3:
        new_word=get_key()
        new_definition=get_value()
        new_dictionary_entry={new_word:new_definition}
        append(new_dictionary_entry)
    else:
        print("Error, please try again")        
    choice=menu()
