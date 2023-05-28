from Utils import *
# from StaticCheck import *
# from StaticError import *
import CodeGenerator as cgen
from MachineCode import MIPSCode
from CodeGenError import *
from AST import *
from SymbolTable import *


class Emitter():
    def __init__(self, filename):
       self.mips = MIPSCode()

    def emitFunction(func : FuncSym): pass