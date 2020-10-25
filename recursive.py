import numpy as np
class Vector(object):
    def __init__(self, list_1):
        self.ownlist = list_1
    def copyfrom(self, given_list):
        new_list = np.array(2*len(given_list))
        for i in range(len(given_list)):
            new_list[i] = given_list[i] 
    def insert(self, item1,location) :
        self.ownlist.append([]) 
        j = 0
        for i in range(len(self.ownlist) -1 ,0,-1):
            if j == location:
                self.ownlist[j] = item1
            else:
               j = j +1
               self.ownlist[i] = self.ownlist[i-1]
    def delete(self, given_list, lo, hi):
        for  i in range(hi - lo):
           if hi + i <= len(given_list) - 1:

            given_list[lo + i] = given_list[hi + i]
           else:
               given_list[lo + i ] = None
        return given_list
    def find(self,given_list, value):
        for i in range(len(given_list) -1, 0, -1):
            if given_list[i] == value:
                 return i
        return 'false'
    def unify_list(self,given_list):
      while i < len(given_list) :
        i = 2
        for j in range(i):
            if given_list[j] == given_list[i]:
             given_list  = self.delete(given_list,j, j+1)
        i  = i + 1


class DCA(object):
    def __init__(self,list1):
        self.list2 = list1
    def recursive(self, list1, start_position, final_position):

        if start_position >= final_position:
            return
        else: 
            middle_term = list1[start_position]
            list1[start_position] = list1[final_position]
            list1[final_position] = middle_term
            self.recursive(list1, start_position +1, final_position -1)
    def Max2(self,list1,start_position,final_position):
        if start_position > final_position - 2:
            if list1[start_position] > list1[final_position]:
                max1 = start_position
                max2 = final_position
            else:
                max1 = final_position
                max2=  start_position
            return max1,max2
        else:
            mid = (start_position+final_position)/2
            max1l,max2l = self.Max2(list1, start_position, mid )
            max1r,max2r = self.Max2(list1, mid+1, final_position)
            if max1l > max1r:
                max1  =  max1l
                if max2l > max1r:
                    max2 = max2l
                else:
                    max2 = max1r
            else:
                max1  =  max1r
                if max2r > max1l:
                    max2 = max2r
                else:
                    max2 = max1l
            return max1, max2
    def findsubsequence(self,list1,list2):

        
        if len(list1) ==0 or len(list2) == 0:
            return {'':0}
        elif  list1[-1] == list2[-1]:
            subanswer  =  self.findsubsequence(list1[:-1],list2[:-1]) 
            answer = {}

            for key, value in subanswer.items():
                answer[key+list1[-1]] = value + 1 
             
        else:
           answer1 = self.findsubsequence(list1[:-1], list2)
           answer2 = self.findsubsequence(list1,list2[:-1])
           
           if len(list(answer1.keys())[0]) > len(list(answer2.keys())[0]):
               answer = answer1
           elif len(list(answer1.keys())[0]) < len(list(answer2.keys())[0]):
               answer = answer2
           else:
               answer = dict(list(answer1.items())+list(answer2.items()))
        return answer
            

if __name__ == "__main__":
    dca = DCA([1,2,3,4])
    list2 = [1,2,3,4]
    dca.recursive(list2,0,3)
    print(list2)
    print(dca.findsubsequence('educational','advantage'))