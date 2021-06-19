import random
from sklearn.naive_bayes import GaussianNB
list = []

#pivovar divadlso JK tyla bazén borský park synagoga

dst_lst = ['tenis','minigolf','volejbal','zámek','hrad','kostel','vodopád','kopec','skála']
vys_vec =[]

for i in range(0,100):
    #narodnost
    oper_lst = []

    oper_lst.append(random.randint(0,2))
    oper_lst.append(random.randint(0,3))
    posledni = random.randint(0,2)
    oper_lst.append(posledni)
    if posledni==0:
        vys_vec.append(random.randint(0,2))
    elif posledni==1:
        vys_vec.append(random.randint(3,5))
    else:
        vys_vec.append(random.randint(6,8))
    print(oper_lst)
    list.append(oper_lst)

model = GaussianNB()
model.fit(list,vys_vec)
x = model.predict([[1,1,1]])

print(dst_lst[x.item(0)])
print("done")

import _pickle as cPickle
# save the classifier
with open('novy_classifier.pkl', 'wb') as fid:
    cPickle.dump(model, fid)
"""
# load it again
with open('my_dumped_classifier.pkl', 'rb') as fid:
    gnb_loaded = cPickle.load(fid)
    """