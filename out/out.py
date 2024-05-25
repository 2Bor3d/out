import json
import os


def get_dict(path: str="dict.json", package_dir: bool=True):
    if package_dir:
        path = f"{os.path.dirname(os.path.abspath(__file__))}/{path}"
    with open(path, "r") as file:
        return json.load(file)


def get_color(name: str, dictionary: dict=None, path: str="dict.json", package_dir: bool=True, no_exeption: bool=False) -> int:
    if dictionary != None:
        colors = dictionary
    else:
        colors = get_dict(path=path, package_dir=package_dir, no_exeption=no_exeption)

    if name in colors:
        for i in colors:
            if name == i:
                return colors[i]
    else:
        if not no_exeption:
            raise Exception(f"Color: '{name}' not found")
        return 38


def out(text, color: int|str=38, *args, dictionary: dict=None, path: str="dict.json", package_dir: bool=True, no_exeption: bool=False, output=True) -> str:
    if type(color) == str:
        color = get_color(color, dictionary=dictionary, path=path, package_dir=package_dir, no_exeption=no_exeption)
    combine = f"\033[{color}m{text}"
    for i in range(int(len(args)/2)):
        if type(args[i*2+1]) == str:
            args[i*2+1] = get_color(args[i*2+1])
        combine += f"\033[{args[i*2+1]}m{args[i*2]}"
    combine += "\033[0m"
    
    if output:
        print(combine)
    return combine


def inp(text, color: int|str=38, *args, dictionary: dict=None, path: str="dict.json", package_dir: bool=True, no_exeption: bool=False) -> str:
    return input(out(text, color, *args, dictionary=dictionary, path=path, package_dir=package_dir, no_exeption=no_exeption, output=False))
    

def options(reach: int=None, dictionary: dict=None, path: str="dict.json", package_dir: bool=True) -> None:
    if type(reach) == int:
        for i in range(reach):
            out(i, i)

    if dictionary == None:
        dictionary = get_dict(path=path, package_dir=package_dir)
    
    for color in dictionary:
        out(f"{color}: {dictionary[color]}", dictionary[color])
