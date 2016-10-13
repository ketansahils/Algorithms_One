# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        sum = 0
        counter = 0
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            digit = sum%10
            carry = sum/10
            if counter == 0:
                l3 = ListNode(digit)
                k = l3
            else:
                k.next = ListNode(digit)
                k = k.next
            counter += 1
        return l3

if __name__ == '__main__':
    l1 = None
    for val in [3,8,1]:
        next = l1
        l1 = ListNode(val)
        l1.next = next

    l2 = None
    for val in [1,7]:
        next = l2
        l2 = ListNode(val)
        l2.next = next

    k = Solution()
    l = k.addTwoNumbers(l1,l2)
    m = l1
    # while m:
    #     print m.val
    #     m = m.next
    while l:
        print l.val,
        l = l.next

# 8 9 9
# 5

#   9 9 8
#   0 0 5
# 1 0 0 3

# 3 0 0 1


