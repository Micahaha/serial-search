
def search(a, first: int, size: int, target: int):
    """Searches for a desired element in a list of elements 
    starting at a a[first]

    Args:
        a (int): list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target (int): the elmenet to srarch

    Returns:
        int: If target appears in the list, index of the element 
        that contains the target. else -1  
    """    
    # set an int variable i = 0 
    i = 0

    # set a boolean variable found to false
    found = False

    # while there are more elements to search 
    # and the target hasn't been found 
    
    while((i < size) and not found):
        # if the current element is the target
        if(a[i + first] == target):
            # set found to true 
            found = True
        else:
            # increment by 1 
            i += 1
    
    # check if the target was found
    if (found):
        # return index of the target
        return i + first
    else:
        # return negative 1 
        return -1
    

