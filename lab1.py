
def max_list_iter(int_list):  # must use iteration not recursion
   if int_list == None:
      raise ValueError
   elif len(int_list) == 0:
      return None
   elif len(int_list) > 0:
      max_num = int_list[0]
      if len(int_list) > 1:
         for num in int_list[1:]:
            if num > max_num:
               max_num = num
         return max_num
      else:
         return max_num

def reverse_rec(int_list,new_list = [],counter = 0,index = 0):   # must use recursion
   if int_list == None:
      raise ValueError
   if counter == 0:
      index = len(int_list) - 1
      counter = 1
   if index < 0:
      return new_list
   new_list.append(int_list[index])
   return reverse_rec(int_list,new_list, counter, index - counter)


def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None:
      raise ValueError
   if int_list[low] == target:
      return low
   if low == high:
      return None
   return bin_search(target, low + 1, high, int_list)
