#!/usr/bin/env python
# coding=utf-8
'''
Date: 2021-01-12 10:01:31
Github: https://github.com/bellalee01
LastEditors: lixuefei
LastEditTime: 2021-01-12 10:16:33
FilePath: /leetcode/1202DisjointSetUnion.py
Description: 
'''
import sys
from typing import List
import collections
class DisjoinSetUnion:
    def __init__(self,n:int):
        self.n = n
        self.rank = [1]*n
        self.f = list(range(n))
    def find(self,x:int):
        if self.f[x]==x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    def union(self,x:int,y:int):
        fx,fy=self.find(x),self.find(y)
        if fx==fy:
            return 
        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx
        self.rank[fx]+=self.rank[fy]
        self.f[fy] = fx

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DisjoinSetUnion(len(s))
        for x,y in pairs:
            dsu.union(x,y)
        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[dsu.find(i)].append(ch)

        for vec in mp.values():
            vec.sort(reverse=True)

        ans = list()
        for i in range(len(s)):
            x = dsu.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()
        
        return "".join(ans)

if __name__ == "__main__":
    s = "dcab"
    pair = collections.defaultdict(list)
    pair = [[0,3],[1,2],[0,2]]
    print(s)
    solution = Solution()
    print(solution.smallestStringWithSwaps(s,pair))

