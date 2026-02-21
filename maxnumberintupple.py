def find_max_score(scores_tuple):
    max = scores_tuple[0]
    for i in scores_tuple:
        if i > max:
            max = i
    print(max)

tup = (45,78,92,65,88)

find_max_score(tup)