tuple_ = 1, 2, 'z', 'auris'
immutable_var = tuple_
 # tuple_ [2] = 100    #Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежa.
print("immutable_var:", immutable_var)

tuple_ = ([1, 2], 'z', 'auris')
tuple_[0][1] = "zero"
mutable_list = tuple_
print("mutable_list:", mutable_list )
