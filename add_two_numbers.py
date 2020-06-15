# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode):
    ans = ListNode()
    current = ans
    carry = 0

    # **** Two List Moving
    while(l1 != None and l2 != None):
        sum = l1.val + l2.val
        if sum + carry > 9:
            current.val = sum + carry - 10
            carry = 1
            current.next = ListNode()
            current = current.next
            l1 = l1.next
            l2 = l2.next
        else:
            current.val = sum + carry
            carry = 0
            if (l1.next != None or l2.next != None):
                current.next = ListNode()
                current = current.next
            l1 = l1.next
            l2 = l2.next

    # **** l1 moving
    while(l1 != None):
        if l1.val + carry > 9:
            current.val = l1.val + carry - 10
            current.next = ListNode()
            current = current.next
            carry = 1
            l1 = l1.next
        else:
            current.val = l1.val + carry
            carry = 0
            if l1.next != None:
                current.next = ListNode()
                current = current.next
            l1 = l1.next

    while(l2 != None):
        if l2.val + carry > 9:
            current.val = l2.val + carry - 10
            carry = 1
            current.next = ListNode()
            current = current.next
            l2 = l2.next
        else:
            current.val = l2.val + carry
            carry = 0
            if l2.next != None:
                current.next = ListNode()
                current = current.next
            l2 = l2.next

    if carry == 1:
        current.val = 1

    return ans


def printList(l: ListNode):
    while(l != None):
        print(str(l.val) + ' -> ', end='')
        l = l.next

    print()


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

printList(l1)
printList(l2)
printList(add_two_numbers(l1, l2))

