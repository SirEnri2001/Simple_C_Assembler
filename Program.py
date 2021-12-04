from typing import Optional

addr_offset = 0
su_id = 0


class Field:
    id: str
    size: int
    type: str

    def __init__(self, id, type_list:list, size):
        self.id = id
        self.size = size
        self.type_list = type_list
        self.fieldType = "Field"

    def __repr__(self):
        return "<"+self.fieldType+" id='" + self.id + "' type='" + str(self.type_list) + "'/>"


class LocalField(Field):
    def __init__(self, id, type_list:list, size, offset):
        super().__init__(id, type_list, size)
        self.fieldType='Local'
        self.offset = offset


class ParamField(LocalField):
    def __init__(self, id, type_list:list, size, offset):
        super().__init__(id, type_list, size,offset)
        self.fieldType='Param'


class StaticField(Field):
    def __init__(self, id, type_list:list, size):
        super().__init__(id, type_list, size)
        self.fieldType='Param'


class FuncField(Field):
    def __init__(self, id, type_list:list):
        super().__init__(id, type_list, 0)
        self.fieldType='Func'


class StorageUnit:
    field_table = {}
    static_list = {}
    constant_list = {}
    sub_storageUnit = []
    func_calling_space = 0
    param_offset = 0
    def __repr__(self):
        sub = ""
        for su in self.sub_storageUnit:
            sub+=str(su)
        return "<Storage id=\""+str(self._su_id)+"\" size=\""+str(self.size)+"\">"+sub+"</Storage>"

    def __init__(self, caller: Optional):
        global su_id
        self.caller = caller
        self._su_id = su_id
        self.field_table = {}
        self.size = 0
        self.func_calling_space = 0
        self.sub_storageUnit = []
        self.param_offset = 0
        if caller is not None:
            self.static_list = caller.static_list
            self.constant_list = caller.constant_list
            caller.sub_storageUnit.append(self)
        su_id = su_id + 1

    def add_field(self, field: Field):
        try:
            if self.field_table[field.id] is not None:
                print(str(field) + " already been declared")
            else:
                self.field_table[field.id] = field
        except KeyError:
            self.field_table[field.id] = field

    def add_size(self, size: int):
        self.size = self.size+size
        if self.caller is not None:
            self.caller.add_size(size)

    def add_local(self, id, type, size):
        field = LocalField(id, type, size, self.size)
        self.add_size(size)
        self.add_field(field)

    def add_param(self, id, type, size):
        field = ParamField(id, type, size, self.param_offset)
        self.param_offset = self.param_offset + size
        self.add_field(field)

    def get(self, id: str) -> Optional[Field]:
        field = None
        try:
            try:
                field = self.field_table[id]
            except KeyError:
                if self.caller is not None:
                    field = self.caller.get(id)
            if field is None:
                field = self.static_list[id]
        except KeyError:
            if field is None:
                print("Error: Undefined Identifier of " + id)
                self.add_local(id,"int",8)
                field = self.get(id)
        return field

    def add_constant(self, id: str, type: str, size: int):
        field = StaticField(id, type, size)
        self.static_list[id]=field
        #if self.caller is not None:
        #    self.caller.add_constant(id,type,size)

    def add_static(self, id: str, type: str, size: int):
        field = StaticField(id, type, size)
        self.static_list[id]=field
        #self.caller.add_static(id,type,size)

    def get_func_calling_space(self):
        space = self.func_calling_space
        for su in self.sub_storageUnit:
            space = max(space,su.func_calling_space)
        return space