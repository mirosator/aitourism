import random
from sklearn.naive_bayes import GaussianNB
list = []


dst_lst = ['tenis','minigolf','volejbal','zámek','hrad','kostel','vodopád','kopec','skála']
vys_vec =[]

for i in range(0,100):
    #narodnost
    oper_lst = []

    #narodnost 0 - cr, 1 - sr, 2 - nemecko
    oper_lst.append(random.randint(0,2))

    #group size 0 - jedinec, 1 - pár, 2 - rodina, 3 - parta
    oper_lst.append(random.randint(0,3))

    #vyber 0 - aktivity, 1 - kultura, 2 - priroda
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