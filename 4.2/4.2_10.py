def secret_replace(sss, **d_rep):
    ss = ""
    for i in sss:
        if i in d_rep:
            ss += d_rep[i][0]
            d_rep[i] = d_rep[i][1:] + d_rep[i][:1]
        else:
            ss += i
    return ss