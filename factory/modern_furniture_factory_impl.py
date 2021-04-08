from factory.furniture_factory import FurnitureFactory
from furniture.modern_chair_impl import ModernChairImpl
from furniture.modern_sofa_impl import ModernSofaImpl


class ModernFurnitureFactoryImpl(FurnitureFactory):
    @staticmethod
    def createChair():
        return ModernChairImpl

    @staticmethod
    def createSofa():
        return ModernSofaImpl