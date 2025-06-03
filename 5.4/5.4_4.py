from datetime import datetime


class ParentTypeError(TypeError):
    pass


class ParentRecursionError(RecursionError):
    pass


class Comment:

    def __init__(self, name, date, text, approved=False, edited=False, linked=None):
        if not all(isinstance(arg, str) for arg in [name, date, text]):
            raise TypeError

        try:
            date_part, time_part = date.split()
            datetime.strptime(date_part, "%d-%m-%Y")
            datetime.strptime(time_part, "%H:%M")
        except Exception:
            raise ValueError

        self.name = name
        self.date = date_part
        self.time = time_part
        self.text = text
        self.approved = approved
        self.edited = edited
        self.linked = linked if linked is not None else []

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
        if not isinstance(text, str):
            raise TypeError
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
        if parent is not None:
            self.set_parent(parent)

    def __repr__(self):
        return f'SubComment({self.name}, {self.date}, {self.time}, {repr(self.parent)})'

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        if not isinstance(parent, (Comment, SubComment)):
            raise ParentTypeError

        if self._contains(parent):
            raise ParentRecursionError

        if self.parent and self in self.parent.linked:
            self.parent.linked.remove(self)

        self.parent = parent
        if self not in parent.linked:
            parent.linked.append(self)