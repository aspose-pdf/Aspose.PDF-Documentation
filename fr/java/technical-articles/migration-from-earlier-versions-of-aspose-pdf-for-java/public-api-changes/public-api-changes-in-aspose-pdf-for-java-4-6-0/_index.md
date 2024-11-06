---
title: Changements de l'API Publique dans Aspose.PDF pour Java 4.6.0
type: docs
weight: 20
url: fr/java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page répertorie les changements de l'API publique qui ont été introduits dans Aspose.PDF pour Java 4.6.0. Elle inclut non seulement les nouvelles méthodes publiques et celles obsolètes, mais aussi une description de tous les changements dans le comportement en coulisses dans Aspose.PDF pour Java qui peuvent affecter le code existant. Tout comportement introduit qui pourrait être considéré comme une régression et modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

{{% alert color="primary" %}}

Dans la dernière version 4.6.0, nous avons supprimé toutes les **ms-classes**. Il est donc nécessaire d'utiliser des wrappers internes.
Cela s'applique aux classes suivantes :

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**Déplacé** :

com.aspose.pdf.facades.PageSize - vers : com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - vers : com.aspose.pdf.DocConverter

com.aspose.pdf.ITable - vers : com.aspose.pdf.generator.legacyxmlmodel.ITable

com.aspose.pdf.ITableCell - vers : com.aspose.pdf.generator.legacyxmlmodel.ITableCell

com.aspose.pdf.ITableRow - vers : com.aspose.pdf.generator.legacyxmlmodel.ITableRow

**Ajouté** :

package com.aspose.pdf.drawing

et les classes suivantes :

com.aspose.pdf.drawing.Arc

com.aspose.pdf.drawing.Circle

com.aspose.pdf.drawing.Curve

com.aspose.pdf.drawing.Graph

com.aspose.pdf.drawing.Line

com.aspose.pdf.drawing.Rectangle

com.aspose.pdf.drawing.Shape

**Ajouté** :

package com.aspose.pdf.excel

et les classes suivantes :

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

**Classes ajoutées :**

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

**Changements dans les classes suivantes :**

com.aspose.pdf.facades.AForm

a été étendu à partir de SaveableFacade

ajouté :

internal public static class FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

les méthodes suivantes ont été marquées comme @Deprecated :

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor 

ajouté :

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

les méthodes suivantes ont été marquées comme @Deprecated :

public String getSrcFileName() 

public void setSrcFileName(String value)

public String getDestFileName() 

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType** 

la classe a été marquée comme @Deprecated

ajouté :

public String toString()

**com.aspose.pdf.facades.APdfFileEditor** 

ajouté :

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean getMergeDuplicateOutlines()

public void setMergeDuplicateOutlines(boolean value)

public boolean getPreserveUserRights()

public void setPreserveUserRights(boolean value)

public boolean getIncrementalUpdates()

public void setIncrementalUpdates(boolean value)

public boolean getOptimizeSize()

public void setOptimizeSize(boolean value)

public static ContentsResizeParameters pageResize(double width, double height)

public static ContentsResizeParameters pageResizePct(double widthPct, double heightPct)

public boolean concatenate(Document[] src, Document dest)

public void splitToPages(String inputFile, String fileNameTemplate)

public void splitToPages(InputStream inputStream, String fileNameTemplate)

**com.aspose.pdf.facades.APdfFileStamp** 

ajouté :
public boolean getOptimizeSize()

public void setOptimizeSize(boolean value)

public int getStampId()

public void setStampId(int value)

**com.aspose.pdf.facades.AutoFiller** 

implémente ISaveableFacade

les méthodes suivantes ont été marquées comme @Deprecated :

void setOutputStreamInternal(Stream value)

public String getInputFileName() 

public void setInputFileName(String value)

public String getOutputFileName() 

public void setOutputFileName(String value)

public void save()

ajouté :
public InputStream getInputStream() 

public void setInputStream(InputStream value)

public void save(String destFile)

public void save(OutputStream destStream)

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void bindPdf(IDocument srcDoc)

public void close()


**com.aspose.pdf.facades.Facade** 

ajouté :

public void bindPdf(InputStream srcStream, String password)

**com.aspose.pdf.facades.Form** 

ajouté :

internal public static final class ImportStatus

**com.aspose.pdf.facades.FormFieldFacade** 

la constante suivante a été marquée comme @Deprecated :

public static final float BORDER_WIDTH_UNDIFIED = 0;

ajouté :

public static final float BORDER_WIDTH_UNDEFINED = -1;


