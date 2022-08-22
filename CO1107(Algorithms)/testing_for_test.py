# Q18

K = []
def integer_matcher(A,B):
    
    for i in range(len(A)):
        if A[i] in B:
            K.append(1)
        else:
            K.append(0)
    
    return K 
            
A = [2,17,12,5]
B = [2,12]
K = integer_matcher(A, B)
print(K)
