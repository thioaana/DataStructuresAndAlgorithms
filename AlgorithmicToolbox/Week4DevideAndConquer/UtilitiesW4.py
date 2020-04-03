def MergeSort(seq) :
    l = len(seq)
    if l == 1 : return seq
    mid = int(l / 2)
    seqLeft = MergeSort(seq[:mid]) # without mid
    seqRight = MergeSort(seq[mid :]) # with mid
    seqResult = Merge(seqLeft, seqRight)
    return seqResult

def Merge(seqL, seqR) :
    # seqL and seqR are already sorted
    sRes = []
    while len(seqL) != 0 and len(seqR) != 0 :
        if seqL[0] <= seqR[0] : sRes.append(seqL.pop(0))
        else : sRes.append(seqR.pop(0))
    sRes.extend(seqL)
    sRes.extend(seqR)
    return sRes
