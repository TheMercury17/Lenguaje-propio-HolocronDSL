# Generated from grammar/HolocronDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HolocronDSLParser import HolocronDSLParser
else:
    from HolocronDSLParser import HolocronDSLParser

# This class defines a complete generic visitor for a parse tree produced by HolocronDSLParser.

class HolocronDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HolocronDSLParser#programa.
    def visitPrograma(self, ctx:HolocronDSLParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#sentencia.
    def visitSentencia(self, ctx:HolocronDSLParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#declaracionMision.
    def visitDeclaracionMision(self, ctx:HolocronDSLParser.DeclaracionMisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#listaParametros.
    def visitListaParametros(self, ctx:HolocronDSLParser.ListaParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#sentenciaAsignacion.
    def visitSentenciaAsignacion(self, ctx:HolocronDSLParser.SentenciaAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#expresionPipeline.
    def visitExpresionPipeline(self, ctx:HolocronDSLParser.ExpresionPipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#expresionBase.
    def visitExpresionBase(self, ctx:HolocronDSLParser.ExpresionBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#instruccionCarga.
    def visitInstruccionCarga(self, ctx:HolocronDSLParser.InstruccionCargaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#llamadaMision.
    def visitLlamadaMision(self, ctx:HolocronDSLParser.LlamadaMisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionPipeline.
    def visitOperacionPipeline(self, ctx:HolocronDSLParser.OperacionPipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionSeleccionar.
    def visitOperacionSeleccionar(self, ctx:HolocronDSLParser.OperacionSeleccionarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#listaIdentificadoresOpcional.
    def visitListaIdentificadoresOpcional(self, ctx:HolocronDSLParser.ListaIdentificadoresOpcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionFiltrar.
    def visitOperacionFiltrar(self, ctx:HolocronDSLParser.OperacionFiltrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionForjar.
    def visitOperacionForjar(self, ctx:HolocronDSLParser.OperacionForjarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionOrdenar.
    def visitOperacionOrdenar(self, ctx:HolocronDSLParser.OperacionOrdenarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ordenDireccion.
    def visitOrdenDireccion(self, ctx:HolocronDSLParser.OrdenDireccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionEliminarClones.
    def visitOperacionEliminarClones(self, ctx:HolocronDSLParser.OperacionEliminarClonesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionSanarVacios.
    def visitOperacionSanarVacios(self, ctx:HolocronDSLParser.OperacionSanarVaciosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#opcionSanado.
    def visitOpcionSanado(self, ctx:HolocronDSLParser.OpcionSanadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionAgrupar.
    def visitOperacionAgrupar(self, ctx:HolocronDSLParser.OperacionAgruparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operacionResumir.
    def visitOperacionResumir(self, ctx:HolocronDSLParser.OperacionResumirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#listaAsignacionesAgregacion.
    def visitListaAsignacionesAgregacion(self, ctx:HolocronDSLParser.ListaAsignacionesAgregacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#asignacionAgregacion.
    def visitAsignacionAgregacion(self, ctx:HolocronDSLParser.AsignacionAgregacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#llamadaAgregacion.
    def visitLlamadaAgregacion(self, ctx:HolocronDSLParser.LlamadaAgregacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#sentenciaArchivado.
    def visitSentenciaArchivado(self, ctx:HolocronDSLParser.SentenciaArchivadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#sentenciaHolograma.
    def visitSentenciaHolograma(self, ctx:HolocronDSLParser.SentenciaHologramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#tipoGrafica.
    def visitTipoGrafica(self, ctx:HolocronDSLParser.TipoGraficaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#propiedadHolograma.
    def visitPropiedadHolograma(self, ctx:HolocronDSLParser.PropiedadHologramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#sentenciaCondicional.
    def visitSentenciaCondicional(self, ctx:HolocronDSLParser.SentenciaCondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#sentenciaTransmision.
    def visitSentenciaTransmision(self, ctx:HolocronDSLParser.SentenciaTransmisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolOr.
    def visitExprBoolOr(self, ctx:HolocronDSLParser.ExprBoolOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolTermino.
    def visitExprBoolTermino(self, ctx:HolocronDSLParser.ExprBoolTerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolAnd.
    def visitExprBoolAnd(self, ctx:HolocronDSLParser.ExprBoolAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolFactor.
    def visitExprBoolFactor(self, ctx:HolocronDSLParser.ExprBoolFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolNot.
    def visitExprBoolNot(self, ctx:HolocronDSLParser.ExprBoolNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolComparacion.
    def visitExprBoolComparacion(self, ctx:HolocronDSLParser.ExprBoolComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolParentesis.
    def visitExprBoolParentesis(self, ctx:HolocronDSLParser.ExprBoolParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprBoolLiteral.
    def visitExprBoolLiteral(self, ctx:HolocronDSLParser.ExprBoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#comparacionRelacional.
    def visitComparacionRelacional(self, ctx:HolocronDSLParser.ComparacionRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#operadorRelacional.
    def visitOperadorRelacional(self, ctx:HolocronDSLParser.OperadorRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprAritTermino.
    def visitExprAritTermino(self, ctx:HolocronDSLParser.ExprAritTerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprAritSumaResta.
    def visitExprAritSumaResta(self, ctx:HolocronDSLParser.ExprAritSumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprAritMultDiv.
    def visitExprAritMultDiv(self, ctx:HolocronDSLParser.ExprAritMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprAritFactor.
    def visitExprAritFactor(self, ctx:HolocronDSLParser.ExprAritFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#ExprAritPotencia.
    def visitExprAritPotencia(self, ctx:HolocronDSLParser.ExprAritPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#AtomoNumero.
    def visitAtomoNumero(self, ctx:HolocronDSLParser.AtomoNumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#AtomoCadena.
    def visitAtomoCadena(self, ctx:HolocronDSLParser.AtomoCadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#AtomoBooleano.
    def visitAtomoBooleano(self, ctx:HolocronDSLParser.AtomoBooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#AtomoIdentificador.
    def visitAtomoIdentificador(self, ctx:HolocronDSLParser.AtomoIdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#AtomoParentesis.
    def visitAtomoParentesis(self, ctx:HolocronDSLParser.AtomoParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#listaIdentificadores.
    def visitListaIdentificadores(self, ctx:HolocronDSLParser.ListaIdentificadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HolocronDSLParser#literal.
    def visitLiteral(self, ctx:HolocronDSLParser.LiteralContext):
        return self.visitChildren(ctx)



del HolocronDSLParser