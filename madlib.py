def read_template(path):
    with open(path, "r") as file:
        contents = file.read()
        return contents

def parse_template(str):
    stripped = ""
    parts = []
    skip = False
    part = ""
    for ch in str:
        if skip:
            if ch == "}":
                stripped += ch
                parts.append(part)
                part = ""
                skip = False
            else:
                part += ch
        elif ch == "{":
            stripped += ch
            skip = True
        else:
            stripped += ch
    return [stripped, tuple(parts)]


def merge(list):
    pass

a = read_template("assets/video_game.txt")
b = parse_template(a)
print(b[0], b[1])