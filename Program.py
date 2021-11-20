from typing import Optional

base_addr = 0

class Field:
    id: str
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "FieldId:"+id


class ProgramContext:
    field_table = {}
    def add_declared(self, id, type):
        field = Field(id)
        self.field_table[id] = field

    def get(self, id) -> Optional[Field]:
        field = self.field_table.get(id)
        if field is None:
            print("Undefined ID "+id)
            return None
        return field