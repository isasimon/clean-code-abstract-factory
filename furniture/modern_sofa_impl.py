from furniture.sofa import Sofa


class ModernSofaImpl(Sofa):
    @staticmethod
    def isLeather():
        return False

    @staticmethod
    def sitOn():
        return True