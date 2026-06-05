'''An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, which involves two key methods:

__iter__(): Returns the iterator object itself.
__next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.'''

'''Built-in iterators'''
# s = "GFG"
# it = iter(s)

# print(next(it))
# print(next(it))
# print(next(it))
#---------------------------------------
'''(CUSTOM IETRATOS)using iterators to print even numbers'''
# class EvenNumbers:
#     def __iter__(self):
#         self.n = 2
#         return self
    
#     def __next__(self):
#         x = self.n
#         self.n += 2
#         return x

# even = EvenNumbers()
# it = iter(even)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

'''StopIteration Exception
StopIteration exception is integrated with Python’s iterator protocol. It signals that the iterator has no more items to return. Once this exception is raised, further calls to next() on the same iterator will continue raising StopIteration.'''

# li = [100,200,300]
# it = iter(li)

# while True:
#     try:
#         print(next(it))
#     except:
#         print("End of iteration")
#         break