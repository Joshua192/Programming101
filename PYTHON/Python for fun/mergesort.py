####SORT OUT CODE
a = [1,3,5,7,9]
b = [2,4,6,8,10]
def merge(list1,list2):
    list3 = list(list1+list2)
    print(list3)
#merge(a,b)

mergedlists = []

def mergesort(list1,list2):
    k = 0
    i = 0
    
    len1 = len(list1)
    len2 = len(list2)

    while k < len1 and i < len2:
        if list1[k] > list2[i]:
            mergedlists.append(list2[i])
            i = i+1
            print(f"Updated the list:  {mergedlists}")
        else:
            mergedlists.append(list1[k])
            k = k+1
            print(f"Updated the list:  {mergedlists}")
    if k < len1:# Resolved the issue, too umch indentation. was appending the rest of the list before doing its second iteration
        for item in range(k,len1):
            mergedlists.append(list1[item])
    elif i < len2:
        for item in range(i,len2):
            mergedlists.append(list2[item])
    print(mergedlists)
mergesort(a,b)

numbers = [2,5,4,3,6,7,2,8,9,10]
listoflists = []
for number in numbers:
    listoflists.append([number])
print(listoflists)

# while len(listoflists)!=1:
#     index = 0
#     newerlist = []
#     for x in range(0,len(listoflists),2):
#         if listoflists[index] >listoflists[index+1]:#my version


while len(listoflists)!=1:
    index = 0
    newerlist = []
    while index < len(listoflists)-1:
        newerlist = mergesort(listoflists[index],listoflists[index+1])
        index = index+2#
        print(f"Updated:    {newerlist}")
        break