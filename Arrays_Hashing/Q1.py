class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        chk=set()
        for n in nums:
            if n in chk:
                return True
            chk.add(n)
        return False

        
