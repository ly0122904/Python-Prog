__author__ = 'w0122904'

subnetList = []
ipAddress = "122.0.0.0"
varClName ="A"    # string

def oneLineIP(aString,subnetSize,aValue):
    bbStr = aString+"."+str(aValue)
    aValue += subnetSize        # subnet size
    bbStr2 = aString+"."+str(aValue-1)
    bbResult = bbStr+" - "+bbStr2

    return bbResult

varSnSize = 32 # integer
varNumSN = 2048  # integer number of subnets
ipAddressPrefix = []

ipList = ipAddress.split(".")

# Prefix depending on the network class
if varClName == "C":
    varPrefix = 3
if varClName == "B":
    varPrefix = 2
if varClName == "A":
    varPrefix = 1
# Save prefix in a list for future use
for i in range(varPrefix):
    ipAddressPrefix.append(ipList[i])

aaStr = ".".join(ipAddressPrefix)

# for class C
a = 0
x = 0
y = 0
if varClName == "C":
    for j in range (12):  #varNumSN):
        bOneLine = oneLineIP(aaStr,varSnSize,a)
        a += varSnSize
        subnetList.append(bOneLine)
if varClName == "B":
    bbStr = aaStr+"."+str(ipList[2])
    for j in range (100):  #varNumSN): <-should be
        if a < 256:
            bOneLine = oneLineIP(bbStr,varSnSize,a)
            a += varSnSize
            subnetList.append(bOneLine)
            print(j,bOneLine)
        else:
            x += int(a/256)
            print("x=",x)
            ipList[2]= x
            a = int(a%256)
            bbStr = aaStr+"."+str(ipList[2])
if varClName == "A":
    bbStr = aaStr+"."+str(ipList[1])+"."+str(ipList[2])
    for j in range (100):  #varNumSN): <-should be
        if a < 256:
            bOneLine = oneLineIP(bbStr,varSnSize,a)
            a += varSnSize
            subnetList.append(bOneLine)
            print(j,bOneLine)
        else:
            if x < 256:
                x += int(a/256)
                print("x=",x)
                ipList[2]= x
                a = int(a%256)
                bbStr = aaStr+"."+str(ipList[1])+"."+str(ipList[2])
            else:
                y += int(x/256)
                ipList[1] = y
                x = int (x%256)
                bbStr = aaStr+"."+str(ipList[1])+"."+str(ipList[2])



#print (subnetList)


    #subnetList.append(bbResult)
    #bbStr = ""
print("End")


"""

    if varClName == "B":
        varPrefix = 2
    if varClName == "A":
        varPrefix = 1



    for i in range (3,varPrefix-1,-1):
# for class C
        a=0
        i=3
        if a < 256:
            bbStr = aaStr+"."+str(a)
            a += varSnSize        # subnet size
            bbStr2 = aaStr+"."+str(a-1)
            bbResult = bbStr+" - "+bbStr2
            print(bbResult)
        else:
            a=int(a%256)
            b=int(a/256)

        #if a >= 256:


    print("===========")

    #subnetList.append(bbResult)
    bbStr = ""
print (subnetList)



# FOR C CLASS
subnetList = []
ipAddress = "192.168.3.0"
varClName ="C"    # string
varNumIP =256  # integer
varNumSN =8  # integer
ipAddressPrefix = []

ipList = ipAddress.split(".")

if varClName == "C":
    varPrefix = 3

for i in range(varPrefix):
    ipAddressPrefix.append(ipList[i])

aaStr = ".".join(ipAddressPrefix)
varNum = int(varNumIP/varNumSN)
a = 0
for j in range (5): #varNumSN):
    for i in range (varPrefix,varPrefix+1):
        ipList[i] = a
        bbStr = aaStr+"."+str(ipList[i])
        a += varNum
        bbStr2 = aaStr+"."+str(a-1)
        bbResult = bbStr+" - "+bbStr2

    subnetList.append(bbResult)
    bbStr = ""
print (subnetList)
"""



