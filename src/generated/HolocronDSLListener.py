# Generated from grammar/HolocronDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HolocronDSLParser import HolocronDSLParser
else:
    from HolocronDSLParser import HolocronDSLParser

# This class defines a complete listener for a parse tree produced by HolocronDSLParser.
class HolocronDSLListener(ParseTreeListener):

    # Enter a parse tree produced by HolocronDSLParser#programa.
    def enterPrograma(self, ctx:HolocronDSLParser.ProgramaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#programa.
    def exitPrograma(self, ctx:HolocronDSLParser.ProgramaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#sentencia.
    def enterSentencia(self, ctx:HolocronDSLParser.SentenciaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#sentencia.
    def exitSentencia(self, ctx:HolocronDSLParser.SentenciaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#declaracionMision.
    def enterDeclaracionMision(self, ctx:HolocronDSLParser.DeclaracionMisionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#declaracionMision.
    def exitDeclaracionMision(self, ctx:HolocronDSLParser.DeclaracionMisionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#listaParametros.
    def enterListaParametros(self, ctx:HolocronDSLParser.ListaParametrosContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#listaParametros.
    def exitListaParametros(self, ctx:HolocronDSLParser.ListaParametrosContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#sentenciaAsignacion.
    def enterSentenciaAsignacion(self, ctx:HolocronDSLParser.SentenciaAsignacionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#sentenciaAsignacion.
    def exitSentenciaAsignacion(self, ctx:HolocronDSLParser.SentenciaAsignacionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#expresionPipeline.
    def enterExpresionPipeline(self, ctx:HolocronDSLParser.ExpresionPipelineContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#expresionPipeline.
    def exitExpresionPipeline(self, ctx:HolocronDSLParser.ExpresionPipelineContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#expresionBase.
    def enterExpresionBase(self, ctx:HolocronDSLParser.ExpresionBaseContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#expresionBase.
    def exitExpresionBase(self, ctx:HolocronDSLParser.ExpresionBaseContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#instruccionCarga.
    def enterInstruccionCarga(self, ctx:HolocronDSLParser.InstruccionCargaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#instruccionCarga.
    def exitInstruccionCarga(self, ctx:HolocronDSLParser.InstruccionCargaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#llamadaMision.
    def enterLlamadaMision(self, ctx:HolocronDSLParser.LlamadaMisionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#llamadaMision.
    def exitLlamadaMision(self, ctx:HolocronDSLParser.LlamadaMisionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionPipeline.
    def enterOperacionPipeline(self, ctx:HolocronDSLParser.OperacionPipelineContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionPipeline.
    def exitOperacionPipeline(self, ctx:HolocronDSLParser.OperacionPipelineContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionSeleccionar.
    def enterOperacionSeleccionar(self, ctx:HolocronDSLParser.OperacionSeleccionarContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionSeleccionar.
    def exitOperacionSeleccionar(self, ctx:HolocronDSLParser.OperacionSeleccionarContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionFiltrar.
    def enterOperacionFiltrar(self, ctx:HolocronDSLParser.OperacionFiltrarContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionFiltrar.
    def exitOperacionFiltrar(self, ctx:HolocronDSLParser.OperacionFiltrarContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionForjar.
    def enterOperacionForjar(self, ctx:HolocronDSLParser.OperacionForjarContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionForjar.
    def exitOperacionForjar(self, ctx:HolocronDSLParser.OperacionForjarContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionAlinear.
    def enterOperacionAlinear(self, ctx:HolocronDSLParser.OperacionAlinearContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionAlinear.
    def exitOperacionAlinear(self, ctx:HolocronDSLParser.OperacionAlinearContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ordenDireccion.
    def enterOrdenDireccion(self, ctx:HolocronDSLParser.OrdenDireccionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ordenDireccion.
    def exitOrdenDireccion(self, ctx:HolocronDSLParser.OrdenDireccionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionEliminarClones.
    def enterOperacionEliminarClones(self, ctx:HolocronDSLParser.OperacionEliminarClonesContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionEliminarClones.
    def exitOperacionEliminarClones(self, ctx:HolocronDSLParser.OperacionEliminarClonesContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionSanarVacios.
    def enterOperacionSanarVacios(self, ctx:HolocronDSLParser.OperacionSanarVaciosContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionSanarVacios.
    def exitOperacionSanarVacios(self, ctx:HolocronDSLParser.OperacionSanarVaciosContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#opcionSanado.
    def enterOpcionSanado(self, ctx:HolocronDSLParser.OpcionSanadoContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#opcionSanado.
    def exitOpcionSanado(self, ctx:HolocronDSLParser.OpcionSanadoContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionAgrupar.
    def enterOperacionAgrupar(self, ctx:HolocronDSLParser.OperacionAgruparContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionAgrupar.
    def exitOperacionAgrupar(self, ctx:HolocronDSLParser.OperacionAgruparContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operacionSintetizar.
    def enterOperacionSintetizar(self, ctx:HolocronDSLParser.OperacionSintetizarContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operacionSintetizar.
    def exitOperacionSintetizar(self, ctx:HolocronDSLParser.OperacionSintetizarContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#listaAsignacionesAgregacion.
    def enterListaAsignacionesAgregacion(self, ctx:HolocronDSLParser.ListaAsignacionesAgregacionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#listaAsignacionesAgregacion.
    def exitListaAsignacionesAgregacion(self, ctx:HolocronDSLParser.ListaAsignacionesAgregacionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#asignacionAgregacion.
    def enterAsignacionAgregacion(self, ctx:HolocronDSLParser.AsignacionAgregacionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#asignacionAgregacion.
    def exitAsignacionAgregacion(self, ctx:HolocronDSLParser.AsignacionAgregacionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#llamadaAgregacion.
    def enterLlamadaAgregacion(self, ctx:HolocronDSLParser.LlamadaAgregacionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#llamadaAgregacion.
    def exitLlamadaAgregacion(self, ctx:HolocronDSLParser.LlamadaAgregacionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#sentenciaArchivado.
    def enterSentenciaArchivado(self, ctx:HolocronDSLParser.SentenciaArchivadoContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#sentenciaArchivado.
    def exitSentenciaArchivado(self, ctx:HolocronDSLParser.SentenciaArchivadoContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#sentenciaHolograma.
    def enterSentenciaHolograma(self, ctx:HolocronDSLParser.SentenciaHologramaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#sentenciaHolograma.
    def exitSentenciaHolograma(self, ctx:HolocronDSLParser.SentenciaHologramaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#tipoGrafica.
    def enterTipoGrafica(self, ctx:HolocronDSLParser.TipoGraficaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#tipoGrafica.
    def exitTipoGrafica(self, ctx:HolocronDSLParser.TipoGraficaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#propiedadHolograma.
    def enterPropiedadHolograma(self, ctx:HolocronDSLParser.PropiedadHologramaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#propiedadHolograma.
    def exitPropiedadHolograma(self, ctx:HolocronDSLParser.PropiedadHologramaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#sentenciaCondicional.
    def enterSentenciaCondicional(self, ctx:HolocronDSLParser.SentenciaCondicionalContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#sentenciaCondicional.
    def exitSentenciaCondicional(self, ctx:HolocronDSLParser.SentenciaCondicionalContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#sentenciaTransmision.
    def enterSentenciaTransmision(self, ctx:HolocronDSLParser.SentenciaTransmisionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#sentenciaTransmision.
    def exitSentenciaTransmision(self, ctx:HolocronDSLParser.SentenciaTransmisionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolOr.
    def enterExprBoolOr(self, ctx:HolocronDSLParser.ExprBoolOrContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolOr.
    def exitExprBoolOr(self, ctx:HolocronDSLParser.ExprBoolOrContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolTermino.
    def enterExprBoolTermino(self, ctx:HolocronDSLParser.ExprBoolTerminoContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolTermino.
    def exitExprBoolTermino(self, ctx:HolocronDSLParser.ExprBoolTerminoContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolAnd.
    def enterExprBoolAnd(self, ctx:HolocronDSLParser.ExprBoolAndContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolAnd.
    def exitExprBoolAnd(self, ctx:HolocronDSLParser.ExprBoolAndContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolFactor.
    def enterExprBoolFactor(self, ctx:HolocronDSLParser.ExprBoolFactorContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolFactor.
    def exitExprBoolFactor(self, ctx:HolocronDSLParser.ExprBoolFactorContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolNot.
    def enterExprBoolNot(self, ctx:HolocronDSLParser.ExprBoolNotContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolNot.
    def exitExprBoolNot(self, ctx:HolocronDSLParser.ExprBoolNotContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolComparacion.
    def enterExprBoolComparacion(self, ctx:HolocronDSLParser.ExprBoolComparacionContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolComparacion.
    def exitExprBoolComparacion(self, ctx:HolocronDSLParser.ExprBoolComparacionContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolParentesis.
    def enterExprBoolParentesis(self, ctx:HolocronDSLParser.ExprBoolParentesisContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolParentesis.
    def exitExprBoolParentesis(self, ctx:HolocronDSLParser.ExprBoolParentesisContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprBoolLiteral.
    def enterExprBoolLiteral(self, ctx:HolocronDSLParser.ExprBoolLiteralContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprBoolLiteral.
    def exitExprBoolLiteral(self, ctx:HolocronDSLParser.ExprBoolLiteralContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#comparacionRelacional.
    def enterComparacionRelacional(self, ctx:HolocronDSLParser.ComparacionRelacionalContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#comparacionRelacional.
    def exitComparacionRelacional(self, ctx:HolocronDSLParser.ComparacionRelacionalContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#operadorRelacional.
    def enterOperadorRelacional(self, ctx:HolocronDSLParser.OperadorRelacionalContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#operadorRelacional.
    def exitOperadorRelacional(self, ctx:HolocronDSLParser.OperadorRelacionalContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprAritTermino.
    def enterExprAritTermino(self, ctx:HolocronDSLParser.ExprAritTerminoContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprAritTermino.
    def exitExprAritTermino(self, ctx:HolocronDSLParser.ExprAritTerminoContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprAritSumaResta.
    def enterExprAritSumaResta(self, ctx:HolocronDSLParser.ExprAritSumaRestaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprAritSumaResta.
    def exitExprAritSumaResta(self, ctx:HolocronDSLParser.ExprAritSumaRestaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprAritMultDiv.
    def enterExprAritMultDiv(self, ctx:HolocronDSLParser.ExprAritMultDivContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprAritMultDiv.
    def exitExprAritMultDiv(self, ctx:HolocronDSLParser.ExprAritMultDivContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprAritFactor.
    def enterExprAritFactor(self, ctx:HolocronDSLParser.ExprAritFactorContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprAritFactor.
    def exitExprAritFactor(self, ctx:HolocronDSLParser.ExprAritFactorContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#ExprAritPotencia.
    def enterExprAritPotencia(self, ctx:HolocronDSLParser.ExprAritPotenciaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#ExprAritPotencia.
    def exitExprAritPotencia(self, ctx:HolocronDSLParser.ExprAritPotenciaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#AtomoNumero.
    def enterAtomoNumero(self, ctx:HolocronDSLParser.AtomoNumeroContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#AtomoNumero.
    def exitAtomoNumero(self, ctx:HolocronDSLParser.AtomoNumeroContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#AtomoCadena.
    def enterAtomoCadena(self, ctx:HolocronDSLParser.AtomoCadenaContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#AtomoCadena.
    def exitAtomoCadena(self, ctx:HolocronDSLParser.AtomoCadenaContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#AtomoBooleano.
    def enterAtomoBooleano(self, ctx:HolocronDSLParser.AtomoBooleanoContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#AtomoBooleano.
    def exitAtomoBooleano(self, ctx:HolocronDSLParser.AtomoBooleanoContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#AtomoIdentificador.
    def enterAtomoIdentificador(self, ctx:HolocronDSLParser.AtomoIdentificadorContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#AtomoIdentificador.
    def exitAtomoIdentificador(self, ctx:HolocronDSLParser.AtomoIdentificadorContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#AtomoParentesis.
    def enterAtomoParentesis(self, ctx:HolocronDSLParser.AtomoParentesisContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#AtomoParentesis.
    def exitAtomoParentesis(self, ctx:HolocronDSLParser.AtomoParentesisContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#listaIdentificadores.
    def enterListaIdentificadores(self, ctx:HolocronDSLParser.ListaIdentificadoresContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#listaIdentificadores.
    def exitListaIdentificadores(self, ctx:HolocronDSLParser.ListaIdentificadoresContext):
        pass


    # Enter a parse tree produced by HolocronDSLParser#literal.
    def enterLiteral(self, ctx:HolocronDSLParser.LiteralContext):
        pass

    # Exit a parse tree produced by HolocronDSLParser#literal.
    def exitLiteral(self, ctx:HolocronDSLParser.LiteralContext):
        pass



del HolocronDSLParser