import numpy as np
import matplotlib.pyplot as plt

boardlimit = 50
walkdist = 10

def point_gen():
    target = np.random.random(2)
    target = target - 0.5
    target = target * boardlimit

    print(target)
    return target

def rew_func(bot, target):
    rew = -np.linalg.norm(bot - target)
    return rew

def fangle(p1, p2):
    dif = p2 - p1
    if (dif[0] == 0):
        return np.arctan(np.infty) if dif[1] > 1 else np.arctan(-np.infty)
    return np.arctan(dif[1]/dif[0])

if __name__ == "__main__":
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    target = point_gen()
    plt.plot(target[0], target[1], marker = 'o', markersize = 5, markerfacecolor = 'yellow')
    
    # plt.show()
    visit = np.array([target])  
    print(visit)
    # nbot = 1
    # bot = [point_gen() for _ in range(nbot)]
    # pbest = {bot[i]: (rew_func(bot[i], target)) for i in range(nbot)}
        # tworst = 0
    # tbest = 
    # for b in pbest:
    #     if pbest[b] < tworst:
    #         tworst = pbest[b]
    
    bot = point_gen()
    pbest = [bot.copy(), rew_func(bot, target)]
    pdir = 0

    while (rew_func(bot, target) < -0.1):
        # Decide walk coefficients
        p = np.random.random(1)[0]
        pb = np.random.random(1)[0]
        # p, pb = 0.5,0.5
        bdir = fangle(bot, pbest[0])
        spos = bot.copy()

        # Walking toward original direction
        for _ in range(10):
            mv = p*(walkdist/10)*np.array([np.cos(pdir), np.sin(pdir)])
            bot = bot + mv
            score = rew_func(bot, target)
            if score > pbest[1]:
                pbest = [bot.copy(), score]
            visit = (np.vstack((visit, bot)))
        
        # Walking toward best spot
        for _ in range(10):
            mv = pb*(walkdist/10)*np.array([np.cos(bdir), np.sin(bdir)])
            bot = bot + mv
            score = rew_func(bot, target)
            if score > pbest[1]:
                pbest = [bot.copy(), score]
            visit = (np.vstack((visit, bot)))
        
        pdir = fangle(spos,bot)
        # plt.plot(bot[0], bot[1], marker = "o", markersize = 3, markerfacecolor = "red")
        # print(visit, bot)
        print(score)
        print()
        visit = (np.vstack((visit, bot)))
        plt.plot(visit[:,0], visit[:,1])
        plt.show()

plt.show()
