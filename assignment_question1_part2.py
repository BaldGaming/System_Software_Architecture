class Problem:
    def __init__(self,name, description):
        self.name = name
        self.description = description

    def BusinessLinkage(self, businessId):
        self.business = Business(businessId)

    def addSeverity(self, severityScore):
        self.severityScore = severityScore
        print(f"The severity score is {self.severityScore}")

class Advantage:
    def __init__(self,name, description):
        self.name = name
        self.description = description

    def BusinessLinkage(self, businessId):
        self.business = Business(businessId)

    def addScore(self, advantageScore):
        self.advantageScore = advantageScore
        print(f"The score is {self.advantageScore}")

class Business:
    business = None
    def __new__(cls, businessId):
        if cls.business is not None:
              return cls.business
        cls.business = super().__new__(cls)
        return cls.business
    def __init__(self, businessId):
        self.id = businessId


class MyProblem(Problem):
    def __init__(self, name, description, platform):
        super().__init__(name, description)
        self.platform = platform
        self.retryAttempts = 0

class MyAdvantage(Advantage):
    def __init__(self, name, description, ordersReceived, ordersCompleted):
        super().__init__(name, description)
        self.ordersReceived = ordersReceived
        self.ordersCompleted = ordersCompleted

class Data:
    def __init__(self, businessId):
        self.businessId = businessId
        self.info = []

        # Create the raw objects
        problem1 = MyProblem("Error #1", "Connection Lost", "Wolt")
        problem2 = MyProblem("Error #2", "Connection Failure", "TenBis")
        advantage = MyAdvantage("Advantage", "Table Report", 25, 15)

        # Wrap them in adapters and add to list
        self.info.append(problemAdapter(problem1))
        self.info.append(problemAdapter(problem2))
        self.info.append(advantageAdapter(advantage))


# Adapter for problems
class problemAdapter:
    def __init__(self, problem):
        self.problem = problem # Stores the original object
    # Translates "updateScore" into "addSeverity"
    def updateScore(self, severityScore):
        self.problem.addSeverity(severityScore)


# Adapter for advantages
class advantageAdapter:
    def __init__(self, advantage):
        self.advantage = advantage # Stores the original object

    # Translates "updateScore" into "addScore"
    def updateScore(self, advantageScore):
        self.advantage.addScore(advantageScore)


def main():
    data = Data(69)

    for i in data.info:
        i.updateScore(5)
        print("\n")
main()