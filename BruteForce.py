def BruteKProposals(k, dates):
    if len(dates) < k:
        return None
    return KProposals(k, dates, [False for i in dates], list())


def Fit(item, itemlist):
    for prop in itemlist:
        for i in item:
            for j in prop:
                if i == j:
                    return False

    return True


def KProposals(k, dates, checkdates, taken):
    if len(taken) == k:
        return taken
    for i in range(len(dates)):
        if Fit(dates[i], taken) and not checkdates[i]:
            newTaken = taken.copy()
            newTaken.append(dates[i])
            checkdates[i] = True
            newcheck = checkdates.copy()
            return KProposals(k, dates, newcheck, newTaken)

    oldcheck = checkdates.copy()
    return KProposals(k, dates, oldcheck, taken[:len(taken) - 1])


dates = [[1, 3, 2],

         [6, 7, 8],
         [2, 4, 5],
         [7, 9, 10],
         [3, 8, 10],
         [11, 9, 12]]
print(BruteKProposals(3, dates))
