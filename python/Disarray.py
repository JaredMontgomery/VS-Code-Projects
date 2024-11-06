class Disarray(list):
    """
    Like a list, but it's reshuffled every time an item is added. You've heard
    of data structures. Now, get ready for data destructures.
    """

    def append(self, obj: object) -> None:
        """
        Append an object to the end of the list. However, the list is shuffled
        every time.

        Time complexity - O(N), where N is [len(self)].
        Space complexity - O(N).
        """

        from random import shuffle

        super().append(obj)

        shuffle(self)

if __name__ == "__main__":
    dis = Disarray()

    for i in range(4):
        dis.append(i)

    # Random!
    print(dis)