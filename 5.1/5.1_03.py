class RedButton:

    def __init__(self, cnt=0):
        self.cnt = cnt

    def click(self):
        self.cnt += 1
        print("Тревога!")

    def count(self):
        return self.cnt