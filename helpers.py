import list_entry

# Creates a list of ListEntry-objects from lists that contain the names of the items and the corresponding rankings
def init_entries(names, ranks1, ranks2, ranks3 = [], ranks4 = []):
    if len(names) != len(ranks1) or len(names) != len(ranks2):
        print("Lists containing names and ranks must be the same length")
        quit()
    
    entries = []

    for name in names:
        index = names.index(name)
        entry = list_entry.ListEntry(name, ranks1[index], ranks2[index], ranks3[index], ranks4[index])
        entries.append(entry)

    return entries
