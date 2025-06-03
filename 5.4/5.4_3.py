class Comment:
    def __init__(self, name, date, text, approved=False, edited=False, linked=None):
        if linked is None:
            linked = []
        date, time = date.split()
        self.name = name
        self.date = date
        self.time = time
        self.text = text
        self.approved = approved
        self.edited = edited
        self.linked = linked

    def __str__(self):
        return self.text + "\n" + f"[{self.name} ({self.date} {self.time})]" + "\n"

    def __repr__(self):
        return f'Comment({self.name}, {self.date}, {self.time})'

    def __iadd__(self, other):
        if isinstance(other, SubComment):
            other.set_parent(self)
        return self

    def __lt__(self, other):
        return self._contains(other)

    def __gt__(self, other):
        return other._contains(self)

    def _contains(self, comment):
        for sub in self.linked:
            if sub is comment or sub._contains(comment):
                return True
        return False

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

    def get_sub_comments(self):
        return self.linked


class SubComment(Comment):
    def __init__(self, name, date, text, parent=None, approved=False, edited=False):
        super().__init__(name, date, text, approved, edited)
        self.parent = None
        if parent:
            self.set_parent(parent)

    def __repr__(self):
        return f'SubComment({self.name}, {self.date}, {self.time}, {repr(self.parent)})'

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        if self.parent and self in self.parent.linked:
            self.parent.linked.remove(self)
        self.parent = parent
        if self not in parent.linked:
            parent.linked.append(self)