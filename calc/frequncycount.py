def CountFrequency(my_list): 
   count = {}
   for i in my_list:
    count[i] = count.get(i, 0) + 1
   return count
