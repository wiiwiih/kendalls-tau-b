import kendalls_tau_b
import math
import scipy.stats as st


def mann_kendall(entries):
    n_conc, n_disconc = kendalls_tau_b.count_concordant_pairs(entries)

    v = calc_v(entries)

    z = (n_conc - n_disconc) / math.sqrt(v)

    p = 2 * (1 - st.norm.cdf(abs(z)))

    return z, p

def calc_v(entries):
    ranks_n1, ranks_n2 = rank_helper(entries)

    tie_adj1 = calc_tie_adjustment(ranks_n1)
    tie_adj2 = calc_tie_adjustment(ranks_n2)

    n = len(entries)

    v0 = n * (n - 1) * (2 * n + 5)
    v1 = calc_v1(ranks_n1, ranks_n2, n)
    v2 = calc_v2(ranks_n1, ranks_n2, n)

    v = (v0 - tie_adj1 - tie_adj2) / 18 + v1 +v2

    return v


def calc_v1(ranks1, ranks2, n):
    r1 = v1_helper(ranks1)
    r2 = v1_helper(ranks2)

    v1 = r1 * r2 / (2 * n * (n - 1))
    return v1
            
def v1_helper(ranks):
    help = 0
    for i in ranks:
        if i > 1:
            help += i * (i - 1)
    return help

def calc_v2(ranks1, ranks2, n):
    r1 = v2_helper(ranks1)
    r2 = v2_helper(ranks2)

    v2 = r1 * r2 / (9 * n * (n - 1) * (n - 2))
    return v2

def v2_helper(ranks):
    help = 0
    for i in ranks:
        if i > 1:
            help += i * (i - 1) * (i - 2)
    return help

def calc_tie_adjustment(ranks):
    tie_adjustment = 0
    for i in ranks:
        if i > 1:
            tie_adjustment += i * (i - 1) * (2 * i + 5)

    return tie_adjustment

def rank_helper(entries):
    ranks_n1 = [0] * len(entries)
    ranks_n2 = [0] * len(entries)

    for entry in entries:
        ranks_n1[entry.rank1] +=1
        ranks_n2[entry.rank2] +=1

    return ranks_n1, ranks_n2