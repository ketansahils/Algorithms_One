class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i]) is not None:
                if nums[i] * 2 == target:
                    return [dic[nums[i]],i]
            dic[nums[i]] = i
            
        for key in dic.keys():
            if dic.get(target-key) is not None:
                if dic[target-key] != dic[key]:
                    arr = [dic[target-key],dic[key]]
        
        if arr[0] > arr[1]:
            return [arr[1],arr[0]]
        return [arr[0],arr[1]]

if __name__ == '__main__':
    l = [217,231,523,52,547,243,648,509,415,149,689,710,265,187,370,56,977,182,400,329,471,805,955,989,255,766,38,566,79,843,295,229,988,108,781,619,704,542,335,307,359,907,727,959,161,699,123,650,147,459,657,188,304,268,405,685,620,721,351,570,899,60,388,771,24,659,425,440,508,373,32,645,409,272,356,175,533,740,370,152,34,510,745,251,227,494,258,527,817,773,178,194,860,387,627,851,449,736,15,212,529,950,316,28,65,484,968,63,4,643,795,669,203,677,139,636,289,555,430,849,150,49]
    #l =[-3,4,3,90]
    t = 718
    #print l[14]
    s = Solution()
    print s.twoSum(l,t)