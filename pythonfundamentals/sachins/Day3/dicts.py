my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict['points']['points2'][1]) #Use dictionary indices to extract the second item of points2

my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict["age"] = 36
my_dict["occupation"] = "Editor"
my_dict["country"] = "Colombia" #change/add attributes to dict