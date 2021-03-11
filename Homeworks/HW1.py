#Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
#Merge two lists. Multiply all values in the newlist by 2.
#Use the loop to print the data type of the all values in the new list.

#Question 1
list1=[5,9,11,25,33]
list2=[6,8,10,22,34]

list1.extend(list2)
print(list1)

list3=[x*2 for x in list1]
print(list3)

for i in list3:
    print(i,end=" ")

print("\n")
    
for i in list3: 
    print(type(i),end=" ")
