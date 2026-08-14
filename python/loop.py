# string = "selva@123"
# i=0
# count =0
# while i <=len(string)-1:
#     if string[i].islower():
#      count = count+1
#      print(string[i])
    
#     i+=1

# print(count)

# text =12334
# i=int(len(text))-1
# while i >=0:
#     print(text[i],end="")
#     i=i-1


# number=str(input("enter the value: "))
# i = 0
# count=0
# while i <=len(number)-1:
#     count =count+1
#     print(number[i])
#     i=i+2

# print("total: ",count)


# tuple_collection=(10,11.11,20,33.22,51,60.89,56)
# i =0
# total =0 
# while i <=len(tuple_collection)-1:
#   if type(tuple_collection[i]) == float:
#     total = total+tuple_collection[i]
#     print(tuple_collection[i])
#   i=i+1

# print("product: ",total)


# x=['pro1.html','file.txt','google.com','yahoo.in']
# out={}
# for i in x:
#   r = i.split('.')
#   out[r[1]]=r[0]
# print(out)


# p = 'emaple on for loop'
# list=p.split()
# print(list)
# output=""
# items=[]
# for i in list:
#      items.append(i[::-1])
# print(items)
# print(" ".join(items)) 
n=5
# for i in range(1,n+1):
#    for j in range(1,n+1):
#       if i==j or i+j==n+1:
#          print("*",end=" ")
#       else:
#          print(" ", end=" ")
#    print()
# list = ["white","black","aoa"]
# last=list[-1]
# return_value=""

# if last[0] in "aeiou" and last==last[::-1]:
#    print(last,"is vowels")
# else:
#    print(last,"first character is not vowels")


# items=["google.com","yoaho.in","facebook.org"]
# out =[]
# join=".".join(items)
# print(join)
# x=join.split(".")
# print(x)
# for i in range(1,len(x),2):
#     out.append(x[i])
# print(out)

# character="abcab"
# out={}
# for i in character:
#   if i == " ":
#     continue
#   if i in out:
#     out[i]=out[i]+1
#   else:
#     out[i]=1
# print(out)
    


# list_items=[1,2,0,3,0,4,0,5,6]
# setitem=[]
# for i in list_items:
#     if i not in setitem:
#         setitem.append(i)
#         print(i)

# list_items=[1,2,0,3,0,4,0,5,6]
# out={}
# for i in list_items:
#    total=list_items.count(i)
#    out[i]=total
# print(out)

#without count
def n_without_count(list_items):
 output={}
 for i in list_items:
    if i in output:
        output[i]=output[i]+1
    else:
        output[i]=1
 return output
list_items=[1,2,0,3,0,4,0,5,6]
print(list_items)

#second max num
def second_max(listnumber):
 max_second_num=[]
 max_num=max(listnumber)
 for i in listnumber:
    if i<max_num:
        max_second_num.append(i)
    else:
        print(f"first max number: {i}")
 print(f"second max number: {max(max_second_num)}")

listnumber=[1,23,4,5,6,9,67]
second_max(listnumber)



# once in word
def n_remove_multi_words(input_items):
 item=input_items.split()
 out=[]
 out2=[]
 print(item)
 for i in item:
     if i not in out:
         out.append(i)
     else:
         out2.append(i)
 for j in out:
    if j not in out2:
        print(j)
input_items="apple mango apple orange mango"
n_remove_multi_words(input_items)

#even or odd
def n_even_odd(input_item):
 even=[]
 odd=[]
 for i in input_item:
  if i%2==0:
    even.append(i)
  else:
   odd.append(i)
 return f"even:{even},odd:{odd}"
input_item=[1,4,7,8,10,13]    
print(n_even_odd(input_item))

#repeated words
def n_repeated(words):
 out=""
 for i in words:
  if i not in out:
    out=out+i
 return out
print(n_repeated("programming"))    

 
 