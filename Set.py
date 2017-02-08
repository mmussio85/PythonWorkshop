class Set(object):

    def __init__(self, elements):
        self.elements = list()
        for i in elements:
            if i not in self.elements:
                self.elements.append(i)

    def add(self, element):
        '''Add an element into the set
        Args:
            element: The element.
        '''

        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        '''Remove an element from the set
        Args:
            element: The element.
        '''

        if element in self.elements:
            self.elements.remove(element)

    def diff(self, setB):
        '''Difference between two sets
        Args:
            setB: The set passed as a parameter.
        Returns:
            A list containing the difference between the two sets.
        '''

        return [a for a in self.elements if a not in setB.elements]

    def intersection(self, setB):
        '''Intersection between two sets
        Args:
            setB: The set passed as a parameter.
        Returns:
            A list containing the elements present in both sets.
        '''

        return [a for a in self.elements if a in setB.elements]

    def isIncluded(self, setB):
        '''Verify id the set includes the setB
        Args:
            setB: The set passed as a parameter.
        Returns:
            True if the set is included in setB, otherwise returns false
        '''

        return reduce(lambda x, y: x and y, map(lambda x: True if x in setB.elements else False, self.elements), True)

    def diffSim(self, setB):
        '''Simetric Difference between two sets
        Args:
            setB: The set passed as a parameter.
        Returns:
            A list containing the simetric difference between the two sets.
        '''

        return self.diff(setB) + setB.diff(self)

    def prodCart(self, setB):
        '''Cartesian product between two sets
        Args:
            setB: The set passed as a parameter.
        Returns:
            A list containing each subset of the cartesian product between the two sets.
        '''

        return [(a, b) for a in self.elements for b in setB.elements]

    def pot(self):
        '''Simetric Difference between two sets
        Returns:
            A list containing the simetric difference between the two sets.
        '''

        result = [[]]
        for i in self.elements:
            newSets = [x + [i] for x in result]
            result.extend(newSets)
        return result

    def __str__(self):
        return " ".join(str(self.elements))



