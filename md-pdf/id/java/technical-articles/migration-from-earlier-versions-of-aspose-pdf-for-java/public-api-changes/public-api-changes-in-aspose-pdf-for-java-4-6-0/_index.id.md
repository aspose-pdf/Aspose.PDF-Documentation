---
title: Perubahan API Publik di Aspose.PDF untuk Java 4.6.0
type: docs
weight: 20
url: /java/public-api-changes-in-aspose-pdf-for-java-4-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan di Aspose.PDF untuk Java 4.6.0. Ini tidak hanya mencakup metode publik baru dan yang usang, tetapi juga deskripsi tentang setiap perubahan dalam perilaku di belakang layar di Aspose.PDF untuk Java yang dapat memengaruhi kode yang ada. Setiap perilaku yang diperkenalkan yang dapat dilihat sebagai regresi dan memodifikasi perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

{{% alert color="primary" %}}

Dalam versi terbaru 4.6.0, kami telah menghapus semua **ms-classes**. Oleh karena itu, perlu menggunakan pembungkus internal.
Ini berlaku untuk kelas-kelas berikut:

com.aspose.ms.System.Drawing.Imaging.ImageFormat -> com.aspose.pdf.ImageFormatInternal

com.aspose.ms.System.Text.TextEncoding -> com.aspose.pdf.TextEncodingInternal

com.aspose.html.HtmlDocumentType -> com.aspose.pdf.HtmlDocumentTypeInternal

{{% /alert %}}

**Pindah**:

com.aspose.pdf.facades.PageSize - ke: com.aspose.pdf.PageSize

com.aspose.doc.wordcore.DocConverter - ke: com.aspose.pdf.DocConverter

com.aspose.pdf.ITable  - ke: com.aspose.pdf.generator.legacyxmlmodel.ITable 

com.aspose.pdf.ITableCell  - ke: com.aspose.pdf.generator.legacyxmlmodel.ITableCell 

com.aspose.pdf.ITableRow  - ke: com.aspose.pdf.generator.legacyxmlmodel.ITableRow 

**Ditambahkan**:

paket com.aspose.pdf.drawing 

dan kelas-kelas berikut:

com.aspose.pdf.drawing.Arc 

com.aspose.pdf.drawing.Circle 

com.aspose.pdf.drawing.Curve 

com.aspose.pdf.drawing.Graph 

com.aspose.pdf.drawing.Line 

com.aspose.pdf.drawing.Rectangle 

com.aspose.pdf.drawing.Shape

**Ditambahkan**:

paket com.aspose.pdf.excel

dan kelas-kelas berikut:

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

**Kelas yang ditambahkan:**

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

**Perubahan pada kelas berikut:**

com.aspose.pdf.facades.AForm

diperluas dari SaveableFacade

ditambahkan:

internal public static class FormImportResult

public FormImportResult[] getImportResult()

public void importXml(InputStream inputXmlStream)

public void extractXfaData(OutputStream outputXmlStream)

public void setXfaData(InputStream inputXmlStream)

public boolean isRequiredField(String fieldName)

public void importXml(InputStream inputXmlStream, boolean IgnoreFormTemplateChanges)

metode berikut ditandai sebagai @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public AForm(String srcFileName, String destFileName)

public AForm(String srcFileName, OutputStream destStream)

public AForm(InputStream srcStream, String destFileName)

public AForm(IDocument document, String destFileName)

com.aspose.pdf.facades.AFormEditor

ditambahkan:

public double getRadioButtonItemSize()

public void setRadioButtonItemSize(double value)

public int getFieldAppearance(String fieldName)

public boolean addFieldScript(String fieldName, String script)

metode berikut ditandai sebagai @Deprecated:

public String getSrcFileName()

public void setSrcFileName(String value)

public String getDestFileName()

public void setDestFileName(String value)

public AFormEditor(String srcFileName, String destFileName)

public void save()

public AFormEditor(IDocument document, String destFileName)

