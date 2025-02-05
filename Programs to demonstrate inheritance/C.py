# Exception class for ITRaid
class ITRaid(Exception):
    def __init__(self, errmsg):
        self.errmsg = errmsg

    def __str__(self):
        return f"ITRaid Exception: {self.errmsg}"

# Base class Person
class Person:
    def __init__(self, name, status):
        self.name = name
        self.__status = status  # Private member

    def getStatus(self):
        return self.__status

    def ITRaid(self):
        return self.doITRaid()

# Class Politician
class Politician:
    def getLIMIT(self):
        return 5_00_00_000  # 5 crores

    def doITRaid(self):
        if self.hasProperty():
            return self.evaluateProperty()
        else:
            return 0

# Class Professional
class Professional:
    def getLIMIT(self, annual_income):
        return 10 * annual_income

    def doITRaid(self):
        if self.hasDeposit():
            return self.getDeposit()
        else:
            return 0

# Derived class Minister
class Minister(Person, Politician):
    def __init__(self, name, status, party_name, asset_value):
        super().__init__(name, status)
        self.party_name = party_name
        self.asset_value = asset_value  # Dictionary with property name and value

    def hasProperty(self):
        return bool(self.asset_value)

    def evaluateProperty(self):
        return sum(self.asset_value.values())

# Derived class Officer
class Officer(Person, Professional):
    def __init__(self, name, status, qualification, monthly_income, deposit_value):
        super().__init__(name, status)
        self.qualification = qualification
        self.monthly_income = monthly_income
        self.deposit_value = deposit_value  # Dictionary with account number and deposit amount

    def hasDeposit(self):
        return bool(self.deposit_value)

    def getDeposit(self):
        return sum(self.deposit_value.values())

# Main program to test the classes
def main():
    persons = [
        Minister("John Doe", "Minister", "ABC Party", {"Property1": 2_00_00_000, "Property2": 3_50_00_000}),
        Minister("Jane Smith", "Minister", "XYZ Party", {}),
        Officer("James Bond", "Officer", "MBA", 12_00_000, {"Acc1": 50_00_000, "Acc2": 60_00_000}),
        Officer("Emily Davis", "Officer", "PhD", 15_00_000, {})
    ]

    for person in persons:
        try:
            raid_value = person.ITRaid()
            if isinstance(person, Minister):
                if raid_value > person.getLIMIT():
                    raise ITRaid("You have Disproportionate Assets")
                else:
                    print(f"{person.name}: Good!")
            elif isinstance(person, Officer):
                if raid_value > person.getLIMIT(person.monthly_income * 12):
                    raise ITRaid("Your Deposits are Locked")
                else:
                    print(f"{person.name}: Good!")
        except ITRaid as e:
            print(e)

# Run the main function
if __name__ == "__main__":
    main()
