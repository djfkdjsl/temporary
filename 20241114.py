# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:04:31 2024

@author: user
"""

# 902~909단
for n in range(902,910):
    print("\n << %d단 >>" % n)
    for m in range(1,10):
        print("{0} x {1} = {2:5,}".format(n,m,n*m)) # {2:5} 처럼 하나라도 인덱스를 주면, 나머지도 인덱스 줘야 됨. { n : m, }-> n-1번째 format요소를 m자리까지, 3자리마다 , 붙여줌
        print(f"{n} x {m} = {n*m:5,}")
#%%
# 2진법
for i in range(0,10,1):
    print(i,"->",bin(i))
    
#%%
# int, bin, oct, hex 등등
print("int : {0:d}".format(77))
print("bin : {0:b}".format(77))
print("oct : {0:o}".format(77))
print("hex : {0:x}".format(77))

#%%

print("{},{},{},{}".format(int(77),bin(77),oct(77),hex(77)))

#%%
# 한 줄로 처리하는 방법
print("int {0:d}, bin {0:b}, oct {0:o}, hex {0:x}".format(42))

#%%

#format 함수의 결과는? (8bit 표시)

for i in range(0,10,1):
    print("{0:d} -> {0:08b}".format(i)) #16비트는 016
    
#%%
# zfill
a="123"
print(a.zfill(8)) # a 문자열을 8자리로 채워라. 나머지는 0으로 채워라
#%%

for i in range(0,10,1):
    print(f"{i} -> {bin(i)[2:].zfill(4)}") #16비트는 016

#%%
a=50
for i in range(0,51,5):
    print(a+i)
#%%
for i in range(50,101,5):
    print(i)
#%%
sum=0
for i in range(10,100,1):
    if i%7==0:
        sum+=i
        print(i)
print("결과 :",sum)

#%%

# 변수와 리스트(=array)
# list -> [], 변경 삭제 가능
# tuple -> () , 변경 삭제 불가
# dictionary -> {}, key가 있고 값이 있어야 함. { a : 3 } 등등. dictionary 역할을 함
# 시험 -> 다음 중 연결이 맞게 된 것은? 특징 ㅇㅇ


score = [95, 90, 80, 85, 93]

num = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(num[1][0]) # 2행 1열

#%%
# append 는 순차적으로 뒤로 더해줌
num = []
num.append(7)
num.append(11)
num.append("Korea")
num.append([1,2,3])
print(num) 

#%%
# [:] = [~] 느낌. 범주를 ㅋㅋ 다만 뒤에거는 for문 range처럼 미만.
# slice 임
n1 = [1,3,5,7]
print(n1[0:3])
print(n1[:3])
print(n1[3:])
print(n1[:])

#%%
n1 = [1,3,5,7]
n1[1]=2
print(n1)
n1.append(9)
n1.insert(2,3) #insert(a,b) -> a를 b-1번째 index에 넣어준다
print(n1)

#%%
# remove
n1 = [1,3,5,7]
c1 = n1
c2 = n1[1:3]
n1 = [1,2,3,5,7]
n1.remove(5) #정확한 요소를 딱 집어서 remove
print(n1) # 다만 remove(a)에서 a가 리스트에 없으면 정지가 됨. 어떻게 스무스하게 넘어가게 할까?
#%%
n1 = [1,2,3,5,7]
for i in range(0,4):
    if n1[i]==2:
        n1.remove(2)
print(n1)
#%%
n1 = [1,2,3,5,7]
if 2 in n1:
    n1.remove(2)
    print(n1)
    
#%%
n1
del n1[2]
n1
#%%
#Last in first out LIFO

n1.pop() #맨 뒤에 있는 놈 아웃임.
n1 
#%%
n1 = [1,3,5,7]
if 5 in n1:
    print(n1.index(5)) # index 5가 어디있는가?
    
#%%
slist = ["서울","대학교","고려","캠퍼스"]
print(slist)

slist.sort(reverse=False) # ㄱㄴㄷㄹ순으로 고쳐줌 , reverse = True를 하면 역순
print(slist)

#파이썬에서는 sort를 하나 더 만들고 싶다.
#%%
slist = ["서울","대학교","고려","캠퍼스"]

new_slist = sorted(slist)
print(new_slist)

#%%
a = list(range(1,11))
b = list(range(5,51,5))
c = list(range(20,0,-3))
print(len(a),len(b),len(c))

#%%
a = [1,3,5]
b = [2,4,6]
a.extend(b)
print(a)

a = [1,3,5]
b = [2,4,6]
c=a+b
print(c)
#%%

scores = []
for i in range(0,5):
    jumsu = int(input("성적 : "))
    scores.append(jumsu)
print(scores)
sum=0
for i in range(0,5):
    sum += scores[i]
print("합계 : ",sum)
print("평균 : ",sum/5)

#%%
#count 함수

a = [7,4,5,7,5,7,9]
print(a.count(5))
print(a.count(7))
print(a.count(9))

#%%

#학생 성적을 입력받고 0 미만인 학생은 제외하고 합계와 평균 구하기

scores = []
for i in range(0,5):
    jumsu = int(input("성적 : "))
    scores.append(jumsu)
print(scores)
sum=0
count=0
for i in range(0,5):
    if scores[i] != 0:
        sum += scores[i]
        count += 1
print("합계 : ",sum)
print("평균 : ",sum/count)

#%%

a = (1,2,3)
b = 1,2,3

print(a,b)

(a,b) = (1,2)
print(a,b)

a,b= (1,2)
print(a,b)

(a,b) = 1,2
print(a,b)

a,b = 1,2
print(a,b)

#%%

# 리스트와 튜플의 차이
# 튜플은 리스트보다 빠른 사용 속도 지원
# 튜플 변경은 리스트로 변환 후 새로운 튜플로 생성

#%%
# 30 부터 7씩 증가하는 list

list1 = []
m=0
for i in range(30,61,7):
    list1.append(i)
    m+=1
print(list1)

#%%

#for문 없이

a = list(range(30,61,7))
print(a)

#%%

a = tuple(range(10,101,10))
mlist = list(a)
mlist[0]=11
mlist.append(200)
new_a = tuple(mlist)
new_a

