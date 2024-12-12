import numpy as np
class csr_mat:
    
    def __init__(s, *args):
        if len(args) == 1: # le constructeur est appellé avec un seul argument
            A = np.array(args[0],dtype=float)
            s.shape = A.shape
            s.AV = []
            s.JC = []
            s.IA = [0]
            for i in range(len(A[1])):
                cnt = 0
                for j in range(len(A)):
                    if A[i,j] != 0:
                        s.AV.append(A[i,j])
                        s.JC.append(j)
                        cnt += 1
                s.IA.append(s.IA[-1] + cnt)
            s.AV = np.array(s.AV)
            s.JC = np.array(s.JC,dtype=int)
            s.IA = np.array(s.IA,dtype=int)
        else:
            s.AV = np.array(args[0])
            s.JC = np.array(args[1],dtype=int)
            s.IA = np.array(args[2],dtype=int)
            s.shape = np.array(args[3],dtype=int)
    
    def toarray(s):
        A = np.zeros(s.shape)
        for row in range(s.shape[0]):
            for p in range(s.IA[row],s.IA[row+1]):
                A[row,s.JC[p]] = s.AV[p]
        return A
        
            

    def dot(s,o):
        Y = np.zeros(s.shape[0])
        for i in range(s.shape[0]):
            k1 = s.IA[i]
            k2 = s.IA[i+1]
            Y[i] = sum(s.AV[k1:k2]*o[s.JC[k1:k2]])
        return Y
    
    def transpose(s):
        aux = np.zeros(s.shape[1])
        for i in s.JC:
            aux[i]+=1
        
        IAt = np.zeros(s.shape[1]+1,dtype=int)
        IAt[0]=aux[0]
        for i in range(len(IAt)-1):
            IAt[i+1]=IAt[i]+aux[i]
        aux = np.zeros(s.shape[1])
        
        AVt = np.zeros(s.AV.shape)
        JCt = np.zeros(s.JC.shape)
        for i in range(len(s.IA)):
            for j in range(len(s.JC)):
                if s.IA[i]<=j<=s.IA[i+1]:
                    k = s.JC[j]
                    JCt[IAt[k]+aux[k]]=i
                    AV[IAt[k]+aux[k]]=AV[j]
                    aux[k]=aux[k]+1
        return csr_mat(AVt,JCt,IAt,(s.shape[1],s.shape[0]))

rng = np.random.default_rng()

shape = 5
filling_rate = .5
lower = 0
upper = 9
def gen_matrix_plain(shape,filling_rate=.5,lower=0,upper=9):
    blank = np.zeros((shape,SHAPE))
    for i in range(shape):
        for j in range(shape):
            if rng.random() < filling_rate:
                blank[i,j] = rng.choice(range(lower,upper+1))
    return blank

