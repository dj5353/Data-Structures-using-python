def valid_parenthesis(n):
    l_parren = "[{("
    r_parren = "]})"
    stack = []
    for i in n:
        if i in l_parren:
            stack.insert(0,i)
        if i in r_parren:
                if stack is None:
                    print("NoT Valid Parrenthesis")
                    exit()
                else:
                    if check_parren(stack[0],i) is True:
                        stack.pop(0)
                    else:
                        print("Not Valid Parrenthesis")
                        exit()
    if stack == []:
        print("Balanced Parrenthesis")
    else:
        print("Invalid Parrenthesis")

def check_parren(l_parren,r_parren):
    if '{' == l_parren and '}' == r_parren:
        return True
    if '[' == l_parren and ']' == r_parren:
        return True
    if '(' == l_parren and ')' == r_parren:
        return True
    else:
        return False

valid_parenthesis("{") 