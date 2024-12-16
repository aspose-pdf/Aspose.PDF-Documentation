---
title: Aspose.PDF for Java 4.6.0におけるパブリックAPIの変更
type: docs
weight: 20
url: /ja/java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、Aspose.PDF for Java 4.6.0で導入されたパブリックAPIの変更を一覧にしています。新しいパブリックメソッドや廃止されたメソッドだけでなく、Aspose.PDF for Javaの裏での動作における変更も含まれており、既存のコードに影響を及ぼす可能性のあるものが記載されています。既存の動作を変更する可能性がある回帰と見なされる新しい動作は特に重要であり、ここに文書化されています。

{{% /alert %}}

{{% alert color="primary" %}}

最新バージョン4.6.0では、すべての**ms-classes**を削除しました。そのため、内部ラッパーを使用する必要があります。これは次のクラスに適用されます:

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**移動**:

com.aspose.pdf.facades.PageSize - から: com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - から: com.aspose.pdf.DocConverter

com.aspose.pdf.ITable - から: com.aspose.pdf.generator.legacyxmlmodel.ITable

com.aspose.pdf.ITableCell - から: com.aspose.pdf.generator.legacyxmlmodel.ITableCell

com.aspose.pdf.ITableRow - から: com.aspose.pdf.generator.legacyxmlmodel.ITableRow

**追加**:

package com.aspose.pdf.drawing

と次のクラス:

com.aspose.pdf.drawing.Arc

com.aspose.pdf.drawing.Circle

com.aspose.pdf.drawing.Curve

com.aspose.pdf.drawing.Graph

com.aspose.pdf.drawing.Line

com.aspose.pdf.drawing.Rectangle

com.aspose.pdf.drawing.Shape

**追加**:

package com.aspose.pdf.excel

と次のクラス:

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

**追加されたクラス:**

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

**次のクラスの変更点:**

com.aspose.pdf.facades.AForm

SaveableFacadeから拡張されました

追加:

internal public static class FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

次のメソッドは@Deprecatedとしてマークされました:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor

追加:

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

次のメソッドは@Deprecatedとしてマークされました:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType**

クラスは@Deprecatedとしてマークされました

追加:

public String toString()

**com.aspose.pdf.facades.APdfFileEditor**

追加:

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean getMergeDuplicateOutlines() // 重複したアウトラインをマージするかどうかを取得

public void setMergeDuplicateOutlines(boolean value) // 重複したアウトラインをマージするかどうかを設定

public boolean getPreserveUserRights() // ユーザーの権限を保持するかどうかを取得

public void setPreserveUserRights(boolean value) // ユーザーの権限を保持するかどうかを設定

public boolean getIncrementalUpdates() // インクリメンタル更新を行うかどうかを取得

public void setIncrementalUpdates(boolean value) // インクリメンタル更新を行うかどうかを設定

public boolean getOptimizeSize() // サイズを最適化するかどうかを取得

public void setOptimizeSize(boolean value) // サイズを最適化するかどうかを設定

public static ContentsResizeParameters pageResize(double width, double height) // ページのサイズを変更

public static ContentsResizeParameters pageResizePct(double widthPct, double heightPct) // ページのサイズをパーセントで変更

public boolean concatenate(Document[] src, Document dest) // ドキュメントを連結

public void splitToPages(String inputFile, String fileNameTemplate) // ページに分割

public void splitToPages(InputStream inputStream, String fileNameTemplate) // ページに分割

**com.aspose.pdf.facades.APdfFileStamp** 

added:
public boolean getOptimizeSize() // サイズを最適化するかどうかを取得

public void setOptimizeSize(boolean value) // サイズを最適化するかどうかを設定

public int getStampId() // スタンプIDを取得

public void setStampId(int value) // スタンプIDを設定

**com.aspose.pdf.facades.AutoFiller** 

implements ISaveableFacade

next methods were marked as @Deprecated: // 次のメソッドは@Deprecatedとしてマークされています:
void setOutputStreamInternal(Stream value)

public String getInputFileName() 

public void setInputFileName(String value)

public String getOutputFileName() 

public void setOutputFileName(String value)

public void save()

追加:
public InputStream getInputStream() 

public void setInputStream(InputStream value)

public void save(String destFile)

public void save(OutputStream destStream)

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void bindPdf(IDocument srcDoc)

public void close()


**com.aspose.pdf.facades.Facade** 

追加:

public  void bindPdf(InputStream srcStream, String password)

**com.aspose.pdf.facades.Form** 

追加:

internal public static  final class ImportStatus

**com.aspose.pdf.facades.FormFieldFacade** 

