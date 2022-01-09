def set_list(list):
    list.append("A")
    list.append("B")
    list.append("C")
    return list
  
def add(list):
    list.append("D")
    return list
  
my_list = ["E"]
  
print(set_list(my_list))
  
print(add(my_list))

print(my_list)