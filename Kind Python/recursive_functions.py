import numpy as np

def recursive_sort(List):
    
    if len(List)>1:
        if len(List)%2:
            List1 = recursive_sort(List[:int(np.floor(len(List)/2))])
            List2 = recursive_sort(List[int(np.floor(len(List)/2)):])
            
            List1 = [x if type(x) == int else x[0] for x in List1]
            List2 = [x if type(x) == int else x[0] for x in List2]
            
            i = 0
            j = 0
            List_returned = []
            while i<len(List1) and j<len(List2):
                if List1[i] <= List2[j]:
                    List_returned.append(List1[i])
                    i+=1
                else:
                    List_returned.append(List2[j])
                    j+=1
            if i == len(List1):
                for x in List2[j:]:
                    List_returned.append(x)
            else:
                for x in List1[i:]:
                    List_returned.append(x)
            return List_returned
        else:
            List1 = recursive_sort(List[:int(len(List)/2)])
            List2 = recursive_sort(List[int(len(List)/2):])
            
            List1 = [x if type(x) == int else x[0] for x in List1]
            List2 = [x if type(x) == int else x[0] for x in List2]
            
            i = 0
            j = 0
            List_returned = []
            while i<len(List1) and j<len(List2):
                if List1[i] <= List2[j]:
                    List_returned.append(List1[i])
                    i+=1
                else:
                    List_returned.append(List2[j])
                    j+=1
            if i == len(List1):
                for x in List2[j:]:
                    List_returned.append(x)
            else:
                for x in List1[i:]:
                    List_returned.append(x)
            return List_returned
        
    else:
        List_returned = List
        return List_returned
    


List = [int(x) for x in input().split(' ')]

print(*recursive_sort(List))

