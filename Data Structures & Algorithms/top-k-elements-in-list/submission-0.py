class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        num_list = [[] for i in range(len(nums)+1)]

        for num, freq in count.items():
            num_list[freq].append(num)
        
        result = []
        for i in range(len(num_list) -1, 0, -1):
            for n in num_list[i]:
                result.append(n)
                if len(result) == k:
                    return result
                
            
        

        