---
title: Cambios en la API Pública en Aspose.PDF para Java 4.6.0
type: docs
weight: 20
url: es/java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista los cambios en la API pública que se introdujeron en Aspose.PDF para Java 4.6.0. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pueda verse como una regresión y modifique el comportamiento existente es especialmente importante y está documentado aquí.

{{% /alert %}}

{{% alert color="primary" %}}

En la última versión 4.6.0, hemos eliminado todas las **ms-classes**. Por lo tanto, es necesario usar envoltorios internos. Esto se aplica a las siguientes clases:

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**Movido**:

com.aspose.pdf.facades.PageSize - a: com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - a: com.aspose.pdf.DocConverter

com.aspose.pdf.ITable - a: com.aspose.pdf.generator.legacyxmlmodel.ITable

com.aspose.pdf.ITableCell - a: com.aspose.pdf.generator.legacyxmlmodel.ITableCell

com.aspose.pdf.ITableRow - a: com.aspose.pdf.generator.legacyxmlmodel.ITableRow

**Añadido**:

paquete com.aspose.pdf.drawing

y las siguientes clases:

com.aspose.pdf.drawing.Arc

com.aspose.pdf.drawing.Circle

com.aspose.pdf.drawing.Curve

com.aspose.pdf.drawing.Graph

com.aspose.pdf.drawing.Line

com.aspose.pdf.drawing.Rectangle

com.aspose.pdf.drawing.Shape

**Añadido**:

paquete com.aspose.pdf.excel

y las siguientes clases:

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

**Clases añadidas:**

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

**Cambios en las siguientes clases:**

com.aspose.pdf.facades.AForm

fue extendido desde SaveableFacade

agregado:

clase pública estática interna FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

los siguientes métodos fueron marcados como @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor 

añadido:

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

los siguientes métodos fueron marcados como @Deprecated:

public String getSrcFileName() 

public void setSrcFileName(String value)

public String getDestFileName() 

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType** 

la clase fue marcada como @Deprecated

añadido:

public String toString()

**com.aspose.pdf.facades.APdfFileEditor** 

añadido:

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean getMergeDuplicateOutlines() // Obtener fusionar esquemas duplicados

public void setMergeDuplicateOutlines(boolean value) // Establecer fusionar esquemas duplicados

public boolean getPreserveUserRights() // Obtener preservar derechos de usuario

public void setPreserveUserRights(boolean value) // Establecer preservar derechos de usuario

public boolean getIncrementalUpdates() // Obtener actualizaciones incrementales

public void setIncrementalUpdates(boolean value) // Establecer actualizaciones incrementales

public boolean getOptimizeSize() // Obtener optimizar tamaño

public void setOptimizeSize(boolean value) // Establecer optimizar tamaño

public static ContentsResizeParameters pageResize(double width, double height) // Redimensionar página

public static ContentsResizeParameters pageResizePct(double widthPct, double heightPct) // Redimensionar página por porcentaje

public boolean concatenate(Document[] src, Document dest) // Concatenar

public void splitToPages(String inputFile, String fileNameTemplate) // Dividir en páginas

public void splitToPages(InputStream inputStream, String fileNameTemplate) // Dividir en páginas

**com.aspose.pdf.facades.APdfFileStamp** 

added: // añadido:
public boolean getOptimizeSize() // Obtener optimizar tamaño

public void setOptimizeSize(boolean value) // Establecer optimizar tamaño

public int getStampId() // Obtener ID de sello

public void setStampId(int value) // Establecer ID de sello

**com.aspose.pdf.facades.AutoFiller** 

implements ISaveableFacade // implementa ISaveableFacade


next methods were marked as @Deprecated: // los siguientes métodos fueron marcados como @Deprecated:

void setOutputStreamInternal(Stream value)

public String getInputFileName() 

public void setInputFileName(String value)

public String getOutputFileName() 

public void setOutputFileName(String value)

public void save()

añadido:
public InputStream getInputStream() 

public void setInputStream(InputStream value)

public void save(String destFile)

public void save(OutputStream destStream)

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void bindPdf(IDocument srcDoc)

public void close()


**com.aspose.pdf.facades.Facade** 

añadido:

public void bindPdf(InputStream srcStream, String password)

**com.aspose.pdf.facades.Form** 

añadido:

internal public static final class ImportStatus

**com.aspose.pdf.facades.FormFieldFacade** 

