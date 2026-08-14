def get_feedback(word,inp):

    if word==inp:
        pass
    result=""
    tempDic={}
    for char in range(5):
        if inp[char]==word[char]:
            result+="2"
            try:
                tempDic[inp[char]]+=1
            except:
                tempDic[inp[char]]=1
        else:
            result+="0"

    temp=result
    result=""
    for char in range(5):
        if temp[char]=="0":
            tempDicCount=0
            try:
                tempDicCount=tempDic[inp[char]]
            except:
                pass
            worC=word.count(inp[char])
            if worC>tempDicCount:
                result+="1"
                tempDic[inp[char]]=tempDicCount+1
                continue
        result+=temp[char]
    return result