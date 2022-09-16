##COSC 499 Github introduction
##Ryder Van Oerle 10817427

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

def desc(list):
   descOrder = []
   temp = list.copy()
   while temp:
      max = temp[0]
      for x in temp:
         if(x > max):
            max = x
      descOrder.append(max)
      temp.remove(max)
   print(descOrder)
   return descOrder

def ascTest(list):
   temp = 0
   for x in range(len(list)-1):
      if list[x] > list[x+1]:
         print("Test failed")
         return
   print("Test Passed")

def descTest(list):
   temp = 0
   for x in range(len(list)-1):
      if list[x] < list[x+1]:
         print("Test failed")
         return
   print("Test Passed")
      
      
feature = input("Enter '0' if you would like to sort the list in ascending order or '1' if you would like to sort in in descending.\n")
if(int(feature)==0):
   print("Pre sorting:")
   print(toSort)
   ascTest(toSort)
   print("\nPost sorting:")
   ascList = asc(toSort)
   ascTest(ascList)
else:
   print("Pre sorting:")
   print(toSort)
   descTest(toSort)
   print("\nPost sorting:")
   descList = desc(toSort)
   descTest(descList)





