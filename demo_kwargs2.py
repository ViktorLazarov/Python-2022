def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"]== 'special':
        return "You get a speacial greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David"
    else:
        return "Wrond User!"
    print("******************************")

print(special_greeting(David="Hello"))
print(special_greeting(Deni="Hello"))
print(special_greeting(David="special"))