**com.aspose.pdf.facades.AlignmentType**

kelas ditandai sebagai @Deprecated

ditambahkan:

public String toString()

**com.aspose.pdf.facades.APdfFileEditor**

ditambahkan:

public String getConversionLog()

public boolean getMergeDuplicateLayers()

public void setMergeDuplicateLayers(boolean value)

public boolean getMergeDuplicateOutlines() // Mendapatkan apakah menggabungkan garis besar duplikat 

public void setMergeDuplicateOutlines(boolean value) // Mengatur apakah menggabungkan garis besar duplikat

public boolean getPreserveUserRights() // Mendapatkan apakah mempertahankan hak pengguna

public void setPreserveUserRights(boolean value) // Mengatur apakah mempertahankan hak pengguna

public boolean getIncrementalUpdates() // Mendapatkan apakah pembaruan bertahap

public void setIncrementalUpdates(boolean value) // Mengatur apakah pembaruan bertahap

public boolean getOptimizeSize() // Mendapatkan apakah mengoptimalkan ukuran

public void setOptimizeSize(boolean value) // Mengatur apakah mengoptimalkan ukuran

public static ContentsResizeParameters pageResize(double width, double height) // Mengubah ukuran halaman dengan lebar dan tinggi tertentu

public static ContentsResizeParameters pageResizePct(double widthPct, double heightPct) // Mengubah ukuran halaman dengan persentase lebar dan tinggi tertentu

public boolean concatenate(Document[] src, Document dest) // Menggabungkan dokumen sumber ke dalam dokumen tujuan

public void splitToPages(String inputFile, String fileNameTemplate) // Memisahkan dokumen menjadi halaman dengan template nama file

public void splitToPages(InputStream inputStream, String fileNameTemplate) // Memisahkan dokumen dari aliran input menjadi halaman dengan template nama file

**com.aspose.pdf.facades.APdfFileStamp** 

added: // ditambahkan:
public boolean getOptimizeSize() // Mendapatkan apakah mengoptimalkan ukuran

public void setOptimizeSize(boolean value) // Mengatur apakah mengoptimalkan ukuran

public int getStampId() // Mendapatkan ID cap

public void setStampId(int value) // Mengatur ID cap

**com.aspose.pdf.facades.AutoFiller** 

implements ISaveableFacade // mengimplementasikan ISaveableFacade

next methods were marked as @Deprecated: // metode berikut ditandai sebagai @Deprecated:

void setOutputStreamInternal(Stream value)

public String getInputFileName() 

public void setInputFileName(String value)

public String getOutputFileName() 

public void setOutputFileName(String value)

public void save()

ditambahkan:
public InputStream getInputStream() 

public void setInputStream(InputStream value)

public void save(String destFile)

public void save(OutputStream destStream)

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void bindPdf(IDocument srcDoc)

public void close()


**com.aspose.pdf.facades.Facade** 

ditambahkan:

public void bindPdf(InputStream srcStream, String password)

**com.aspose.pdf.facades.Form** 

ditambahkan:

internal public static final class ImportStatus

**com.aspose.pdf.facades.FormFieldFacade** 

konstanta berikut ditandai sebagai @Deprecated:

public static final float BORDER_WIDTH_UNDIFIED = 0;

ditambahkan:

public static final float BORDER_WIDTH_UNDEFINED = -1;


**com.aspose.pdf.facades.PdfAnnotationEditor** 

memperpanjang SaveableFacade

ditambahkan:

public void importAnnotationFromXfdf(InputStream xfdfSteam, int[] annotType)


parameters);

public void importAnnotationFromXfdf(InputStream xfdfSteam)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, String[] annotTypes)

public void exportAnnotationsXfdf(OutputStream xmlOutputStream, int start, int end, int[] annotTypes)

**com.aspose.pdf.facades.PdfBookmarkEditor** 

memperluas SaveableFacade

**com.aspose.pdf.facades.PdfConverter** 

ditambahkan:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileEditor** 

