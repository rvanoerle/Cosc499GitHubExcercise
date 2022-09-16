

toSort = [0,7,4,5,8,3,2,9,1,6]

def asc(list):
   ascOrder = []
   temp = list.copy()
   while temp:
      min = temp[0]
      for x in temp:
         if(x < min):
            min = x
      ascOrder.append(min)
      temp.remove(min)
        
   print(ascOrder)
   return ascOrder

def ascTest(list):
   temp = 0
   for x in range(len(list)-1):
      if list[x] > list[x+1]:
         print("Test failed")
         return
   print("Test Passed")

print(toSort)
ascTest(toSort)
ascList = asc(toSort)
ascTest(ascList)





