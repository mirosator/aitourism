import random
from sklearn.naive_bayes import GaussianNB
list = []

#pivovar divadlso JK tyla bazén borský park synagoga

dst_lst = ['pivovar','divadlo','bazén','park','hřiště','synagoga']
vys_vec =[]
for i in range(0,1600):
    vys_vec.append(random.randint(0,5))


for i in range(0,1600):
    #narodnost
    oper_lst = []

    if(i <1150):
        oper_lst.append(0)
    elif(i<1150+400):
        oper_lst.append(1)
    else:
        oper_lst.append(2)

    if (i < 100):
        oper_lst.append(0)
    elif (i < 100 + 8):
        oper_lst.append(1)
    elif (i < 100 + 8 + 152):
        oper_lst.append(2)
    elif (i < 100 + 8 + 152+85):
        oper_lst.append(3)
    elif (i < 100 + 8 + 152+85+17):
        oper_lst.append(4)
    else:
        oper_lst.append(5)

    if (i < 362):
        oper_lst.append(0)
    elif (i < 362+342):
        oper_lst.append(1)
    elif (i < 362+342+389):
        oper_lst.append(2)
    elif (i < 362+342+389+420):
        oper_lst.append(3)
    else:
        oper_lst.append(4)
    print(oper_lst)
    list.append(oper_lst)

model = GaussianNB()
model.fit(list,vys_vec)
x = model.predict([[1,1,1]])

print(dst_lst[x.item(0)])
print("done")

import _pickle as cPickle
# save the classifier
with open('my_dumped_classifier.pkl', 'wb') as fid:
    cPickle.dump(model, fid)
"""
# load it again
with open('my_dumped_classifier.pkl', 'rb') as fid:
    gnb_loaded = cPickle.load(fid)
    """