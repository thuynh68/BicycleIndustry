class Bicycle(object):
  def __init__(self, modelName, weight, productionCost):
    self.modelName = modelName
    self.weight = weight
    self.productionCost = productionCost
    
class BikeShop(object):
  def __init__(self, name, margin):
    self.name = name
    self.inventory = {}
    self.profits = 0.00
    self.margin = margin
          
  def getBikeCost(self, bike):
    return bike.productionCost * ((100.00 + self.margin) / 100.00)
  
  def getAffordableBikes(self, customer):
    affordableBikes = []
    for bike in self.inventory.keys():
      if self.getBikeCost(bike) <= customer.budget:
        affordableBikes.append(bike)
    
    return affordableBikes
  
  def purchaseBike(self, customer, bike):
    if customer.budget > self.getBikeCost(bike):
      bikeInventory = self.inventory[bike]
      bikeInventory = bikeInventory - 1
      self.inventory[bike] = bikeInventory
      customer.budget = customer.budget - self.getBikeCost(bike)
      self.profits = self.profits + (self.getBikeCost(bike) * (self.margin / 100))
      return True
    else:
      return False
  
class Customer(object):
  def __init__(self, name, budget, canBuy, canOwn):
    self.name = name
    self.budget = budget
    self.canBuy = canBuy
    self.canOwn = canOwn
      