"""
varClassName = "A"
varBinSM = "11111111.11111111.11111111.11100000"
if varClassName == "A":
    aStr = varBinSM[9:]
if varClassName == "B":
    aStr = varBinSM[18:]
if varClassName == "C":
    aStr = varBinSM[27:]
countOne = aStr.count("1")
numSN = 2**countOne
print(numSN)
"""
"""
astring = "11111111.11111111.11111111.11100000"
aList = astring.split(".")
aNumList = []
b = []
for a in aList:
    a = int(a,2) # convert to decimal number
    b.append(str(a))
stringSM = ".".join(b)
numSM = astring.count("1")
print (stringSM + "  or /"+str(numSM))

#a=input("ip: ")
#print(int("1111", 2))
"""
"""
def ff(hostNum): # calculate subnet size
    b  = bin(int(hostNum))[2:] # b is a binary string
    varNum = 2**len(b)
    return varNum
def aa(hostNum): # calculate subnet mask
    aValue = ff(hostNum)
    aBinStr = bin(aValue)[2:]
    binNum1 = int("11111111111111111111111111111111",2) #32 binary
    binNum2 = int(aBinStr,2)
    binNum3 = bin(binNum1- binNum2 + 1)
    ms = binNum3[2:]
    aSMstring = ms[:8]+"."+ms[8:16]+"."+ms[16:24]+"."+ms[24:]
    print(aSMstring)

    return aSMstring


"""
"""
# take in a string of ip address, return a list contain number of ip address
def convertStrList(ipAddString): # take in a string of ip address, return a list contain number of ip address
    aList = ipAddString.split(".")
    bList = []
    for aa in aList:
        bb = int(aa)
        bList.append(bb)
    return bList
def convertBinary(a): # Get a number return a binary string
    b = bin(a)[2:]
    c=[]
    if len(b)< 8:
        for j in range(0,8-len(b)):
            c.append("0")
    result=c+list(b)
    print(result)
    return "".join(result)
def CalculateBinaryAddress(ipAddress): # returns a string
    ipAddNumList = convertStrList(ipAddress)
    varA = []
    for i in ipAddNumList:
        aa = convertBinary(i)
        varA.append(aa)

    return ".".join(varA)


def convertStrList (ipAddString):
    aList = ipAddString.split(".")
    bList=[]
    for aa in aList:
        bb = int(aa)
        bList.append(bb)
    ipAddNumList = bList
    return ipAddNumList

def CalculateDecimalAddress(ipAddress): # returns an integer
        ipAddNumList = convertStrList(ipAddress)

        ipAddNumList.reverse()
        print(ipAddNumList)
        total=0

        for i in range(0,4):

            print(i,ipAddNumList[i])
            total += ipAddNumList[i]*(256**i)
            print(total)

        return total

def CalculateBinaryAddress(ipAddress):
    ipAddNumList = convertStrList(ipAddress)

"""

"""
def convertBinary(f): # Get a number
    a=int(f)
    b=[]
    s=[]
    sth=[]
    checkA = 1
    while checkA > 0:
        midN=a/2
        if midN >= 1:
            aB=a%2
            b.append(str(aB))
        else:
            checkA = 0
            b.append(str(a))

        a=int(midN)


    b.reverse()
    if len(b)< 8:

        for j in range(0,8-len(b)):
            s.append("0")
    sth=s+b
    return "".join(sth)
def convertHexNum(aNum): # Give a number sting return a hex value str
    result = 0
    for i in range(4):
        result += int(aNum[i])*2**(3-i)
    if result == 10:
        result = "A"
    elif result == 11:
        result = "B"
    elif result == 12:
        result = "C"
    elif result == 13:
        result = "D"
    elif result == 14:
        result = "E"
    elif result == 15:
        result = "F"
    else:
        result = str(result)
    return result
def convertHexOctet(aNum): # Give a number Return a string
    aStr = convertBinary(aNum)
    aList = list(aStr)
    a1List=[]
    a2List=[]
    for i in range(0,4):
        a1List.append(aList[i])
    for i in range(4,8):
        a2List.append(aList[i])
    b1 = "".join(a1List)
    b2 = "".join(a2List)
    c1 = convertHexNum(b1)
    c2 = convertHexNum(b2)
    resultList = [c1,c2]
    print(resultList)

    return "".join(resultList)
"""
"""
# Hex number give a string return a string
a=input("a: ")
b=hex(int(a))
c = b[2:]
print(c.upper())

# Binary : give a string return a string
b = bin(int(a))
c = b[2:]
print(c)
"""