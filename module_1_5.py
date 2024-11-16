immutable_var = 1,2,"str", [1,2,3,4]
print(immutable_var)
immutable_var[3][0]=5
print(immutable_var)
#immutable_var[2]=привет --str неизменяемый элемент в кортеже
#print(immutable_var)
#Только значения внутри списка внутри кортежа можно менять

mutable_list = [2,3,"string", [1,2,3]]
print(mutable_list)
mutable_list[0] = 56
print(mutable_list)
mutable_list[1] = str("line")
print(mutable_list)
mutable_list[-1] = int(80)
print(mutable_list)