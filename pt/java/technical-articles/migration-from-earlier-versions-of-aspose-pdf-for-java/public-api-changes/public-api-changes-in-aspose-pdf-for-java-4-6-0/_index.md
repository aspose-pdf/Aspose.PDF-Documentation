---
title: Alterações na API Pública no Aspose.PDF para Java 4.6.0
type: docs
weight: 20
url: /pt/java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as alterações na API pública que foram introduzidas no Aspose.PDF para Java 4.6.0. Inclui não apenas novos métodos públicos e métodos obsoletos, mas também uma descrição de quaisquer alterações no comportamento nos bastidores no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifique o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

{{% alert color="primary" %}}

Na versão mais recente 4.6.0, removemos todas as **ms-classes**. Portanto, é necessário usar wrappers internos. 
Isso se aplica às seguintes classes:

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**Movido**:

com.aspose.pdf.facades.PageSize - para: com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - para: com.aspose.pdf.DocConverter

com.aspose.pdf.ITable  - para: com.aspose.pdf.generator.legacyxmlmodel.ITable 

com.aspose.pdf.ITableCell  - para: com.aspose.pdf.generator.legacyxmlmodel.ITableCell 

com.aspose.pdf.ITableRow  - para: com.aspose.pdf.generator.legacyxmlmodel.ITableRow 

**Adicionado**:

pacote com.aspose.pdf.drawing 

e as seguintes classes:

com.aspose.pdf.drawing.Arc 

com.aspose.pdf.drawing.Circle 

com.aspose.pdf.drawing.Curve 

com.aspose.pdf.drawing.Graph 

com.aspose.pdf.drawing.Line 

com.aspose.pdf.drawing.Rectangle 

com.aspose.pdf.drawing.Shape

**Adicionado**:

pacote com.aspose.pdf.excel

e as seguintes classes:

com.aspose.pdf.excel.ColumnManager 

com.aspose.pdf.excel.ContentManager 

com.aspose.pdf.excel.DataKeeper 

com.aspose.pdf.excel.DataManager 

com.aspose.pdf.excel.ExcelConverterInternal 

com.aspose.pdf.excel.ItemPropertyStore 

com.aspose.pdf.excel.Log 

com.aspose.pdf.excel.OverrideContentManager 

com.aspose.pdf.excel.RegexManager

com.aspose.pdf.excel.SpreadSheetManager

com.aspose.pdf.excel.SSCell

com.aspose.pdf.excel.SSColumn

com.aspose.pdf.excel.SSConvertToXml

com.aspose.pdf.excel.SSFileComponents

com.aspose.pdf.excel.SSFont

com.aspose.pdf.excel.SSRow

com.aspose.pdf.excel.SSStyle

com.aspose.pdf.excel.SSTable

com.aspose.pdf.excel.SSWorkbook

com.aspose.pdf.excel.SSWorksheet

**Classes adicionadas:**

com.aspose.pdf.exceptions.FontNotFoundException

com.aspose.pdf.generator.legacyxmlmodel.enums.InconsistentXmlImageParamsHandlingTypes

com.aspose.pdf.text.FontTypes

com.aspose.pdf.text.TextProcessingContext

com.aspose.pdf.EpubConverter

com.aspose.pdf.EpubLoadOptions

com.aspose.pdf.EpubSaveOptions

com.aspose.pdf.ExcelConverter

com.aspose.pdf.ExcelSaveOptions

com.aspose.pdf.FolderFontSource

com.aspose.pdf.GraphInfo

com.aspose.pdf.HtmlDocumentType

com.aspose.pdf.InvalidFormTypeOperationException

com.aspose.pdf.IWarningCallback

com.aspose.pdf.LatexLoadOptions

com.aspose.pdf.LatexToPdfConverter

com.aspose.pdf.MhtMainHtmlPart

com.aspose.pdf.MhtParcedPackage

com.aspose.pdf.MhtPart

com.aspose.pdf.MhtResourcePart

