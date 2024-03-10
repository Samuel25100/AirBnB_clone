#!/usr/bin/python3
"""Class Consl is cmd interpreter for airbnb."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The class were console or cmd interpreter define at."""

    prompt = "(hbnb) "
    cl = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """Do nothing when there is no command or empty line."""
        pass

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_create(self, line):
        """Create a new inst BaseModel,saves it to JSON and prints the id."""
        if line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.cl:
            print("** class doesn't exist **")
        else:
            class_name = line.strip()
            n_model = globals()[class_name]()
            n_model.save()
            print("{}".format(n_model.id))

    def do_show(self, line):
        """Print the string rep __str of inst based on the class name and id."""
        argv = line.split()
        len_arg = len(argv)
        all_arg = storage.all()

        if line == "":
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len_arg == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in all_arg:
            print("** no instance found **")
        else:
            print(all_arg["{}.{}".format(argv[0], argv[1])].__str__())

    def do_destroy(self, line):
        """Delete an instance based on the class name and id."""
        argv = line.split()
        len_arg = len(argv)
        all_arg = storage.all()

        if line == "":
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len_arg == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in all_arg:
            print("** no instance found **")
        else:
            del all_arg["{}.{}".format(argv[0], argv[1])]
            BaseModel.save(self)

    def do_all(self, line):
        """Print all __str__ of all instances based or not on the class name."""
        list_str = []
        dict_v = storage.all()

        if len(line) != 0:
            if line not in HBNBCommand.cl:
                print("** class doesn't exist **")
            else:
                for key, val in dict_v.items():
                    k = key.split('.')[0]
                    if k == line:
                        list_str.append(val.__str__())
                print("{}".format(list_str))
        else:
            for key, val in dict_v.items():
                k = key.split('.')[0]
                if k in HBNBCommand.cl:
                    list_str.append(val.__str__())
            print("{}".format(list_str))

    def do_update(self, line):
        """Update an instance based on class name and id."""
        argv = line.split()
        dict_all = storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in dict_all.keys():
            print("** no instance found **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif (len(argv) == 3):
            try:
                type(eval(argv[2])) != dict
            except NameError:
                print("** value missing **")
        else:
            key = "{}.{}".format(argv[0], argv[1])
            inst = dict_all[key]
            if hasattr(inst, argv[1]):
                getattr(inst, argv[1], argv[2])
                inst.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
