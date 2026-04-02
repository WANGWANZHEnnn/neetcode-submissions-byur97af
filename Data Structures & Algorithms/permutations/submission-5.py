class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
    
        def backtrack(current, used):
            if len(current) == len(nums):  # 三个空格填满了
                result.append(current[:])  # 加入结果
                return
            
            for num in nums:
                if num in used:            # 用过了，跳过
                    continue
                
                used.add(num)              # 标记用过
                current.append(num)        # 填进空格
                backtrack(current, used)   # 继续填下一个空格
                current.pop()              # 撤销
                used.remove(num)           # 撤销标记
        
        backtrack([], set())
        return result

 



        