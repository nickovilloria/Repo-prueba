import sys 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = []

flattened_list= [item for sublist in nested_list for item in sublist]   #List comprehension
print(flattened_list)

gen_flat_list=(item for sublist in nested_list for item in sublist)
print(gen_flat_list)  #Gives obscured object "<generator object <genexpr> at 0x00000283638513C0>" that can be seen with next or bucling over results
print(sys.getsizeof(next(gen_flat_list))) #first item  1
print(sys.getsizeof(next(gen_flat_list))) #second item  2
print(sys.getsizeof(flattened_list),flattened_list)    #184 bytes
total=([i for i in gen_flat_list]) #runs the rest of the sequence [3, 4, 5, 6, 7, 8, 9]
print(sys.getsizeof(total),total)  #120 bytes (less consumption)