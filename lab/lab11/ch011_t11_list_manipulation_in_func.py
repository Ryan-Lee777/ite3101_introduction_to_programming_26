n = [3, 5, 7]
# Add your function here
def list_extender(lst:list)->list:
    lst.append(9)
    return lst

print(list_extender(n))
