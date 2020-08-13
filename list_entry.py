class ListEntry:
    def __init__(self, name, rank1, rank2):
        self.name = name
        self.rank1 = rank1
        self.rank2 = rank2

    def __repr__(self):  
        return "ListEntry name:% s rank 1:% s rank 2: % s" % (self.name, self.rank1, self.rank2)  
    
    def __str__(self):  
        return "ListEntry % s % s % s" % (self.name, self.rank1, self.rank2)