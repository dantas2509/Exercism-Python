def slices(series, length):
    subs = []
    if 0 < length <= len(series):
        return [series[p:p + length] for p in range(len(series) + 1) if p + length <= len(series)]
    else:
        raise ValueError('Amount of characters not supported')



