
class Memory:

    mem = [None] * 52

    @staticmethod
    def store(ch, value):
        Memory.mem[Memory.indexOf(ch)] = value

    @staticmethod
    def indexOf(ch):
        if not ch.isalpha():
            raise Exception ("invalid identifier argument")

        index = None

        if ch.islower():
            index = ord(ch) - ord('a')
        else:
            index = 26 + ord(ch) - ord('A')
        return index

    @staticmethod
    def fetch(ch):
        return Memory.mem[Memory.indexOf(ch)]