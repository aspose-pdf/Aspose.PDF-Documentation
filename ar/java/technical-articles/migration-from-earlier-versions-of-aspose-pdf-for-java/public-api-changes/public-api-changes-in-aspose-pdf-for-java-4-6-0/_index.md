---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 4.6.0
type: docs
weight: 20
url: /ar/java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة التي تم تقديمها في Aspose.PDF لـ Java 4.6.0. وهي تشمل ليس فقط الطرق العامة الجديدة والمهملة، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF لـ Java والتي قد تؤثر على الكود الموجود. أي سلوك تم تقديمه يمكن اعتباره تراجعًا ويعدل السلوك الموجود هو مهم بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

{{% alert color="primary" %}}

في الإصدار الأحدث 4.6.0، قمنا بإزالة جميع **الفئات ms-classes**. لذلك من الضروري استخدام الأغلفة الداخلية. ينطبق هذا على الفئات التالية:

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**نقل**:

com.aspose.pdf.facades.PageSize - إلى: com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - إلى: com.aspose.pdf.DocConverter

com.aspose.pdf.ITable  - إلى: com.aspose.pdf.generator.legacyxmlmodel.ITable 

com.aspose.pdf.ITableCell  - إلى: com.aspose.pdf.generator.legacyxmlmodel.ITableCell 

com.aspose.pdf.ITableRow  - إلى: com.aspose.pdf.generator.legacyxmlmodel.ITableRow 

**أضيف**:

package com.aspose.pdf.drawing 

والفئات التالية:

com.aspose.pdf.drawing.Arc 

com.aspose.pdf.drawing.Circle 

com.aspose.pdf.drawing.Curve 

com.aspose.pdf.drawing.Graph 

com.aspose.pdf.drawing.Line 

com.aspose.pdf.drawing.Rectangle 

com.aspose.pdf.drawing.Shape

**أضيف**:

package com.aspose.pdf.excel

والفئات التالية:

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

**تمت إضافة الفئات:**

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

**التغييرات في الفئات التالية:**

com.aspose.pdf.facades.AForm

تم تمديده من SaveableFacade

أضيف:

internal public static class FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

تم وضع علامة على الطرق التالية كـ @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor 

أضيفت:

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public  int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

تم وضع علامة على الطرق التالية على أنها @Deprecated:

public String getSrcFileName() 

public void setSrcFileName(String value)

public String getDestFileName() 

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType** 

تم وضع علامة على الصف كـ @Deprecated

أضيفت:

public  String toString()

**com.aspose.pdf.facades.APdfFileEditor** 

أضيفت:

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean getMergeDuplicateOutlines() // الحصول على دمج المخططات المكررة

public void setMergeDuplicateOutlines(boolean value) // تعيين دمج المخططات المكررة

public boolean getPreserveUserRights() // الحصول على الحفاظ على حقوق المستخدم

public void setPreserveUserRights(boolean value) // تعيين الحفاظ على حقوق المستخدم

public boolean getIncrementalUpdates() // الحصول على التحديثات التدريجية

public void setIncrementalUpdates(boolean value) // تعيين التحديثات التدريجية

public boolean getOptimizeSize() // الحصول على تحسين الحجم

public void setOptimizeSize(boolean value) // تعيين تحسين الحجم

public static ContentsResizeParameters pageResize(double width, double height) // تغيير حجم الصفحة

public static ContentsResizeParameters pageResizePct(double widthPct, double heightPct) // تغيير حجم الصفحة بالنسبة المئوية

public boolean concatenate(Document[] src, Document dest) // دمج المستندات

public void splitToPages(String inputFile, String fileNameTemplate) // تقسيم إلى صفحات

public void splitToPages(InputStream inputStream, String fileNameTemplate) // تقسيم إلى صفحات

**com.aspose.pdf.facades.APdfFileStamp** 

added: // أضيفت
public boolean getOptimizeSize() // الحصول على تحسين الحجم

public void setOptimizeSize(boolean value) // تعيين تحسين الحجم

public int getStampId() // الحصول على معرف الختم

public void setStampId(int value) // تعيين معرف الختم

**com.aspose.pdf.facades.AutoFiller** 

implements ISaveableFacade // تنفيذ واجهة ISaveableFacade

next methods were marked as @Deprecated: // تم تمييز الطرق التالية بأنها متقادمة:

 void setOutputStreamInternal(Stream value)

public String getInputFileName() 

public void setInputFileName(String value)

public String getOutputFileName() 

public void setOutputFileName(String value)

public void save()

أضيف:
public InputStream getInputStream() 

public void setInputStream(InputStream value)

public void save(String destFile)

public void save(OutputStream destStream)

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void bindPdf(IDocument srcDoc)

public void close()


**com.aspose.pdf.facades.Facade** 

أضيف:

public  void bindPdf(InputStream srcStream, String password)

