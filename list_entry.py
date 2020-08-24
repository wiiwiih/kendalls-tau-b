# A class for list entries in two ranked lists
# Each object includes the name of the ranked item and it's rank in both rankings
class ListEntry:
    def __init__(self, name, rank1, rank2, rank3, rank4):
        self.name = name
        self.rank1 = rank1
        self.rank2 = rank2
        self.rank3 = rank3
        self.rank4 = rank4

    def __repr__(self):  
        return "ListEntry % s % s % s % s % s" % (self.name, self.rank1, self.rank2, self.rank3, self.rank4)
    
    def __str__(self):  
        return "ListEntry % s % s % s % s % s" % (self.name, self.rank1, self.rank2, self.rank3, self.rank4)