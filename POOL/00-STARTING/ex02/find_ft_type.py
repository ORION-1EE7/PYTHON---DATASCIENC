

def all_thing_is_obj(object):
    try:
        if "tata!" in object:
            print("List : <class 'list'>")
        elif "toto!" in object:
            print("Tuple : <class 'tuple'>")
        elif "tutu!" in object:
            print("Set : <class 'set'>")
        elif "titi!" in object:
            print("Dict : <class 'dict'>")
        elif "Brian" in object:
            print("Brian is in the kitchen :", object.__class__)
        elif "Toto" in object:
            print("Toto is in the kitchen :", object.__class__)
        else:
            print("Type not found")
            return 42
    except Exception:
        print("Type not found")
        return 42




ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))