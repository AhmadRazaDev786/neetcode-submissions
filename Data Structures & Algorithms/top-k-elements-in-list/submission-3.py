class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] +=1
            else:
                dic[nums[i]] = 1


        answer = []
        for number, count in dic.items():
            answer.append((count, number))
        answer = sorted(answer, reverse=True)

        result = []
        for key, value in answer[:k]:
            result.append(value)
            
        return result