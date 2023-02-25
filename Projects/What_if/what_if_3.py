# Create Battle function that takes self and other as arguments
def battle(self, other):
    # If attack of self > other, then increase min and max attack by 1
    if self.attack < other.attack:
        self.min_attack += 1
        self.max_attack += 1
        other.min_attack += 0
        other.max_attack += 0
        return self

def battle(self, other):
    if self.attack > other.attack:
        self.max_attack += 1
        self.min_attack += 1
        other.max_attack += 0
        other.min_attack += 0
        return self

def battle(self, other):
    if self.attack > other.attack:
        self.max_attack += 1
        self.min_attack += 1
        other.max_attack += 0
        other.min_attack += 0
        return self

def battle(self, other):
    if self.attack > other.attack:
        self.max_attack += 1
        self.min_attack += 1
        other.max_attack += 0
        other.min_attack += 0
        return self
    elif self.attack < other.attack:
        self.max_attack += 0
        self.min_attack += 0
        other.max_attack += 1
        other.min_attack += 1
        return other
    else:
        return "Draw"
