import list_entry

def init_entries(names, ranks1, ranks2):
    if len(names) != len(ranks1) or len(names) != len(ranks2):
        raise Exception("Lists containing names and ranks must be the same length")
    
    entries = []

    for name in names:
        index = names.index(name)
        entry = list_entry.ListEntry(name, ranks1[index], ranks2[index])
        entries.append(entry)

    return entries