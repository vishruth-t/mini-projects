
zzz = input("message: ")

def rot13(message):
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dict={}
    for i in range(0,26):
        dict[alp[i]] = i
    res = ''
    for a in message:
        if a.lower() in dict.keys():
            num = dict.get(a.lower())

            if num <= 12:
                num = num + 26
            num -=13
            for key, value in dict.items():
                if num == value:
                    if a == a.upper():
                        res += key.upper()
                    else:
                        res += key
                    break   
        else:res += a
    print(res)
    return res

rot13(zzz)
