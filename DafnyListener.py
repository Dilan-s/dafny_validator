# Generated from Dafny.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DafnyParser import DafnyParser
else:
    from DafnyParser import DafnyParser

# This class defines a complete listener for a parse tree produced by DafnyParser.
class DafnyListener(ParseTreeListener):

    # Enter a parse tree produced by DafnyParser#translation_unit.
    def enterTranslation_unit(self, ctx:DafnyParser.Translation_unitContext):
        pass

    # Exit a parse tree produced by DafnyParser#translation_unit.
    def exitTranslation_unit(self, ctx:DafnyParser.Translation_unitContext):
        pass


    # Enter a parse tree produced by DafnyParser#program.
    def enterProgram(self, ctx:DafnyParser.ProgramContext):
        pass

    # Exit a parse tree produced by DafnyParser#program.
    def exitProgram(self, ctx:DafnyParser.ProgramContext):
        pass


    # Enter a parse tree produced by DafnyParser#main.
    def enterMain(self, ctx:DafnyParser.MainContext):
        pass

    # Exit a parse tree produced by DafnyParser#main.
    def exitMain(self, ctx:DafnyParser.MainContext):
        pass


    # Enter a parse tree produced by DafnyParser#method.
    def enterMethod(self, ctx:DafnyParser.MethodContext):
        pass

    # Exit a parse tree produced by DafnyParser#method.
    def exitMethod(self, ctx:DafnyParser.MethodContext):
        pass


    # Enter a parse tree produced by DafnyParser#dafnyType.
    def enterDafnyType(self, ctx:DafnyParser.DafnyTypeContext):
        pass

    # Exit a parse tree produced by DafnyParser#dafnyType.
    def exitDafnyType(self, ctx:DafnyParser.DafnyTypeContext):
        pass


    # Enter a parse tree produced by DafnyParser#paramList.
    def enterParamList(self, ctx:DafnyParser.ParamListContext):
        pass

    # Exit a parse tree produced by DafnyParser#paramList.
    def exitParamList(self, ctx:DafnyParser.ParamListContext):
        pass


    # Enter a parse tree produced by DafnyParser#returnList.
    def enterReturnList(self, ctx:DafnyParser.ReturnListContext):
        pass

    # Exit a parse tree produced by DafnyParser#returnList.
    def exitReturnList(self, ctx:DafnyParser.ReturnListContext):
        pass


    # Enter a parse tree produced by DafnyParser#paramArg.
    def enterParamArg(self, ctx:DafnyParser.ParamArgContext):
        pass

    # Exit a parse tree produced by DafnyParser#paramArg.
    def exitParamArg(self, ctx:DafnyParser.ParamArgContext):
        pass


    # Enter a parse tree produced by DafnyParser#returnArg.
    def enterReturnArg(self, ctx:DafnyParser.ReturnArgContext):
        pass

    # Exit a parse tree produced by DafnyParser#returnArg.
    def exitReturnArg(self, ctx:DafnyParser.ReturnArgContext):
        pass


    # Enter a parse tree produced by DafnyParser#typeList.
    def enterTypeList(self, ctx:DafnyParser.TypeListContext):
        pass

    # Exit a parse tree produced by DafnyParser#typeList.
    def exitTypeList(self, ctx:DafnyParser.TypeListContext):
        pass


    # Enter a parse tree produced by DafnyParser#baseType.
    def enterBaseType(self, ctx:DafnyParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by DafnyParser#baseType.
    def exitBaseType(self, ctx:DafnyParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by DafnyParser#collectionType.
    def enterCollectionType(self, ctx:DafnyParser.CollectionTypeContext):
        pass

    # Exit a parse tree produced by DafnyParser#collectionType.
    def exitCollectionType(self, ctx:DafnyParser.CollectionTypeContext):
        pass


    # Enter a parse tree produced by DafnyParser#stat.
    def enterStat(self, ctx:DafnyParser.StatContext):
        pass

    # Exit a parse tree produced by DafnyParser#stat.
    def exitStat(self, ctx:DafnyParser.StatContext):
        pass


    # Enter a parse tree produced by DafnyParser#printStat.
    def enterPrintStat(self, ctx:DafnyParser.PrintStatContext):
        pass

    # Exit a parse tree produced by DafnyParser#printStat.
    def exitPrintStat(self, ctx:DafnyParser.PrintStatContext):
        pass


    # Enter a parse tree produced by DafnyParser#returnStat.
    def enterReturnStat(self, ctx:DafnyParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by DafnyParser#returnStat.
    def exitReturnStat(self, ctx:DafnyParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by DafnyParser#ifElseStat.
    def enterIfElseStat(self, ctx:DafnyParser.IfElseStatContext):
        pass

    # Exit a parse tree produced by DafnyParser#ifElseStat.
    def exitIfElseStat(self, ctx:DafnyParser.IfElseStatContext):
        pass


    # Enter a parse tree produced by DafnyParser#assignStat.
    def enterAssignStat(self, ctx:DafnyParser.AssignStatContext):
        pass

    # Exit a parse tree produced by DafnyParser#assignStat.
    def exitAssignStat(self, ctx:DafnyParser.AssignStatContext):
        pass


    # Enter a parse tree produced by DafnyParser#variableList.
    def enterVariableList(self, ctx:DafnyParser.VariableListContext):
        pass

    # Exit a parse tree produced by DafnyParser#variableList.
    def exitVariableList(self, ctx:DafnyParser.VariableListContext):
        pass


    # Enter a parse tree produced by DafnyParser#variableArg.
    def enterVariableArg(self, ctx:DafnyParser.VariableArgContext):
        pass

    # Exit a parse tree produced by DafnyParser#variableArg.
    def exitVariableArg(self, ctx:DafnyParser.VariableArgContext):
        pass


    # Enter a parse tree produced by DafnyParser#exprList.
    def enterExprList(self, ctx:DafnyParser.ExprListContext):
        pass

    # Exit a parse tree produced by DafnyParser#exprList.
    def exitExprList(self, ctx:DafnyParser.ExprListContext):
        pass


    # Enter a parse tree produced by DafnyParser#expr.
    def enterExpr(self, ctx:DafnyParser.ExprContext):
        pass

    # Exit a parse tree produced by DafnyParser#expr.
    def exitExpr(self, ctx:DafnyParser.ExprContext):
        pass


    # Enter a parse tree produced by DafnyParser#literal.
    def enterLiteral(self, ctx:DafnyParser.LiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#literal.
    def exitLiteral(self, ctx:DafnyParser.LiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#intLiteral.
    def enterIntLiteral(self, ctx:DafnyParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#intLiteral.
    def exitIntLiteral(self, ctx:DafnyParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#charLiteral.
    def enterCharLiteral(self, ctx:DafnyParser.CharLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#charLiteral.
    def exitCharLiteral(self, ctx:DafnyParser.CharLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#boolLiteral.
    def enterBoolLiteral(self, ctx:DafnyParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#boolLiteral.
    def exitBoolLiteral(self, ctx:DafnyParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#realLiteral.
    def enterRealLiteral(self, ctx:DafnyParser.RealLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#realLiteral.
    def exitRealLiteral(self, ctx:DafnyParser.RealLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:DafnyParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:DafnyParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#setLiteral.
    def enterSetLiteral(self, ctx:DafnyParser.SetLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#setLiteral.
    def exitSetLiteral(self, ctx:DafnyParser.SetLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#seqLiteral.
    def enterSeqLiteral(self, ctx:DafnyParser.SeqLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#seqLiteral.
    def exitSeqLiteral(self, ctx:DafnyParser.SeqLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#multisetLiteral.
    def enterMultisetLiteral(self, ctx:DafnyParser.MultisetLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#multisetLiteral.
    def exitMultisetLiteral(self, ctx:DafnyParser.MultisetLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#stringLiteral.
    def enterStringLiteral(self, ctx:DafnyParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#stringLiteral.
    def exitStringLiteral(self, ctx:DafnyParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#mapLiteral.
    def enterMapLiteral(self, ctx:DafnyParser.MapLiteralContext):
        pass

    # Exit a parse tree produced by DafnyParser#mapLiteral.
    def exitMapLiteral(self, ctx:DafnyParser.MapLiteralContext):
        pass


    # Enter a parse tree produced by DafnyParser#binaryOperator.
    def enterBinaryOperator(self, ctx:DafnyParser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by DafnyParser#binaryOperator.
    def exitBinaryOperator(self, ctx:DafnyParser.BinaryOperatorContext):
        pass


    # Enter a parse tree produced by DafnyParser#op1.
    def enterOp1(self, ctx:DafnyParser.Op1Context):
        pass

    # Exit a parse tree produced by DafnyParser#op1.
    def exitOp1(self, ctx:DafnyParser.Op1Context):
        pass


    # Enter a parse tree produced by DafnyParser#op2.
    def enterOp2(self, ctx:DafnyParser.Op2Context):
        pass

    # Exit a parse tree produced by DafnyParser#op2.
    def exitOp2(self, ctx:DafnyParser.Op2Context):
        pass


    # Enter a parse tree produced by DafnyParser#op3.
    def enterOp3(self, ctx:DafnyParser.Op3Context):
        pass

    # Exit a parse tree produced by DafnyParser#op3.
    def exitOp3(self, ctx:DafnyParser.Op3Context):
        pass


    # Enter a parse tree produced by DafnyParser#op4.
    def enterOp4(self, ctx:DafnyParser.Op4Context):
        pass

    # Exit a parse tree produced by DafnyParser#op4.
    def exitOp4(self, ctx:DafnyParser.Op4Context):
        pass


    # Enter a parse tree produced by DafnyParser#op6.
    def enterOp6(self, ctx:DafnyParser.Op6Context):
        pass

    # Exit a parse tree produced by DafnyParser#op6.
    def exitOp6(self, ctx:DafnyParser.Op6Context):
        pass


    # Enter a parse tree produced by DafnyParser#op7.
    def enterOp7(self, ctx:DafnyParser.Op7Context):
        pass

    # Exit a parse tree produced by DafnyParser#op7.
    def exitOp7(self, ctx:DafnyParser.Op7Context):
        pass


    # Enter a parse tree produced by DafnyParser#unaryOperator.
    def enterUnaryOperator(self, ctx:DafnyParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by DafnyParser#unaryOperator.
    def exitUnaryOperator(self, ctx:DafnyParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by DafnyParser#callExpr.
    def enterCallExpr(self, ctx:DafnyParser.CallExprContext):
        pass

    # Exit a parse tree produced by DafnyParser#callExpr.
    def exitCallExpr(self, ctx:DafnyParser.CallExprContext):
        pass


    # Enter a parse tree produced by DafnyParser#ifElseExpr.
    def enterIfElseExpr(self, ctx:DafnyParser.IfElseExprContext):
        pass

    # Exit a parse tree produced by DafnyParser#ifElseExpr.
    def exitIfElseExpr(self, ctx:DafnyParser.IfElseExprContext):
        pass


    # Enter a parse tree produced by DafnyParser#indexExpr.
    def enterIndexExpr(self, ctx:DafnyParser.IndexExprContext):
        pass

    # Exit a parse tree produced by DafnyParser#indexExpr.
    def exitIndexExpr(self, ctx:DafnyParser.IndexExprContext):
        pass


    # Enter a parse tree produced by DafnyParser#update.
    def enterUpdate(self, ctx:DafnyParser.UpdateContext):
        pass

    # Exit a parse tree produced by DafnyParser#update.
    def exitUpdate(self, ctx:DafnyParser.UpdateContext):
        pass


    # Enter a parse tree produced by DafnyParser#subsequence.
    def enterSubsequence(self, ctx:DafnyParser.SubsequenceContext):
        pass

    # Exit a parse tree produced by DafnyParser#subsequence.
    def exitSubsequence(self, ctx:DafnyParser.SubsequenceContext):
        pass


    # Enter a parse tree produced by DafnyParser#variable.
    def enterVariable(self, ctx:DafnyParser.VariableContext):
        pass

    # Exit a parse tree produced by DafnyParser#variable.
    def exitVariable(self, ctx:DafnyParser.VariableContext):
        pass


