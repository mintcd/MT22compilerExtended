class Kind: pass
class Function(Kind): pass
class Block(Kind): pass

class Frame():
    def __init__(self, name, kind = Block()):
        
        self.kind = kind

    