def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = int((len(list)/2))

        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else: 
                return recursive_binary_search(list[:mid], target)

def verify(result):
    print('target found:', result)

nb = [1,2,3,4,5,6,7,8,9]
result = recursive_binary_search(nb, 5)
verify(result)  