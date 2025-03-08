class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        start,end,count = [],[],0
        
        for i in nums:
            if i < pivot:
                start.append(i)
            elif i == pivot:
                count +=1

            else:
                end.append(i)

        return start + [pivot] * count + end


        