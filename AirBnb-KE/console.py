#!/usr/bin/python3
"""The console runner
"""
import cmd
import sys
import models.base_model
from models import storage


class KBNBCommand(cmd.Cmd):
    """Console app
    """
    prompt = '(kbnb) '
    classList = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
    file = None

    def do_EOF(self):
        """Prints new line
        """
        print()

    def do_quit(self, arg):
        'Stop recoding and quits the program'
        quit()
        return True


    def do_create(self, arg):
        """Creates BaseModel
        Args: None
        """
        argv = args.split()
        if len(argv) < 1:
            print('** class name missing **')
        elif argv[0] not in self.classList:
            print('** class doesn\'t exist **')
        else:
            className = argv[0]
            if className == 'BaseModel':
                class_mdl = models.basemodel.BaseModel()
                class_mdl.save()
                print(class_mdl.id)
            elif className == 'User':
                class_mdl = models.basemodel.BaseModel()
                class_mdl.save()
                print(class_mdl.id)
                pass
            elif className == 'Place':
                class_mdl = models.basemodel.BaseModel()
                class_mdl.save()
                print(class_mdl.id)
                pass
            elif className == 'State':
                class_mdl = models.basemodel.BaseModel()
                class_mdl.save()
                print(class_mdl.id)
                pass
            elif className == 'Amenity':
                class_mdl = models.basemodel.BaseModel()
                class_mdl.save()
                print(class_mdl.id)
                pass
            else:
                class_mdl = models.basemodel.BaseModel()
                class_mdl.save()
                print(class_mdl.id)
                pass
            class_mdl.save()
            print(class_mdl.id)

    def do_show(self, args):
        argv = args.split()
        if len(argv) < 2:
            print('** class name missing **')
        elif sys.argv[1] not in self.classList:
            print('** class doesn\'t exist **')
        else:
            className = argv[0]
            classId = argv[1]
            all_objs = storage.all()
            obj_search = all_objs[className].get(classId)
            print(obj_search)

    def do_destroy(self, args):
        argv = args.split()
        if len(sys(argv)) < 2:
            print('** class name missing **')
        elif sys.argv[1] not in self.classList:
            print('** class doesn\'t exist **')
        else:
            className = sys.argv[1]
            classId = sys.argv[2]
            if className not in self.classList:
                print('** class doesn\'t exist **')
            else:
                classKey= "{}.{}".format(className, classId)
                del(storage[classKey])
                storage.save()

    def do_all(self, args):
        argv = args.split()
        if len(argv) > 0:
            className = sys.argv[0]
            if className not in self.classList:
                print('** class doesn\'t exist **')
            all_objs = list(storage.all())
            newList = []
            for m in range(len(all_objs)):
                if all_objs[m] == className:
                    newList.append(all_objs[m])

            print(newList)

        else:
            all_objs = storage.all()
            print(all_objs)

    def do_update(self, args):
        """Update a class
        """
        argv = args.split()
        if len(argv) < 2:
            print('** class name missing **')
        elif argv[0] not in self.classList:
            print('** class doesn\'t exist **')
        elif len(argv) < 3:
            print('** instance id missing **')
        elif len(argv) < 4:
            print('** class name missing **')

        else:
            className = argv[0]
            classId = argv[1]
            attrName = argv[2]
            attrValue = argv[3]
            all_objs = storage.all()
            updateObj = all_objs[className][classId].get(attrName)
            if updateObj is None:
                updateObj = all_objs[className][classId][attrName] = attrValue
            storage.save()
  


if __name__ == '__main__':
    KBNBCommand().cmdloop()
