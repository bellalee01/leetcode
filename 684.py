#!/usr/bin/env python
# coding=utf-8
'''
Date: 2021-01-13 09:53:08
Github: https://github.com/bellalee01
LastEditors: lixuefei
LastEditTime: 2021-01-13 10:21:03
FilePath: /leetcode/684.py
Description: 冗余连接 并查集
             求联通分量的这种题都可以用并查集
'''
from typing import List
class DisJoinSetUnion:
    def __init__(self,n:int):
        self.n = n
        self.f = list(range(n))
        self.rank = [1]*n
    def find(self,x:int):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    def union(self,x:int,y:int):
        fx,fy = self.find(x),self.find(y)
        if fx==fy:
            return
        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx
        self.rank[fx]+=self.rank[fy]
        self.f[fy]=fx

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        djsu = DisJoinSetUnion(len(edges))
        for x,y in edges:
            if djsu.find(x)==djsu.find(y):
                return [x,y]
            else:
                djsu.union(x,y)
            
        

