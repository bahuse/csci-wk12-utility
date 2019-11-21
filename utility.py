
def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(name):
    lst=[]
    openfile=open(name, 'r')
    readfile=openfile.readlines()
    for line in readfile:
        lines=line[:-1]
        lst.append(lines)
    print('OUTPUT', lst)
    openfile.close

def UpdateString(string, replace, index):
    newstring=string[:index] + replace + string[(index+1):]
    print('OUTPUT', newstring)

def FindWordCount(text, check):
    count=0
    text=text.split(' ')
    for word in text:
        if word==check:
            count+=1
    return count

def ScoreFinder(players, scores, search):
    search=search.upper()
    error=0
    for i in range(len(players)):
        check=players[i].upper()
        if check==search:
            location=i
            error=1
    if error==0:
        print('OUTPUT player not found)
    elif error==1:
        player=players[location]
        score=scores[location]
        print('OUTPUT {0} got a score of {1}'.format(player, score))

def Union(hi)

more
