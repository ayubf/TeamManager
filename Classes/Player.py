class Player:
    def __init__(self, name: str, age: int, jNum: int, vert: int, ppg: int, apg: int, rpg: int, mpg: int, bpg: int, draftyr: str, contract: list, isCaptain: bool, pos: str, note: str):
        self.name = name
        self.age = age
        self.jNum = jNum
        self.vert = vert
        self.stats = {"ppg": ppg, "apg": apg, "rpg": rpg, "mpg":mpg, "bpg": bpg}
        self.draftyr = draftyr
        self.contract = contract
        self.salary = contract[0]/contract[1]
        self.isCaptain = isCaptain
        self.pos = pos
        self.note = note

    def pack(self):
        res = {}
        res["Name"] = self.name
        res["Age"] = self.age
        res["Jersey Number"] = self.jNum
        res["Vertical Jump"] = self.vert
        res["Points Per Game"] = self.stats["ppg"]
        res["Assists Per Game"] = self.stats["apg"]
        res["Rebounds Per Game"] = self.stats["rpg"]
        res["Minutes Per Game"] = self.stats["mpg"]
        res["Blocks Per Game"] = self.stats["bpg"]
        res["Draft Year"] = self.draftyr
        res["Contract"] = "${} for {} years".format(self.contract[0], self.contract[1])
        res["Salary"] = self.salary
        res["Captain"] = self.isCaptain
        res["Position"] = self.pos
        res["Note"] = self.note
        return res
    
    def getSummary(self):
        return "{} plays {} and is {} years of age. {} was drafted in {} and is being paid {} a year to play {} years".format(self.name, self.pos, self.age, " ".split(self.name)[0], self.draftyr, self.salary, self.contract[1])
    