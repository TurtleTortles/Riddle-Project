import random
import time


class eventclass:
    def __init__(self, the_event, answer, riddle_num):
        self.the_event = the_event
        self.riddle_num = riddle_num
        self.answer = answer

    def give_ans(self):
        if self.the_event == 'give ans':
            print('')
            print('答案是：')
            print(self.answer[self.riddle_num])

    def min2opp(self, p1score, p2score, counter):
        if self.the_event == '-2opp':
            print('')
            print('對手扣了兩分！')
            if counter % 2 == 0:
                return p2score - 2, p1score
            else:
                return p2score, p1score - 2
        else:
            return p1score, p2score

    def min2(self, p1score, p2score, counter):
        if self.the_event == '-2':
            print('你扣了兩分')
            if counter % 2 == 0:
                return p1score - 3, p2score
            else:
                return p1score, p2score - 3
        else:
            return p1score, p2score

    def plus5(self, p1score, p2score, counter):
        if self.the_event == '+5 points':
            if counter % 2 == 0:
                return p1score + 4, p2score
            else:
                return p1score, p2score + 4
        else:
            return p1score, p2score
    def plus1opp(self, p1score, p2score, counter):
        if self.the_event == '+1opp':
            if counter % 2 == 0:
                return p1score, p2score + 1
            else:
                return p1score + 1, p2score
        else:
            return p1score, p2score


def choose_game():

    var = ""
    while True:
        game = input()
        if game == "riddle" or "riddles" or "字謎":
            var = "rid"
            break
        elif game == "proverb" or "proverbs" or "成語謎語":
            var = "pro"
            break
        else:
            print("empty for now")
def intro():
    print('這是個猜謎語的遊戲')
    print('我們有30個謎語')
    print('')
    print('如果你要繁體字打繁，如果你要簡體打簡')

    #FIX ABOVE PRINT STATMENT CHINESE TIPS
    while True:
        lang = input()
        if lang == '繁':
            return 'trd'

        elif lang == '簡':
            return 'sim'
        else:
            print('請打繁或簡')

def intro2(ch_type, ins, event, tip):
    print('如果你要幫忙，打instructions, 如果你想要看到隨機事件，打events, 如果你想要tips，如果你要開始，打字謎如果你要玩字謎，或打成語如果你要玩成語謎語')
    while True:
        select = input()
        if select == 'instructions':
            print(ins[ch_type])



        elif select == 'events':
            print(event[ch_type])
        elif select == 'tips':
            print(tip[ch_type])
        elif select == '成語':
            return '成語'
        elif select == '字謎':
            return '字'

def create_events(events):
    for i in range(60):
        events.append('n')
    for i in range(10):
        events.append('-2opp')
    for i in range(10):
        events.append('-2')
    for i in range(5):
        events.append('give ans')
    for i in range(5):
        events.append('+5 pts')
    for i in range(10):
        events.append('+1opp')


def end_game_check(riddles):
    if len(riddles) == 0:
        print('你都猜完了！')
        return False
    else:
        return True
#selects the riddle and makes sure there are no repeat riddles
def select_riddle(riddle_lst):
    riddle_num = random.randint(0, len(riddle_lst) - 1)
    riddle = riddle_lst.pop(riddle_num)
    return riddle, riddle_num

def select_player(counter):
    pnum = ''
    if counter % 2 == 0:
        pnum = '一'
    else:
        pnum = '二'
    return pnum


def guess(pnum, riddle, riddle_num, Answers, counter):
    p1 = 0
    p2 = 0

    print('第%s個人猜' % pnum)
    print(riddle + ':')
    ans = input()
    if ans == Answers[riddle_num]:
        print('你猜對了！')
        if counter % 2 == 0:
            p1 = 1
        else:
            p2 = 1
        del Answers[riddle_num]
        return False, counter, p1, p2

    if ans == "skip":
        print("第%s選擇跳過這個問題" % pnum)
        if pnum == '一':
            print("第二個人，寫skip如果你要跳過這個問題，如果你不要跳過打enter")
            confirm = input()

        else:
            print('第一個人，寫skip如果你要跳過這個問題，如果你不要跳過打enter')
            confirm = input()
        if confirm == "skip":
            print("正確的答案是", end = '“')
            print(Answers[riddle_num], end = '"')
            print("")
            time.sleep(0.5)
            print("執行跳過...")
            time.sleep(0.5)
            return False, counter, 0, 0
    else:
        print('你猜錯了！')
        return True, counter + 1


def timer():
    counter = 0
    remaining = 60
    print("the round starts now, you have 60 seconds to answer")
    while counter != 4:
        time.sleep(15)
        remaining -= 15
        print("you have", end = " ")
        print(remaining, end = " ")
        print("seconds remaining")
    print("you ran out of time, next person")
   #connect this to a break statement for main while loop

