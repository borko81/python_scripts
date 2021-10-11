class A:
    def __init__(self) -> None:
        self.x = 0


class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.y = 1


test = B()
print(test.x, test.y)