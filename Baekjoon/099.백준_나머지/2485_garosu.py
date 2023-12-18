# 2485

import sys
input = sys.stdin.readline

import math

n = int(input()) # 전체 나무 개수
before = int(input()) # 앞에 있는 나무
first = 

dist = [] # 각 나무들의 거리를 저장할 배열

for i in range(n-1): 
    after = int(input()) # 뒤에 있는 나무
    dist.append(after-before) # 두 나무사이의 거리
    before = after

before_gcd = dist[0]
for i in dist[1:]:
    before_gcd = math.gcd(before_gcd, i)
    
final_gcd = before_gcd
    
total = 0
for each_dist in dist: 
    total += each_dist // final_gcd - 1 # 각 거리들을 최대공약수 거리만큼 나눠주면 해당 그루에 심는 나무의 개수가 됌
    
print(total)