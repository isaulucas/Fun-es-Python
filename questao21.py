def lst_to_dic(lst, dic):
    for e in lst:
        if e not in dic:
            lst.remove(e)
