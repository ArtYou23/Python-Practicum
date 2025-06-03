class Comment:

    def __init__(self, name, date, text, approved=False, edited=False):
        date, time = date.split()
        self.name = name
        self.date = date
        self.time = time
        self.text = text
        self.approved = approved
        self.edited = edited

    def __str__(self):
        return self.text + "\n" + f"[{self.name} ({self.date} {self.time})]" + "\n"

    def get_author(self):
        return self.name

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_text(self):
        return self.text

    def approve(self):
        self.approved = True

    def is_approved(self):
        return self.approved

    def set_text(self, text):
        self.text = text
        self.approved = False
        self.edited = True

    def is_edited(self):
        return self.edited