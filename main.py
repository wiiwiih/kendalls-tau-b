import kendalls_tau_b
import mann_kendall
import helpers

# Names of the ranked items
NAMES = ["a", "b", "c", "d", "e"]

# Two rankings for the items (in the same order as the names)
RANKS1 = [1, 2, 2, 2, 3]
RANKS2 = [3, 2, 1, 1, 2]

# Calculate Kendall's tau-b, do the Kendall-Mann test and print the results
def main():
    entries = helpers.init_entries(NAMES, RANKS1, RANKS2)

    tau = kendalls_tau_b.calculate(entries)

    z, p = mann_kendall.test(entries)

    print("--------------------------------------")
    print("Kendall Tau-b and Kendall Mann's test:")
    print("--------------------------------------")
    print("tau = " + str(tau))
    print("z = " + str(z))
    print("p = " + str(p))
    print("--------------------------------------")

if __name__ == "__main__":
    main()