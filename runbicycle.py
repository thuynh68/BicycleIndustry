from bicycle import Bicycle, BikeShop, Customer

myBikeShop = BikeShop("Advanced Bike Shop", 20.0)
bike = Bicycle("Super Bike", 75, 800.00)
myBikeShop.inventory[bike] = 50
bike = Bicycle("Dirt Bike", 30, 500.00)
myBikeShop.inventory[bike] = 50
bike = Bicycle("Girl Bike", 25, 300.00)
myBikeShop.inventory[bike] = 50
bike = Bicycle("Boy Bike", 35, 95.00)
myBikeShop.inventory[bike] = 50
bike = Bicycle("Mountain Bike", 40, 250.00)
myBikeShop.inventory[bike] = 50
bike = Bicycle("Street Bike", 40, 250.00)
myBikeShop.inventory[bike] = 50

customer1 = Customer("customer1", 200.00, True, True)
customer2 = Customer("customer2", 500.00, True, True)
customer3 = Customer("customer3", 1000.00, True, True)

print "Store Inventory"
for bike in myBikeShop.inventory.keys():
  print "%s: %d" % (bike.modelName, myBikeShop.inventory[bike])
print

affordableBikes = myBikeShop.getAffordableBikes(customer1)
print customer1.name
for bike in affordableBikes:
  print bike.modelName 
print
myBikeShop.purchaseBike(customer1, bike)
print "Name of bike bought: " + bike.modelName
print "Cost of bike: %5.2f" % myBikeShop.getBikeCost(bike)
print "Customer budget after purchsase: %5.2f" % customer1.budget
print
  
affordableBikes = myBikeShop.getAffordableBikes(customer2);
print customer2.name
for bike in affordableBikes:
  print bike.modelName 
print
myBikeShop.purchaseBike(customer2, bike)
print "Name of bike bought: " + bike.modelName
print "Cost of bike: %5.2f" % myBikeShop.getBikeCost(bike)
print "Customer budget after purchsase: %5.2f" % customer2.budget
print

affordableBikes = myBikeShop.getAffordableBikes(customer3);
print customer3.name
for bike in affordableBikes:
  print bike.modelName
print
myBikeShop.purchaseBike(customer3, bike)
print "Name of bike bought: " + bike.modelName
print "Cost of bike: %5.2f" % myBikeShop.getBikeCost(bike)
print "Customer budget after purchsase: %5.2f" % customer3.budget
print

print "Remaining inventory of store: "
for bike in myBikeShop.inventory.keys():
  print "Bike Model: " + bike.modelName
  print "Amount left: %d" % myBikeShop.inventory[bike]
print "Profit from sales: %5.2f" % myBikeShop.profits