class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        lr = ListNode(0)
        lrr = lr

        while l1 and l2:
            sum = l1.val + l2.val + lrr.val

            if sum >= 10:
                lrr.val = 0
                sum -= 10
                lrr.val += sum
                lrr.next = ListNode(1)
            else:
                lrr.val += sum
                if l1.next or l2.next:
                    lrr.next = ListNode(0)

            lrr = lrr.next
            l1 = l1.next
            l2 = l2.next


        if l1:
            while l1:
                sum = lrr.val + l1.val
                if sum >= 10:
                    sum -= 10
                    lrr.val = sum
                    lrr.next = ListNode(1)
                else:
                    lrr.val = sum
                    if l1.next:
                        lrr.next = ListNode(0)

                l1 = l1.next
                lrr = lrr.next


        else:
            while l2:
                sum = lrr.val + l2.val
                if sum >= 10:
                    sum -= 10
                    lrr.val = sum
                    lrr.next = ListNode(1)
                else:
                    lrr.val = sum
                    if l2.next:
                        lrr.next = ListNode(0)

                l2 = l2.next
                lrr = lrr.next


        return lr


if __name__ == "__main__":
    l1 = ListNode(3)
    l2 = ListNode(9)

    l1r = l1
    l1r.next = ListNode(7)
    # l1r = l1r.next
    # l1r.next = ListNode(1)
    # l1r = l1r.next
    # l1r.next = ListNode(9)
    # l1r = l1r.next
    # l1r.next = ListNode(9)
    # l1r = l1r.next
    # l1r.next = ListNode(9)
    # l1r = l1r.next
    # l1r.next = ListNode(9)

    l2r = l2
    l2r.next = ListNode(2)
    # l2r = l2r.next
    # l2r.next = ListNode(9)
    # l2r = l2r.next
    # l2r.next = ListNode(9)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    while result:
        print(result.val)
        result = result.next

