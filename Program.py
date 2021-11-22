from typing import Optional

base_addr = 0

class Field:
    id: str
    size: int
    type: str
    def __init__(self, id,type,size):
        self.id = id
        self.size = size
        self.type = type

    def __repr__(self):
        return "<field id='"+self.id+" type='"+self.type+"'/>"


class StorageUnit:
    field_table = {}
    static_list = []

    def add_field(self,field: Field):
        try:
            self.field_table[field.id].append(field)
        except KeyError:
            self.field_table[field.id] = [field]

    def add_declared(self, id, type,size):
        field = Field(id,type,size)
        self.add_field(field)

    def get(self, id) -> Optional[Field]:
        field = self.field_table.get(id)
        if field is None:
            print("Undefined ID "+id)
            return None
        return field

    def add_constant(self, id: str, type: str, size: int):
        field = Field(id, type, size)
        self.static_list.append(field)
        self.add_field(field)

    def add_static(self, id: str, type: str,size:int):
        field = Field(id,type,size)
        self.static_list.append(field)
        self.add_field(field)

