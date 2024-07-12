import json
import argparse

parser = argparse.ArgumentParser(description="Phonebook application")
subparser = parser.add_subparsers(dest="command", required=True, help="command")
# for save a person
save_parser = subparser.add_parser("save", help="to save a contact")
save_parser.add_argument("name", help="name of contants", type=str)
save_parser.add_argument("num", help="number of contants", type=str)
# for find a person
find_parser = subparser.add_parser("find", help="contants to find")
find_parser.add_argument("name", help="to find a contants", type=str)
# for del a person
del_parser = subparser.add_parser("del", help="to dell a contants")
del_parser.add_argument("name", help="to dell a contants", type=str)
# for ls a person
ls_parser = subparser.add_parser("ls", help="to represent all list contants")

args = parser.parse_args()
# for saving a person
if args.command == "save":
    def save_name(name, num):
        try:
            with open("contacts.json", "r") as file:
                phonebook = json.load(file)
        except FileNotFoundError:
            phonebook = {}
        phonebook[name] = num
        with open("contacts.json", "w") as file:
            string = json.dump(phonebook, file, indent=4)

    if args.name and args.num:
        save_name(args.name, args.num)
        print("person have been saved successfuly")
# for finding a person
if args.command == "find":
    def find_name(name):
        try:
            with open("contacts.json", "r") as file:
                phonebook = json.load(file)
        except FileNotFoundError:
            print("there is no list of persons")
        try:
            print(f"{name}: {phonebook[name]}")
        except KeyError:
            print("person not found")   
    if args.name:
        find_name(args.name)
# for removing a person
if args.command == "del":
    def dell_name(name):
        try:
            with open("contacts.json", "r") as file:
                phonebook = json.load(file)
        except FileNotFoundError:
            print("there is no list of persons")
        try:
            del phonebook[name]
            with open("contacts.json", "w") as file:
                json.dump(phonebook, file, indent=4)
            print(f"person has been deleted succefully")
        except KeyError:
            print("person not found")   
    if args.name:
        dell_name(args.name)
# for showing list of persons
if args.command == "ls":
    try:
        with open("contacts.json", "r") as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        print("there is no list of persons")
    for key, values in phonebook.items():
        print(f"{key}: {values}")