**com.aspose.pdf.facades.PdfAnnotationEditor** 

extends SaveableFacade

ajouté :


public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType)


public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor** 

s'étend de SaveableFacade

**com.aspose.pdf.facades.PdfConverter** 

ajouté :

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor** 

ajouté :

public static final String E_EMPTY_PAGE_RANGE = "Le tableau des plages de pages n'est pas défini";

public static final String E_SMALL_PAGE_RANGE = "Le tableau de la plage de pages doit avoir deux éléments";

public static final String E_WRONG_PAGE_RANGE = "Plage de pages invalide";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)


public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, 


public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

extends SaveableFacade

ajouté :

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

la constante suivante a été marquée comme @Deprecated :

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

extends SaveableFacade 

les méthodes suivantes ont été marquées comme @Deprecated :

public void setOutputFile(String value) 

public PdfFileSecurity(String inputFile, String outputFile)

public PdfFileSecurity(IDocument document, String outputFile)

public PdfFileSecurity(IDocument document, OutputStream outputStream)

ajouté :

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature**

extends SaveableFacade

la constante suivante a été marquée comme @Deprecated :

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

ajouté :

public void removeSignature(String signName, boolean removeField)

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor**

ajouté :

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment()

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType()

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()


la constante suivante a été marquée comme @Deprecated :


public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

supprimé :

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer** 

ajouté :

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

a été marqué comme @Deprecated

**com.aspose.pdf.generator.legacyxmlmodel.EndNote** 

renommé :
getNumberingContinuation_EndNote_New() en
getNumberingContinuation()
setNumberingContinuation_EndNote_New() en setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image** 

ajouté :

public  void load(XmlTextReader xmlReader, LoadingContext context)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

ajouté :

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table** 

ajouté :

public int getColumnCount()

**com.aspose.pdf.text.Font** 

supprimé car il duplique com.aspose.pdf.Font 

**com.aspose.pdf.ADocument** 

ajouté :

public boolean isPdfaCompliant()

public int getPdfaFormat() 

**com.aspose.pdf.Annotation** 

ajouté :

public int getHorizontalAlignment_Annotation_New() 

public void setHorizontalAlignment_Annotation_New(int value)

la constante suivante a été marquée comme @Deprecated :

public int getAlignment() 

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection** 

ajouté :

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter** 

ajouté :

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact** 

ajouté :

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph** 

ajouté :

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo** 

modifications :

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

ajouté :

public GraphInfo getBottom()

public void setBottom(GraphInfo value) public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

supprimé :

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo** 

renommé :

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField** 

ajouté :

public ButtonField() 

**com.aspose.pdf.CellBorderStyle** 

classe a été supprimée

**com.aspose.pdf.CheckboxField** 

ajouté :

public java.util.ArrayList getAllowedStates()

public String getOnState() 

**com.aspose.pdf.ComboBoxField** 

ajouté :

public ComboBoxField()

**com.aspose.pdf.Field** 

ajouté :

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination** 

prochaine constante a été marquée comme @Deprecated :

public FitBExplicitDestination(Document document, int pageNumber) 

ajouté :

public FitBExplicitDestination(int pageNumber)

**com.aspose.pdf.FitBHExplicitDestination** 

la constante suivante a été marquée comme @Deprecated :

public FitBHExplicitDestination(Document document, int pageNumber, double top)

ajouté :

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination** 

la constante suivante a été marquée comme @Deprecated :

public FitBVExplicitDestination(Document document, int pageNumber, double left)

ajouté :

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

la constante suivante a été marquée comme @Deprecated :

public FitHExplicitDestination(Document document, int pageNumber, double top)

ajouté :

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination** 

la constante suivante a été marquée comme @Deprecated :

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

ajouté :

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination** 

la constante suivante a été marquée comme @Deprecated :

public FitVExplicitDestination(Document document, int pageNumber, double left)

ajouté :

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository** 
ajouté :

public static FontSubstitutionCollection getSubstitutions() 

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream, int fontType)

**com.aspose.pdf.FontSource** 

modifications :

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form** 

modifications :

com.aspose.pdf.Form.getFields_Rename_Namesake() - renommé en : com.aspose.pdf.Form.getFields;

ajouté :

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation** 

ajouté :

public int getStartingStyle()

public void setStartingStyle(int value)

public int getEndingStyle()

public void setEndingStyle(int value)

public DefaultAppearance getDefaultAppearanceObject()

