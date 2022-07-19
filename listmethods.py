# n=[1,3,5,7,11,13,15]
# n.insert(0,'hello')     #['heelo',1,3,5,7,11,13,15]
# n.insert(1,'hello')  #[1,hello,3,5,7,11,13,15]
# n.insert(2,4)          # [1,3,4,5,7,11,13,15]
# n.insert(-1,8)         #[1,3,5,7,11,13,8,15]
# n.insert(-2,8)           #[1,3,5,7,11,8,13,15]
# print(n)
import numbers


n=[10,20,30,40]
# print(n.pop())    #40
# n.pop()
# print(n)             #[10,20,30]
# n.pop(0)
# print(n)           #[20,30,40]
# n.pop(1)
# print(n)      # [10,30,40]
# n.pop(3)
# print(n)    # [10,20,30]
# n.pop(4)
# print(n)n        #pop index out of range
# n=[10,20,'hello',30,40]
# n.remove('hello')
# print(n)        #[10,20,30,40]
# n.remove(hey)
# print(n)     #name 'hey' is not defined  valueerrror
# print(n.index('hello'))    #2
# print(n.index(30))
# print(n.index('hell'))      # valueerror hell is not in list
# print(n)
# n=[1,2,3,4,5]
# print(n[: : -1])     # [5,4,3,2,1]
# print(n[: :-2])      # [5,3,1]
# n.reverse()
# print(n)               #  [5,4,3,2,1]
# n=[1,5,4,3,2]
# print(*n)      # 1 5 4 3 2
# n.sort()
# print(n)                # [1,2,3,4,5]
# n.sort(reverse=False)       #[1,2,3,4,5]
# n.sort(reverse=True)         #[5,4,3,2,1]
# print(n)
# j=[2.8,3.5,6.8,1.4,2.6]
# j.sort()
# print(j)
# k=['HD','LK','SL','HH','HA','s','BA','PA','DA','WM','LH','PZ']
# k.sort()
# print(k)    #['BA','DA','HA','HD','HH,'LH','LK','PA','PZ','SL','WM','s']
# ASCII:-american standard code for information interchange
# ascii values 
# a->97.......z->122
# A->65.........z->90
# o->48,1->49.......9->57
# chr  pass only numbers
# ord    pass only strings
# print(chr(65))     #A
# print(chr(66))     #B
# print(chr(69))     #E
# print(chr(90))     #Z
# print(ord('A'))      #65
# print(ord('B'))      #66
# print(ord('E'))      #69
# print(ord('Z'))      #90
# print(ord('a'))      #97
# print(ord('b'))      #98
# print(ord('e'))      #101
# print(ord('z'))      #122
# print(chr(69))            #E
# print(chr(122))        #z
# print(dir(list))