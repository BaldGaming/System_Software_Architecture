class Data:
    def __init__(self, businessId):
        self.businessId = businessId 
        self.info = []

        # Create the raw objects
        problem1 = MyProblem("Error #1", "Connection Lost", "Wolt")
        problem2 = MyProblem("Error #2", "Connection Lost", "TenBis")
        advantage1= MyAdvantage("Advantage #1", "Table Report", 51, 49)

        # Wrap them in adapters
        self.info.append(ProblemAdapter(problem1))
        self.info.append(ProblemAdapter(problem2))
        self.info.append(AdvantageAdapter(advantage1))

# Adapter for problems
class ProblemAdapter:
    def __init__(self, problem):
        self.problem = problem # Stores the original object
        
    # Translates "updateScore" into "addSeverity"
    def updateScore(self, severityScore):
        self.problem.addSeverity(severityScore)


# Adapter for advantages
class AdvantageAdapter:
    def __init__(self, advantage):
        self.advantage = advantage # Stores the original object

    # Translates "updateScore" into "addScore"
    def updateScore(self, advantageScore):
        self.advantage.addScore(advantageScore)
        
def main():
    business = MyBusiness(1, ["Wolt", "TenBis", "Mishloha"], "Active")
    
    data = Data(business.id)
        
    for i in data.info:
        i.updateScore(5)
        print('\n')
main()