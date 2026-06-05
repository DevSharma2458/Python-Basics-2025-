def reverse_string(s):
    s = list(s)
    i,j = 0, len(s)-1
    # i-> Start  
    # j-> End
    # if left char is special move i
    # if right char is special move j
    # if both are normal swap

    while i < j:
        if not s[i].isalnum():
            i+=1
        elif not s[j].isalum():
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i+=1
            j+=1

    return "".join(s)