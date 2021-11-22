from typing import Optional

base_addr = 0
su_id = 0
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
    const_list = []
    caller = None

    def __str__(self):
        return "<StorageUnit id="+str(self._su_id)+' field='+str(self.field_table)+'> called by '+str(self.caller)

    def __init__(self, caller:Optional):
        global su_id
        self.caller = caller
        self._su_id = su_id
        self.field_table = {}
        su_id = su_id+1

    def add_field(self, field: Field):
        try:
            if self.field_table[field.id] is not None:
                print(self.field_table[field.id])
            else:
                self.field_table[field.id] = field
        except KeyError:
            self.field_table[field.id] = field

    def add_declared(self, id, type, size):
        field = Field(id,type,size)
        self.add_field(field)

    def get(self, id: str) -> Optional[Field]:
        field = None
        try:
            field = self.field_table[id]
        except KeyError:
            if self.caller is not None:
                field = self.caller.get(id)
        if field is None:
            print("Undefined Identifier of "+ id)
        return field

    def add_constant(self, id: str, type: str, size: int):
        field = Field(id, type, size)
        self.static_list.append(field)
        self.add_field(field)

    def add_static(self, id: str, type: str,size:int):
        field = Field(id,type,size)
        self.static_list.append(field)
        self.add_field(field)

