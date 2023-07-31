class Player:
    # 1:N with strategies, which are effectively functions from InfoSet -> Strategy
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name
