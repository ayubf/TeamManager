import locale



class Coach:
    def __init__(self, name: str, team:str, age: int, exp: int, record: list, contract: list, note: str):
        self.name = name
        self.age = age
        self.exp = exp
        self.record = record
        self.contract = contract
        self.salary = contract[0]/contract[1]
        self.note = note
        self.team = team
    
    def getSummary(self):
        return "{} is a {} year old coach that is paid {} a year and has a {}-{} record with {} years of experience".format(self.name, self.age, self.salary, self.record[0], self.record[1], self.exp)

    def pack(self):
        locale.setlocale(locale.LC_ALL, '')
        res = {}
        res["Name"] = self.name
        res["Age"] = self.age
        res["Team"] = self.team
        res["Experience"] = self.exp
        res["Record"] = "{}-{}".format(self.record[0], self.record[1])
        res["Contract"] = "{0} per {0} years".format(locale.currency(self.contract[0], self.contract[1]))
        res["Salary"] = self.salary
        res["Note"] = self.team
        return res
