---
title: Изменения в публичном API в Aspose.PDF для Java 4.6.0
type: docs
weight: 20
url: /java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения в публичном API, которые были внесены в Aspose.PDF для Java 4.6.0. Она включает не только новые и устаревшие публичные методы, но также описание любых изменений в поведении "за кулисами" в Aspose.PDF для Java, которые могут повлиять на существующий код. Любое введенное поведение, которое может рассматриваться как регрессия и модифицирует существующее поведение, особенно важно и документировано здесь.

{{% /alert %}}

{{% alert color="primary" %}}

В последней версии 4.6.0 мы удалили все **ms-классы**. Поэтому необходимо использовать внутренние обертки.
Это относится к следующим классам:

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**Перемещено**:

com.aspose.pdf.facades.PageSize - в: com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - в: com.aspose.pdf.DocConverter

com.aspose.pdf.ITable  - в: com.aspose.pdf.generator.legacyxmlmodel.ITable 

com.aspose.pdf.ITableCell  - в: com.aspose.pdf.generator.legacyxmlmodel.ITableCell 

com.aspose.pdf.ITableRow  - в: com.aspose.pdf.generator.legacyxmlmodel.ITableRow 

**Добавлено**:

package com.aspose.pdf.drawing 

и следующие классы:

com.aspose.pdf.drawing.Arc 

com.aspose.pdf.drawing.Circle 

com.aspose.pdf.drawing.Curve 

com.aspose.pdf.drawing.Graph 

com.aspose.pdf.drawing.Line 

com.aspose.pdf.drawing.Rectangle 

com.aspose.pdf.drawing.Shape

**Добавлено**:

package com.aspose.pdf.excel

и следующие классы:

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

**Добавлены классы:**

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

**Изменения в следующих классах:**

com.aspose.pdf.facades.AForm

был расширен от SaveableFacade

добавлено:

internal public static class FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

следующие методы были помечены как @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor

добавлено:

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

следующие методы были отмечены как @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType**

класс был отмечен как @Deprecated

добавлено:

public String toString()

**com.aspose.pdf.facades.APdfFileEditor**

добавлено:

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean getMergeDuplicateOutlines() // Получить слияние дублирующих контуров

public void setMergeDuplicateOutlines(boolean value) // Установить слияние дублирующих контуров

public boolean getPreserveUserRights() // Получить сохранение прав пользователей

public void setPreserveUserRights(boolean value) // Установить сохранение прав пользователей

public boolean getIncrementalUpdates() // Получить инкрементные обновления

public void setIncrementalUpdates(boolean value) // Установить инкрементные обновления

public boolean getOptimizeSize() // Получить оптимизацию размера

public void setOptimizeSize(boolean value) // Установить оптимизацию размера

public static ContentsResizeParameters pageResize(double width, double height) // Изменение размера страницы

public static ContentsResizeParameters pageResizePct(double widthPct, double heightPct) // Изменение размера страницы в процентах

public boolean concatenate(Document[] src, Document dest) // Конкатенация документов

public void splitToPages(String inputFile, String fileNameTemplate) // Разделение на страницы

public void splitToPages(InputStream inputStream, String fileNameTemplate) // Разделение на страницы

**com.aspose.pdf.facades.APdfFileStamp** 

added: // добавлено:
public boolean getOptimizeSize() // Получить оптимизацию размера

public void setOptimizeSize(boolean value) // Установить оптимизацию размера

public int getStampId() // Получить идентификатор штампа

public void setStampId(int value) // Установить идентификатор штампа

**com.aspose.pdf.facades.AutoFiller** 

implements ISaveableFacade // реализует ISaveableFacade

next methods were marked as @Deprecated: // следующие методы были отмечены как @Deprecated:

void setOutputStreamInternal(Stream value)

public String getInputFileName() 

public void setInputFileName(String value)

public String getOutputFileName() 

public void setOutputFileName(String value)

public void save()

добавлено:
public InputStream getInputStream() 

public void setInputStream(InputStream value)

public void save(String destFile)

public void save(OutputStream destStream)

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void bindPdf(IDocument srcDoc)

public void close()


**com.aspose.pdf.facades.Facade** 

добавлено:

public void bindPdf(InputStream srcStream, String password)

**com.aspose.pdf.facades.Form** 

добавлено:

internal public static final class ImportStatus

**com.aspose.pdf.facades.FormFieldFacade** 

следующая константа была отмечена как @Deprecated:

public static final float BORDER_WIDTH_UNDIFIED = 0;

добавлено:

public static final float BORDER_WIDTH_UNDEFINED = -1;


