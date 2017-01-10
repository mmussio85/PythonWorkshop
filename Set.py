class Set(object):

    def __init__(self, elements):
        self.elements = list()
        for i in elements:
            if i not in self.elements:
                self.elements.append(i)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def diff(self, setB):
        return [a for a in self.elements if a not in setB.elements]

    def intersection(self, setB):
        return [a for a in self.elements if a in setB.elements]

    def isIncluded(self, setB):
        return reduce(lambda x, y: x and y, map(lambda x: True if x in setB.elements else False, self.elements), True)

    def diffSim(self, setB):
        return self.diff(setB) + setB.diff(self)

    def prodCart(self, setB):
        return [(a, b) for a in self.elements for b in setB.elements]

    def pot(self):
        result = [[]]
        for i in self.elements:
            newSets = [x + [i] for x in result]
            result.extend(newSets)
        return result

    def __str__(self):
        return " ".join(str(self.elements))



