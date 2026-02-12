def check_feel_good(n, s):
    temp = 0
    s = s.replace(" ","")
    s= s.strip(" ")
    if len(s) != n:
        n = len(s)
    for i in range(n):
        if s[i] == "a":
            temp += 1
            continue
        elif s[i] == "e":
            temp += 1
            continue
        elif s[i] == "i":
            temp += 1
            continue
        elif s[i] == "o":
            temp += 1
            continue
        elif s[i] == "u":
            temp += 1
            continue

    # vowel = "aeiou"
    # temp = sum(1 for ch in s if ch in vowel)
        
    if temp >= int(n/2):
        print("Feel Good")
    else:
        print("Feel Bad")

num = int(input("Enter the string length: "))
word = input("Ente the String: ")

check_feel_good(n=num, s=word)