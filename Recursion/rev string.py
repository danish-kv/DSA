def rev_string(string):
    if len(string) <=1 :
        return string
    else:
        return string[-1] + rev_string(string[:-1])


print(rev_string('hello'))