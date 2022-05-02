class Sort():
    currentSortOrder: int

    def __init__(self, currentSortOrder):
        self.currentSortOrder = currentSortOrder

    def bubble_sort_ascending(self, array, attr):
        for i in range(0, len(array)):
            for j in range(i + 1, len(array)):
                if(getattr(array[i], attr) > getattr(array[j], attr)):
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp

    def bubble_sort_descending(self, array, attr):
        for i in range(0, len(array)):
            for j in range(i + 1, len(array)):
                if(getattr(array[i], attr) < getattr(array[j], attr)):
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
