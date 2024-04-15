# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.ref = None
# #
# #
# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
# #
# #     def print(self):
# #         if self.head is None:
# #             print('LL is Empty')
# #             return
# #         n = self.head
# #         while n is not None:
# #             print(n.data,'-->', end=" ")
# #             n = n.ref
# #
# #     def add_empty(self, data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #         else:
# #             print('LL is Not empty')
# #
# #     def add_begin(self,data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #         else:
# #             new_node.ref = self.head
# #             self.head = new_node
# #
# #     def add_end(self,data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #         else:
# #             n = self.head
# #             while n.ref is not None:
# #                 n = n.ref
# #             n.ref = new_node
# #
# #     def add_after(self,data, pos):
# #         if self.head is None:
# #             print('LL is Empty')
# #             return
# #         if pos == self.head.data:
# #             new_node = Node(data)
# #             new_node.ref = self.head.ref
# #             self.head.ref = new_node
# #             return
# #         n = self.head
# #         while n is not None:
# #             if pos == n.data:
# #                 break
# #             n = n.ref
# #
# #         if n is None:
# #             print('Not Found')
# #         else:
# #             new_node = Node(data)
# #             new_node.ref = n.ref
# #             n.ref = new_node
# #
# #     def add_before(self, data, pos):
# #         if self.head is None:
# #             print('LL is empty')
# #             return
# #         if pos == self.head.data:
# #             new_node = Node(data)
# #             new_node.ref = self.head
# #             self.head = new_node
# #             return
# #
# #         n = self.head
# #         while n.ref is not None:
# #             if pos == n.ref.data:
# #                 break
# #             n = n.ref
# #
# #         if n is None:
# #             print('Not Found')
# #         else:
# #             new_node = Node(data)
# #             new_node.ref = n.ref
# #             n.ref = new_node
# #
# #     def remove_begin(self):
# #         if self.head is None:
# #             print("LL is Epmty")
# #             return
# #         self.head = self.head.ref
# #
# #     def remove_end(self):
# #         if self.head is None:
# #             print('LL is Empty')
# #             return
# #         if self.head.ref is None:
# #             self.head = None
# #             return
# #
# #         n = self.head
# #         while n.ref.ref is not None:
# #             n = n.ref
# #         n.ref = None
# #
# #     def array_to_ll(self,arr):
# #         if not arr:
# #             return None
# #
# #         self.head = Node(arr[0])
# #         n = self.head
# #         for i in arr[1:]:
# #             n.ref = Node(i)
# #             n = n.ref
# #
# #
# # arr = [12, 23, 34, 45, 45]
# # LL = LinkedList()
# # # LL.add_empty(20)
# # # LL.add_begin(10)
# # # LL.add_end(30)
# # # LL.add_after(100, 10)
# # # LL.add_before(1, 30)
# # # LL.remove_begin()
# # # LL.remove_end()
# # LL.array_to_ll(arr)
# # LL.print()
# #
#
#
#
# class Node:
#     def __init__(self,data):
#         self.prev = None
#         self.data = data
#         self.nref = None
#
#
# class Doubly_LL:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         n = self.head
#         while n is not None:
#             print(n.data, '-->', end=" ")
#             n = n.nref
#
#     def print_rev(self):
#         print()
#         n = self.head
#         while n.nref is not None:
#             n = n.nref
#         while n is not None:
#             print(n.data, '-->', end=" ")
#             n = n.prev
#
#
#     def add_empty(self,data):
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#         else:
#             print("LL is not empty")
#
#     def add_begin(self,data):
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#             return
#
#         new_node = Node(data)
#         new_node.nref = self.head
#         self.head.prev = new_node
#         self.head = new_node
#
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         if self.head.nref is None:
#             new_node.prev = self.head
#             self.head.nref = new_node
#         else:
#             n = self.head
#             while n.nref is not None:
#                 n = n.nref
#             n.nref = new_node
#             new_node.prev = n
#
#     def add_after(self,data,pos):
#         if self.head is None:
#             print('LL is empty')
#             return
#         if pos == self.head.data:
#             new_node = Node(data)
#             new_node.nref = self.head.nref
#             new_node.prev = self.head
#             self.head.nref.prev = new_node
#             self.head.nref = new_node
#
#         else:
#             n = self.head
#             while n is not None:
#                 if pos == n.data:
#                     break
#                 n = n.nref
#
#             if n is None:
#                 print("not found")
#             else:
#                 new_node = Node(data)
#                 new_node.nref = n.nref
#                 new_node.prev = n
#                 if n.nref:
#                     n.nref.prev = new_node
#                 n.nref = new_node
#
#
#
#
#
#
# DLL = Doubly_LL()
# DLL.add_empty(10)
# DLL.add_begin(100)
# DLL.add_end(1000)
# DLL.add_after(20,1000)
# DLL.print()
# DLL.print_rev()


arr = [10, 20, 30, 40, 50]


