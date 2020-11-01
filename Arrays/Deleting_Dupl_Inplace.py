def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while(i <= len(nums) - 1):
            if nums[i] == val:
                nums.pop(i)
                i = 0
                continue
            i += 1
        print(nums)
        return len(nums)
