def addBinary(a: str, b: str):
    carry = 0
    result = ''
    a = list(a)
    b = list(b)
    print('a=',a,'b=',b,'carry=',carry)
    while a or b or carry:
        print('a=',a,'b=',b,'carry=',carry)
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        result += str(carry %2)
        carry //= 2
    return result[::-1]
print(addBinary('1010','1011'))
#1010+1011=10101
