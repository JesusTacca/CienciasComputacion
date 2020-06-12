def binP(num):
    num = int(num)
    b_num = bin(num)
    b_num2 = b_num[slice(2,len(b_num),1)]
    return b_num2
def deci(num):
    rango = len(num)
    value = 0
    for i in range(rango):
            digit = num[rango-i-1]
            if digit == '1':
                    value = value + pow(2, i)
    return value

def andB(num1,num2):
    len1=len(num1)
    len2=len(num2)
    print("estos son los num")
    print(num1)
    print(num2)
    print("termina num")
    if len1 < len2:
        rest = len2-len1
        for i in range (rest):
            num1 = '0' + num1 
    else:
        rest = len1-len2
        for i in range (rest):
            num2 = '0' + num2
    print("estos son los num con ceros")
    print(num1)
    print(num2)
    print("termina num")  
    rango = len(num1)

    value = ''
    
    for i in range (0,rango):
        if(num1[rango-1-i] == '1' and num2[rango-1-i] == '1' ):
            value = '1' + value
        else:
            value = '0' + value
    print(value,"values")
    return value



while True :
    x = input()
    y = input()
    print()
    print( deci ( andB(binP(x),binP(y) ) ) )
    print("-----------")
