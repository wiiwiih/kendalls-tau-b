import math

def kendalls_tau_b(entries):
    n_conc, n_disconc = count_concordant_pairs(entries)
    n_ties1, n_ties2 = count_ties(entries)

    #print("Concordant " + str(n_conc) + ", disconcordant " + str(n_disconc))
    #print("Ties 1 " + str(n_ties1) + ", ties 2 " + str(n_ties2))

    n_entries = len(entries)
    n_pairs = n_entries * (n_entries - 1) / 2
    
    #print("Entries " + str(n_entries))
    #print("Pairs " + str(n_pairs))

    tau = (n_conc - n_disconc) / math.sqrt((n_pairs - n_ties1) * (n_pairs - n_ties2))

    return tau
    

# Count concordant and disconcordant pairs in the rankings
def count_concordant_pairs(entries):
    n_conc = 0 # number of concordant pairs
    n_disconc = 0 # number of disconcordant pairs

    for entry1 in entries:
        for entry2 in entries[entries.index(entry1) + 1:]:
            # If the entries are in the same order in both rankings, increase the number of concordant pairs
            if entry1.rank1 > entry2.rank1 and entry1.rank2 > entry2.rank2:
                n_conc += 1
            elif entry1.rank1 < entry2.rank1 and entry1.rank2 < entry2.rank2:
                n_conc += 1
            elif entry1.rank1 == entry2.rank1 or entry1.rank2 == entry2.rank2:
                pass # Tied pairs are neither concordant or disconcordant
            # If the entries are in different orders in the rankings, increase the number of disconcordant pairs
            else:
                n_disconc += 1

    return n_conc, n_disconc

# Count tied pairs in each ranking
def count_ties(entries):
    n_ties1 = 0 # Number of tied pairs in ranking 1
    n_ties2 = 0 # Number of tied pairs in ranking 2

    for entry1 in entries:
        for entry2 in entries[entries.index(entry1) + 1:]:
            if entry1.rank1 == entry2.rank1:
                n_ties1 += 1
            if entry1.rank2 == entry2.rank2:
                n_ties2 += 1

    return n_ties1, n_ties2

