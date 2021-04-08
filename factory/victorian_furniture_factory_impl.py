from factory.furniture_factory import FurnitureFactory
from furniture.victorian_chair_impl import VictorianChairImpl
from furniture.victorian_sofa_impl import VictorianSofaImpl


class VictorianFurnitureFactoryImpl(FurnitureFactory):
    @staticmethod
    def createChair():
        return VictorianChairImpl

    @staticmethod
    def createSofa():
        return VictorianSofaImpl
