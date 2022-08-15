def input_ith_number(ith_num):
    n1 = int(input("\nEnter number "+ str(ith_num) + " to be added: "))
    return n1

def addition(n1, n2):
    sum = n1+n2
    return sum
    
def output(n1, n2, sum):
    print(str(n1) +"+"+ str(n2) + "=" + str(sum))
    
num1 = input_ith_number(1)
num2 = input_ith_number(2)
sum = addition(num1, num2)
output(num1, num2, sum)
