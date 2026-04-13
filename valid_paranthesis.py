def is_valid(s: str) -> bool:
    lst  =  list(s)
    i = 0
    while i < len(s):
        if lst[i] == "(":
            end = s.find(")")
            lst.pop

    if lst == []:
        return True
    else:
        return False


s = input("Enter Value: ")
print(is_valid(s))
