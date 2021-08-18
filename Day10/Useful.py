def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    else:
        name = f_name.title() + " " + l_name.title()
        return name

f_name = input("What is your first name? ")
l_name = input("What is your last name? ")

format = format_name(f_name=f_name, l_name=l_name)
print(format)