com.aspose.pdf.MhtToPdfConverter

com.aspose.pdf.MhtUtility

com.aspose.pdf.MobiXmlConverter

com.aspose.pdf.MobiXmlSaveOptions

com.aspose.pdf.ReturnAction

com.aspose.pdf.SvgConverter

com.aspose.pdf.WarningInfo

com.aspose.pdf.WarningType

**Alterações nas próximas classes:**

com.aspose.pdf.facades.AForm

foi estendida de SaveableFacade

adicionado:

classe interna pública estática FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

os próximos métodos foram marcados como @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor 

adicionado:

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

próximos métodos foram marcados como @Deprecated:

public String getSrcFileName() 

public void setSrcFileName(String value)

public String getDestFileName() 

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType** 

classe foi marcada como @Deprecated

adicionado:

public String toString()

**com.aspose.pdf.facades.APdfFileEditor** 

adicionado:

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean obterMesclarSumariosDuplicados()

public void definirMesclarSumariosDuplicados(boolean valor)

public boolean obterPreservarDireitosDoUsuario()

public void definirPreservarDireitosDoUsuario(boolean valor)

public boolean obterAtualizacoesIncrementais()

public void definirAtualizacoesIncrementais(boolean valor)

public boolean obterOtimizarTamanho()

public void definirOtimizarTamanho(boolean valor)

public static ContentsResizeParameters redimensionarPagina(double largura, double altura)

public static ContentsResizeParameters redimensionarPaginaPct(double larguraPct, double alturaPct)

public boolean concatenar(Document[] src, Document dest)

public void dividirEmPaginas(String arquivoEntrada, String modeloNomeArquivo)

public void dividirEmPaginas(InputStream fluxoEntrada, String modeloNomeArquivo)

**com.aspose.pdf.facades.APdfFileStamp** 

adicionado:
public boolean obterOtimizarTamanho()

public void definirOtimizarTamanho(boolean valor)

public int obterIdCarimbo()

public void definirIdCarimbo(int valor)

**com.aspose.pdf.facades.AutoFiller** 

implementa ISaveableFacade


próximos métodos foram marcados como @Deprecated:

void setOutputStreamInternal(Stream value)

public String getInputFileName()

public void setInputFileName(String value)

public String getOutputFileName()

public void setOutputFileName(String value)

public void save()

adicionado:
public InputStream getInputStream()

public void setInputStream(InputStream value)

public void save(String destFile)

public void save(OutputStream destStream)

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void bindPdf(IDocument srcDoc)

public void close()


**com.aspose.pdf.facades.Facade**

adicionado:

public void bindPdf(InputStream srcStream, String password)

**com.aspose.pdf.facades.Form**

adicionado:

internal public static final class ImportStatus

**com.aspose.pdf.facades.FormFieldFacade**

a próxima constante foi marcada como @Deprecated:

public static final float BORDER_WIDTH_UNDIFIED = 0;

adicionado:

public static final float BORDER_WIDTH_UNDEFINED = -1;


**com.aspose.pdf.facades.PdfAnnotationEditor**

extends SaveableFacade

adicionado:


public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType)


ContentsResizeParameters parameters)

public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor**

extends SaveableFacade

**com.aspose.pdf.facades.PdfConverter**

adicionado:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor**

adicionado:

public static final String E_EMPTY_PAGE_RANGE = "Matriz de intervalos de páginas não está definida";

public static final String E_SMALL_PAGE_RANGE = "A matriz de intervalos de páginas deve ter dois elementos";

