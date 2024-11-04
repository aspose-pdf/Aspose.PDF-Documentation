---
title: Aspose.PDF for Java 4.6.0 中的公共 API 更改
type: docs
weight: 20
url: /java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了 Aspose.PDF for Java 4.6.0 中引入的公共 API 更改。它不仅包括新的和废弃的公共方法，还包括对 Aspose.PDF for Java 背后的行为进行的任何更改的描述，这些更改可能会影响现有代码。任何被视为回归并修改现有行为的行为尤其重要，并在此记录。

{{% /alert %}}

{{% alert color="primary" %}}

在最新版本 4.6.0 中，我们删除了所有 **ms-classes**。因此，必须使用内部包装器。
这适用于以下类：

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**移动**:

com.aspose.pdf.facades.PageSize - 到: com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - 到: com.aspose.pdf.DocConverter

com.aspose.pdf.ITable  - 到: com.aspose.pdf.generator.legacyxmlmodel.ITable 

com.aspose.pdf.ITableCell  - 到: com.aspose.pdf.generator.legacyxmlmodel.ITableCell 

com.aspose.pdf.ITableRow  - 到: com.aspose.pdf.generator.legacyxmlmodel.ITableRow 

**添加**:

package com.aspose.pdf.drawing 

以及以下类:

com.aspose.pdf.drawing.Arc 

com.aspose.pdf.drawing.Circle 

com.aspose.pdf.drawing.Curve 

com.aspose.pdf.drawing.Graph 

com.aspose.pdf.drawing.Line 

com.aspose.pdf.drawing.Rectangle 

com.aspose.pdf.drawing.Shape

**添加**:

package com.aspose.pdf.excel

以及以下类:

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

**添加的类：**

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

**下述类中的更改：**

com.aspose.pdf.facades.AForm

从 SaveableFacade 扩展

已添加：

internal public static class FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

以下方法标记为 @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor

已添加：

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

以下方法被标记为@Deprecated：

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType**

类被标记为@Deprecated

已添加：

public String toString()

**com.aspose.pdf.facades.APdfFileEditor**

已添加：

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean getMergeDuplicateOutlines() // 获取合并重复轮廓

public void setMergeDuplicateOutlines(boolean value) // 设置合并重复轮廓

public boolean getPreserveUserRights() // 获取保留用户权限

public void setPreserveUserRights(boolean value) // 设置保留用户权限

public boolean getIncrementalUpdates() // 获取增量更新

public void setIncrementalUpdates(boolean value) // 设置增量更新

public boolean getOptimizeSize() // 获取优化大小

public void setOptimizeSize(boolean value) // 设置优化大小

public static ContentsResizeParameters pageResize(double width, double height) // 页面调整大小

public static ContentsResizeParameters pageResizePct(double widthPct, double heightPct) // 页面按百分比调整大小

public boolean concatenate(Document[] src, Document dest) // 合并文档

public void splitToPages(String inputFile, String fileNameTemplate) // 分割成单页

public void splitToPages(InputStream inputStream, String fileNameTemplate) // 分割成单页

**com.aspose.pdf.facades.APdfFileStamp** 

added: // 添加
public boolean getOptimizeSize() // 获取优化大小

public void setOptimizeSize(boolean value) // 设置优化大小

public int getStampId() // 获取印章ID

public void setStampId(int value) // 设置印章ID

**com.aspose.pdf.facades.AutoFiller** 

implements ISaveableFacade // 实现 ISaveableFacade

next methods were marked as @Deprecated: // 以下方法已标记为@Deprecated:
void setOutputStreamInternal(Stream value)

public String getInputFileName() // 获取输入文件名

public void setInputFileName(String value) // 设置输入文件名

public String getOutputFileName() // 获取输出文件名

public void setOutputFileName(String value) // 设置输出文件名

public void save() // 保存

added:
public InputStream getInputStream() // 获取输入流

public void setInputStream(InputStream value) // 设置输入流

public void save(String destFile) // 保存到指定文件

public void save(OutputStream destStream) // 保存到输出流

public void bindPdf(String srcFile) // 绑定PDF文件

public void bindPdf(InputStream srcStream) // 绑定PDF流

public void bindPdf(IDocument srcDoc) // 绑定PDF文档

public void close() // 关闭


**com.aspose.pdf.facades.Facade** // 外观

added:

