
trans_matrix = {('A','A'):'A', ('A','B'):'B', ('A','C'):'C', ('A','D'):'D', ('B','A'):'B', ('B','B'):'A', ('B','C'):'D', ('B','D'):'C',('C','A'):'C', ('C','B'):'D', ('C','C'):'A', ('C','D'):'B',('D','A'):'D', ('D','B'):'C', ('D','C'):'B', ('D','D'):'A'}

def pmix(s, k):
    # s: protein ring
    # k: number of seconds
    chr_array = [ltr for ltr in s]
    #every iteration is seen as a second
    for sec in range(k):
        for pos in range(len(s)):
            chr_array[pos] = trans_matrix[(chr_array[pos],chr_array[(pos+1)%len(s)])]
        print("".join(chr_array))
    return "".join(chr_array)

pmix("AAAADAAAADDDDDDABBBBCCCCDDDDDDDDAAADDDDDDDADDDDDDDAAACCCCBBB", 100000)
