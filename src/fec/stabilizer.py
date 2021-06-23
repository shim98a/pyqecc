import numpy as np
from .abstruct import *
from ..util import *
class SC(CODE):
    def __init__(self,n,k,H='random',T=None,L=None):
        self._name = "stabilizer"
        self._n = n
        self._k = k
        self._R = self._k/self._n
        if H in ['random']:
            pass
        else:
            self._H = H
        self._T = T
        self._L = L

        self.enc_circuit = None
        self.dec_circuit = None

    #量子情報ビット
    def get_enc_circ(self):
        return self.enc_circuit

    #シンドロームと確率分布を受け取る．
    def get_dec_circ(self):
        return self.dec_circuit

    # soft decision
    def ml_dec(self,p):
        return L

    # soft decision
    def rn_dec(self,p):
        return L

    # hard decision
    def get_syndrome(self,e):
        return symplex_binary_inner_product(self._H,e)

    def get_T(self,ind):
        T = np.zeros(2*self.n,dtype='i1')
        #print(T,self.T[1],self.n - self.k)
        for i in range(self.n - self.k):
            T+=(ind[i]*self.T[i])
        return np.mod(T,2)

    def get_S(self,ind):
        S = np.zeros(2*self.n,dtype='i1')
        for i in range(self.n-self.k):
            S+=(((ind>>i)&1)*self.H[i])
        return np.mod(S,2)

    def get_L(self,ind):
        L = np.zeros(2*self.n,dtype='i1')
        for i in range(2*self.k):
            L+=(((ind>>i)&1)*self.L[i])
        return np.mod(L,2)

    def in_S(self,b):
        return sum(gaussjordan(np.c_[self._H.T,b])[self.n-self.k+1,:])!=0 or sum(b)==0

    def hard_decode(self,e):
        s = symplex_binary_inner_product(self._H,e)
        ee = np.zeros(2*self.n,dtype='i1')
        for i in range(self.n-self.k):
            ee=s[i]*self._T[i]+ee
        #print(s,ee,111)
        ee = np.mod(ee,2)
        return ee

    def ML_decode(self,P,T,limit=15,iid=True):
        if iid:
            P=np.array([P.tolist()]*self.n)

        #decoding_metric: メトリック．受信語と通信路情報から計算する．
        if self.n>limit:
            ValueError("Error: The qubit n ="+str(self.n)+" is limited because of a large decoding complexity. You can change the qubit limit.")

        #Lについてビット全探索
        P_L = np.zeros(4**self.k)
        for li in range(4 ** self.k):
            SUM_P = np.zeros(4)
            L = self.get_L(li)

            #Sについてビット全探索
            for si in range(2 ** (self.n-self.k)):
                S = self.get_S(si)
                E = T^S^L
                #print(self.get_syndrome(E),self.get_syndrome(T))
                #exit()
                #print(T,S,L,E)

                #E = ()のうち，確率を入力
                Ptmp = 1
                #print(E)
                for ei in range(self.n):
                    #ind=(1&(E[ei]^E[ei+self.n]))+(1<<(1&(E[ei]&E[ei+self.n])))
                    ind=E[ei]+2*E[ei+self.n]
                    #print(ind,E[ei],E[ei+self.n])
                    #print(E[ei],ei,E,ind,1&(E[ei]^E[ei+self.n]),(1<<(1&(E[ei]&E[ei+self.n]))))
                    #print(li,ei,ind,E[ei],E[ei+self.n],1<<(1&E[ei]&E[ei+self.n]),1&(E[ei]^E[ei+self.n]))
                    #print("e",E,(1&(E[ei]^E[ei+self.n])),(1<<(1&(E[ei]&E[ei+self.n]))),ei,ind,P[ei][ind],P)
                    Ptmp*=P[ei][ind]
                print(E,T,S,L,Ptmp)
                P_L[li]+=Ptmp
        print(P_L)
        l_ind = np.argmax(P_L[li])
        L = np.zeros(2*self.n,dtype='i1')
        for lj in range(2**self.k):
            L+=(((l_ind>>lj)&1)*self.L[lj])
        print(L)
        return L

    def __str__(self):
        output = ""
        output+="codename        :"+str(self.name)+"\n"
        output+="n               : "+str(self.n)+"\n"
        output+="k               : "+str(self.k)+"\n"
        output+="R               : "+str(self.R)+"\n"
        return output
