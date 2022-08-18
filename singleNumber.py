    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        "xor var where if a number is equal to another it will cancel out 1xor1 =0"
        xor = 0
        
        for i in nums:
            xor ^=i
        
        return xor
            
