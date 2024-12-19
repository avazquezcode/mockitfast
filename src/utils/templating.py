def replace_variables_in_str(variables: dict, text: str) -> str:
    #  This is a function that replaces all occurrences of variables in a string
    for var, val in variables.items():
        var_candidate = "{" + var + "}"
        if text is not None:
            text = text.replace(var_candidate, val)
    return text


def replace_variables_in_dict(variables: dict, data: dict) -> dict:
    #  This is a function that replaces all occurrences of variables in dictionaries
    #  considering both the case where the variables might be in the key
    #  or in the value

    def replace_variable(target):
        if not isinstance(target, str):
            #  The target is not a string, so we return
            #  to go deeper on it afterwards
            return target

        for var, val in variables.items():
            var_candidate = "{" + var + "}"
            target = target.replace(var_candidate, val)
        return target

    new_dict = {}
    for key, value in data.items():
        #  Handle the key
        new_key = replace_variable(key)

        #  Handle the value
        if isinstance(value, str):
            new_value = replace_variable(value)
        elif isinstance(value, dict):
            #  Recursive call to get inside the next level of the dictionary
            new_value = replace_variables_in_dict(variables, value)
        elif isinstance(value, list):
            new_value = [
                replace_variable(v) if isinstance(v, str) else v
                for v in value
            ]
        else:
            new_value = value

        new_dict[new_key] = new_value
    return new_dict
