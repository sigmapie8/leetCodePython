class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for index, num in enumerate(numbers):
            try:
                if(visited[target-num] is not None):
                    return [visited[target-num]+1, index+1]
            except:
                visited[num] = index
