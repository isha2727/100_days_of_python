# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def reversed_linked_list(head) :
#     prev,curr=None,head
#     while curr:
#         next_node=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next_node
#     return prev           


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("namaste"))  # True
print(is_palindrome("hello"))  # False


