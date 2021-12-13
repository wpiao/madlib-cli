import re

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

def parse_template2(str):
    parts = []
    pattern = "{([\w'-]+\s*)+}"
    stripped = re.sub(pattern, "{}", str)
    for part in re.finditer(pattern, str):
        parts.append(part.group()[1:-1])
    return [stripped, tuple(parts)]
    


def merge(str, parts):
    result = ""
    index = 0
    for ch in str:
        if ch == "{":
            continue
        elif ch == "}":
            result += parts[index]
            index += 1
        else:
            result += ch
    return result

if __name__ == "__main__":
    welcome = """
    **************************************
    **       Welcome to the Madlib      **
    **                                  **
    **      Please follow the prompt    **
    **      and provide the response    **
    **************************************
    """
    try:
        contents = read_template("assets/dark_and_stormy_night_template.txt")
        print(welcome)
        stripped, parts = parse_template(contents)
        user_inputs = []
        for part in parts:
            user_inputs.append(input(f"{part}: "))
        results = merge(stripped, tuple(user_inputs))
        with open("assets/results.txt", "w") as file:
            file.write(results)
        print(results)
    except FileNotFoundError as e:
        print(e)