次の定数は@Deprecatedとしてマークされました:

public static final float BORDER_WIDTH_UNDIFIED = 0;

追加:

public static final float BORDER_WIDTH_UNDEFINED = -1;


**com.aspose.pdf.facades.PdfAnnotationEditor** 

extends SaveableFacade

追加:


public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType)


public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor** 

extends SaveableFacade

**com.aspose.pdf.facades.PdfConverter** 

追加:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor** 

追加:

public static final String E_EMPTY_PAGE_RANGE = "ページ範囲の配列が設定されていません";

public static final String E_SMALL_PAGE_RANGE = "ページ範囲の配列には2つの要素が必要です";

public static final String E_WRONG_PAGE_RANGE = "無効なページ範囲";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)


public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, 


public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

extends SaveableFacade

追加された:

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

次の定数は@Deprecatedとしてマークされました:

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

extends SaveableFacade 

次のメソッドは@Deprecatedとしてマークされました:

public void setOutputFile(String value) 


public PdfFileSecurity(String inputFile, String outputFile)

public PdfFileSecurity(IDocument document, String outputFile)

public PdfFileSecurity(IDocument document, OutputStream outputStream)

追加:

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature**

extends SaveableFacade

次の定数は @Deprecated としてマークされました:

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

追加:

public void removeSignature(String signName, boolean removeField)

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor**

追加:

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment()

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType()

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()

次の定数は @Deprecated としてマークされました:

public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

削除されました:

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer** 

追加されました:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

@廃止予定としてマークされました

**com.aspose.pdf.generator.legacyxmlmodel.EndNote** 

名前が変更されました:
getNumberingContinuation_EndNote_New() to
getNumberingContinuation()
setNumberingContinuation_EndNote_New() to setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image** 

追加されました:

public  void load(XmlTextReader xmlReader, LoadingContext context)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

追加:

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table** 

追加:

public int getColumnCount()

**com.aspose.pdf.text.Font** 

削除されました、com.aspose.pdf.Fontと重複しているため

**com.aspose.pdf.ADocument** 

追加:

public boolean isPdfaCompliant()

public int getPdfaFormat() 

**com.aspose.pdf.Annotation** 

追加:

public int getHorizontalAlignment_Annotation_New() 

public void setHorizontalAlignment_Annotation_New(int value)

次の定数が@Deprecatedとしてマークされました:

public int getAlignment() 

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection** 

追加:

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter**

追加:

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact**

追加:

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph**

追加:

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo**

変更:

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

追加:

public GraphInfo getBottom()

public void setBottom(GraphInfo value) public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

削除されました：

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo**

名前が変更されました：

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField**

追加されました：

public ButtonField()

**com.aspose.pdf.CellBorderStyle**

クラスが削除されました

**com.aspose.pdf.CheckboxField**

追加されました：

public java.util.ArrayList getAllowedStates()

public String getOnState()

**com.aspose.pdf.ComboBoxField**

追加されました：

public ComboBoxField()

**com.aspose.pdf.Field**

追加されました：

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination**

次の定数が@Deprecatedとしてマークされました：

public FitBExplicitDestination(Document document, int pageNumber)

追加されました：

public FitBExplicitDestination(int pageNumber)

**com.aspose.pdf.FitBHExplicitDestination**

次の定数は@Deprecatedとしてマークされました:

public FitBHExplicitDestination(Document document, int pageNumber, double top)

追加されました:

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination**

次の定数は@Deprecatedとしてマークされました:

public FitBVExplicitDestination(Document document, int pageNumber, double left)

追加されました:

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

次の定数は@Deprecatedとしてマークされました:

public FitHExplicitDestination(Document document, int pageNumber, double top)

追加されました:

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination**

次の定数は@Deprecatedとしてマークされました:

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

追加されました:

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination** 

次の定数は @Deprecated としてマークされています:

public FitVExplicitDestination(Document document, int pageNumber, double left)

追加されました:

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository** 
追加されました:

public static FontSubstitutionCollection getSubstitutions() 

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream,int fontType)

**com.aspose.pdf.FontSource** 

変更:

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form** 

変更:

com.aspose.pdf.Form.getFields_Rename_Namesake() - 名前が変更されました: com.aspose.pdf.Form.getFields();

追加されました:

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation** 

追加されました:

public int getStartingStyle()

public void setStartingStyle(int value)

public int getEndingStyle()

public void setEndingStyle(int 値)

public DefaultAppearance getDefaultAppearanceObject()

**com.aspose.pdf.HtmlSaveOptions** 

内部クラスが追加されました:

public static  final class HtmlImageType

