#!/usr/bin/env python
# coding=utf-8
'''
Date: 2021-01-15 14:27:44
Github: https://github.com/bellalee01
LastEditors: lixuefei
LastEditTime: 2021-01-15 15:04:55
FilePath: /leetcode/947.py
Description: 移除最多的同行或同列石头
思路：将点转化成图，进行dfs，查找联通分量的数目就是最终解
'''
import collections
from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if x1==x2 or y1==y2:
                    edge[i].append(j)

        vis = set()
        num = 0
        def dfs(x:int):
            vis.add(x)
            for s in edge[x]:
                if s not in vis:
                    dfs(s)

        for i in range(n):
            if i not in vis:
                num+=1
                dfs(i)
        
        return n-num

if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    so = Solution()
    print(so.removeStones(stones))
    
