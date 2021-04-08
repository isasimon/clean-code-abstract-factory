from factory.furniture_factory import FurnitureFactory


class Client:
    __slots__ = 'furniture_factory'

    def __init__(self, furniture_factory: FurnitureFactory):
        self.furniture_factory = furniture_factory

    def orderSaloon(self):
        chair = self.furniture_factory.createChair()
        sofa = self.furniture_factory.createSofa()
        return chair, sofa

    def describeChair(self):
        chair = self.furniture_factory.createChair()
        print("The chair has legs: {}. You can sit on it: {}"
              .format(chair.hasLegs(), chair.sitOn()))

    def describeSofa(self):
        sofa = self.furniture_factory.createSofa()
        print("The sofa is made of leather: {}. You can sit on it: {}"
              .format(sofa.isLeather(), sofa.sitOn()))

