#!/usr/bin/python3
"""Module: console.py"""
import cmd


class HBNBCommand(cmd.Cmd):
    """"""

    prompt = '(hbnb)'

    def do_hola(self, persona):
        """asdasdasd"""
        if persona:
            print("Bien ", persona)
        else:
            print("No hay persona")

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
