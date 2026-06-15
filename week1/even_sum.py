# 1 WAP to find a sum of even number into 1D array.

def  even_sum(arr=[]): 
    result=0
    for i in arr:
       if  i % 2== 0:
            result += i
    
    return  result

my_array=[12,234,3423,32]

#  using list comprehensive

def using_list_copm(arr=[]):
    return sum([i for i in arr if i% 2 ==0])

print(even_sum(my_array))
print(using_list_copm(my_array))
