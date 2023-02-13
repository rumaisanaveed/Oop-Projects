###LINEAR SEARCH
###WITHOUT FUNCTION
lst = [2,9,0,1,45,99]
key = int(input("Enter the key which you want to search from the list:"))
if key not in lst:
   print("The",key,"not found in the list.")
else:
   for i in range(len(lst)):
       if lst[i] == key:
           print("The",key,"is found at",i)

#WITH FUNCTION
def linearSearch(lst,n):
   if key not in lst:
       print("Not found at any location.")
   else:
       for i in range(len(lst)):
           if key == lst[i]:
               print(f"{key} found at index {i}.")
           
   

list = [99,2,38,0,12,45,56,34,89,76,32,90,54,21]
key = int(input("Enter the key which you want to search:"))
linearSearch(list,key)
##----------------------------------------------------------------------------------------------------------------------------
#BINARY SEARCH
def binarySearch(lst,n):
   if key not in lst:
       print("Not found at any index.")
   else:
       l = 0
       u = len(lst) - 1
       while True:
           mid = (l + u) // 2
           if lst[mid] == key:
               print(f"{key} found at index {mid}.")
               break
           else:
               if lst[mid] > key:
                   u = mid - 1
               else:
                   l = mid + 1
                   
           
list = [23,45,67,89,90,91,999]
key = int(input("Enter the key which you want to search:"))
binarySearch(list,key)
##-----------------------------------------------------------------------------------------------------------------------------

#SELECTION SORT:

def selectionSort(lst):
    for i in range(len(lst) - 1):
        minValue = i
        for j in range(i,len(lst)):
            if lst[j] < lst[minValue] :
                minValue = j 
        lst[i] , lst[minValue] = lst[minValue] , lst[i]
    return lst
        
list = [34,2,56,90,9,32,21]
print(selectionSort(list))

#------------------------------------------------------------------------------------------------------------------------------
