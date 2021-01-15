#!/usr/bin/env python
# coding=utf-8
'''
Date: 2021-01-13 17:18:49
Github: https://github.com/bellalee01
LastEditors: lixuefei
LastEditTime: 2021-01-13 21:03:53
FilePath: /leetcode/108.py
Description: 
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(start,end):
            if start<=end:
                mid = (start+end)//2
                root = TreeNode(nums[mid])
                root.left = dfs(start,mid-1)
                root.right = dfs(mid+1,end)
                return root
            else:
                return None
        return dfs(0,len(nums)-1)

