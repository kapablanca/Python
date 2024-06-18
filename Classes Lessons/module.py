class MaxSizeList(object):

    def __init__(self, val):
        self.list = [None] * val
        self.length = len(self.list)

    def push(self, item):
        self.list.pop(0)
        self.list.append(item)

    def get_list(self):
        return self.list
