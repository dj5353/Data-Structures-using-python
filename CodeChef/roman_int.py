def RomanToInt(num):
    pair={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
    key = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    if num in pair.keys():
        return(pair[num])
    else:
        sum = 0
        for i in range(len(num)-1):
            if pair[num[i]] < pair[num[i+1]]: 
                sum = sum - pair[num[i]]
            else:
                sum = sum + pair[num[i]]
        sum += pair[num[-1]]
        return sum

print(RomanToInt("V"))

