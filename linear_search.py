def linear_search(list, target):
    '''
    Return the index position of the target if found, else return None
    '''
    #temp = 0
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        #temp = temp + 1
        #print(temp)
    return None

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')

nb = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(nb, 10)
verify(result)