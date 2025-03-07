import keyword
import string
def variable_name(name):
    if name in keyword.kwlist:
        return False
    if any(c.isupper() for c in name):
        return False
    if name[0].isdigit():
        return False
    if name.count("_") > 1:
        return False
    if not all(just in string.ascii_lowercase + string.digits + "_" for just in name):
        return False
    return True
user_input = input("Enter variable name: ").strip()
print(variable_name(user_input))
