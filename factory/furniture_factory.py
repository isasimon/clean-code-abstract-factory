from abc import ABCMeta


class FurnitureFactory(ABCMeta):
    @staticmethod
    def createChair():
        pass

    @staticmethod
    def createSofa():
        pass
