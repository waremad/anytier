import random

# .txtファイルから辞書を返す
def txt_dict(path):
    with open(path) as f:
        txt = []
        for s in f.readlines():
            txt.append(s.rstrip())
    out = {}
    for i in txt:
        now = (i.split(":"))[1].split(",")
        if "" in now:
            now.remove("")
        out[(i.split(":"))[0]] = now
    return out

# 相性辞書からカウント用の辞書を返す
def make_outdict(dic):
    out = {}
    for i in list(dic.keys()):
        out[i] = 0
    return out

# 辞書のキーからランダムに１つ返す
def randomdic(dic):
    return random.choice(list(dic.keys()))

# ランダムに次にする
def nextkey(dic,self):
    if dic[self] == []:
        return ""
    return random.choice(dic[self])

# 85%の確率でTrue
def continuee():
    return random.random() < 0.85

# 辞書の中の最小値を返す
def dicmin(dic):
    return min(list(dic.values()))

# 辞書を降順にソート
def dictsort(dict):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    z = list(zip( list(dict.values()),list(dict.keys())))
    z = sorted(z,reverse=True)
    out = {}
    for i in z:
        out[i[1]] = i[0]
    return out

#ランク付けされて、降順にソードされた辞書データをn個のtierに分ける
def tierrank(n,dict):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    #print("|",n,dict,"|")
    if n > len(list(dict.keys())):
        ValueError("n > len(list(dict.keys()))",n,">",len(list(dict.keys())))
    if n == 0:
        ValueError("n==0")
    if n%2 == 0:
        m = n//2
        #print("dict,dict.values(),list(dict.values())",dict,dict.values(),list(dict.values()))
        maxv = max(list(dict.values()))
        minv = min(list(dict.values()))
        long = len(list(dict.values()))
        if long%2 == 0:
            mid = list(dict.values())[long//2] + list(dict.values())[long//2-1]
            mid = mid/2 
        else:
            mid = list(dict.values())[long//2 - 1 + long%2]
        overs = []
        unders = []
        for i in list(dict.keys()):
            if dict[i] < mid:
                unders.append(i)
            else:
                overs.append(i)
        #print("overs,unders",overs,unders)
        #print("mid,m",mid,m)
        orange = (maxv - mid)/m
        urange = (mid - minv)/m
        #print("orange,urange",orange,urange)
        outovers = []
        outunders = []
        for i in range(m):
            outovers.append([])
            outunders.append([])
        if urange == 0:
            outunders = [unders]
        else:
            for i in unders:
                #print("(dict[i]-minv)//urange",(dict[i]-minv)//urange)
                """
                prnit("V--------------------")
                prnit("unders",unders)
                prnit("outunders",outunders)
                print("i,dict[i]",i,dict[i])
                print("minv,dict[i]-minv",minv,dict[i]-minv)
                prnit("urange,(dict[i]-minv)//urange",urange,(dict[i]-minv)//urange)
                prnit("^--------------------")
                prnit("Bf outunders",outunders)
                prnit(-1-int((dict[i]-minv)//urange))
                """
                outunders[-1-int((dict[i]-minv)//urange)].append(i)
                #prnit("Af outunders",outunders)
                
        if orange == 0:
            outovers = [overs]
        else:
            for i in overs:
                #print("int((dict[i]-mid)//orange)",int((dict[i]-mid)//orange))
                if dict[i] == maxv:
                    outovers[0].append(i)
                else:
                    outovers[-1-int((dict[i]-mid)//orange)].append(i)
        #print("outovers,outunders",outovers,outunders)
        return outovers + outunders
    else:
        wout = tierrank(n*2,dict)
        out = []
        for i in range(n):
            out.append(wout[i*2]+wout[i*2+1])
        return out

#dic[self] += 1
ls = txt_dict("in.txt")
con = make_outdict(ls)
while not(dicmin(con) >= 10000):
    do = True
    now = randomdic(ls)
    while do:
        con[now] += 1
        if nextkey(ls,now) == "":
            con[now] += 1
            do = False
        else:
            if continuee():
                now = nextkey(ls,now)
            else:
                do = False
print(dictsort(con))

# ティアランクをつける
rankls = tierrank(4,dictsort(con))

# 出力ファイルを初期化
with open("out.txt",mode="w",encoding="utf-8") as f:
    f.writelines("")

# 出力
for i in range(len(rankls)):
    with open("out.txt",mode="a",encoding="utf-8") as f:
        f.write("\n"+str(i+1)+"\n")
    for j in rankls[i]:
        with open("out.txt",mode="a",encoding="utf-8") as f:
            f.write(str(j)+":"+str(con[j])+"\n")

