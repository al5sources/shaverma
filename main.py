import random
#import matplotlib
#import matplotlib.pyplot as plt

badarr = []
sim_num = 1000  # количество симуляций
random.seed(11)

def get_seven():
    state = [True, True, False, False, False, False, False]
    random.shuffle(state)
    return state

def serega_est(state):
    return random.sample(state, 4)

for i in range(0, sim_num - 1):
    sample1 = serega_est(get_seven())
    print(sample1)
    badnum = 0
    for n in range(4):
        #        print(sample1[n])
        if sample1[n] == True:
            badnum = badnum + 1
    #        print(badnum)
    badarr.append(badnum)
print(badarr)

from collections import Counter
c = Counter(badarr)

print("Число выпадений шавух в выборке 4 ")
print(c)

# теперь поделим на общее число подбрасываний и получим вероятности:
print("Вероятности выпадений каждой из сторон:")
print({k: v/sim_num for k, v in c.items()})