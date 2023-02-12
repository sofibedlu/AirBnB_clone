#!/usr/bin/python3

"""define the class HBNBCommand
    this class inherit Cmd class from cmd module wich facilitates
    the design of custome command line interpretor by providing
    different builtin function and attributes
"""

import re
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """an entry point of the command interpretor"""

    prompt = "(hbnb) "

    @staticmethod
    def list_of_classes():
        """return list of classes"""

        return ['BaseModel', 'User', 'Place', 'State', 'City',
                'Amenity', 'Review']

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ctrl+D to exit the program"""
        return True

    def emptyline(self):
        """don't do anything when its emptyline"""
        pass

    def default(self, line):
        """update the default method
        """

        if '.' in line:
            class_name, command = line.split('.')
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                print(self.do_count(class_name))
            elif bool(re.match(r"\w+\.show\([\"'][\w-]+[\"']\)", line)):
                arg = line.split('.')
                class_name = arg[0]
                uid = arg[1].split('"')[1]
                name_id = "{} {}".format(class_name, uid)
                self.do_show(name_id)

    def do_create(self, line):
        """create new instance of BaseModel, saves it(to the JSON file)
            and prints the id
            Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
        elif not (line in HBNBCommand.list_of_classes()):
            print("** class doesn't exist **")
        else:
            new = eval(line)()
            new.save()
            print("{}".format(new.id))

    def do_show(self, line):
        """Prints the string representation of an instance based on
            the class name and id
            Usage: show <class name> <id>
        """

        objs = storage.all()
        if not line:
            print("** class name missing **")
        elif not line.split()[0] in HBNBCommand.list_of_classes():
            print("** class doesn't exist **")
        elif len(line.split()) == 1:
            print("** instance id missing **")
        elif (objs.get("{}.{}".format(line.split()[0], line.split()[1]))
                is None):
            print("** no instance found **")
        else:
            args = line.split()
            key = "{}.{}".format(args[0], args[1])
            print(objs.get(key))

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
            and save the changes into the JSON file
        """

        objs = storage.all()
        if not line:
            print("** class name missing **")
        elif not line.split()[0] in HBNBCommand.list_of_classes():
            print("** class doesn't exist **")
        elif len(line.split()) == 1:
            print("** instance id missing **")
        elif (objs.get("{}.{}".format(line.split()[0], line.split()[1]))
                is None):
            print("** no instance found **")
        else:
            args = line.split()
            key = "{}.{}".format(args[0], args[1])
            del(objs[key])
            storage.save()

    def do_all(self, line):
        """prints all string representation of all instances based or not on
            the class name.
            the printed result must be a list of strings
        """

        list_objs = []
        objs = storage.all()
        if line:
            if not (line in HBNBCommand.list_of_classes()):
                print("** class doesn't exist **")
            else:
                for key, value in objs.items():
                    if line == value.__class__.__name__:
                        list_objs.append(str(value))
                print(list_objs)
        else:
            for key, value in objs.items():
                list_objs.append(str(value))
            print(list_objs)

    def do_count(self, line):
        """
        return nuber of instances of a class
        """
        list_objs = []
        objs = storage.all()
        if line:
            if not (line in HBNBCommand.list_of_classes()):
                return("** class doesn't exist **")
            else:
                for key, value in objs.items():
                    if line == value.__class__.__name__:
                        list_objs.append(str(value))
            return(len(list_objs))

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save the change to JSON file.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        """

        objs = storage.all()
        if not line:
            print("** class name missing **")
        elif not line.split()[0] in HBNBCommand.list_of_classes():
            print("** class doesn't exist **")
        elif len(line.split()) == 1:
            print("** instance id missing **")
        elif (objs.get("{}.{}".format(line.split()[0], line.split()[1]))
                is None):
            print("** no instance found **")
        elif len(line.split()) == 2:
            print("** attribute name missing **")
        elif len(line.split()) == 3:
            print("** value missing **")
        else:
            x = 0
            args = line.split()
            if x == 0:
                try:
                    new_value = int(args[3])
                except ValueError:
                    x = 1
            if x == 1:
                try:
                    new_value = float(args[3])
                except ValueError:
                    if args[3].startswith("'") and args[3].endswith("'"):
                        new_value = args[3][1:-1]
                    elif args[3].startswith('"') and args[3].endswith('"'):
                        new_value = args[3][1:-1]
                    else:
                        new_value = args[3]

            obj = objs["{}.{}".format(args[0], args[1])]
            setattr(obj, args[2], new_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
