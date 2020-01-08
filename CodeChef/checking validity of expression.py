class stack():
    def valid_expression(self, exp):
        l_paren = "{[("
        r_paren = "}])"
        list = []
        for i in exp:
            if i in l_paren:
                list.insert(0,i)
            if i in r_paren:
                if list == []:
                    print("Invalid Expression")
                    exit()
                else:
                    if self.match_parenthesis(list[0],i):
                         list.pop(0)
                    else:
                        print("Invalid Expression")
                        exit()

        if list == []:
            print("Balanced Parenthesis")
        else:
            print("Invalid Parenthesis")

    def match_parenthesis(self, l_par, r_par):
        if "(" == l_par and ")" == r_par:
            return True
        if "{" == l_par and "}" == r_par:
            return True
        if "[" == l_par and "]" == r_par:
            return True
        return False
    

obj = stack()
obj.valid_expression("[({})]")