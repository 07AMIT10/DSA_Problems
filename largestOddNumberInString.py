def maxOdd( s):
    maxm = []
    for i in range(-1, -(len(s)), -1):
        # if s[i]=="":
        #     pass
            
        if int(s[:i])%2!=0:
            print(s[:i+1])
            # if len(s)==1:
            #     maxm.append(int(s))
                
            # else:
            # maxm.append(int(s[:i]))
            # print(maxm)
        # if len(s)==1:
        #     return(s)
        # else:
        #      return(max(maxm))
        # print(a)
    # return a
    # return maxm
        
print(maxOdd('123453298523434322334'))
print(maxOdd('9'))