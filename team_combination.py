#coding=utf-8
#중복 전공 조짜기 프로그램
'''
간단 알고리즘 설계
1. 이름 입력 및 친구의 전공 이름 모두 기입
2. 값 받는대로 동일전공끼리 유니온 형성
3. 전공 입력후 원하는 조 인원 숫자 입력
4. 조 인원의 수가 동일전공 최대 인원수보다 적거나 같을시 combination 써서 조 전체 출력
'''
import sys,itertools
input=sys.stdin.readline
db={}
while True:
    a,b=map(str,input().split())
    l=list(db.keys())
    if a=="0":break
    if b not in l: db[b]=[a]
    else: db[b].append(a)
print(db)
k=input().strip("\n")
print(db[k])
while True:
    n=int(input())
    if n<=len(db[k]):break
asd=list(itertools.combinations(db[k],n))
for i in asd:
    print(i)
