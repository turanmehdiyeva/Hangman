def Hangman():
    x = np.random.choice(wordslist,1)
    print(x[0])
    g = '-'*len(x[0])
    s = ''
    lst = []
    lst[:0] = x[0]
    arr1 = np.array(lst)
    for i in range(10):
        print(f'Welcome, you have to guess a word of {len(x[0])} {g.upper()} letters\nYou have {10-i} lives')
        a = input('Enter a letter: ')
        s+=a
        if a in x[0]:
            item_index = np.where(arr1==a)
            for i in item_index[0]:
                g = rep(g,i,a)
            print(f'Yay correct letter\n {g.upper()}\nUsed letter: {s.upper()}')
        else:
            print(f'Wrong answer\nUsed letters: {s.upper()}')
        if (g.count('-'))==0:
            return 'congrats'
        else:
            continue
    print(f'Game ended\nYour word was: {x[0].upper()}')  
