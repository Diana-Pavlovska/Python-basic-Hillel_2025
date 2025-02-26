def last(my_list):
    if len(my_list)>1:
        return [my_list[-1]] + my_list[:-1]
    return my_list
exmpl_1 = [12,3,4,10]
exmpl_2 = [1]
exmpl_3 = []
exmpl_4 = [12,3,4,10,8]
print(f"{exmpl_1} => {last(exmpl_1)}")
print(f"{exmpl_2} => {last(exmpl_2)}")
print(f"{exmpl_3} => {last(exmpl_3)}")
print(f"{exmpl_4} => {last(exmpl_4)}")