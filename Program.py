base_addr = 0

class Field:
    id: str
    mem_addr: int
    def __init__(self, id):
        self.id = id


class ProgramContext:
    field_table = {}
    def add_declared(self, id, type):
        field = Field(id)
        self.field_table[id] = field

    def get(self, id):
        return self.field_table.get(id)