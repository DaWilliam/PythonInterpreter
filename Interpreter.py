from Parser import Parser
from Program import Program

class Interpreter:
    p = Parser("test3.txt")
    print("Program Started")
    prog = p.parse()
    prog.execute()

    try:
        print("Ended")
    except:
        print("Crashed for some reason")
