def mergerecur(items):
    print(f"splitting   {items}")
    if len(items)>1:
        mid=len(items)//2
        lefthalf=items[:mid]
        righthalf=items[mid:]
        mergerecur(lefthalf)
        mergerecur(righthalf)
        i=0
        j=0
        k=0
        print("merging",items)
        while i < len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                items[k]=lefthalf[i]
                i+=1
            else:
                items[k]=righthalf[j]
                j+=1
            k+=1
        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            items[k]=righthalf[j]
            j+=1
            k+=1


items = [2,5,4,3,6,6,1,7,8,9,0]
mergerecur(items)
print(items)