def winner(p1, p2):
    if p1 == p2:
        print('沒有人輸或贏')
    elif p1 > p2:
        print('第一個人贏了')
    else:
        print('第二個人贏了')

def main():
    trd_riddles = ['一月七日,猜一個字', '一加一,猜一字', '一半兒,猜一個字',
    '一字十三點,難在如何點,猜一個字', '一百減一,猜一個字', '一夜又一夜,猜一字',
    '一個人搬兩個土,猜一個字', '一個禮拜,猜一個字', '一家十一口,猜一字',
    '一家有七口,種田種一畝,自己吃不夠,還養一條狗', '一根木棍,吊個方箱,一把梯子,搭在中央',
    '一隻牛,猜一個字', '一隻狗四個口,猜一個字', '一一箭穿心,猜一字',
    '一點一橫長,一撇到南洋,南洋有個人,只有一寸長', '一邊是水,一邊是山,猜一個字',
    '一邊是紅,一邊是綠,一邊喜風,一邊喜雨', '七人八隻眼,猜一個字', '七人頭上長了草,猜一字',
    '七十二小時,猜一個字', '王先生白小姐坐在石頭上', '九十九,猜一字', '九隻鳥,猜一個字',
    '九號,猜一字', '九輛車,猜一個字', '四個人搬個木頭,猜一個字', '一人,猜一個字',
    '一人一張口,口下長隻手,猜一字', '一人在內,猜一字', '一人挑兩小人,猜一字' ]
    trd_Answers = ['脂', '王', '臼', '汁', '白', '多', '佳', '旨', '吉', '獸', '面', '生', '器', '必', '府', '汕', '秋', '貨', '花', '晶',
    '碧', '白', '鳩', '旭', '軌', '傑', '大', '拿', '肉', '夾']



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
    sim_Answers = ['脂', '王', '臼', '汁', '白', '多', '佳', '旨', '吉', '兽', '面', '生', '器', '必', '府', '汕', '秋', '货', '花', '晶',
    '碧', '白', '鸠', '旭', '轨', '杰', '大', '拿', '肉', '夹']

    spec_event = []

    trd_chengyu_rid = ['蛇有腳', '一隻青蛙在井裡', '有個人給牛彈琴', '一個人每次等在一個地方抓兔子', '兩個東西是相反的',
    '有個人用刀刻船來記得他的東西掉在哪裡', '有個人拔他的植物', '羊死了因為牢有洞', '有個人把玲打碎來偷玲', '有個人以為他的杯子有蛇',
    '一個人用一塊石頭打兩隻鳥', '一個人只用弓的聲音讓鳥掉下來', '一個人把馬和老虎換了', '用一個東西拿到兩個好處', '很多很多的人']
    trd_chengyu_ans = ['畫蛇添足', '井底之蛙', '對牛彈琴', '守株待兔', '自相矛盾', '刻舟求劍', '拔苗助長', '亡羊補牢', '掩耳盗铃',
    '杯弓蛇影', '一石二鳥', '驚弓之鳥', '馬馬虎虎', '一舉兩得', '人山人海']
    sim_chengyu_rid = ['蛇有脚', '一只青蛙在井里', '有个人给牛弹琴', '一个人每次等在一个地方抓兔子', '两个东西是相反的',
    '有个人用刀刻船来记得他的东西掉在哪里', '有个人拔他的植物', '羊死了因为牢有洞', '有个人把玲打碎来偷玲', '有个人以为他的杯子有蛇',
    '一个人用一块石头打两只鸟', '一个人只用弓的声音让鸟掉下来', '一个人把马和老虎换了', '用一个东西拿到两个好处', '很多很多的人']
    sim_chengyu_ans = ['画蛇添足', '井底之蛙', '对牛弹琴', '守株待兔', '自相矛盾', '刻舟求剑', '拔苗助长', '亡羊补牢', '掩耳盗铃',
    '杯弓蛇影', '一石二鸟', '惊弓之鸟', '马马虎虎', '一举两得', '人山人海']



    instruction = [
    '''這個謎語的遊戲就是一個跟你和另外一個人比誰可以先猜謎語的答案。第一個人會先猜。如果他猜對了，他就得到一分。
如果他沒大隊，另外一個人就可以猜。遊戲開始的時候，你就可以選如果你要玩這個遊戲用繁體或簡體。如果你先要用繁體玩，打繁。
如果你想要用簡體玩，打簡。你選完以後，遊戲就開始。遊戲開始的時候，你就可以看到密語和可以開始猜一猜。小心！
你只有60秒猜。每一個15秒，你會看到你還有幾秒可以用來猜。你必須在時間用完前回答，否則你的輪會被跳過！
如果兩個人都覺得這個謎語太難，你們可以打skip來跳過那個謎語。你猜對的時候你會得到一分。謎語都猜完的時候，有最多的分數的人會贏。
有的時候，特別活動會發生。如果你打events你會看到每個特別活動。''',
    '''这个谜语的游戏就是一个跟你和另外一个人比谁可以先猜谜语的答案。第一个人会先猜。如果他猜对了，他就得到一分。
如果他没大队，另外一个人就可以猜。游戏开始的时候，你就可以选如果你要玩这个游戏用繁体或简体。如果你先要用繁体玩，打——。
如果你想要用简体玩，打——。你选完以后，游戏就开始。游戏开始的时候，你就可以看到密语和可以开始猜一猜。小心！
你只有60秒猜。每一个15秒，你会看到你还有几秒可以用来猜。你必须在时间用完前回答，否则你的轮会被跳过！
如果两个人都觉得这个谜语太难，你们可以打skip来跳过那个谜语。你猜对的时候你会得到一分。谜语都猜完的时候，有最多的分数的人会赢。
有的时候，特别活动会发生。如果你打events你会看到每个特别活动。''']

    event_ins = [
    '''特別活動：
特別的活動會隨機發生

對手丟兩分:
你還會得到一分，但是對手丟兩分

得到答案:
如果這個特別活動發生，你會知道答案

加五分：
在這個很少發生的特別活動，你會得到五分

丟兩分：
如果這個特別活動發生，你猜對的時候會丟兩分

對手得到一分：
你不會拿到分數，反而對手會拿到一分''',
    '''特别活动：
特别的活动会随机发生

对手丢两分:
你还会得到一分，但是对手丢两分

得到答案:
如果这个特别活动发生，你会知道答案

加五分：
在这个很少发生的特别活动，你会得到五分

丢两分：
如果这个特别活动发生，你猜对的时候会丢两分

对手得到一分：
你不会拿到分数，反而对手会拿到一分''']
    tipntrick = [
    '''遊戲技巧!:
大部分的謎語把一些字合起來作一個大的字，所以想如果你把那些字起來，它們會作成什麼。
大部分的時候，你不會遇到特別的活動，所以不要擔心不好的特別活動會發生。
有的謎語很難，所以不要擔心如果你要跳過一個問題。
遊戲有30個謎語。''',
    '''游戏技巧!:
大部分的谜语把一些字合起来作一个大的字，所以想如果你把那些字起来，它们会作成什么。
大部分的时候，你不会遇到特别的活动，所以不要担心不好的特别活动会发生。
有的谜语很难，所以不要担心如果你要跳过一个问题。
游戏有30个谜语。''']



    pscore1 = 0
    pscore2 = 0
    counter = 0
    ans = [0, 0, 0, 0]
    my_bool = True

    create_events(spec_event)



    words = intro()

    if words == 'trd':
        ch_set = 0
    elif words == 'sim':
        ch_set = 1
    riddle_type = intro2(ch_set, instruction, event_ins, tipntrick)
    if riddle_type == '成語':
        if ch_set == 0:
            riddles = trd_chengyu_rid
            Answers = trd_chengyu_ans
        else:
            riddles = sim_chengyu_rid
            Answers = sim_chengyu_ans
    elif riddle_type == '字謎':
        if ch_set == 0:
            riddles = trd_riddles
            Answers = trd_Answers
        else:
            riddles = sim_riddles
            Answers = sim_Answers

    while my_bool:
        my_event = random.choice(spec_event)

        my_bool2 = True
        pscore1 += ans[2]
        pscore2 += ans[3]

        riddle_val = select_riddle(riddles)
        riddle_str = riddle_val[0]
        riddle_int = riddle_val[1]

        while my_bool2:
            #print('event is:')
            #print(my_event)
            event_ob = eventclass(my_event, Answers, riddle_int)
            event_ob.give_ans()

            player = select_player(counter)
            ans = guess(player, riddle_str, riddle_int, Answers, counter)
            my_bool2 = ans[0]
            counter = ans[1]
            if my_bool2 == False:
                pscore1, pscore2 = event_ob.min2opp(pscore1, pscore2, counter)
                pscore1, pscore2 = event_ob.min2(pscore1, pscore2, counter)
                pscore1, pscore2 = event_ob.plus5(pscore1, pscore2, counter)
                pscore1, pscore2 = event_ob.plus1opp(pscore1, pscore2, counter)



        #print(my_bool2)
        #print('length')
        #print(len(riddles))
        my_bool = end_game_check(riddles)
    winner(pscore1, pscore2)


if __name__ == '__main__':
    main()
