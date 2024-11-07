adarsh = [('Protein',5000),('Lays',10),('Chicken roll',50),('Sandwhich',100)]
arun = [('Chips',50),('maggie',10),('Chicken roll',50),('egg roll',100)]
mithun = [('biryani',500),('Lays',10),('Creatine',5500),('gobi',100)]
darshan = [('Muscle blaze',5000),('bingo',10),('noodles',50),('burger',100)]

shop_list = list(set(adarsh+arun+mithun+darshan))

print('list eithout any duplicate is',shop_list)

total = 0
for i in shop_list:
    total += i[1]
    
print(f'Final billing amount is {total}')


    