la siguiente constante fue marcada como @Deprecated:

public static final float BORDER_WIDTH_UNDIFIED = 0;

añadido:

public static final float BORDER_WIDTH_UNDEFINED = -1;


**com.aspose.pdf.facades.PdfAnnotationEditor** 

extends SaveableFacade

añadido:


public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType)


public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor** 

extiende SaveableFacade

**com.aspose.pdf.facades.PdfConverter** 

agregado:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor** 

agregado:

public static final String E_EMPTY_PAGE_RANGE = "El rango de páginas no está configurado";

public static final String E_SMALL_PAGE_RANGE = "El rango de página debe tener dos elementos";

public static final String E_WRONG_PAGE_RANGE = "Rango de página inválido";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)


public boolean resizeContents(InputStream source, OutputStream destination, int[] pages,


public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

extends SaveableFacade

añadido:

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

la siguiente constante fue marcada como @Deprecated:

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

extends SaveableFacade 

los siguientes métodos fueron marcados como @Deprecated:

public void setOutputFile(String value) 


public PdfFileSecurity(String inputFile, String outputFile)

public PdfFileSecurity(IDocument document, String outputFile)

public PdfFileSecurity(IDocument document, OutputStream outputStream)

añadido:

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature**

extiende SaveableFacade

la siguiente constante fue marcada como @Deprecated:

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

añadido:

public void removeSignature(String signName, boolean removeField)

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor**

añadido:

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment()

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType()

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()

la siguiente constante fue marcada como @Deprecated:


public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

eliminado:

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer** 

agregado:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

fue marcado como @Deprecated

**com.aspose.pdf.generator.legacyxmlmodel.EndNote** 

renombrado:
getNumberingContinuation_EndNote_New() a
getNumberingContinuation()
setNumberingContinuation_EndNote_New() a setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image** 

agregado:

public  void load(XmlTextReader xmlReader, LoadingContext context)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

agregado:

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table** 

agregado:

public int getColumnCount()

**com.aspose.pdf.text.Font** 

eliminado ya que duplica com.aspose.pdf.Font 

**com.aspose.pdf.ADocument** 

agregado:

public boolean isPdfaCompliant()

public int getPdfaFormat() 

**com.aspose.pdf.Annotation** 

agregado:

public int getHorizontalAlignment_Annotation_New() 

public void setHorizontalAlignment_Annotation_New(int value)

la siguiente constante fue marcada como @Deprecated:

public int getAlignment() 

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection** 

agregado:

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter** 

agregado:

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact** 

agregado:

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph** 

agregado:

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo** 

cambios:

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

agregado:

public GraphInfo getBottom()

public void setBottom(GraphInfo value) public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

eliminado:

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo** 

renombrado:

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField** 

añadido:

public ButtonField() 

**com.aspose.pdf.CellBorderStyle** 

la clase fue eliminada

**com.aspose.pdf.CheckboxField** 

añadido:

public java.util.ArrayList getAllowedStates()

public String getOnState() 

**com.aspose.pdf.ComboBoxField** 

añadido:

public ComboBoxField()

**com.aspose.pdf.Field** 

añadido:

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination** 

la siguiente constante fue marcada como @Deprecated:

public FitBExplicitDestination(Document document, int pageNumber) 

añadido:

public FitBExplicitDestination(int pageNumber)

**com.aspose.pdf.FitBHExplicitDestination**

el siguiente constante fue marcado como @Deprecated:

public FitBHExplicitDestination(Document document, int pageNumber, double top)

añadido:

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination**

el siguiente constante fue marcado como @Deprecated:

public FitBVExplicitDestination(Document document, int pageNumber, double left)

añadido:

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

el siguiente constante fue marcado como @Deprecated:

public FitHExplicitDestination(Document document, int pageNumber, double top)

añadido:

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination**

el siguiente constante fue marcado como @Deprecated:

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

añadido:

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination** 

la siguiente constante fue marcada como @Deprecated:

public FitVExplicitDestination(Document document, int pageNumber, double left)

añadido:

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository** 
añadido:

public static FontSubstitutionCollection getSubstitutions() 

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream,int fontType)

**com.aspose.pdf.FontSource** 

cambios:

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form** 

cambios:

com.aspose.pdf.Form.getFields_Rename_Namesake() - renombrado a: com.aspose.pdf.Form.getFields;

añadido:

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation** 

añadido:

