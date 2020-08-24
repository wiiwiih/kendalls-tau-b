import kendalls_tau_b
import mann_kendall
import helpers
import kendalls_w

# If this is true, calculate Kendall's tau, otherwise calculate Kendall's W
TAU = False

# Names of the ranked items
NAMES = ["a", "b", "c", "d", "e"] 

# Two rankings for the items for Kendall's tau (in the same order as the names)
RANKS1 = [1, 2, 2, 3, 4]
RANKS2 = [5, 3, 2, 4, 1]

# Two more rankings for Kendall's W
RANKS3 = [1, 1, 2, 3, 3]
RANKS4 = [1, 2, 3, 4, 3]

# Calculate Kendall's tau-b, do the Kendall-Mann test and print the results
def main():
    if TAU:
        entries = helpers.init_entries(NAMES, RANKS1, RANKS2, RANKS3, RANKS4)

        tau = kendalls_tau_b.calculate(entries)

        z, p = mann_kendall.test(entries)

        print("----------------------------------------")
        print("Kendall's Tau-b and Kendall Mann's test:")
        print("----------------------------------------")
        print("tau = " + str(tau))
        print("z = " + str(z))
        print("p = " + str(p))
        print("----------------------------------------")
    else:
        w, chi_sqr, p = kendalls_w.calculate(RANKS1, RANKS2, RANKS3, RANKS4)

        print("----------------------------------------")
        print("Kendall's W:")
        print("----------------------------------------")
        print("w = " + str(w))
        print("x^2 = " + str(chi_sqr))
        print("p = " + str(p))
        print("----------------------------------------")

if __name__ == "__main__":
    main()