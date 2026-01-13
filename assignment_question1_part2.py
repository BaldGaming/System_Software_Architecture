class Data:
    def __init__(self, businessId):
        self.businessId = businessId 
        self.info = []

        problem1 = MyProblem("Error #1", "Connection Lost", "Wolt")
        problem2 = MyProblem("Error #2", "Connection Lost", "TenBis")
        advantage1= MyAdvantage("Advantage #1", "Table Report", 51, 49)

        self.info.append(ProblemAdapter(problem1))
        self.info.append(ProblemAdapter(problem2))
        self.info.append(AdvantageAdapter(advantage1))

# Adapter for problems
class ProblemAdapter:
    def __init__(self, problem):
        self.problem = problem

    def updateScore(self, severityScore):
        self.problem.AddSeverity(severityScore)


# Adapter for advantages
class AdvantageAdapter:
    def __init__(self, advantage):
        self.advantage = advantage

    def updateScore(self, advantageScore):
        self.advantage.AddScore(advantageScore)
        
def main():
    business = MyBusiness(1, ["Wolt", "TenBis", "Mishloha"], "Active")
    
    data = Data(business.id)
    
    print("--- Running Example: ---")
    for i in data.info:
        i.updateScore(5)
        print('\n')
main()