class solution:
    TOI = {'Monday': 3, 'Tuesday': 3, 'Wednesday': 3, 'Thursday': 3, 'Friday': 3, 'Saturday': 5, 'Sunday': 6}
    Hindu = {'Monday': 2.5, 'Tuesday': 2.5, 'Wednesday': 2.5, 'Thursday': 2.5, 'Friday': 2.5, 'Saturday': 4,'Sunday': 4}
    ET = {'Monday': 4, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 4, 'Friday': 4, 'Saturday': 4, 'Sunday': 10}
    BM = {'Monday': 1.5, 'Tuesday': 1.5, 'Wednesday': 1.5, 'Thursday': 1.5, 'Friday': 1.5, 'Saturday': 1.5,'Sunday': 1.5}
    HT = {'Monday': 2, 'Tuesday': 2, 'Wednesday': 2, 'Thursday': 2, 'Friday': 2, 'Saturday': 4, 'Sunday': 4}
    def _init_(self,val):
        self.budget=val

    def sum(self):
        week_sum={'TOI':sum(self.TOI.values()),
                  'Hindu':sum(self.Hindu.values()),
                  'ET':sum(self.ET.values()),
                  'BM':sum(self.BM.values()),
                  'HT':sum(self.HT.values())}
        return week_sum


    def comb(self):
        ls=['TOI','Hindu','ET','BM','HT']
        ans=[]
        for i in range(5):
            for j in range(i+1,5):
                if self.sum()[ls[i]]+self.sum()[ls[j]]<=self.budget:
                    ans.append({ls[i]:ls[j]})
        return ans



ob1=solution(40)
ob2=solution(35)
print(ob1.comb())
print(ob2.comb())