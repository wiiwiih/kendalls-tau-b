import kendalls_tau_b
import math
import scipy.stats as st

# Do a Kendall-Mann test for a list of ListEntries
def test(entries):
    # Count the number of concordant and disconcordant pairs
    n_conc, n_disconc = kendalls_tau_b.count_concordant_pairs(entries)

    # Calculate the "scaling parameter"
    v = calc_v(entries)

    # Calculate z-value
    z = (n_conc - n_disconc) / math.sqrt(v)

    # Get p-palue with the normal distribution cumulative function
    p = 2 * (1 - st.norm.cdf(abs(z)))

    return z, p

# Calculate the scaling parameter for Mann-Kendall test
def calc_v(entries):
    # Make lists with the amounts of items in each rank
    ranks_n1, ranks_n2 = rank_helper(entries)

    # Calculate parameters for tied pairs in both rankings
    tie_adj1 = calc_tie_adjustment(ranks_n1)
    tie_adj2 = calc_tie_adjustment(ranks_n2)

    # The number of ranked items
    n = len(entries)

    v0 = n * (n - 1) * (2 * n + 5)

    # More accommodation for tied pairs
    v1 = calc_v1(ranks_n1, ranks_n2, n)
    v2 = calc_v2(ranks_n1, ranks_n2, n)

    # Calculate the scaling parameter
    v = (v0 - tie_adj1 - tie_adj2) / 18 + v1 +v2

    return v

# Calculate the first parameter to factor in tied pairs
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

# Calculate the second parameter to factor in tied pairs
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

# Calculate adjustments to factor in tied pairs
def calc_tie_adjustment(ranks):
    tie_adjustment = 0
    for i in ranks:
        if i > 1:
            tie_adjustment += i * (i - 1) * (2 * i + 5)

    return tie_adjustment


# Make lists with the amounts of items in each rank, with indexes signifying the rank
# Example: 
# Ranking 1, 2, 2, 3, 4 becomes the following list: [0, 1, 2, 1, 1, 0]
def rank_helper(entries):
    ranks_n1 = [0] * (len(entries) + 1)
    ranks_n2 = [0] * (len(entries) + 1)

    for entry in entries:
        ranks_n1[entry.rank1] +=1
        ranks_n2[entry.rank2] +=1

    return ranks_n1, ranks_n2