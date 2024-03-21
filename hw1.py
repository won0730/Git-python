#원의 반지름을 정수로 입력받아 그 원의 넓이를 구하는 프로그램

#사용자 정의 함수부
def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(r):
    r=int(r)
    return 3.14*r*r

#주 프로그램부
input_prompt=input('넓이를 구하고자 하는 원의 반지름은? ')
r=input_prompt
area= get_circle_area(r)

print('반지름',r,'인 원의 넓이= 3.14 x',r,'x',r,'=',area)
