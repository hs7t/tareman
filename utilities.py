def invertDictionary(dict):
    return {v: k for k, v in dict.items()}


def canBeInt(value):
    try:
        int(value)
    except ValueError:
        return False
    return True


def canBeString(value):
    try:
        str(value)
    except ValueError:
        return False
    return True

def toType(type_string):
    return {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool
    }.get(type_string)

def listSelect(options, intro="select one:", prompt="your answer", names_allowed=False):
    """
    Gives the user a simple list selection input given:
    - options, a dictionary comprised of option name (str), number (int) pairs
    Settings:
    - intro (str), to be printed before the option list ("")
    - prompt (str), to be printed before the input
    - names_allowed (bool), whether to allow case-insensitive names as input
        > this may cause issues if option names are intable

    Returns an option name or None.
    """
    print(intro)
    for option, key in options.items():
        print(f" - {option} [{key}]")

    response = input(f"{prompt} > ")

    if canBeInt(response):
        return invertDictionary(options)[int(response)]
    elif names_allowed == True and response.lower() in options:
        return response
    else:
        return None
