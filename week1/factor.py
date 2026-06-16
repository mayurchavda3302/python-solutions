
# WAP to find a Factor of a given number (iterative and recursive) 


def factorial(num)->int:
    #   0 * n alwas 0
    result=1
    for i in range(1,num+1):
        # print("i",i)
        result *=i
    return result


num=12



def fact_recusion(n)->int:
    # print("n  is ", n)
    if n== 0 or n ==1 :
        return 1

    return  n* fact_recusion(n-1)
 
print(factorial(num))
print(fact_recusion(num))