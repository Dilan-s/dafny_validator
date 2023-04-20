from typing import List

from DafnyListener import DafnyListener
from DafnyParser import DafnyParser
from dafny_program import *

class DafnyValidatorListener(DafnyListener):

    def __init__(self):
        self.varType = {}

    # Enter a parse tree produced by DafnyParser#translation_unit.
    def enterTranslation_unit(self, ctx:DafnyParser.Translation_unitContext):
        self.enterProgram(ctx.program())

    # Enter a parse tree produced by DafnyParser#program.
    def enterProgram(self, ctx:DafnyParser.ProgramContext):
        for m in ctx.method():
            self.enterMethod(m)

        self.enterMain(ctx.main())

    # Enter a parse tree produced by DafnyParser#main.
    def enterMain(self, ctx:DafnyParser.MainContext):
        for s in ctx.stat():
            self.enterStat(s)

    # Enter a parse tree produced by DafnyParser#method.
    def enterMethod(self, ctx:DafnyParser.MethodContext):
        self.enterParamList(ctx.paramList())

        for s in ctx.stat():
            self.enterStat(s)

    # Enter a parse tree produced by DafnyParser#dafnyType.
    def enterDafnyType(self, ctx:DafnyParser.DafnyTypeContext) -> Type:
        t = ctx.baseType()
        if t is not None:
            return self.enterBaseType(t)

        t = ctx.collectionType()
        if t is not None:
            collection_type = self.enterCollectionType(t)
            type_list = self.enterTypeList(ctx.typeList())
            for t in type_list:
                collection_type.add_inner_type(t)

            return collection_type

    # Enter a parse tree produced by DafnyParser#paramList.
    def enterParamList(self, ctx:DafnyParser.ParamListContext):
        if ctx is not None:
            for p in ctx.paramArg():
                self.enterParamArg(p)

    # Enter a parse tree produced by DafnyParser#returnList.
    def enterReturnList(self, ctx:DafnyParser.ReturnListContext):
        pass

    # Enter a parse tree produced by DafnyParser#paramArg.
    def enterParamArg(self, ctx:DafnyParser.ParamArgContext):
        param_name = str(ctx.PARAM_NAME())

        dafny_type = ctx.dafnyType()
        if dafny_type is not None:
            param_type = self.enterDafnyType(dafny_type)
            self.varType[param_name] = param_type

    # Enter a parse tree produced by DafnyParser#returnArg.
    def enterReturnArg(self, ctx:DafnyParser.ReturnArgContext):
        pass

    # Enter a parse tree produced by DafnyParser#typeList.
    def enterTypeList(self, ctx:DafnyParser.TypeListContext) -> List[Type]:
        type_list = []
        if ctx is not None:
            for dafny_type in ctx.dafnyType():
                type_list.append(self.enterDafnyType(dafny_type))
        return type_list

    # Enter a parse tree produced by DafnyParser#baseType.
    def enterBaseType(self, ctx:DafnyParser.BaseTypeContext) -> BaseType:
        base_type = BaseType()
        type = ctx.INT()
        if type is not None:
            base_type.set_name(str(type))
            return base_type

        type = ctx.CHAR()
        if type is not None:
            base_type.set_name(str(type))
            return base_type

        type = ctx.REAL()
        if type is not None:
            base_type.set_name(str(type))
            return base_type

        type = ctx.STRING()
        if type is not None:
            base_type.set_name(str(type))
            return base_type

        type = ctx.BOOL()
        if type is not None:
            base_type.set_name(str(type))
            return base_type

    # Enter a parse tree produced by DafnyParser#collectionType.
    def enterCollectionType(self, ctx:DafnyParser.CollectionTypeContext) -> CollectionType:
        collection_type = CollectionType()
        type = ctx.ARRAY()
        if type is not None:
            collection_type.set_name(str(type))
            return collection_type

        type = ctx.SEQ()
        if type is not None:
            collection_type.set_name(str(type))
            return collection_type

        type = ctx.SET()
        if type is not None:
            collection_type.set_name(str(type))
            return collection_type

        type = ctx.MULTISET()
        if type is not None:
            collection_type.set_name(str(type))
            return collection_type

        type = ctx.MAP()
        if type is not None:
            collection_type.set_name(str(type))
            return collection_type


    # Enter a parse tree produced by DafnyParser#stat.
    def enterStat(self, ctx:DafnyParser.StatContext):
        stat = ctx.printStat()
        if stat is not None:
            self.enterPrintStat(stat)
            return

        stat = ctx.ifElseStat()
        if stat is not None:
            self.enterIfElseStat(stat)
            return

        stat = ctx.assignStat()
        if stat is not None:
            self.enterAssignStat(stat)
            return

    # Enter a parse tree produced by DafnyParser#printStat.
    def enterPrintStat(self, ctx:DafnyParser.PrintStatContext):
        expr_list = self.enterExprList(ctx.exprList())
        for expr in expr_list:
            if expr in self.varType:
                if not self.varType[expr].isPrintable():
                    print("Attempt to print invalid variable type")
                    exit(1)


    # Enter a parse tree produced by DafnyParser#ifElseStat.
    def enterIfElseStat(self, ctx:DafnyParser.IfElseStatContext):
        for s in ctx.stat():
            self.enterStat(s)


    # Enter a parse tree produced by DafnyParser#assignStat.
    def enterAssignStat(self, ctx:DafnyParser.AssignStatContext):
        self.enterVariableList(ctx.variableList())


    # Enter a parse tree produced by DafnyParser#variableList.
    def enterVariableList(self, ctx:DafnyParser.VariableListContext):
        for varArg in ctx.variableArg():
            self.enterVariableArg(varArg)



    # Enter a parse tree produced by DafnyParser#exprList.
    def enterExprList(self, ctx:DafnyParser.ExprListContext) -> List[str]:
        expr_list = []
        for expr in ctx.expr():
            e = self.enterExpr(expr)
            if e is not None:
                expr_list.append(e)

        return expr_list


    # Enter a parse tree produced by DafnyParser#expr.
    def enterExpr(self, ctx:DafnyParser.ExprContext):
        if ctx.variable() is not None:
            return self.enterVariable(ctx.variable())
        return None

    # Enter a parse tree produced by DafnyParser#variableArg.
    def enterVariableArg(self, ctx: DafnyParser.VariableArgContext):
        variable_name = self.enterVariable(ctx.variable())

        if ctx.dafnyType() is not None:
            dafny_type = self.enterDafnyType(ctx.dafnyType())
            self.varType[variable_name] = dafny_type
        elif ctx.expr() is not None:
            type = self.varType[variable_name]
            self.varType[variable_name + str(ctx.expr())] = type.get_inner_type()

    # Enter a parse tree produced by DafnyParser#variable.
    def enterVariable(self, ctx:DafnyParser.VariableContext) -> str:
        name = ctx.PARAM_NAME()
        if name is not None:
            return str(name)

        name = ctx.VARIABLE_NAME()
        if name is not None:
            return str(name)
