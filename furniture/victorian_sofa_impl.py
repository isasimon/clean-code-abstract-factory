from furniture.sofa import Sofa


class VictorianSofaImpl(Sofa):
    @staticmethod
    def isLeather():
        return True

    @staticmethod
    def sitOn():
        return True