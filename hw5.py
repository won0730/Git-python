def read_single_digit(digit):
    if digit==0:
        return '영'
    elif digit==1:
        return '일'
    elif digit==2:
        return '이'
    elif digit==3:
        return '삼'
    elif digit==4:
        return '사'
    elif digit==5:
        return '오'
    elif digit==6:
        return '육'
    elif digit==7:
        return '칠'
    elif digit==8:
        return '팔'
    elif digit==9:
        return '구'

def read_number(number):
    result=""
    if number>=100:
        result+=read_single_digit(number//100)
        number%=100
    if number>=10:
        result+=read_single_digit(number//10)
        number%=10
    if number>=0:
        result+=read_single_digit(number)
    return result

number=int(input('세 자리수 이하 정수 입력: '))
if 0<=number<=999:
    print(read_number(number))
else:
    print('세 자리수 이하의 정수를 입력해주세요.')
