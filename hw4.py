def rep_char(c,n):
    print(c*n)

def draw_line_string(msg1):
    msg2='Welcome to seoul'
    if len(msg1)>len(msg2):
        nstr=len(msg1)
    else:
        nstr=len(msg2)
    rep_char('-',nstr+2)                                                                     
    print(f'Hello {msg1}, \n{msg2}.')
    rep_char('-',nstr+2)

msg1=input('Input his/her name: ')
draw_line_string(msg1)