ditambahkan:

public static final String E_EMPTY_PAGE_RANGE = "Rentang halaman tidak diatur";

public static final String E_SMALL_PAGE_RANGE = "Array rentang halaman harus memiliki dua elemen";

public static final String E_WRONG_PAGE_RANGE = "Rentang halaman tidak valid";

public boolean concatenate(Document[] src, Document dest)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, ContentsResizeParameters parameters)

public boolean resizeContents(InputStream source, OutputStream destination, int[] pages, 


public boolean resizeContentsPct(InputStream source, OutputStream destination, int[] pages, double newWidth, double newHeight)

public boolean addMargins(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

public boolean addMarginsPct(InputStream source, OutputStream destination, int[] pages, double leftMargin, double rightMargin, double topMargin, double bottomMargin)

**com.aspose.pdf.facades.PdfFileInfo** 

memperluas SaveableFacade

ditambahkan:

public java.util.Map getHeader() 

public void setHeader(java.util.Map value) 

public void save(OutputStream destStream)  

konstanta berikut ditandai sebagai @Deprecated:

public String getInputFile() 

public void setInputFile(String value)

public InputStream getInputStream() 

public void setInputStream(InputStream value)

**com.aspose.pdf.facades.PdfFileSecurity** 

memperluas SaveableFacade 

metode berikut ditandai sebagai @Deprecated:

public void setOutputFile(String value) 


public PdfFileSecurity(String inputFile, String outputFile)


public PdfFileSecurity(IDocument document, String outputFile) 

public PdfFileSecurity(IDocument document, OutputStream outputStream)

ditambahkan:

public void bindPdf(String srcFile)

public void bindPdf(InputStream srcStream)

public void close()

**com.aspose.pdf.facades.PdfFileSignature** 

extends SaveableFacade

konstanta berikut ditandai sebagai @Deprecated:

public PdfFileSignature(String inputFile)

public PdfFileSignature(String inputFile, String outputFile)

public void save()

ditambahkan:

public void removeSignature(String signName, boolean removeField) 

public java.util.Date getDateTime(String signName)

**com.aspose.pdf.facades.PdfPageEditor** 

ditambahkan:

public java.util.Map getPageRotations()

public java.util.Map getPageRotations()

public int getHorizontalAlignment() 

public void setHorizontalAlignment(int value)

public int getVerticalAlignmentType() 

public void setVerticalAlignmentType(int value)

public java.awt.Rectangle getPageBoxSize(int page, String pageBoxName)

public void applyChanges()

konstanta berikut ditandai sebagai @Deprecated:


public AlignmentType getAlignment()

public void setAlignment(AlignmentType value)

public VerticalAlignmentType getVerticalAlignment()

public void setVerticalAlignment(VerticalAlignmentType value)

dihapus:

public void setAlignment(AlignmentType value)

**com.aspose.pdf.facades.PdfViewer** 

ditambahkan:

public boolean getShowHiddenAreas()

public void setShowHiddenAreas(boolean value)

public int getCopiesPrinted()

public void printLargePdf(InputStream inputStream, PrinterSettings printerSettings)

public void printLargePdf(InputStream inputStream, PageSettings pageSettings, PrinterSettings printerSettings)

public void bindPdf(InputStream srcStream)

**com.aspose.pdf.facades.VerticalAlignmentType**

ditandai sebagai @Deprecated

**com.aspose.pdf.generator.legacyxmlmodel.EndNote** 

diganti nama:
getNumberingContinuation_EndNote_New() menjadi
getNumberingContinuation()
setNumberingContinuation_EndNote_New() menjadi setNumberingContinuation()

**com.aspose.pdf.generator.legacyxmlmodel.Image** 

ditambahkan:

public  void load(XmlTextReader xmlReader, LoadingContext context)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**

ditambahkan:

public int InconsistentXmlImageParamsHandlingType;

**com.aspose.pdf.generator.legacyxmlmodel.Table** 

ditambahkan:

public int getColumnCount()

**com.aspose.pdf.text.Font** 

dihapus karena menggandakan com.aspose.pdf.Font 

**com.aspose.pdf.ADocument** 

ditambahkan:

public boolean isPdfaCompliant()

public int getPdfaFormat() 

**com.aspose.pdf.Annotation** 

ditambahkan:

public int getHorizontalAlignment_Annotation_New() 

public void setHorizontalAlignment_Annotation_New(int value)

konstanta berikut ditandai sebagai @Deprecated:

public int getAlignment() 

public void setAlignment(int value)

**com.aspose.pdf.AnnotationActionCollection** 

ditambahkan:

public PdfAction getOnModifyCharacter()

public void setOnModifyCharacter(PdfAction value)

public PdfAction getOnValidate()

public void setOnValidate(PdfAction value)

public PdfAction getOnFormat()

public void setOnFormat(PdfAction value)

public PdfAction getOnCalculate()

public void setOnCalculate(PdfAction value)

**com.aspose.pdf.ApsToPdfConverter** 

ditambahkan:

public void visitFormFieldButton(ApsButton field)

**com.aspose.pdf.BackgroundArtifact** 

ditambahkan:

public java.awt.Color getBackgroundColor()

public void setBackgroundColor(java.awt.Color value)

**com.aspose.pdf.BaseParagraph** 

ditambahkan:

public int getHorizontalAlignment()

**com.aspose.pdf.BorderInfo** 

perubahan:

public CellBorderStyle getLeft() -> public GraphInfo getLeft()

public void setLeft(CellBorderStyle value) -> public void setLeft(GraphInfo value)

public CellBorderStyle getRight() -> public GraphInfo getRight()

public void setRight(CellBorderStyle value) -> public void setRight(GraphInfo value)

public CellBorderStyle getTop() -> public GraphInfo getTop()

public void setTop(CellBorderStyle value) -> public void setTop(GraphInfo value)

public BorderInfo(int borderSide, CellBorderStyle borderStyle) -> public BorderInfo(int borderSide, GraphInfo borderStyle)

ditambahkan:

public GraphInfo getBottom()

public void setBottom(GraphInfo value) 

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

dihapus:

public CellBorderStyle getBottom()

public void setBottom(CellBorderStyle value)

public double getRoundedBorderRadius()

public void setRoundedBorderRadius(double value)

**com.aspose.pdf.BuildVersionInfo** 

berganti nama:

Assembly_version -> AssemblyVersion

File_version -> FileVersion

**com.aspose.pdf.ButtonField** 

ditambahkan:

public ButtonField() 

**com.aspose.pdf.CellBorderStyle** 

kelas dihapus

**com.aspose.pdf.CheckboxField** 

ditambahkan:

public java.util.ArrayList getAllowedStates()

public String getOnState() 

**com.aspose.pdf.ComboBoxField** 

ditambahkan:

public ComboBoxField()

**com.aspose.pdf.Field** 

ditambahkan:

public int getPageIndex()

public static boolean getFitIntoRectangle()

public static void setFitIntoRectangle(boolean value)

**com.aspose.pdf.FitBExplicitDestination** 

konstanta berikut ditandai sebagai @Deprecated:

public FitBExplicitDestination(Document document, int pageNumber) 

ditambahkan:

public FitBExplicitDestination(int pageNumber)

**com.aspose.pdf.FitBHExplicitDestination**

konstanta berikut ditandai sebagai @Deprecated:

public FitBHExplicitDestination(Document document, int pageNumber, double top)

ditambahkan:

public FitBHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitBVExplicitDestination**

konstanta berikut ditandai sebagai @Deprecated:

public FitBVExplicitDestination(Document document, int pageNumber, double left)

ditambahkan:

public FitBVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FitHExplicitDestination**

konstanta berikut ditandai sebagai @Deprecated:

public FitHExplicitDestination(Document document, int pageNumber, double top)

ditambahkan:

public FitHExplicitDestination(int pageNumber, double top)

**com.aspose.pdf.FitRExplicitDestination**

konstanta berikut ditandai sebagai @Deprecated:

public FitRExplicitDestination(Document document, int pageNumber, double left, double bottom, double right, double top)

ditambahkan:

public FitRExplicitDestination(int pageNumber, double left, double bottom, double right, double top)

**com.aspose.pdf.FitVExplicitDestination**

konstanta berikut ditandai sebagai @Deprecated:

public FitVExplicitDestination(Document document, int pageNumber, double left)

ditambahkan:

public FitVExplicitDestination(int pageNumber, double left)

**com.aspose.pdf.FontRepository**

ditambahkan:

public static FontSubstitutionCollection getSubstitutions()

public static FontSourceCollection getSources()

public static Font openFont(InputStream fontStream, int fontType)

**com.aspose.pdf.FontSource**

perubahan:

public abstract FontDefinition[] getFontDefinitions() - > abstract FontDefinition[] getFontDefinitions()

**com.aspose.pdf.Form**

perubahan:

com.aspose.pdf.Form.getFields_Rename_Namesake() - diubah menjadi: com.aspose.pdf.Form.getFields();

ditambahkan:

public void setType(int value)

public void add(Field field)

public void addFieldAppearance(Field field, int pageNumber, Rectangle rect)

**com.aspose.pdf.FreeTextAnnotation**

ditambahkan:

public int getStartingStyle()

public void setStartingStyle(int value)

public int getEndingStyle()

public void setEndingStyle(int value)

public DefaultAppearance getDefaultAppearanceObject()

**com.aspose.pdf.HtmlSaveOptions** 

ditambahkan kelas dalam:

public static final class HtmlImageType

public static class HtmlImageSavingInfo

public static class CssSavingInfo

public static class CssUrlRequestInfo

public interface ResourceSavingStrategy

public interface CssUrlMakingStrategy

public interface CssSavingStrategy

**com.aspose.pdf.ImagePlacement**

ditambahkan:

public int getRotation()

public void save(OutputStream outputStream)

public void save(OutputStream outputStream, ImageFormat format)

**com.aspose.pdf.ListBoxField** 

ditambahkan:

public ListBoxField()

**com.aspose.pdf.LoadOptions** 

ditambahkan:

public IWarningCallback getWarningHandler()

public void setWarningHandler

public String ApsIntermediateFileIfAny;

public String XpsIntermediateFileIfAny;

**com.aspose.pdf.MarkupAnnotation** 

ditambahkan:

public java.util.Date getCreationDate()

**com.aspose.pdf.Matrix** 

ditambahkan:

public IPdfArray getMatrix(ITrailerable trailer)

**com.aspose.pdf.Page** 

mengimplementasikan ISupportsMemoryCleanup

ditambahkan:

public void setBackground(Color value) 

**com.aspose.pdf.PageCollection** 

ditambahkan:

public int indexOf(Page entity)

**com.aspose.pdf.PageLabelCollection** 

perubahan:

UpdateLabel  -> updateLabel

RemoveLabel -> removeLabel

GetPages      -> getPages

**com.aspose.pdf.PageSize** 

ditambahkan:

public static final float LEAVE_INTACT = -1; 

**com.aspose.pdf.RichTextBoxField** 

ditambahkan:

public RichTextBoxField(Page page, java.awt.Rectangle rect)  

**com.aspose.pdf.SaveOptions** 

menambahkan kelas internal:

public static  final class HtmlBorderLineType

public static class BorderPartStyle

public static class BorderInfo

public static  final class NodeLevelResourceType

public static class ResourceSavingInfo

ditambahkan:

public IWarningCallback getWarningHandler()

public void setWarningHandler(IWarningCallback value) 

public boolean getCloseResponse()

public void setCloseResponse(boolean value) 

**com.aspose.pdf.Signature** 

ditambahkan:

public java.util.Date getDate()

public void setDate(java.util.Date value)

public Signature(InputStream pfx, String password) 

**com.aspose.pdf.SignatureField** 

ditambahkan:

public void sign(Signature signature, InputStream pfx, String pass)

public void clear()

**com.aspose.pdf.Stamp** 

ditambahkan:

public double getZoomX()

public void setZoomX(double value)

public double getWidth()

public void setWidth(double value)

public double getHeight()

public void setHeight(double value)

public double getZoomY()

public void setZoomY(double value)

**com.aspose.pdf.SvgSaveOptions** 

ditambahkan kelas dalam:

public interface EmbeddedImagesSavingStrategy

public static final class SvgExternalImageType

public static class SvgImageSavingInfo 

ditambahkan:

public EmbeddedImagesSavingStrategy CustomStrategyOfEmbeddedImagesSaving 

**com.aspose.pdf.TextParagraph** 

ditambahkan:

public float getSubsequentLinesIndent()

public void setSubsequentLinesIndent(float value) 

**com.aspose.pdf.TextSearchOptions** 

ditambahkan:

public void isRegularExpressionUsed(boolean value)

**com.aspose.pdf.TextStamp** 

ditambahkan:

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

ditambahkan:

TextState( java.awt.Color backgroundColor, java.awt.Color foregroundColor, int fontStyle, Font font, float fontSize)

perubahan:

public java.awt.Color getForegroundColor() -> public com.aspose.pdf.Color getForegroundColor() 

public void setForegroundColor(java.awt.Color value) -> public void setForegroundColor(com.aspose.pdf.Color value)

public java.awt.Color getBackgroundColor() -> public com.aspose.pdf.Color getBackgroundColor() 

public void setBackgroundColor(java.awt.Color value) -> public void setBackgroundColor(com.aspose.pdf.Color value)

**com.aspose.pdf.TextStyle** 

metode berikut ditandai sebagai @Deprecated:

public void setAlignment(int value)

public int getAlignment()

ditambahkan:

public void setHorizontalAlignment(int value)

public int getHorizontalAlignment()

public java.awt.Color getColor()

public void setColor(java.awt.Color value)

**com.aspose.pdf.XfdfReader**

ditambahkan:

public static void readAnnotations(InputStream stream, IDocument document)

public static void readFields(InputStream stream, Document document)

public static java.util.Map getElements(XmlReader reader)

perubahan:

public static void readFields(Stream stream, IDocument document) -> public static void readFields(Stream stream, IDocument document, IList foundFields, IList notFoundFields)

**com.aspose.pdf.XfdfTags**

ditambahkan:

public static final String CalloutLine = "callout-line";

public static final String TextRectangle = "text-recangle";

**com.aspose.pdf.XslFoLoadOptions**

ditambahkan:

public boolean isUseOldXslFoEngine()

public void setUseOldXslFoEngine(boolean useOldXslFoEngine)

**com.aspose.pdf.XYZExplicitDestination**

metode berikut ditandai sebagai @Deprecated:


public XYZExplicitDestination(Document document, int pageNumber, double left, double top, double zoom)

ditambahkan:

public XYZExplicitDestination(int pageNumber, double left, double top, double zoom)

Kembali pada versi 4.4.0 beberapa kelas "enum" dibuat untuk menggantikan pustaka ms, dan mulai dari rilis 4.6.0, kami harus menghapus semua kelas ms tersebut dari akses publik. Oleh karena itu, perlu menggunakan pembungkus internal.

{{% alert color="primary" %}}

**Ini berlaku untuk kelas-kelas berikut:**

com.aspose.pdf.HtmlDocumentTypeInternal - sebagai pengganti com.aspose.html.HtmlDocumentType
com.aspose.pdf.ImageFormatInternal - sebagai pengganti com.aspose.ms.System.Drawing.Imaging.ImageFormat
com.aspose.pdf.TextEncodingInternal - sebagai pengganti com.aspose.ms.System.Text.TextEncoding

{{% /alert %}}