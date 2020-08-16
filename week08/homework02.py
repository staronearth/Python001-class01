def add_1(nums):
    return nums+1

def mapper(func,iterables):
    # print(list(iterables))
    for i in iterables:
        yield func(i)





a = mapper(add_1,(1,2,3,4))
# a = map(add_1,(1,2,3,4))
print(list(a))
        