
class Block:

    stmts = []

    def __init__(self):
        self.stmts = []

    def add(self, stmt):
        if(stmt == None):
            raise Exception("null statement argument")
        self.stmts.append(stmt)

    def execute(self):
        for i in self.stmts:
            i.execute()

