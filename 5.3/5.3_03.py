class Error:

    def __repr__(self):
        raise ValueError


func(Error())