public static final String E_WRONG_PAGE_RANGE = "Intervalo de páginas inválido";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)
`

public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

extends SaveableFacade

adicionado:

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

a próxima constante foi marcada como @Deprecated:

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

extends SaveableFacade 

os próximos métodos foram marcados como @Deprecated:

public void setOutputFile(String value) 

public PdfFileSecurity(String inputFile, String outputFile)

public PdfFileSecurity(IDocument document, String outputFile) 

public PdfFileSecurity(IDocument document, OutputStream outputStream)

adicionado:

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature** 

extends SaveableFacade

a próxima constante foi marcada como @Deprecated:

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

adicionado:

public void removeSignature(String signName, boolean removeField) 

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor** 

adicionado:

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment() 

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType() 

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()


a próxima constante foi marcada como @Deprecated:

public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

removido:

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer** 

adicionado:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

foi marcado como @Deprecated

**com.aspose.pdf.generator.legacyxmlmodel.EndNote** 

renomeado:
getNumberingContinuation_EndNote_New() para
getNumberingContinuation()
setNumberingContinuation_EndNote_New() para setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image** 

adicionado:

public  void load(XmlTextReader xmlReader, LoadingContext context)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

adicionado:

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table** 

adicionado:

public int getColumnCount()

**com.aspose.pdf.text.Font** 

removido, pois duplica com.aspose.pdf.Font 

**com.aspose.pdf.ADocument** 

adicionado:

public boolean isPdfaCompliant()

public int getPdfaFormat() 

**com.aspose.pdf.Annotation** 

adicionado:

public int getHorizontalAlignment_Annotation_New() 

public void setHorizontalAlignment_Annotation_New(int value)

a próxima constante foi marcada como @Deprecated:

public int getAlignment() 

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection** 

adicionado:

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter** 

adicionado:

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact** 

adicionado:

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph** 

adicionado:

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo** 

alterações:

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

adicionado:

public GraphInfo getBottom()

public void setBottom(GraphInfo value) public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

removido:

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo**

renomeado:

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField**

adicionado:

public ButtonField()

**com.aspose.pdf.CellBorderStyle**

classe foi removida

**com.aspose.pdf.CheckboxField**

adicionado:

public java.util.ArrayList getAllowedStates()

public String getOnState()

**com.aspose.pdf.ComboBoxField**

adicionado:

public ComboBoxField()

**com.aspose.pdf.Field**

adicionado:

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination**

próxima constante foi marcada como @Deprecated:

public FitBExplicitDestination(Document document, int pageNumber)

adicionado:

public FitBExplicitDestination(int pageNumber)

**com.aspose.pdf.FitBHExplicitDestination**

próxima constante foi marcada como @Deprecated:

public FitBHExplicitDestination(Document document, int pageNumber, double top)

adicionado:

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination**

próxima constante foi marcada como @Deprecated:

public FitBVExplicitDestination(Document document, int pageNumber, double left)

adicionado:

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

próxima constante foi marcada como @Deprecated:

public FitHExplicitDestination(Document document, int pageNumber, double top)

adicionado:

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination**

próxima constante foi marcada como @Deprecated:

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

adicionado:

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination**

a próxima constante foi marcada como @Deprecated:

public FitVExplicitDestination(Document document, int pageNumber, double left)

adicionado:

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository**

adicionado:

public static FontSubstitutionCollection getSubstitutions()

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream, int fontType)

**com.aspose.pdf.FontSource**

alterações:

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form**

alterações:

com.aspose.pdf.Form.getFields_Rename_Namesake() - renomeado para: com.aspose.pdf.Form.getFields;

adicionado:

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation**

adicionado:

public int getStartingStyle()

public void setStartingStyle(int value)

public int getEndingStyle()

public void setEndingStyle(int value)

public DefaultAppearance getDefaultAppearanceObject()

**com.aspose.pdf.HtmlSaveOptions** 

classes internas adicionadas:

public static final class HtmlImageType

public static class HtmlImageSavingInfo

public static class CssSavingInfo

public static class CssUrlRequestInfo

public interface ResourceSavingStrategy

public interface CssUrlMakingStrategy

public interface CssSavingStrategy

**com.aspose.pdf.ImagePlacement**

adicionado:

public int getRotation()

public void save(OutputStream outputStream)

public void save(OutputStream outputStream, ImageFormat format)

**com.aspose.pdf.ListBoxField** 

adicionado:

public ListBoxField()

**com.aspose.pdf.LoadOptions** 

adicionado:

public IWarningCallback getWarningHandler()

public void setWarningHandler

public String ApsIntermediateFileIfAny;

public String XpsIntermediateFileIfAny;

**com.aspose.pdf.MarkupAnnotation** 

adicionado:

public java.util.Date getCreationDate()

**com.aspose.pdf.Matrix** 

adicionado:

public IPdfArray getMatrix(ITrailerable trailer)

**com.aspose.pdf.Page**

implementa ISupportsMemoryCleanup

adicionado:

public void setBackground(Color value)

**com.aspose.pdf.PageCollection**

adicionado:

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection**

alterações:

UpdateLabel -> updateLabel

RemoveLabel -> removeLabel

GetPages -> getPages

**com.aspose.pdf.PageSize**

adicionado:

public static final float LEAVE_INTACT = -1;

**com.aspose.pdf.RichTextBoxField**

adicionado:

public RichTextBoxField(Page page, java.awt.Rectangle rect)

**com.aspose.pdf.SaveOptions**

classes internas adicionadas:

public static final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static final class NodeLevelResourceType

public static class ResourceSavingInfo

adicionado:

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value)

public boolean getCloseResponse()

public void setCloseResponse(boolean value)

**com.aspose.pdf.Signature**

adicionado:

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password)

**com.aspose.pdf.SignatureField**

adicionado:

public void sign(Signature signature,InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp**

adicionado:

public double getZoomX()

public void setZoomX(double value)

public double getWidth()

public void setWidth(double value)

public double getHeight()

public void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions**

adicionadas classes internas:

public interface EmbeddedImagesSavingStrategy

public static final class SvgExternalImageType

public static class SvgImageSavingInfo

adicionado:

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving

**com.aspose.pdf.TextParagraph**

adicionado:

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value)

**com.aspose.pdf.TextSearchOptions**

adicionado:

public void isRegularExpressionUsed(boolean value)

**com.aspose.pdf.TextStamp** 

adicionado:

public boolean getWordWrap()

public void setWordWrap(boolean value)

public boolean getJustify()

public void setJustify(boolean value)

public boolean getScale()

public void setScale(boolean value)

public  double getWidth()

public  void setWidth(double value)

public  double getHeight()

public  void setHeight(double value)

**com.aspose.pdf.TextState** 

adicionado:

TextState( java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize)

alterações:

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor() 

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value)

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor() 

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value)

**com.aspose.pdf.TextStyle** 

os próximos métodos foram marcados como @Deprecated:

public void setAlignment(int value)

public int getAlignment() 

adicionado:

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader** 

adicionado:

public static void readAnnotations(InputStream stream, IDocument document)

public static void readFields(InputStream stream, Document document)

public static java.util.Map getElements(XmlReader reader)

alterações:

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags** 

adicionado:

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions** 

adicionado:

public boolean isUseOldXslFoEngine() 

public void setUseOldXslFoEngine(boolean useOldXslFoEngine) 

**com.aspose.pdf.XYZExplicitDestination** 

próximos métodos foram marcados como @Deprecated:

public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

adicionado:

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

Na versão 4.4.0 foram criadas algumas classes "enum" para substituir bibliotecas ms, e a partir da versão 4.6.0, tivemos que remover todas as classes ms do acesso público. Portanto, é necessário usar wrappers internos.

{{% alert color="primary" %}}

**Isso se aplica às seguintes classes:**

com.aspose.pdf.HtmlDocumentTypeInternal - em vez de com.aspose.html.HtmlDocumentType
com.aspose.pdf.ImageFormatInternal - em vez de com.aspose.ms.System.Drawing.Imaging.ImageFormat
com.aspose.pdf.TextEncodingInternal - em vez de com.aspose.ms.System.Text.TextEncoding

{{% /alert %}}