**com.aspose.pdf.facades.PdfAnnotationEditor** 

extends SaveableFacade

добавлено:


public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType)

public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor** 

расширяет SaveableFacade

**com.aspose.pdf.facades.PdfConverter** 

добавлено:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor** 

добавлено:

public static final String E_EMPTY_PAGE_RANGE = "Массив диапазонов страниц не установлен";

public static final String E_SMALL_PAGE_RANGE = "Массив диапазона страниц должен содержать два элемента";

public static final String E_WRONG_PAGE_RANGE = "Недопустимый диапазон страниц";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)


public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, 


public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

расширяет SaveableFacade

добавлено:

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

следующая постоянная была помечена как @Deprecated:

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

расширяет SaveableFacade 

следующие методы были помечены как @Deprecated:

public void setOutputFile(String value) 

public PdfFileSecurity(String inputFile, String outputFile)


public PdfFileSecurity(IDocument document, String outputFile)

public PdfFileSecurity(IDocument document, OutputStream outputStream)

добавлено:

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature**

расширяет SaveableFacade

следующая константа была отмечена как @Deprecated:

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

добавлено:

public void removeSignature(String signName, boolean removeField)

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor**

добавлено:

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment()

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType()

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()

следующая константа была отмечена как @Deprecated:

public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

удалено:

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer**

добавлено:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

был отмечен как @Deprecated

**com.aspose.pdf.generator.legacyxmlmodel.EndNote**

переименовано:
getNumberingContinuation_EndNote_New() в getNumberingContinuation()
setNumberingContinuation_EndNote_New() в setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image**

добавлено:

public void load(XmlTextReader xmlReader, LoadingContext context)


**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

добавлено:

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table**

добавлено:

public int getColumnCount()

**com.aspose.pdf.text.Font**

удалено, поскольку дублирует com.aspose.pdf.Font

**com.aspose.pdf.ADocument**

добавлено:

public boolean isPdfaCompliant()

public int getPdfaFormat()

**com.aspose.pdf.Annotation**

добавлено:

public int getHorizontalAlignment_Annotation_New()

public void setHorizontalAlignment_Annotation_New(int value)

следующая константа была помечена как @Deprecated:

public int getAlignment()

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection**

добавлено:

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter** 

добавлено:

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact** 

добавлено:

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph** 

добавлено:

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo** 

изменения:

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

добавлено:

public GraphInfo getBottom()

public void setBottom(GraphInfo value) public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

удалено:

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo** 

переименовано:

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField** 

добавлено:

public ButtonField() 

**com.aspose.pdf.CellBorderStyle** 

класс был удален

**com.aspose.pdf.CheckboxField** 

добавлено:

public java.util.ArrayList getAllowedStates()

public String getOnState() 

**com.aspose.pdf.ComboBoxField** 

добавлено:

public ComboBoxField()

**com.aspose.pdf.Field** 

добавлено:

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination** 

следующая константа была помечена как @Deprecated:

public FitBExplicitDestination(Document document, int pageNumber) 

добавлено:

public FitBExplicitDestination(int pageNumber)

**com.aspose.pdf.FitBHExplicitDestination**

следующая константа была отмечена как @Deprecated:

public FitBHExplicitDestination(Document document, int pageNumber, double top)

добавлено:

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination**

следующая константа была отмечена как @Deprecated:

public FitBVExplicitDestination(Document document, int pageNumber, double left)

добавлено:

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

следующая константа была отмечена как @Deprecated:

public FitHExplicitDestination(Document document, int pageNumber, double top)

добавлено:

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination**

следующая константа была отмечена как @Deprecated:

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

добавлено:

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination** 

следующая константа была отмечена как @Deprecated:

public FitVExplicitDestination(Document document, int pageNumber, double left)

добавлено:

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository** 
добавлено:

public static FontSubstitutionCollection getSubstitutions() 

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream,int fontType)

**com.aspose.pdf.FontSource** 

изменения:

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form** 

изменения:

com.aspose.pdf.Form.getFields_Rename_Namesake() - переименовано в: com.aspose.pdf.Form.getFields;

добавлено:

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation** 

добавлено:

public int getStartingStyle()

public void setStartingStyle(int value)


public int getEndingStyle()

public void setEndingStyle(int value) // Установить стиль окончания

public DefaultAppearance getDefaultAppearanceObject() // Получить объект внешнего вида по умолчанию

**com.aspose.pdf.HtmlSaveOptions** 

добавлены внутренние классы:

public static  final class HtmlImageType // Внутренний класс для типа изображения HTML

public static class HtmlImageSavingInfo // Внутренний класс для информации о сохранении изображения HTML