public int getStartingStyle()

public void setStartingStyle(int value)


public int getEndingStyle()

public void setEndingStyle(int value)

public DefaultAppearance getDefaultAppearanceObject()

**com.aspose.pdf.HtmlSaveOptions** 

se añadieron clases internas:

public static  final class HtmlImageType

public static class HtmlImageSavingInfo

public static class CssSavingInfo

public static class CssUrlRequestInfo

public interface ResourceSavingStrategy

public interface CssUrlMakingStrategy

public interface CssSavingStrategy

**com.aspose.pdf.ImagePlacement**

se añadió:

public int getRotation()

public void save(OutputStream outputStream)

public void save(OutputStream outputStream,ImageFormat format)

**com.aspose.pdf.ListBoxField** 

se añadió:

public ListBoxField()

**com.aspose.pdf.LoadOptions** 

se añadió:

public IWarningCallback getWarningHandler()

public void setWarningHandler

public String ApsIntermediateFileIfAny;

public String XpsIntermediateFileIfAny;

**com.aspose.pdf.MarkupAnnotation** 

se añadió:

public java.util.Date getCreationDate()

**com.aspose.pdf.Matrix** 

se añadió:

public IPdfArray getMatrix(ITrailerable trailer)

**com.aspose.pdf.Page** 

implementa ISupportsMemoryCleanup

agregado:

public void setBackground(Color value) 

**com.aspose.pdf.PageCollection** 

agregado:

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection** 

cambios:

UpdateLabel  -> updateLabel

RemoveLabel -> removeLabel

GetPages      -> getPages

**com.aspose.pdf.PageSize** 

agregado:

public static final float LEAVE_INTACT = -1; 

**com.aspose.pdf.RichTextBoxField** 

agregado:

public RichTextBoxField(Page page, java.awt.Rectangle rect)  

**com.aspose.pdf.SaveOptions** 

clases internas agregadas:

public static  final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static  final class NodeLevelResourceType

public static class ResourceSavingInfo

agregado:

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value) 

public boolean getCloseResponse()

public void setCloseResponse(boolean value) 

**com.aspose.pdf.Signature** 

agregado:

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password) 

**com.aspose.pdf.SignatureField** 

añadido:

public void sign(Signature signature, InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp** 

añadido:

public double getZoomX()

public void setZoomX(double value)

public  double getWidth()

public  void setWidth(double value)

public  double getHeight()

public  void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions** 

clases internas añadidas:

public interface EmbeddedImagesSavingStrategy

public static  final class SvgExternalImageType

public static class SvgImageSavingInfo 

añadido:

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving 

**com.aspose.pdf.TextParagraph** 

añadido:

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value) 

**com.aspose.pdf.TextSearchOptions** 

añadido:

public void isRegularExpressionUsed(boolean value)

**com.aspose.pdf.TextStamp** 

añadido:

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

añadido:

TextState( java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize)

cambios:

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor() 

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value)

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor() 

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value)

**com.aspose.pdf.TextStyle** 

los siguientes métodos fueron marcados como @Deprecated:

public void setAlignment(int value)

public int getAlignment() 

añadido:

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader** 

añadido:

public static  void readAnnotations(InputStream stream,IDocument document)

public static  void readFields(InputStream stream,Document document)

public static java.util.Map getElements(XmlReader reader)

cambios:

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags** 

añadido:

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions** 

añadido:

public boolean isUseOldXslFoEngine() 

public void setUseOldXslFoEngine(boolean useOldXslFoEngine) 

**com.aspose.pdf.XYZExplicitDestination** 

los siguientes métodos fueron marcados como @Deprecated:


public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

agregado:

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

En la versión 4.4.0 se crearon algunas clases "enum" para reemplazar las bibliotecas ms, y a partir de la versión 4.6.0, tuvimos que eliminar todas las ms-clases de acceso público. Por lo tanto, es necesario utilizar envoltorios internos.

{{% alert color="primary" %}}

**Esto se aplica a las siguientes clases:**

com.aspose.pdf.HtmlDocumentTypeInternal - en lugar de com.aspose.html.HtmlDocumentType
com.aspose.pdf.ImageFormatInternal - en lugar de com.aspose.ms.System.Drawing.Imaging.ImageFormat
com.aspose.pdf.TextEncodingInternal - en lugar de com.aspose.ms.System.Text.TextEncoding

{{% /alert %}}