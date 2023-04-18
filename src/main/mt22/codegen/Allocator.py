from Visitor import *
from AST import *
from copy import deepcopy
from Emitter import Emitter

class LiveVisitor(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
    
    def __str__(self):
        return "I am a LiveVisitor"
    
    # decls: List[Decl]
    def visitProgram(self, ast : Program, c):
        c = self.visit(ast.decls[0], [])
        return c
        
    def visitFuncDecl(self, ast, c):
        c = self.visit(ast.body, c)
        return c

    def visitBlockStmt(self, ast: BlockStmt, c):
        for ele in ast.body[::-1]:
            c = self.visit(ele, c)
        return c

    def visitAssignStmt(self, ast: AssignStmt, c):
        if len(c) == 0:
            c = [self.visit(ast.lhs, c)] + c
        vars = deepcopy(c[0])
        vars = vars.difference(self.visit(ast.lhs, c))
        vars = vars | self.visit(ast.rhs, c)
        c = [vars] + c
        return c
    
    def visitVarDecl(self, ast: VarDecl, c):
        return c
    
    def visitBinExpr(self, ast : BinExpr, c):
        return self.visit(ast.left, c) | self.visit(ast.right, c)
    
    def visitId(self, ast: Id, c):
        return {ast.name}
    def visitIntegerLit(self, ast, param):
        return {None}
    def visitFloatLit(self, ast, param):
        return {None}


# @storage: relative location to the $sp
class Symbol:
    def __init__(self, name : str, typ, storage):
        self.name = name
        self.typ = typ
        self.storage = storage

class VarSym(Symbol):
    def __init__(self, name, typ, storage, value = None):
        super().__init__(name, typ, storage)
        self.value = value

        
class Register:
    def __init__(self, number, name = None, var : VarSym or None  = None):
        self.number = number
        self.name = name
        self.var = var



class Allocator:
    def __init__(self, ast, reg_num):
        self.reg_num = reg_num
        self.liveranges = LiveVisitor(ast).visitProgram(ast, [])
        self.rig = self.graph()
        self.optimal = self.chaitin()
        self.registers = list(map(lambda i: Register(i), range(reg_num)))
        self.vars : List[VarSym] = []
        self.sp = 0
        self.emit = Emitter()

    def addVar(self, name, typ, value = None):
        self.vars.append(VarSym(name, None, self.sp, value))
        self.sp = self.sp - 4
        return self.emit.emitEXPANDSTACK(4)

    # @avoid is the list of registers needing to be avoided
    # because of dependency with this new allocated var
    # return the number of allocated register
    def allocVar(self, name : str, avoid):
        # If it is already allocated, return
        for reg in self.registers:
            if reg.var is not None and reg.var.name.name == name: 
                return "", reg.number

        for var in self.vars:
            if var.name.name == name:
                # If it is meant to be in a register, push it into this
                if self.optimal[name] is not None:
                    self.registers[self.optimal[name]].var = var
                    avoid.add(self.optimal[name])
                    print("Load", var.name, "into", self.optimal[name])
                    return self.emit.emitLOADWORD(self.optimal[name], var.storage), reg.number
                # Find an empty register
                else:
                    for reg in self.registers:
                        if reg.var is None: 
                            reg.var = var
                            avoid.add(reg.number)
                            return self.emit.emitLOADWORD(reg.number, var.storage), reg.number
                    # If there is no empty register, push a random one rather than AVOID back to memory
                    for reg in self.registers:
                        if reg.number not in avoid:
                            reg.var = var
                            avoid.add(reg.number)
                            return self.emit.emitSTOREWORD(reg.number, var.storage) + self.emit.emitLOADWORD(reg.number, var.storage), reg.number
        # It is not a var, just find a place
        for reg in self.registers:
            if reg.number not in avoid:
                reg.var = var
                avoid.add(reg.number)
                return "", reg.number
        raise Exception("All registers are busy")


    # For each statement or vardecl, just take the ID's name to mark that it must be living
    def graph(self):
        res = dict()
        for ins in self.liveranges:
            for ele in ins:
                if not res.get(ele):
                    res[ele] = set([i for i in ins if i != ele])
                else: res[ele] = res[ele] | set([i for i in ins if i != ele])

        sorted_keys = sorted(res.keys())
        sorted_res = {key: res[key] for key in sorted_keys}
        return sorted_res
    
    def chaitin(self):
        colors = {}  # Dictionary to store assigned colors for each vertex
        available_colors = set(range(self.reg_num - 1))  # Set to store available colors at each step
        graph = self.graph()
        # Helper function to get the neighboring colors of a vertex
        def get_neighboring_colors(vertex):
            neighboring_colors = set()
            for neighbor in graph[vertex]:
                if neighbor in colors:
                    neighboring_colors.add(colors[neighbor])
            return neighboring_colors

        # Find simplifyable vertices (vertices with fewer than num_colors outgoing edges)
        simplifyable_vertices = [vertex for vertex in graph if len(graph[vertex]) < self.reg_num]

        # Initialize available colors and assigned colors
        for vertex in graph:
            colors[vertex] = None

        # Loop through each simplifyable vertex in the graph
        for vertex in simplifyable_vertices:
            neighboring_colors = get_neighboring_colors(vertex)
            # Find the first available color not used by any neighboring vertices
            for color in available_colors:
                if color not in neighboring_colors:
                    colors[vertex] = color
                    break

            # If no color can be assigned, mark the vertex as "troublesome"
            if colors[vertex] is None:
                colors[vertex] = "troublesome"

        # Loop through the remaining vertices in the graph
        for vertex in graph:
            if vertex not in simplifyable_vertices:
                neighboring_colors = get_neighboring_colors(vertex)
                # Find the first available color not used by any neighboring vertices
                for color in available_colors:
                    if color not in neighboring_colors:
                        colors[vertex] = color
                        break
        print(180, colors)
        colors.update((k, colors[k] + 1) for k in colors if colors[k] is not None)
        print(182, colors)
        return colors