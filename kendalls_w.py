import scipy.stats as st

def calculate(ranks1, ranks2, ranks3, ranks4):
    if len(ranks1) != len(ranks2) or len(ranks2) != len(ranks3) or len(ranks3) != len(ranks4):
        print("The ranking must be of equal length")
        quit()

    cor_rank1, t1 = correct_ties(ranks1)
    cor_rank2, t2  = correct_ties(ranks2)
    cor_rank3, t3  = correct_ties(ranks3)
    cor_rank4, t4  = correct_ties(ranks4)

    t_sum = t1 + t2 + t3 + t4

    r_sum = calculate_r_sum(cor_rank1, cor_rank2, cor_rank3, cor_rank4)

    n = len(ranks1)

    m = 4

    w = (12 * r_sum - 3 * m ** 2 * n * (n + 1) ** 2) / (m ** 2 * n * (n ** 2 - 1) - m * t_sum)

    f, p = test_significance(w, m, n)

    return w, f, p


def correct_ties(ranks):
    corrected = [0] * len(ranks)
    t = 0
    helper = [0] * (len(ranks) + 1)


    for rank in ranks:
        helper[rank] += 1

    n = 0
    for i in range(0, len(helper)):
        n_rank = helper[i]

        if n_rank > 1:
            t += (n_rank**3 - n_rank)

        helper[i] = (n + 1 + n + n_rank) / 2
        n += n_rank

    for i in range(0, len(ranks)):
        corrected[i] = helper[ranks[i]]

    return corrected, t

def calculate_r_sum(ranks1, ranks2, ranks3, ranks4):
    r_sum = 0

    for i in range(0, len(ranks1)):
        r = ranks1[i] + ranks2[i] + ranks3[i] + ranks4[i]
        r_sum += r ** 2

    return r_sum

def test_significance(w, m, n):
    f = w * (m - 1) / (1 - w)

    df1 = n - 1 - (2 / m)
    df2 = (m - 1) * df1

    p = 1 - st.f.cdf(f, df1, df2)

    return f, p