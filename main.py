from factory.modern_furniture_factory_impl import ModernFurnitureFactoryImpl
from factory.victorian_furniture_factory_impl import VictorianFurnitureFactoryImpl
from client import Client

modern_factory = Client(ModernFurnitureFactoryImpl)
victorian_factory = Client(VictorianFurnitureFactoryImpl)

modern_saloon = modern_factory.orderSaloon()
victorian_saloon = victorian_factory.orderSaloon()

print(modern_saloon)
print(victorian_saloon)

print("---MODERN FURNITURE DESCRIPTION---")
modern_factory.describeChair()
modern_factory.describeSofa()
print("---VICTORIAN FURNITURE DESCRIPTION---")
victorian_factory.describeChair()
victorian_factory.describeSofa()

