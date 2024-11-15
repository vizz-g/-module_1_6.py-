my_dict = {"nikita" : 1999, "egor": 2013}
print(my_dict)
print(my_dict["nikita"])
my_dict["grisha"] = 2011
print(my_dict["grisha"])
print(my_dict)
my_dict.update({"kiril": 1991,
                "saha": 1942})
print(my_dict)
a = my_dict.pop("nikita")
print(a)
print(my_dict)
my_set = {1,1,1,1,1,2,3,4,4,4,5,6,6,6,6,False,False,"ASD","ASD",True}
print(my_set)
my_set.update({1234,"qwerty"})
my_set.discard(1)
print(my_set)