class Account:
    def __init__(self, act_num, value):
        self.act_num = act_num
        self.value = value

    def __str__(self):
        return f"{self.act_num} @ ${self.value}"
