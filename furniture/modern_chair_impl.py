from furniture.chair import Chair


class ModernChairImpl(Chair):
    @staticmethod
    def hasLegs():
        return False