**com.aspose.pdf.HtmlSaveOptions** 

ajouté des classes internes :

public static  final class HtmlImageType

public static class HtmlImageSavingInfo

public static class CssSavingInfo

public static class CssUrlRequestInfo

public interface ResourceSavingStrategy

public interface CssUrlMakingStrategy

public interface CssSavingStrategy

**com.aspose.pdf.ImagePlacement**

ajouté :

public int getRotation()

public void save(OutputStream outputStream)

public void save(OutputStream outputStream,ImageFormat format)

**com.aspose.pdf.ListBoxField** 

ajouté :

public ListBoxField()

**com.aspose.pdf.LoadOptions** 

ajouté :

public IWarningCallback getWarningHandler()

public void setWarningHandler

public String ApsIntermediateFileIfAny;

public String XpsIntermediateFileIfAny;

**com.aspose.pdf.MarkupAnnotation** 

ajouté :

public java.util.Date getCreationDate()

**com.aspose.pdf.Matrix** 

ajouté :

public IPdfArray getMatrix(ITrailerable trailer)


**com.aspose.pdf.Page** 

implémente ISupportsMemoryCleanup

ajouté :

public void setBackground(Color value) 

**com.aspose.pdf.PageCollection** 

ajouté :

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection** 

modifications :

UpdateLabel  -> updateLabel

RemoveLabel -> removeLabel

GetPages      -> getPages

**com.aspose.pdf.PageSize** 

ajouté :

public static final float LEAVE_INTACT = -1; 

**com.aspose.pdf.RichTextBoxField** 

ajouté :

public RichTextBoxField(Page page, java.awt.Rectangle rect)  

**com.aspose.pdf.SaveOptions** 

ajouté classes internes :

public static  final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static  final class NodeLevelResourceType

public static class ResourceSavingInfo

ajouté :

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value) 

public boolean getCloseResponse()

public void setCloseResponse(boolean value) 

**com.aspose.pdf.Signature** 

ajouté :

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password)

**com.aspose.pdf.SignatureField**

ajouté :

public void sign(Signature signature, InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp**

ajouté :

public double getZoomX()

public void setZoomX(double value)

public double getWidth()

public void setWidth(double value)

public double getHeight()

public void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions**

ajouté classes internes :

public interface EmbeddedImagesSavingStrategy

public static final class SvgExternalImageType

public static class SvgImageSavingInfo

ajouté :

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving

**com.aspose.pdf.TextParagraph**

ajouté :

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value)

**com.aspose.pdf.TextSearchOptions**

ajouté :

public void isRegularExpressionUsed(boolean value)


**com.aspose.pdf.TextStamp** 

ajouté :

public boolean getWordWrap()

public void setWordWrap(boolean value)

public boolean getJustify()

public void setJustify(boolean value)

public boolean getScale()

public void setScale(boolean value)

public double getWidth()

public void setWidth(double value)

public double getHeight()

public void setHeight(double value)

**com.aspose.pdf.TextState** 

ajouté :

TextState( java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize)

modifications :

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor() 

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value)

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor() 

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value)

**com.aspose.pdf.TextStyle** 

les méthodes suivantes ont été marquées comme @Deprecated :

public void setAlignment(int value)

public int getAlignment()

ajouté :

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader**

ajouté :

public static void readAnnotations(InputStream stream, IDocument document)

public static void readFields(InputStream stream, Document document)

public static java.util.Map getElements(XmlReader reader)

modifications :

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags**

ajouté :

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions**

ajouté :

public boolean isUseOldXslFoEngine()

public void setUseOldXslFoEngine(boolean useOldXslFoEngine)

**com.aspose.pdf.XYZExplicitDestination**

les méthodes suivantes ont été marquées comme @Deprecated :


public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

ajouté :

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

De retour dans la version 4.4.0, certaines classes "enum" ont été créées pour remplacer les bibliothèques ms, et à partir de la version 4.6.0, nous avons dû retirer toutes les classes ms de l'accès public. Il est donc nécessaire d'utiliser des wrappers internes.

{{% alert color="primary" %}}

**Cela s'applique aux classes suivantes :**

com.aspose.pdf.HtmlDocumentTypeInternal - au lieu de com.aspose.html.HtmlDocumentType  
com.aspose.pdf.ImageFormatInternal - au lieu de com.aspose.ms.System.Drawing.Imaging.ImageFormat  
com.aspose.pdf.TextEncodingInternal - au lieu de com.aspose.ms.System.Text.TextEncoding

{{% /alert %}}