**com.aspose.pdf.facades.Form** 

أضيف:

internal public static  final class ImportStatus

**com.aspose.pdf.facades.FormFieldFacade** 

تم وضع الثابت التالي كـ @Deprecated:

public static final float BORDER_WIDTH_UNDIFIED = 0;

أضيف:

public static final float BORDER_WIDTH_UNDEFINED = -1;


**com.aspose.pdf.facades.PdfAnnotationEditor** 

يمتد SaveableFacade

أضيف:


public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType)


public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor** 

يمتد SaveableFacade

**com.aspose.pdf.facades.PdfConverter** 

أضيف:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor** 

أضيف:

public static final String E_EMPTY_PAGE_RANGE = "لم يتم تعيين نطاق الصفحات";

public static final String E_SMALL_PAGE_RANGE = "يجب أن تحتوي مجموعة نطاق الصفحات على عنصرين";

public static final String E_WRONG_PAGE_RANGE = "نطاق الصفحة غير صالح";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)


public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, 


public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

يمتد SaveableFacade

تمت الإضافة:

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

تم وضع العلامة التالية كـ @Deprecated:

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

يمتد SaveableFacade 

تم وضع العلامات التالية كـ @Deprecated:

public void setOutputFile(String value) 

public PdfFileSecurity(String inputFile, String outputFile)

public PdfFileSecurity(IDocument document, String outputFile) 

public PdfFileSecurity(IDocument document, OutputStream outputStream)

تمت الإضافة:

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature** 

يمتد SaveableFacade

تم وضع العلامة التالية على أنها @Deprecated:

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

تمت الإضافة:

public void removeSignature(String signName, boolean removeField) 

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor** 

تمت الإضافة:

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment() 

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType() 

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()


تم وضع العلامة التالية على أنها @Deprecated:


public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

تمت الإزالة:

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer** 

تمت الإضافة:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

تم وضع علامة @Deprecated

**com.aspose.pdf.generator.legacyxmlmodel.EndNote** 

تمت إعادة التسمية:
getNumberingContinuation_EndNote_New() إلى
getNumberingContinuation()
setNumberingContinuation_EndNote_New() إلى setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image** 

تمت الإضافة:

public  void load(XmlTextReader xmlReader, LoadingContext context)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

تمت الإضافة:

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table** 

تمت الإضافة:

public int getColumnCount()

**com.aspose.pdf.text.Font** 

تمت الإزالة لأنه يكرر com.aspose.pdf.Font 

**com.aspose.pdf.ADocument** 

تمت الإضافة:

public boolean isPdfaCompliant()

public int getPdfaFormat() 

**com.aspose.pdf.Annotation** 

تمت الإضافة:

public int getHorizontalAlignment_Annotation_New() 

public void setHorizontalAlignment_Annotation_New(int value)

تم تعليم الثابت التالي كـ @Deprecated:

public int getAlignment() 

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection** 

تمت الإضافة:

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter** 

تمت الإضافة:

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact** 

تمت الإضافة:

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph** 

تمت الإضافة:

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo** 

التغييرات:

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

تمت الإضافة:

public GraphInfo getBottom()

public void setBottom(GraphInfo value) public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

تمت الإزالة:

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo**

تمت إعادة التسمية:

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField**

تمت الإضافة:

public ButtonField()

**com.aspose.pdf.CellBorderStyle**

تمت إزالة الفئة

**com.aspose.pdf.CheckboxField**

تمت الإضافة:

public java.util.ArrayList getAllowedStates()

public String getOnState()

**com.aspose.pdf.ComboBoxField**

تمت الإضافة:

public ComboBoxField()

**com.aspose.pdf.Field**

تمت الإضافة:

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination**

تم وضع العلامة التالية كـ @Deprecated:

public FitBExplicitDestination(Document document, int pageNumber)

تمت الإضافة:

public FitBExplicitDestination(int pageNumber)


**com.aspose.pdf.FitBHExplicitDestination**

تم وضع العلامة التالية على أنها @Deprecated:

public FitBHExplicitDestination(Document document, int pageNumber, double top)

تمت الإضافة:

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination**

تم وضع العلامة التالية على أنها @Deprecated:

public FitBVExplicitDestination(Document document, int pageNumber, double left)

تمت الإضافة:

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

تم وضع العلامة التالية على أنها @Deprecated:

public FitHExplicitDestination(Document document, int pageNumber, double top)

تمت الإضافة:

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination**

تم وضع العلامة التالية على أنها @Deprecated:

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

تمت الإضافة:

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination** 

تم وضع علامة على الثابت التالي كـ @Deprecated:

public FitVExplicitDestination(Document document, int pageNumber, double left)

أضيف:

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository** 
أضيف:

public static FontSubstitutionCollection getSubstitutions() 

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream,int fontType)

**com.aspose.pdf.FontSource** 

التغييرات:

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form** 

