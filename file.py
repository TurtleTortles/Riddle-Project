print('這是個猜謎語的遊戲')
print('我們有30個謎語')
while True:
    #ends game
    if len(sim_riddles) == 0:
        print('你都猜完了！')
        break
    print('這是個猜謎語的遊戲')
    print('我們有30個謎語')
    while True:
        #ends game
        if len(sim_riddles) == 0:
            print('你都猜完了！')
            break

    #selects the riddle number
    riddle_num = random.randint(0, len(sim_riddles) - 1)
    #selects the riddle based on the number .pop() for no repeats
    riddle = sim_riddles.pop(riddle_num)
    #next 2 lines is debug code
    #print(riddle_num)
    #print(Answers[riddle_num])
    while True:
        print(riddle + ':')
        ans = input()
        if ans == Answers[riddle_num]:
            print('你猜對了！')
            #makes sure that the riddle's index and the answer's index is the same
            del Answers[riddle_num]
            break
        else:
            print('你猜錯了！')
