def combinationSort(strList):

    #Sorting for l1 i.e based on alphabets in ascending order
    alpha = sorted(strList, key = lambda x: x[0])
    
    # sorting the list based on the numbers present in every element of list in descending order
    num = sorted_lst = sorted(strList, key=lambda x: (x[0], -int(x[1:])))
    
    return alpha, num