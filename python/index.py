#slice : extract python.
s='Pythonprograming'
print(s[:6:1])

#slice : extract programing.
print(s[6::1])

#slice : extract first 6 characters of s.
print(s[:6:1])

#slice : extract first 5 characters of s.
print(s[11::1])

#slice : extract characters from index 3 to 9
print(s[3:9+1:1])

#slice : reverse the string 
print(s[::-1])

#slice : extract every second character from s
print(s[::2])

#slice : extract every third character from s
print(s[::3])

#slice : extract the string in reverse order,skipping one character each time 
print(s[::-2])

#from s = 'Datascience'.extract science  using negative indexing 
s ='Datscience'
print(s[-7:])

#extract first 4 elements 
nums = [10,20,30,40,50,60,70,80]
print(nums[:4:1])

#extract last 3 elements 
nums = [10,20,30,40,50,60,70,80]
print(nums[5::1])

#extract elements from index 2 to 5 
nums = [10,20,30,40,50,60,70,80]
print(nums[2:5+1:1])

#extract all elements except the first and last
nums = [10,20,30,40,50,60,70,80]
print(nums[1:7:1])

#extract reverse the list using slice
nums = [10,20,30,40,50,60,70,80]
print(nums[::-1])

#extract every alternate element
nums = [10,20,30,40,50,60,70,80]
print(nums[::2])

#extract element at odd indices only  
nums = [10,20,30,40,50,60,70,80]
print(nums[::2])

#extract element at even indices only  
nums = [10,20,30,40,50,60,70,80]
print(nums[1::2])

#extract element at odd indices only  
nums = [10,20,30,40,50,60,70,80]
print(nums[::2])


#extract from nums,create a new list containing elements in reverse order , skipping second element 
nums = [10,20,30,40,50,60,70,80]
new_list=nums[::-2]
print(new_list)

#given t = ('apple','banana','cherry','data','fig','grape') extract the first 3 items
t = ('apple','banana','cherry','data','fig','grape')
print(t[:3])

#given t = ('apple','banana','cherry','data','fig','grape') extract the last 2 items
t = ('apple','banana','cherry','data','fig','grape')
print(t[4:])

#extract t = ('cherry','data','fig')
t = ('apple','banana','cherry','data','fig','grape')
print(t[2:5:1])

#reverse tuple using slicing
t = ('apple','banana','cherry','data','fig','grape')
print(t[::-1])

#extract every second item
t = ('apple','banana','cherry','data','fig','grape')
print(t[1::2])

#extract every third item starting from index 1
t = ('apple','banana','cherry','data','fig','grape')
print(t[1::3])

#extract the tuple in reverse order, skipping one item each time 
t = ('apple','banana','cherry','data','fig','grape')
print(t[::-2])

#extract 1st four items in reverse
t = ('apple','banana','cherry','data','fig','grape')
print(t[:-5:-1])

# given s ='MechineLearning' extract learning and reverse it
s ='MechineLearning'
print(s[:-9:-1])

#given list = [1,2,3,4,5,6,7,8,9,10] extract all odd numbers using slicing
list = [1,2,3,4,5,6,7,8,9,10] 
print(list[::2])

# given t =(10,20,30,40,50,60,70,80) extract 80,60,40,20 using slicing
t =(10,20,30,40,50,60,70,80)
print(t[::-2])

# given s= 'Artificialintelligence' extract every second character in reverse order
s= 'Artificialintelligence'
print(s[1::2])

