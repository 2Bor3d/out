def out(text: any, color: int=38, *args):
    print(f"\033[{color}m{text}\033[0m")
    