#
# def binarysearch(key):
#     l = 0
#     r = len(arr) - 1
#
#     while l <= r:
#         m = (l+r) // 2
#
#         if arr[m] == key:
#             return m
#         elif key < arr[m]:
#             r = m - 1
#         else:
#             l = m + 1
#     return -1
#
# print(binarysearch(60))


# def rbinary(l, r, key):
#     if l <= r:
#         m = (l + r) // 2
#
#         if arr[m] == key:
#             return m
#         elif key < arr[m]:
#             return rbinary(l, m-1, key)
#         else:
#             return rbinary(m+1, r, key)
#     return -1
#
# print(rbinary(0, len(arr), 60))


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        n = self.head
        while n is not None:
            print(n.data, '-->', end=" ")
            n = n.ref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Its Not Empty')

    def add_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            print('LL is Empty ')
            return

        n = self.head
        while n is not None:
            if pos == n.data:
                break
            n = n.ref

        if n is None:
            print('Element Not Found')
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            print('its empty')
            return
        if pos == self.head.data:
            new_node.ref = self.head
            self.head = new_node
            return

        n = self.head
        while n.ref is not None:
            if pos == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print(f'Not {pos}found')
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is not None:
            if self.head.ref is not None:
                self.head = self.head.ref
            else:
                self.head = None
        else:
            print('LL is Empty')

    def delete_end(self):
        if self.head is None:
            print('Its empty bro')
            return
        if self.head.ref is not None:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
        else:
            self.head = None

    def delete_by_value(self, pos):
        if self.head is None:
            print('ITs empty')
            return
        if pos == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n is not None:
            if pos == n.ref.data:
                break
            n = n.ref
        if n is None:
            print('not found')
        else:
            n.ref = n.ref.ref

    def get_index(self, pos):
        c = -1
        if self.head is None:
            print('its empty')
            return
        n = self.head
        while n is not None:
            c += 1
            if pos == n.data:
                return c
            n = n.ref
        return -1

    def array_linkedlist(self, arr):
        n = self.head
        while n.ref is not None:
            n = n.ref

        for i in arr:
            n.ref = Node(arr[i])
            n = n.ref

    def ll_to_array(self):
        n = self.head
        l = []
        while n is not None:
            l.append(n.data)
            n = n.ref
        print(l)

    def insert_at_index(self, data, pos):
        if self.head is None:
            print('its empty')
            return
        if pos == 0:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            c = 0
            while n is not None:
                c += 1
                if c == pos:
                    break
                n = n.ref

            if n is None:
                print('Position out of range')
                return

            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def middle_node(self):
        slow = fast = self.head
        while fast and fast.ref:
            slow = slow.ref
            fast = fast.ref.ref
        print(slow.data)

    # def rev_linked(self):


LL = LinkedList()
LL.insert_empty(30)
LL.add_end(20)
# LL.add_after(15, 10)
LL.add_before(50, 20)
# LL.delete_end()
# LL.delete_begin()
# LL.delete_by_value(10)
# p = LL.get_index(100)
LL.add_begin(10)
# LL.ll_to_array()
LL.insert_at_index(100, 1)


# LL.array_linkedlist([1, 1, 1, 1, 1])
# LL.middle_node()
# LL.print()


def binary(arr, find, l, r):
    # l = 0
    # r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2

        if arr[m] == find:
            return m
        elif find < arr[m]:
            return binary(arr, find, l, m - 1)
        else:
            return binary(arr, find, m + 1, r)
    return -1


arr = [10, 20, 30, 40, 50]
l = 0
r = len(arr)
# print(binary(arr,20,l,r))


s = 'my name is muhammed danish'
p = ' '
for i in s:
    p = i + p


# print(p)


def sum_arraY(arr, n):
    if n == 1:
        return 1
    else:
        return n + sum_arraY(arr, n - 1)


arr = [1, 2, 3, 4, 5]
print(sum_arraY(arr, len(arr)))


def rev_sting(str):
    if len(str) <= 1:
        return str
    else:
        return rev_sting(str[1:]) + str[0]


s = 'i am muhammed danish'
print(rev_sting(s))


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))


def fibinacci(n):
    if n < 2:
        return n
    else:
        return fibinacci(n - 1) + fibinacci(n - 2)


print(fibinacci(10))


def binary(arr, find):
    l = 0
    r = len(arr)
    while l <= r:
        m = (l + r) // 2
        if find == arr[m]:
            return m
        elif find < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


print(binary([1, 2, 3, 4, 5], 3))


class Node1:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList1:
    def __init__(self):
        self.head = None

    def print(self):
        n = self.head
        while n is not None:
            print(n.data, '-->', end=" ")
            n = n.ref

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def array_to_ll(self, arr):
        n = self.head
        while n.ref is not None:
            n = n.ref

        for data in arr:
            n.ref = Node1(data)
            n = n.ref


LL1 = LinkedList1()
LL1.add_end(10)
LL1.array_to_ll([1, 2, 3, 4])
LL1.print()
