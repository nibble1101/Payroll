
class Employee:

    def __init__(self, id, name, title, points, tipPool=True, gratuityPool=True, tipPercent=0.95, gratuityPercent=0.75, processingCharge=0.95):

        self.id = id
        self.name = name
        self.title = title
        self.points = points
        self.tipPool = tipPool
        self.gratuityPool = gratuityPool
        self.tipPercent = tipPercent
        self.gratuityPercent = gratuityPercent
        self.processingCharge = processingCharge