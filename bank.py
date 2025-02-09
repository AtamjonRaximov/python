class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

        
    def yechmoq(self,miqdor):
        
        if miqdor <= self.balance:
            self.balance -= miqdor
            return f"{miqdor}" " muvafaqayatli yechildi"
        return "mablag' yetarli emas"
        
        
        