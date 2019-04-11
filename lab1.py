
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
      new_list = []
   if index < 0:
      return new_list
   new_list.append(int_list[index])
   return reverse_rec(int_list,new_list, counter, index - counter)


def bin_search(target, low, high, int_list, median = 0, counter = 0, status = 0):  # must use recursion
   if int_list == None:
      raise ValueError
   if status == 0:
      median = (high + low)/2
      if median.is_integer() == False:
         if abs(int_list[int(median) + 1] - target) < abs(int_list[int(median)] - target):
            median = int(median) + 1
            counter = True
         else:
            median = int(median)
            counter = False
      else:
         median = int(median)
         if abs(int_list[median + 1] - target) < abs(int_list[median-1] - target):
            counter = True
         else:
            counter = False
      status = 1
   if int_list[median] == target:
      return median
   if median == low or median == high:
      return None
   if counter == True:
      return bin_search(target, low, high, int_list, median + 1, counter, status)
   if counter == False:
      return bin_search(target, low, high, int_list, median - 1, counter, status)