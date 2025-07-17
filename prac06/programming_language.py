


class ProgrammingLanguage:
    def __init__(self,name,type,reflection,year):
        self.name = name
        self.type=type
        self.year=year
        self.reflection = reflection

    def is_dynamic(self):
        return self.type == 'Dynamic'

    def __str__(self):
        return (f"{self.name}, {self.type} Typing, Reflection={self.reflection},"
                f" First appeared in {self.year}")