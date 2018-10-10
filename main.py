# encoding: utf-8
import re
'''
config
'''
DictDir = 'dict.txt'
MaxLen = 6

def readDict():
    dictionary = {}
    with open(DictDir,"r") as f:
        lines = f.readlines()
        for line in lines:
            tList = line.strip().split(" ")
            dictionary[tList[0]] = [int(tList[1]),tList[2]]
    return dictionary
            #print(dictionary[tList[0]])#for test

def wordToken(strList,dic):
    s2 = ''
    if strList:
        while(strList):
            #print(s2)
            w1Len = MaxLen
            while(w1Len):
                w1List = strList[:w1Len] #if w1Len<= len(strList) else strList
                w1Len = len(w1List)
                if(w1Len == 1):
                    s2 = s2+ w1List[0]+ '/'
                    strList = strList[1:] #if len(strList)>1 else []
                    break

                else:
                    w1 = ''.join(w1List)
                    if(re.match(r"^[0-9]*$",w1)):
                        s2 =s2+ w1 + '/'
                        strList = strList[len(w1List):]
                        break
                    elif w1 in dic:
                        s2 =s2+ w1 + '/'
                        strList = strList[w1Len:]
                        break

                    else:
                        w1Len -= 1

        return s2



    else:
        #空列表
        return s2

if __name__ == '__main__':
    aDict = readDict()
    sentence = input()
    strList = list(sentence)
    res = wordToken(sentence,aDict)
    print(res)


