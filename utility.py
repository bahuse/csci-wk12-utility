
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
