
class Employee:

    """
    Description: Class holds the Employee data.

    ...

    Attributes
    ----------

    id : str
        a formatted string that signifies employee ID.
    name : str
        name of the employee.
    title : str
        job title of the employee
    points : int
        number of points held by employee in tip pool.
    tipPool : float
        amount of tip pool held by the employee.
    gratuityPool : float
        amount of gratuity pool held by employee.
    tipPercent : float
        percentage of tip pool held by the employee.
    gratuityPercent : float
        percentage of gratuity pool held by employee.
    processingCharge : float
        processing charge per card.

    Methods
    -------
    *****
    """

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