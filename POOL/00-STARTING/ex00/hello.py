
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[-1] = "world!"
ft_tuple = ft_tuple[:1] + ("morocco", )
ft_set.clear()
ft_set.update({"Hello", "Rabat"})

ft_dict["Hello"] = 1337

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)