public void bindPdf(InputStream srcStream, String password) // 使用密码绑定PDF流

**com.aspose.pdf.facades.Form** // 表单

added:

internal public static final class ImportStatus // 内部公共静态最终类导入状态

**com.aspose.pdf.facades.FormFieldFacade** // 表单字段外观

next constant were marked as @Deprecated: // 下一个常量被标记为已弃用：

public static final float BORDER_WIDTH_UNDIFIED = 0; // 未定义边框宽度

added:

public static final float BORDER_WIDTH_UNDEFINED = -1; // 未定义边框宽度


**com.aspose.pdf.facades.PdfAnnotationEditor** // PDF注释编辑器

extends SaveableFacade // 扩展可保存外观

added:

public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType) // 从XFDF流导入注释


public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor** 

继承 SaveableFacade

**com.aspose.pdf.facades.PdfConverter** 

已添加:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor** 

已添加:

public static final String E_EMPTY_PAGE_RANGE = "页面范围数组未设置";

public static final String E_SMALL_PAGE_RANGE = "页面范围数组必须有两个元素";

public static final String E_WRONG_PAGE_RANGE = "无效的页面范围";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)


public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, 


public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

扩展 SaveableFacade

已添加：

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

下一个常量被标记为 @Deprecated：

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

扩展 SaveableFacade 

下一个方法被标记为 @Deprecated：

public void setOutputFile(String value) 

public PdfFileSecurity(String inputFile, String outputFile)

public PdfFileSecurity(IDocument document, String outputFile)

public PdfFileSecurity(IDocument document, OutputStream outputStream)

已添加：

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature**

继承自 SaveableFacade

下一个常量已标记为 @Deprecated：

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

已添加：

public void removeSignature(String signName, boolean removeField)

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor**

已添加：

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment()

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType()

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()

下一个常量已标记为 @Deprecated：

public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

已移除：

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer** 

已添加：

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

被标记为@已弃用

**com.aspose.pdf.generator.legacyxmlmodel.EndNote** 

重命名：
getNumberingContinuation_EndNote_New() 为 getNumberingContinuation()
setNumberingContinuation_EndNote_New() 为 setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image** 

已添加：

public  void load(XmlTextReader xmlReader, LoadingContext context)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

添加：

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table**

添加：

public int getColumnCount()

**com.aspose.pdf.text.Font**

已移除，因为它是 com.aspose.pdf.Font 的重复

**com.aspose.pdf.ADocument**

添加：

public boolean isPdfaCompliant()

public int getPdfaFormat()

**com.aspose.pdf.Annotation**

添加：

public int getHorizontalAlignment_Annotation_New()

public void setHorizontalAlignment_Annotation_New(int value)

以下常量被标记为 @Deprecated：

public int getAlignment()

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection**

添加：

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter** 

添加：

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact** 

添加：

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph** 

添加：

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo** 

变更：

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

添加：

public GraphInfo getBottom()

public void setBottom(GraphInfo value) public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

已移除:

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo** 

已重命名:

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField** 

已添加:

public ButtonField() 

**com.aspose.pdf.CellBorderStyle** 

类已移除

**com.aspose.pdf.CheckboxField** 

已添加:

public java.util.ArrayList getAllowedStates()

public String getOnState() 

**com.aspose.pdf.ComboBoxField** 

已添加:

public ComboBoxField()

**com.aspose.pdf.Field** 

已添加:

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination** 

下一个常量已标记为@Deprecated:

public FitBExplicitDestination(Document document, int pageNumber) 

已添加:

public FitBExplicitDestination(int pageNumber)

**com.aspose.pdf.FitBHExplicitDestination** 

下一个常量被标记为@Deprecated：

public FitBHExplicitDestination(Document document, int pageNumber, double top)

添加：

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination** 

下一个常量被标记为@Deprecated：

public FitBVExplicitDestination(Document document, int pageNumber, double left)

添加：

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

下一个常量被标记为@Deprecated：

public FitHExplicitDestination(Document document, int pageNumber, double top)

添加：

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination** 

下一个常量被标记为@Deprecated：

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

添加：

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination** 

下一个常量被标记为@Deprecated：

public FitVExplicitDestination(Document document, int pageNumber, double left)

新增：

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository** 

新增：

public static FontSubstitutionCollection getSubstitutions() 

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream, int fontType)

