import kendalls_tau_b
import mann_kendall
import helpers

NAMES = ["a", "b", "c", "d", "e"]
RANKS1 = [1, 2, 2, 2, 3]
RANKS2 = [3, 2, 1, 1, 2]

def main():
    entries = helpers.init_entries(NAMES, RANKS1, RANKS2)

    tau = kendalls_tau_b.kendalls_tau_b(entries)

    z, p = mann_kendall.mann_kendall(entries)

    print("--------------------------------------")
    print("Kendall Tau-b and Kendall Mann's test:")
    print("--------------------------------------")
    print("tau = " + str(tau))
    print("z = " + str(z))
    print("p = " + str(p))
    print("--------------------------------------")

if __name__ == "__main__":
    main()