def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
    print("************************")

fav_colors(colt="Purple", ethel="Red", Deni="Blue")
fav_colors(colt="Purple", ethel="Red")
fav_colors(colt="Purple")
