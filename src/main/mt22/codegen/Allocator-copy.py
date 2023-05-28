from Analyzer import LiveRangeAnalyzer

class Allocator:
    def __init__(self, ast):
        self.ast = ast
        self.liveranges = LiveRangeAnalyzer(ast)
        self.st = self.analyzer.st
    
    def chaitin():
        pass