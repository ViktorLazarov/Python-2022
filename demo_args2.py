def correct_user(*args):
    if "Viktor" and "Lazarov" in args:
        return "Welcome!"
    else:
        return "Wrong User!"


print(correct_user("Viktor", 1, True))
print(correct_user("Viktor", 2, False, "Lazarov"))
