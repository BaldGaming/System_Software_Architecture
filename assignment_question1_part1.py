class Problem:
    def __init__(self,name, description):
        self.name = name
        self.description = description

    def BusinessLinkage(self, businessId):
        self.business = Business(businessId)

    def AddSeverity(self, severityScore):
        self.severityScore = severityScore
        print(f"The severity score is {self.severityScore}\n")


class Advantage:
    def __init__(self,name, description):
        self.name = name
        self.description = description

    def BusinessLinkage(self, businessId):
        self.business = Business(businessId)

    def AddScore(self, advantageScore):
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


# This class describes a situation where an order was places but didn't show up in OrderHub because of a faulty connection.
class MyProblem(Problem):
    def __init__(self, name, description, platform):
        super().__init__(name, description)
        self.platform = platform
        self.retryAttempts = 0

    # This method describes an attempt to reconnect to OrderHub
    # Severity levels are defines from 10 to 0, being the highest and lowest respectively.
    def reconnectOrder(self):
        self.retryAttempts += 1
        print(f"Attempting to reconnect to {self.platform}...")

        # Sets the severity level in accordance to the amount of attempts made to reconnect.
        if self.retryAttempts > 3:
            print("Failed to connect after 3 tries.. Escalating severity.")
            self.AddSeverity(10)
        else:
            self.AddSeverity(3)

# This class describes the advantages of using OrderHub's services.
class MyAdvantage(Advantage):
    def __init__(self, name, description, ordersReceived, ordersCompleted):
        super().__init__(name, description)
        self.ordersReceived = ordersReceived # Describes the amount of received orders.
        self.ordersCompleted = ordersCompleted # Describes the amount of completed orders.

    def AddScore(self, score):
        super().AddScore(score)

    # This method describes the amount of received and completed orders.
    def orderReport(self):
        return f"OrderHub currently holds {self.ordersReceived} orders and reports {self.ordersCompleted} completed orders."

# This class describes our business, partners that work with us and the sites current status.
class MyBusiness(Business):
    def __new__(self, businessId, partners, status):
        return super().__new__(self, businessId)

    def __init__(self, businessId, partners, status):
        if not hasattr(self, 'initialized'):
            super().__init__(businessId)
            self.businessName = "OrderHub"
            self.partners = partners
            self.status = status
            self.initialized = True

    def businessDescription(self):
        return f"{self.businessName} links orders from: {', '.join(self.partners)}.\nCurrent status: {self.status}"

def main():
    business = MyBusiness(1, ["Wolt", "TenBis", "Mishloha"], "Active")
    print(business.businessDescription())

    print("\n--- Problem: ---")
    syncIssue = MyProblem("Error #1", "Connection Lost", "Wolt")
    syncIssue.BusinessLinkage(business.id)

    syncIssue.reconnectOrder() # Reconnection attempt
    syncIssue.reconnectOrder() # Reconnection attempt
    syncIssue.reconnectOrder() # Reconnection attempt
    syncIssue.reconnectOrder() # Triggers severity

    print("--- Advantages: ---")
    analytics = MyAdvantage("Advantage #1", "Table Report", 25, 15)
    analytics.BusinessLinkage(business.id)
    print(analytics.orderReport())
    analytics.AddScore(60)
main()