# Funções que substituem métodos python
def split(line, char=",", i=0):
    if i >= len(line):
        return [line[:-1]]
    if line[i] == char:
        return [line[:i]] + split(line[i+1:], char, 0) 
    else:
        return split(line, char, i+1)
    
def join(string_list, i=0):
    if i >= len(string_list):
        return ""
    
    txt_join = string_list[i]
    return txt_join + join(string_list, i+1)

