
class Employee:

    def __init__(self, id, name, type, points, tipPool=True, gratuityPool=True, tipPercent=0.95, gratuityPercent=0.75, processingCharge=0.95):

        self.id = id
        self.name = name
        self.type = type
        self.points = points
        self.tipPool = tipPool
        self.gratuityPool = gratuityPool
        self.tipPercent = tipPercent
        self.gratuityPercent = gratuityPercent
        self.processingCharge = processingCharge