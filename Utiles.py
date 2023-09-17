def num_there(s):
    return any(i.isdigit() for i in s)

def is_string_valid(string):
    if num_there(string):
        print("El texto introducido no debe contener números")
        return False
    else:
        return True