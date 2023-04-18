from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program  : mptype 'main' LB RB blockstmt EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([FuncDecl('main', IntegerType(), [], None, self.visit(ctx.blockstmt()))])

    # blockstmt: LP stmtlist RP;
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.stmtlist()))

    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
        if ctx.stmtlist():
            if ctx.stmt():
                return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
            return [self.visit(ctx.vardecl())] + self.visit(ctx.stmtlist())
        return []


    # stmt: assignstmt;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.assignstmt(): 
            return self.visit(ctx.assignstmt())

    # assignstmt: lhs EQUAL rhs SEMI;
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.rhs()))

    # vardecl: mptype ID SEMI;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.mptype()))
    
    # lhs: ID;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.ID(): return Id(ctx.ID().getText())

    # mptype: INTTYPE | VOIDTYPE ;
    def visitMptype(self, ctx: MT22Parser.MptypeContext):
        if ctx.INTTYPE(): return IntegerType()
        if ctx.VOIDTYPE(): return VoidType()

    # exp: exp ADD exp1 | exp1;
    def visitExp(self, ctx:MT22Parser.ExpContext):
        if ctx.exp(): 
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.exp()), self.visit(ctx.exp1()))
        return self.visit(ctx.exp1())

    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.FLOATLIT(): return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT(): return IntegerLit(int(ctx.INTLIT().getText()))