public static class HtmlImageSavingInfo

public static class CssSavingInfo

public static class CssUrlRequestInfo

public interface ResourceSavingStrategy

public interface CssUrlMakingStrategy

public interface CssSavingStrategy

**com.aspose.pdf.ImagePlacement**

追加されました:

public int getRotation()

public void save(OutputStream 出力ストリーム)

public void save(OutputStream 出力ストリーム,ImageFormat 形式)

**com.aspose.pdf.ListBoxField** 

追加されました:

public ListBoxField()

**com.aspose.pdf.LoadOptions** 

追加されました:

public IWarningCallback getWarningHandler()

public void setWarningHandler

public String ApsIntermediateFileIfAny;

public String XpsIntermediateFileIfAny;

**com.aspose.pdf.MarkupAnnotation** 

追加されました:

public java.util.Date getCreationDate()

**com.aspose.pdf.Matrix** 

追加されました:

public IPdfArray getMatrix(ITrailerable トレーラ)

**com.aspose.pdf.Page**

実装 ISupportsMemoryCleanup

追加:

public void setBackground(Color value)

**com.aspose.pdf.PageCollection**

追加:

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection**

変更:

UpdateLabel -> updateLabel

RemoveLabel -> removeLabel

GetPages -> getPages

**com.aspose.pdf.PageSize**

追加:

public static final float LEAVE_INTACT = -1;

**com.aspose.pdf.RichTextBoxField**

追加:

public RichTextBoxField(Page page, java.awt.Rectangle rect)

**com.aspose.pdf.SaveOptions**

内部クラス追加:

public static final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static final class NodeLevelResourceType

public static class ResourceSavingInfo

追加:

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value)

public boolean getCloseResponse()

public void setCloseResponse(boolean value)

**com.aspose.pdf.Signature**

追加:

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password) 

**com.aspose.pdf.SignatureField** 

追加:

public void sign(Signature signature, InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp** 

追加:

public double getZoomX()

public void setZoomX(double value)

public double getWidth()

public void setWidth(double value)

public double getHeight()

public void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions** 

追加された内部クラス:

public interface EmbeddedImagesSavingStrategy

public static final class SvgExternalImageType

public static class SvgImageSavingInfo 

追加:

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving 

**com.aspose.pdf.TextParagraph** 

追加:

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value) 

**com.aspose.pdf.TextSearchOptions** 

追加:

public void isRegularExpressionUsed(boolean value)

**com.aspose.pdf.TextStamp** 

追加:

public boolean getWordWrap() // テキストの折り返しを取得

public void setWordWrap(boolean value) // テキストの折り返しを設定

public boolean getJustify() // テキストの両端揃えを取得

public void setJustify(boolean value) // テキストの両端揃えを設定

public boolean getScale() // スケールを取得

public void setScale(boolean value) // スケールを設定

public  double getWidth() // 幅を取得

public  void setWidth(double value) // 幅を設定

public  double getHeight() // 高さを取得

public  void setHeight(double value) // 高さを設定

**com.aspose.pdf.TextState** 

追加:

TextState( java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize) // テキスト状態の初期化

変更:

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor() // 前景色を取得

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value) // 前景色を設定

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor() // 背景色を取得

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value) // 背景色を設定

**com.aspose.pdf.TextStyle** 

次のメソッドは@Deprecatedとしてマークされました:

public void setAlignment(int value)

public int getAlignment()

追加:

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader**

追加:

public static void readAnnotations(InputStream stream, IDocument document)

public static void readFields(InputStream stream, Document document)

public static java.util.Map getElements(XmlReader reader)

変更:

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags**

追加:

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions**

追加:

public boolean isUseOldXslFoEngine()

public void setUseOldXslFoEngine(boolean useOldXslFoEngine)

**com.aspose.pdf.XYZExplicitDestination**

次のメソッドは@Deprecatedとしてマークされました:


public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

追加:

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

バージョン4.4.0に戻って、msライブラリを置き換えるためにいくつかの「enum」クラスが作成され、リリース4.6.0から、すべてのmsクラスをパブリックアクセスから削除する必要がありました。そのため、内部ラッパーを使用する必要があります。

{{% alert color="primary" %}}

**これは次のクラスに適用されます:**

com.aspose.pdf.HtmlDocumentTypeInternal - com.aspose.html.HtmlDocumentTypeの代わりに
com.aspose.pdf.ImageFormatInternal - com.aspose.ms.System.Drawing.Imaging.ImageFormatの代わりに
com.aspose.pdf.TextEncodingInternal - com.aspose.ms.System.Text.TextEncodingの代わりに

{{% /alert %}}