**com.aspose.pdf.FontSource** 

更改：

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form** 

更改：

com.aspose.pdf.Form.getFields_Rename_Namesake() - 重命名为：com.aspose.pdf.Form.getFields;

新增：

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation** 

新增：

public int getStartingStyle()

public void setStartingStyle(int value)

public int getEndingStyle()

public void setEndingStyle(int value)

public DefaultAppearance getDefaultAppearanceObject()

**com.aspose.pdf.HtmlSaveOptions** 

添加了内部类：

public static  final class HtmlImageType

public static class HtmlImageSavingInfo

public static class CssSavingInfo

public static class CssUrlRequestInfo

public interface ResourceSavingStrategy

public interface CssUrlMakingStrategy

public interface CssSavingStrategy

**com.aspose.pdf.ImagePlacement**

添加了：

public int getRotation()

public void save(OutputStream outputStream)

public void save(OutputStream outputStream,ImageFormat format)

**com.aspose.pdf.ListBoxField** 

添加了：

public ListBoxField()

**com.aspose.pdf.LoadOptions** 

添加了：

public IWarningCallback getWarningHandler()

public void setWarningHandler

public String ApsIntermediateFileIfAny;

public String XpsIntermediateFileIfAny;

**com.aspose.pdf.MarkupAnnotation** 

添加了：

public java.util.Date getCreationDate()

**com.aspose.pdf.Matrix** 

添加了：

public IPdfArray getMatrix(ITrailerable trailer)

**com.aspose.pdf.Page**

实现 ISupportsMemoryCleanup

已添加：

public void setBackground(Color value)

**com.aspose.pdf.PageCollection**

已添加：

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection**

更改：

UpdateLabel -> updateLabel

RemoveLabel -> removeLabel

GetPages -> getPages

**com.aspose.pdf.PageSize**

已添加：

public static final float LEAVE_INTACT = -1;

**com.aspose.pdf.RichTextBoxField**

已添加：

public RichTextBoxField(Page page, java.awt.Rectangle rect)

**com.aspose.pdf.SaveOptions**

已添加内部类：

public static final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static final class NodeLevelResourceType

public static class ResourceSavingInfo

已添加：

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value)

public boolean getCloseResponse()

public void setCloseResponse(boolean value)

**com.aspose.pdf.Signature**

已添加：

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password) 

**com.aspose.pdf.SignatureField** 

已添加:

public void sign(Signature signature,InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp** 

已添加:

public double getZoomX()

public void setZoomX(double value)

public  double getWidth()

public  void setWidth(double value)

public  double getHeight()

public  void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions** 

添加内部类:

public interface EmbeddedImagesSavingStrategy

public static  final class SvgExternalImageType

public static class SvgImageSavingInfo 

已添加:

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving 

**com.aspose.pdf.TextParagraph** 

已添加:

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value) 

**com.aspose.pdf.TextSearchOptions** 

已添加:

public void isRegularExpressionUsed(boolean value)

**com.aspose.pdf.TextStamp**

已添加：

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

已添加：

TextState(java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize)

更改：

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor()

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value)

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value)

**com.aspose.pdf.TextStyle**

以下方法被标记为@Deprecated：

public void setAlignment(int value)

public int getAlignment()

新增：

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader**

新增：

public static void readAnnotations(InputStream stream,IDocument document)

public static void readFields(InputStream stream,Document document)

public static java.util.Map getElements(XmlReader reader)

更改：

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags**

新增：

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions**

新增：

public boolean isUseOldXslFoEngine()

public void setUseOldXslFoEngine(boolean useOldXslFoEngine)

**com.aspose.pdf.XYZExplicitDestination**

以下方法被标记为@Deprecated：


public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

添加：

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

回到版本4.4.0时创建了一些“枚举”类以替换ms库，从4.6.0版本开始，我们不得不将所有ms类从公共访问中移除。因此，有必要使用内部包装器。

{{% alert color="primary" %}}

**这适用于以下类：**

com.aspose.pdf.HtmlDocumentTypeInternal - 代替 com.aspose.html.HtmlDocumentType
com.aspose.pdf.ImageFormatInternal - 代替 com.aspose.ms.System.Drawing.Imaging.ImageFormat
com.aspose.pdf.TextEncodingInternal - 代替 com.aspose.ms.System.Text.TextEncoding

{{% /alert %}}