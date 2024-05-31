import pickle
import os

def input_scores():
    s=[]
    i=1
    while True:
        n=int(input(f'#{i}? '))
        if n<0:
            break
        s.append(n)
        i+=1
    return s

def get_average(s):
    total=0
    for n in s:
        total+=n
    return total/len(s)

def show_scores(s):
    for n in s:
        print(n,end=' ')
    print()

def save(s,fn):
    with open(fn,'wb') as file:
        pickle.dump(s,file)

def load(fn):
    if os.path.exists(fn):
        with open(fn,'rb') as file:
            t=pickle.load(file)
        return t
    else:
        return None

filename ='score.bin'
loaded=load(filename)

if loaded:
    print('[파일읽기]')
    print('\n[점수 출력]\n개인점수:',end='')
    show_scores(loaded)
    aver=get_average(loaded)
    print(f'평균:{aver:.1f}')
else:
    print('[점수 입력]')
    scores=input_scores()
    print('\n[점수 출력]\n개인점수:',end='')
    show_scores(scores)
    aver=get_average(scores)
    print(f'평균:{aver:.1f}')
    save(scores,filename)
