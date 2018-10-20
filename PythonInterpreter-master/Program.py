from Block import Block

class Program:

    blk = None

    def __init__(self, blk):
        if blk is None:
            raise Exception ("null block argument")
        self.blk = blk

    def execute(self):
        self.blk.execute()