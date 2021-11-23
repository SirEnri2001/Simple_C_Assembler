from typing import Optional

addr_offset = 0
su_id = 0


class Field:
    id: str
    size: int
    type: str

    def __init__(self, id, type, size):
        self.id = id
        self.size = size
        self.type = type

    def __repr__(self):
        return "<Field id='" + self.id + "' type='" + self.type + "'/>"


class LocalField(Field):
    def __init__(self, id, type, size, offset):
        super().__init__(id, type, size)
        self.offset = offset

    def __repr__(self):
        return "<LocalField id='" + self.id + "' type='" + self.type + "' address='"+str(self.offset)+"'/>"


class StaticField(Field):
    def __init__(self, id, type, size):
        super().__init__(id, type, size)


class StorageUnit:
    field_table = {}
    static_list = []
    constant_list = []
    sub_storageUnit = []

    def __repr__(self):
        sub = ""
        for su in self.sub_storageUnit:
            sub+=str(su)
        return "<Storage id=\""+str(self._su_id)+"\" fields=\""+str(self.field_table)+"\">"+sub+"</Storage>"

    def __init__(self, caller: Optional):
        global su_id
        self.caller = caller
        self._su_id = su_id
        self.field_table = {}
        self.size = 0
        self.sub_storageUnit = []
        if caller is not None:
            self.static_list = caller.static_list
            self.constant_list = caller.constant_list
            caller.sub_storageUnit.append(self)
        su_id = su_id + 1

    def add_field(self, field: Field):
        try:
            if self.field_table[field.id] is not None:
                print(field.id + " already been declared")
            else:
                self.field_table[field.id] = field
        except KeyError:
            self.field_table[field.id] = field

    def add_local(self, id, type, size):
        field = LocalField(id, type, size, self.size)
        self.size = self.size + size
        self.add_field(field)

    def get(self, id: str) -> Optional[Field]:
        field = None
        try:
            field = self.field_table[id]
        except KeyError:
            if self.caller is not None:
                field = self.caller.get(id)
        if field is None:
            print("Undefined Identifier of " + id)
        return field

    def add_constant(self, id: str, type: str, size: int):
        field = Field(id, type, size)
        self.static_list.append(field)
        self.add_field(field)

    def add_static(self, id: str, type: str, size: int):
        field = Field(id, type, size)
        self.static_list.append(field)
        self.add_field(field)
