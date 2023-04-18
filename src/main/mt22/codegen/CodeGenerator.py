'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Visitor import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from copy import deepcopy
from AST import *
from Allocator import Allocator
from functools import reduce

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, ast, reg_num):

        # Allocator for current ast and reg_num
        self.allocator = Allocator(ast, reg_num-1)
        # Store main code
        self.main = ""
        # Store function code
        self.funcs = []

    # @avoid is used to mark register needing to be avoided when process this instruction
    # decls: List[Decl]
    def visitProgram(self, ast, avoid):
        for decl in ast.decls:
            self.visit(decl, {0})

    def visitFuncDecl(self, ast, avoid):
        return self.visit(ast.body, avoid)

    def visitBlockStmt(self, ast: BlockStmt, avoid):

        for ele in ast.body:
            self.main += self.visit(ele, avoid)
    
    def visitVarDecl(self, ast: VarDecl, avoid):
        return self.allocator.addVar(ast.name, ast.typ)
    
    def visitAssignStmt(self, ast: AssignStmt, avoid):
        lcode, lreg = self.visit(ast.lhs, avoid)
        rcode, rreg = self.visit(ast.rhs, avoid)

        # Free avoid
        if lreg in avoid: avoid.remove(lreg)
        if rreg and rreg in avoid: avoid.remove(rreg)
        # It must be a literal
        if rcode is None:
            return lcode + rcode + f"addi ${lreg}, $0, {ast.rhs.value}\n"

        else:
            return lcode + rcode + f"addi ${lreg}, ${rreg}, 0 \n"
        

    # Returns code need to complete this BinExpr and resnum
    def visitBinExpr(self, ast: BinExpr, avoid):
        lcode, lreg = self.visit(ast.left, avoid)
        rcode, rreg = self.visit(ast.right, avoid)

        
        code = lcode + rcode
        # If both are LIT, compiler can handles
        if lreg is None: 
            code += f"addi ${lreg}, ${rreg}, 0 \n"
            return code, lreg
        if rreg is None: 
            code += f"addi ${rreg}, ${lreg}, 0 \n"
            return code, lreg

        
        # Find another register to save the result
        # Name it as the concatenation of the 2 names
        rescode, resreg = self.allocator.allocVar(str(ast.left.name+ast.right.name), avoid)
        code += rescode + f"add ${resreg}, ${lreg}, ${rreg}\n"
        # Free avoid
        if lreg and lreg in avoid: avoid.remove(lreg)
        if rreg and rreg in avoid: avoid.remove(rreg)

        return code, resreg
    
    def visitId(self, ast, avoid): 
        return self.allocator.allocVar(ast.name, avoid)

    # Return its value, suppose with all can use addi
    def visitIntegerLit(self, ast : IntegerLit, avoid):
        return None, None


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"


    def gen(self, ast, dir_):
        visitor = CodeGenVisitor(ast, 7)
        visitor.visit(ast, {0})
        return visitor.main
