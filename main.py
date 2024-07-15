def oneDigit(num):
    match num:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000
    
    
def intToRoman(num):
    temp = num
    answer = ""

    while temp > 0:
        if str(temp)[0] in ('4', '9'): #use subtractive form
            if temp >= 900:
                answer += "CM"
                temp = temp - 900
            elif temp >= 400:
                answer += "CD"
                temp = temp - 400
            elif temp >= 90:
                answer += "XC"
                temp = temp - 90
            elif temp >= 40:
                answer += "XL"
                temp = temp - 40
            elif temp >= 9:
                answer += "IX"
                temp = temp - 9
            elif temp >= 4:
                answer += "IV"
                temp = temp - 4
        else:
            if temp >= 1000:
                answer += "M"
                temp = temp - 1000
            elif temp >= 500:
                answer += "D"
                temp = temp - 500
            elif temp >= 100:
                answer += "C"
                temp = temp - 100
            elif temp >= 50:
                answer += "L"
                temp = temp - 50
            elif temp >= 40:
                answer += "XL"
                temp = temp - 40
            elif temp >= 10:
                answer += "X"
                temp = temp - 10
            elif temp >= 9:
                answer += "IX"
                temp = temp - 9
            elif temp >= 5:
                answer += "V"
                temp = temp - 5
            elif temp >= 4:
                answer += "IV"
                temp = temp - 9
            elif temp >= 1:
                answer += "I"
                temp = temp - 1

    return answer


#Example 1:
#Input: 
num = 3749
print(intToRoman(num))
#Output: "MMMDCCXLIX"
#Explanation:
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

#Example 2:
#Input: 
num = 58
print(intToRoman(num))
#Output: "LVIII"
#Explanation:
# 50 = L
#  8 = VIII

#Example 3:
#Input: 
num = 1994
print(intToRoman(num))
#Output: "MCMXCIV"
#Explanation:
# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
