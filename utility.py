#https://github.com/bahuse/csci-wk12-utility
#Brady Huseman
#CSCI 102 - Section C
#Week 11 - Part B
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
        print('OUTPUT player not found')
    elif error==1:
        player=players[location]
        score=scores[location]
        print('OUTPUT {0} got a score of {1}'.format(player, score))

def Union(list1, list2):
    output_list=list1+list2
    return output_list

def Intersection(list1, list2):
    match=[]
    for ele in list1:
        for ele2 in list2:
            if ele==ele2:            
                match.append(ele)
    return match

def NotIn(list1, list2):
    notin=[]
    match=[]
    for ele in list1:
        for ele2 in list2:
            if ele==ele2:            
                match.append(ele)
    for ele in list1:
        if ele not in match:
            notin.append(ele)
    return notin
