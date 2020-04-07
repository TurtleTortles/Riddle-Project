import random

def end_game_check(riddles):
    if len(riddles) == 0:
        print('你都猜完了！')
        return False

#selects the riddle and makes sure there are no repeat riddles
def select_riddle(riddle_lst):
    riddle_num = random.randint(0, len(riddle_lst) - 1)
    riddle = riddlelst.pop(riddle_num)
    return riddle, riddle_num
    
def select_player(counter):
    pnum = ''
    if counter % 2 == 0:
        pnum = '一'
    else:
        pnum = '二'
    return pnum
            
            
            
def guess(pnum, riddle, riddle_num, player, Answers):
    p1 = 0
    p2 = 0
    print('第%s個人猜' % pnum)
    print(riddle + ':')
    ans = input()
    if ans == Answers[riddle_num]:
        print('你猜對了！')
        if player % 2 == 0:
            p1 += 1
        else:
            p2 += 1
        del Answers[riddle_num]
        return False

    if ans == "skip":
        print("player%s has decided to skip" % pnum)
        if pnum == '一':
            print("第二個人，寫skip如果你要跳過這個問題，如果你不要跳過打enter")
            confirm = input()
        else:
            print('第一個人，寫skip如果你要跳過這個問題，如果你不要跳過打enter')
            confirm = input()
            if confirm == "skip":
                print("executing skip...")
                return False     
    else:
        print('你猜錯了！')
        return counter + 1
        
                        
def winner(p1, p2):
    if p1 == p2:
        print('沒有人輸或贏')
    elif p1 > p2:
        print('第一個人贏了')
    else:
        print('第二個人贏了')
            
main():
    sim_riddles = ['一月七日,猜一个字', '一加一,猜一字', '一半儿,猜一个字',
    '一字十三点,难在如何点,猜一个字', '一百减一,猜一个字', '一夜又一夜,猜一字',
    '一个人搬两个土,猜一个字', '一个礼拜,猜一个字', '一家十一口,猜一字',
    '一家有七口,种田种一亩,自己吃不够,还养一条狗', '一根木棍,吊个方箱,一把梯子,搭在中央',
    '一只牛,猜一个字', '一只狗四个口,猜一个字', '一一箭穿心,猜一字',
    '一点一横长,一撇到南洋,南洋有个人,只有一寸长', '一边是水,一边是山,猜一个字',
    '一边是红,一边是绿,一边喜风,一边喜雨', '七人八只眼,猜一个字', '七人头上长了草,猜一字',
    '七十二小时,猜一个字', '王先生白小姐坐在石头上', '九十九,猜一字', '九只鸟,猜一个字',
    '九号,猜一字', '九辆车,猜一个字', '四个人搬个木头,猜一个字', '一人,猜一个字',
    '一人一张口,口下长只手,猜一字', '一人在内,猜一字', '一人挑两小人,猜一字' ]
    Answers = ['脂', '王', '臼', '汁', '白', '多', '佳', '旨', '吉', '兽', '面', '生', '器', '必', '府', '汕', '秋', '货', '花', '晶',
    '碧', '白', '鸠', '旭', '轨', '杰', '大', '拿', '肉', '夹']
    pscore1 = 0
    pscore2 = 0
    counter = 0
    my_bool = True
    
    print('這是個猜謎語的遊戲')
    print('我們有30個謎語')
    while my_bool:

        riddle_val = select_riddle(sim_riddles)
        riddle_str = riddle_val[0]
        riddle_int = riddle_val[1]
        
        while my_bool2:
            
            player = select_player(counter)
            guess(player, riddle_str, riddle_int, player)
            
        my_bool = end_game_check(sim_riddles)
    winner()
    
if __name__ == "__main__":
    
    main()
    
    
    
    

    
    
    
    
    
