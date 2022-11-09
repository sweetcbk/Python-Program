
capitals = {}
temp_list = []
received_str = str(input("Enter the Country and it's capital"))

for dict_elem in received_str.split(","):

    temp_list = list(dict_elem.split(":"))
    capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()

print(capitals)