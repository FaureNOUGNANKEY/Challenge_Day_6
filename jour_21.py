# 💻 Exercises: Day 21
# Exercises: Level 1
# 1.
class statistics:
    def __init__(self,data):
        self.data = data 
    def count(self):
        return len(self.data)
    def sum (self):
        return sum(self.data)
    def min (self):
        return min(self.data)
    def max (self):
        return max(self.data)
    def range (self):
        return max(self.data)- min(self.data)
    def mean (self):
        return self.sum() / self.count()
    def median (self):
        lst_sort = sorted(self.data)
        n = len(self.data)
        if n %2 == 0 :
            midle1 = lst_sort[n//2-1]
            midle2 = lst_sort[n//2]
            median = (midle1 + midle2)/2
        else :
            median = lst_sort[n//2]
        return median
    def mode (self):
        from collections import Counter
        compt = Counter(self.data)
        fequence_max = max(compt.values())
        mode = [val for val ,fqt in compt.items() if fqt == fequence_max]
        return mode
    def variance (self):
        n = len(self.data)
        mean = self.mean()
        somme_ecart_carree = sum((x - mean)**2 for x in self.data)
        variance = somme_ecart_carree/n-1
        return variance
    def std (self):
        from math import sqrt
        return sqrt(self.variance())
    def freq_dist(self):
        from collections import Counter
        freq = Counter(self.data)
        return sorted([(v, k) for k, v in freq.items()], reverse=True)
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = statistics(ages)
print('Count:', data.count()) 
print('Sum: ', data.sum()) 
print('Min: ', data.min()) 
print('Max: ', data.max()) 
print('Range: ', data.range())
print('Mean: ', data.mean()) 
print('Median: ', data.median()) 
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.variance()) 
print('Frequency Distribution: ', data.freq_dist())

# Exercices:Level 2
class PersonAccount:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = {}   # key = description, value = amount
        self.expenses = {}  # key = description, value = amount
    def total_income(self):
        return sum(self.incomes.values())
    def total_expense(self):
        return sum(self.expenses.values())
    def account_info(self):
        return f"{self.first_name} {self.last_name} → Total Income: {self.total_income()} | Total Expenses: {self.total_expense()} | Balance: {self.account_balance()}"
    def add_income(self, description, amount):
        self.incomes[description] = amount
    def add_expense(self, description, amount):
        self.expenses[description] = amount
    def account_balance(self):
        return self.total_income() - self.total_expense()

account = PersonAccount("Faure", "NOUGNANKEY")
account.add_income("Salary", 2000000)
account.add_income("Freelance", 500000)
account.add_expense("Rent", 600000)
account.add_expense("Internet", 15000)

print(account.account_info())