# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:56:04 2024

@author: user
"""

#%%


mydict={"lee" : "객체지향프로그래밍","kim" : "프로그래밍", "han" : "컴퓨팅사고"}


for i,j in mydict.items(): # mydict.items() 함수 쓰면 key value 동시에 끌고 옴
    print(f"key : {i}, values : {j}")


#%%
'''
# 함수의 장점
1. 반복적인 코드
2. 소스코드 분석
3. 복잡한 문제 -> 작은 문제로 분해 해결
4. 재사용 가능
'''
#%%


9900 + 3630 + 16500 + 9900

#%%

def func(x):
    y=x**2 + 5*x + 3
    return y

func(2)

#%%

def sum(x1,x2):
    result = x1+x2
    return result
print(sum(1,2))
#%%
def func(n1,n2,n3):
    print(n1,n2,n3)
#func(20,7,100)
#func(n1=20,n2=7,n3=100)
func('n1'=='n1', 7, 100)
func(20,n2=7,n3=100)
#func(n1=20,7,100)

#keyword인수, 위치 인수
# 


#%%

def func(str,num):
   print(str,num)
func(str='안녕',num=77)

#%%

def agePrint(year):
    age=2024-year+1
    print("%d년생입니다. 올해 %d살입니다" % (year, age))

agePrint(1998)

#%%

def korea(name,n):
    for k in range(n):
        print("HELLO",name)
        
korea("대학교",2)
korea("캠퍼스",3) #캠퍼스 3번 출력

#%%
def func(x=0):
    y=7*x+10
    return y

print(func(1000)) #값이 변경됨
print(func())
#%%

import math

def sine(x):
    return float(math.sin(math.pi * (x/180)))

def cosine(x):
    return float(math.cos(math.pi*(x/180)))

def tan(x):
    return float(math.tan(math.pi*(x/180)))
x=0
print("각도    ","sin(x)","cos(x)","tan(x)")
print("-"*30)
print(f"{x}\t\t","%.2f",'\t',"%.2f",'\t',"%.2f",% (sine(x),cosine(x),tan(x)))
x=30
print(f"{x}\t\t",sine(x),'\t',cosine(x),'\t',tan(x))
x=45
print(f"{x}\t\t",sine(x),'\t',cosine(x),'\t',tan(x))
x=60
print(f"{x}\t\t",sine(x),'\t',cosine(x),'\t',tan(x))
x=90
print(f"{x}\t\t",sine(x),'\t',cosine(x),'\t',tan(x))
#%%

print("각도\t","sin(x)","cos(x)","tan(x)")
print("-"*30)

print()
print("-"*50)
deg = [0,30,46,60,90]

for k in df:
    a = math.sin(math.pi * (x/180))
    b = math.cos(math.pi*(x/180))
    c = math.tan(math.pi*(x/180))
    print(f"{k:2d}\t{a:.4f}\t{b:.4f}\t{c:,4f}")

#%%


def func(x):
    result = x*100/14
    return result


print(func(13))
print(func(12))
print(func(11))