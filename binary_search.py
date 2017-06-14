
''' the first function is just to test that we have a sorted array.
Returns True if the array is sorted otherwise returns False '''
def sorting_check(list_to_check):
    for i in range(1, len(list_to_check)):
        if list_to_check[i] < list_to_check[i-1]:
            return False
    return True

''' Binary search'''
def binary_search(list_elements, element):
    found_element = -1
    low_element = 0
    high_element = len(list_elements) - 1
    mid = list_elements[len(list_elements)//2]

    if list_elements[low_element] > element or list_elements[high_element] < element:
        return found_element
    continue_search = True

    while continue_search:
        if list_elements[mid] == element:
            found_element = mid
            #print('the elements was found in {} position'.format(mid + 1)) # we people like to begin count numbers from the first, not zero
            continue_search = False
        elif low_element == mid or high_element == mid:
            #print('there is no such element in the list')
            continue_search = False
        else:
            if element > list_elements[mid]:
                low_element = mid
                mid = (high_element - low_element)//2 + low_element
            if element < list_elements[mid]:
                high_element = mid
                mid = (mid - low_element)//2 + low_element
    return found_element

#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 23, 24, 25, 26, 27, 28, 80, 89, 90]
#binary_search(l, 7)
