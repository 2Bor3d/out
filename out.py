def out(text: any, color: int=38):
    print(f"\033[{color}m{text}\033[0m")
    