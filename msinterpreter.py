
import sys
from words import *
from commands import *
from ignored_characters import *

class Command:
    """A command.
    
    A command represents the most basic units of the language. Each one can be executed
    separately.

    Attributes:
        name: A string indicating the reserved words for the command.
        content: A string indicating extra words that go with the command. Depending on
        whether it needs them or not, it can be used or simply ignored. Most of the time,
        it is ignored.
    """

    def __init__(self, name: str, content: str) -> None:
        self.name = name
        self.content = content

    def __repr__(self) -> str:
        return f"({ self.name },{ self.content })"


def file_to_commands(file_code) -> list:
    """Takes the source code of a given program and returns a list of the commands."""

    commands = []

    while(len(file_code) > 0):
        
        command_name_matched = False
        i = 0

        while i < len(COMMAND_NAMES) and not command_name_matched:
            if file_code[0].strip().startswith(COMMAND_NAMES[i]):

                command_name_matched = True

                if file_code[0].strip().startswith(LOOP_START):
                    file_code.pop(0)
                    commands.append(file_to_commands(file_code))
                elif file_code[0].strip().startswith(LOOP_END):
                    file_code.pop(0)
                    return commands
                else:
                    command_content = file_code[0].replace(COMMAND_NAMES[i], "")
                    command_content = remove_ignored_characters(command_content)

                    command = Command(COMMAND_NAMES[i], command_content)

                    commands.append(command)
                    file_code.pop(0)
            i += 1

        if not command_name_matched:
            file_code.pop(0)
    
    return commands


def remove_ignored_characters(command_content: str) -> str:
    """Takes a string and returns the same string, but without including any of the
    characters in IGNORED_CHARACTERS."""

    modified_content = command_content

    for letter in command_content:
        if letter in IGNORED_CHARACTERS:
            modified_content = modified_content.replace(letter, "")
    
    return modified_content


def execute_commands(commands: list, position: list, clipboard: list, array: list) -> None:

    while(len(commands) > 0):

        if type(commands[0]) == list:
            while array[position[0]] != 0:

                loop = []

                for command in commands[0]:
                    loop.append(command)

                execute_commands(loop, position, clipboard, array)

        elif commands[0].name == ASSIGN_VALUE:

            words = commands[0].content.split(" ")

            for word in words:
                if word in NOUNS:
                    array[position[0]] += 1

                elif word in ADJECTIVES:
                    array[position[0]] *= 2

                elif word == CHANGE_SIGN:
                    array[position[0]] *= -1


        elif commands[0].name == PRINT_POSITION_CHAR:
            print(chr(array[position[0]]), end="")
        
        elif commands[0].name == PRINT_POSITION_INT:
            print(array[position[0]], end="")

        elif commands[0].name == INPUT_TO_POSITION_CHAR:
            input_value = input()
            
            if len(input_value) == 1:
                array[position[0]] = ord(input_value)
        
        elif commands[0].name == INPUT_TO_POSITION_INT:
            input_value = input()
            
            try:
                input_value = int(input_value)
            except:
                print("El valor ingresado no es un int.")

            if type(input_value) == int:
                array[position[0]] = input_value
        
        elif commands[0].name == COPY:
            clipboard[0] = array[position[0]]
        
        elif commands[0].name == PASTE:
            array[position[0]] = clipboard[0]
        
        elif commands[0].name == ASSIGN_ZERO or commands[0].name == ASSIGN_ZERO_ALT:
            array[position[0]] = 0

        elif commands[0].name == MOVE_POINTER_RIGHT:
            if len(array) == position[0]+1:
                array.append(0)

            position[0] += 1
        
        elif commands[0].name == MOVE_POINTER_LEFT:
            if not position[0] == 0:
                position[0] -= 1
        
        commands.pop(0)


def interpretate(path: str) -> None: 
    """Takes a string with the path to the script and interpretates it."""
    
    try:    
        script = open(path, "r", encoding='utf-8')
        file_code = script.read().lower().split(".")
    
        position = [0]
        array = [0]
        clipboard = [0]
        commands = file_to_commands(file_code)
    
        if commands[0].name == PROGRAM_START:
            if commands[len(commands) - 1].name == PROGRAM_END:
    
                execute_commands(commands, position, clipboard, array)
    
            else:
                print("Error: No se encuentra final del código. ¿Termina acaso con "
                        f"\"{ PROGRAM_END }\"?")
        else:
            print("Error: No se encuentra inicio del código. ¿Comienza acaso con "
                    f"\"{ PROGRAM_START }\"?")
        script.close()
            
    except OSError as e:
            print(f"No se pudo abrir {path}:\n{e}\n", file=sys.stderr)


if __name__ == "__main__":
    interpretate(sys.argv[1])         