التغييرات:

com.aspose.pdf.Form.getFields_Rename_Namesake() - أعيدت تسميته إلى: com.aspose.pdf.Form.getFields;

أضيف:

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation** 

أضيف:

public int getStartingStyle()

public void setStartingStyle(int value)

public int getEndingStyle()

public void setEndingStyle(int value)

public DefaultAppearance getDefaultAppearanceObject()

**com.aspose.pdf.HtmlSaveOptions** 

تمت إضافة الفئات الداخلية:

public static  final class HtmlImageType

public static class HtmlImageSavingInfo

public static class CssSavingInfo

public static class CssUrlRequestInfo

public interface ResourceSavingStrategy

public interface CssUrlMakingStrategy

public interface CssSavingStrategy

**com.aspose.pdf.ImagePlacement**

تمت الإضافة:

public int getRotation()

public void save(OutputStream outputStream)

public void save(OutputStream outputStream,ImageFormat format)

**com.aspose.pdf.ListBoxField** 

تمت الإضافة:

public ListBoxField()

**com.aspose.pdf.LoadOptions** 

تمت الإضافة:

public IWarningCallback getWarningHandler()

public void setWarningHandler

public String ApsIntermediateFileIfAny;

public String XpsIntermediateFileIfAny;

**com.aspose.pdf.MarkupAnnotation** 

تمت الإضافة:

public java.util.Date getCreationDate()

**com.aspose.pdf.Matrix** 

تمت الإضافة:

public IPdfArray getMatrix(ITrailerable trailer)

**com.aspose.pdf.Page**

ينفذ ISupportsMemoryCleanup

أُضيف:

public void setBackground(Color value)

**com.aspose.pdf.PageCollection**

أُضيف:

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection**

التغييرات:

UpdateLabel -> updateLabel

RemoveLabel -> removeLabel

GetPages -> getPages

**com.aspose.pdf.PageSize**

أُضيف:

public static final float LEAVE_INTACT = -1;

**com.aspose.pdf.RichTextBoxField**

أُضيف:

public RichTextBoxField(Page page, java.awt.Rectangle rect)

**com.aspose.pdf.SaveOptions**

أُضيفت الفئات الداخلية:

public static final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static final class NodeLevelResourceType

public static class ResourceSavingInfo

أُضيف:

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value)

public boolean getCloseResponse()

public void setCloseResponse(boolean value)

**com.aspose.pdf.Signature**

أُضيف:

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password) 

**com.aspose.pdf.SignatureField** 

تمت الإضافة:

public void sign(Signature signature, InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp** 

تمت الإضافة:

public double getZoomX()

public void setZoomX(double value)

public  double getWidth()

public  void setWidth(double value)

public  double getHeight()

public  void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions** 

تمت إضافة الفئات الداخلية:

public interface EmbeddedImagesSavingStrategy

public static  final class SvgExternalImageType

public static class SvgImageSavingInfo 

تمت الإضافة:

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving 

**com.aspose.pdf.TextParagraph** 

تمت الإضافة:

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value) 

**com.aspose.pdf.TextSearchOptions** 

تمت الإضافة:

public void isRegularExpressionUsed(boolean value)

**com.aspose.pdf.TextStamp** 

تمت الإضافة:

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

تمت الإضافة:

TextState( java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize)

التغييرات:

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor() 

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value)

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor() 

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value)

**com.aspose.pdf.TextStyle** 

تم وضع علامة على الطرق التالية كـ @Deprecated:

public void setAlignment(int value)

public int getAlignment()

أضيف:

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader**

أضيف:

public static void readAnnotations(InputStream stream,IDocument document)

public static void readFields(InputStream stream,Document document)

public static java.util.Map getElements(XmlReader reader)

التغييرات:

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags**

أضيف:

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions**

أضيف:

public boolean isUseOldXslFoEngine()

public void setUseOldXslFoEngine(boolean useOldXslFoEngine)

**com.aspose.pdf.XYZExplicitDestination**

تم وضع علامة على الطرق التالية كـ @Deprecated:


public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

تمت الإضافة:

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

في الإصدار 4.4.0 تم إنشاء بعض فئات "enum" لاستبدال مكتبات ms، وبدءًا من الإصدار 4.6.0، كان علينا إزالة جميع فئات ms من الوصول العام. لذلك من الضروري استخدام الأغلفة الداخلية.

{{% alert color="primary" %}}

**ينطبق هذا على الفئات التالية:**

com.aspose.pdf.HtmlDocumentTypeInternal - بدلاً من com.aspose.html.HtmlDocumentType
com.aspose.pdf.ImageFormatInternal - بدلاً من com.aspose.ms.System.Drawing.Imaging.ImageFormat
com.aspose.pdf.TextEncodingInternal - بدلاً من com.aspose.ms.System.Text.TextEncoding

{{% /alert %}}