public static class CssSavingInfo // Внутренний класс для информации о сохранении CSS

public static class CssUrlRequestInfo // Внутренний класс для информации о запросе URL CSS

public interface ResourceSavingStrategy // Интерфейс для стратегии сохранения ресурсов

public interface CssUrlMakingStrategy // Интерфейс для стратегии создания URL CSS

public interface CssSavingStrategy // Интерфейс для стратегии сохранения CSS

**com.aspose.pdf.ImagePlacement**

добавлено:

public int getRotation() // Получить угол поворота

public void save(OutputStream outputStream) // Сохранить в выходной поток

public void save(OutputStream outputStream, ImageFormat format) // Сохранить в выходной поток с указанным форматом изображения

**com.aspose.pdf.ListBoxField** 

добавлено:

public ListBoxField() // Конструктор для поля списка

**com.aspose.pdf.LoadOptions** 

добавлено:

public IWarningCallback getWarningHandler() // Получить обработчик предупреждений

public void setWarningHandler // Установить обработчик предупреждений

public String ApsIntermediateFileIfAny; // Промежуточный файл APS, если имеется

public String XpsIntermediateFileIfAny; // Промежуточный файл XPS, если имеется

**com.aspose.pdf.MarkupAnnotation** 

добавлено:

public java.util.Date getCreationDate() // Получить дату создания

**com.aspose.pdf.Matrix** 

добавлено:

public IPdfArray getMatrix(ITrailerable trailer) // Получить матрицу с трейлером

**com.aspose.pdf.Page** 

реализует ISupportsMemoryCleanup

добавлено:

public void setBackground(Color value) 

**com.aspose.pdf.PageCollection** 

добавлено:

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection** 

изменения:

UpdateLabel  -> updateLabel

RemoveLabel -> removeLabel

GetPages      -> getPages

**com.aspose.pdf.PageSize** 

добавлено:

public static final float LEAVE_INTACT = -1; 

**com.aspose.pdf.RichTextBoxField** 

добавлено:

public RichTextBoxField(Page page, java.awt.Rectangle rect)  

**com.aspose.pdf.SaveOptions** 

добавлены внутренние классы:

public static  final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static  final class NodeLevelResourceType

public static class ResourceSavingInfo

добавлено:

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value) 

public boolean getCloseResponse()

public void setCloseResponse(boolean value) 

**com.aspose.pdf.Signature** 

добавлено:

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password) 

**com.aspose.pdf.SignatureField** 

добавлено:

public void sign(Signature signature, InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp** 

добавлено:

public double getZoomX()

public void setZoomX(double value)

public double getWidth()

public void setWidth(double value)

public double getHeight()

public void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions** 

добавлены внутренние классы:

public interface EmbeddedImagesSavingStrategy

public static final class SvgExternalImageType

public static class SvgImageSavingInfo 

добавлено:

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving 

**com.aspose.pdf.TextParagraph** 

добавлено:

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value) 

**com.aspose.pdf.TextSearchOptions** 

добавлено:

public void isRegularExpressionUsed(boolean value)

**com.aspose.pdf.TextStamp**

добавлено:

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

добавлено:

TextState(java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize)

изменения:

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor()

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value)

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value)

**com.aspose.pdf.TextStyle**

следующие методы были помечены как @Deprecated:

public void setAlignment(int value)

public int getAlignment() 

добавлено:

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader** 

добавлено:

public static void readAnnotations(InputStream stream, IDocument document)

public static void readFields(InputStream stream, Document document)

public static java.util.Map getElements(XmlReader reader)

изменения:

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags** 

добавлено:

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions** 

добавлено:

public boolean isUseOldXslFoEngine() 

public void setUseOldXslFoEngine(boolean useOldXslFoEngine) 

**com.aspose.pdf.XYZExplicitDestination** 

следующие методы были отмечены как @Deprecated:


public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

добавлено:

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

В версии 4.4.0 были созданы некоторые классы "enum", чтобы заменить библиотеки ms, и начиная с выпуска 4.6.0, нам пришлось удалить все классы ms из публичного доступа. Поэтому необходимо использовать внутренние обертки.

{{% alert color="primary" %}}

**Это относится к следующим классам:**

com.aspose.pdf.HtmlDocumentTypeInternal - вместо com.aspose.html.HtmlDocumentType  
com.aspose.pdf.ImageFormatInternal - вместо com.aspose.ms.System.Drawing.Imaging.ImageFormat  
com.aspose.pdf.TextEncodingInternal - вместо com.aspose.ms.System.Text.TextEncoding  

{{% /alert %}}