---
title: Perubahan API Publik di Aspose.PDF untuk Java 9.5.0
type: docs
weight: 70
url: id/java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan dalam [Aspose.PDF untuk Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx). Ini mencakup tidak hanya metode publik baru dan yang usang, tetapi juga deskripsi tentang perubahan perilaku di balik layar di Aspose.PDF untuk Java yang mungkin mempengaruhi kode yang ada. Setiap perilaku yang diperkenalkan yang dapat dianggap sebagai regresi dan mengubah perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

**Properti CoordinateType ditambahkan ke PdfViewer dan PdfConverter**<p>
Properti CoordinateType memungkinkan untuk mengatur area yang dapat dicetak ke MediaBox atau CropBox (nilai default)

**Metode SetFieldImage ditambahkan ke kelas XFA:** 

public void SetFieldImage(string fieldName, Stream image)

Contoh:

Cuplikan kode berikut menunjukkan bagaimana cara mengatur gambar untuk bidang formulir XFA:

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

Enumerasi **ReplaceAdjustment** ditambahkan ke kelas **TextReplaceOptions**

Enum ini menyediakan nilai-nilai berikut:

- **None** - Tidak ada aksi, panjang baris dapat berubah
- **AdjustSpaceWidth** - Coba sesuaikan spasi antar kata agar panjang baris tetap

Properti **ReplaceAdjustmentAction** ditambahkan ke kelas **TextReplaceOptions**

Kelas **TextReplaceOptions** memiliki konstruktor baru yang memungkinkan untuk mengatur parameter **ReplaceAdjustment**:

TextReplaceOptions(int adjustment, int scope)

Properti **TextReplaceOptions** ditambahkan ke dalam kelas **TextFragmentAbsorber**

Kelas **Ellipse** diimplementasikan:

Konstruktor:

public Ellipse(float left, float bottom, float width, float height)

Properti:

- Left - nilai float yang menunjukkan posisi kiri dari elips.

- Bottom - nilai float yang menunjukkan posisi bawah dari elips.
- Width - nilai float yang menunjukkan lebar elips.
- Height - nilai float yang menunjukkan tinggi elips.

Contoh:
Cuplikan kode berikut menunjukkan cara menambahkan Elips:

```java
String outFile = "Ellipse.pdf";
Document doc = new Document();
Page page = doc.getPages().add();
Graph canvas = new Graph(400, 100);
page.getParagraphs().add(canvas);
Ellipse ellipse1 = new Ellipse(50, 10, 100, 50);
canvas.getShapes().add(ellipse1);
doc.save(outFile);
```

Kelas **Path** telah diimplementasikan

Konstruktor:

public Path()
public Path(Shape[] shapes)

Properti:

- Shapes - koleksi bentuk

Contoh:
cuplikan kode berikut menunjukkan cara menambahkan Path:

```java
Document doc = new Document();
Page page = doc.getPages().add();
Graph graph = new Graph(100, 400);
page.getParagraphs().add(graph);

Path path = new Path();
path.getGraphInfo().setFillColor ( Color.getRed());
graph.getShapes().add(path);

Line line = new Line(new float[] { 200, 80, 200, 100 });
path.getShapes().add(line);
Arc arc = new Arc(200, 50, 50, 90, 270);
path.getShapes().add(arc);
float[] curPos = arc.getEndPosition();
line = new Line(new float[] { curPos[0], curPos[1], 200, 20 });
path.getShapes().add(line);
arc = new Arc(200, 50, 30, 270, 90);
path.getShapes().add(arc);
doc.Save(outFile);
```


**Kelas HtmlFragment** ditambahkan ke dalam paket com.aspose.pdf*

Konstruktor:

- public HtmlFragment(string text)

Parameter:

- Text - teks HTML
  Properti:
- Text - teks HTML

Contoh:
Potongan kode berikut menunjukkan cara menambahkan fragmen HTML:

```java
Document doc = new Document();
Page page = doc.getPages().add();
HtmlFragment titel = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
titel.setKeptWithNext (true);
titel.getMargin().setBottom (10);
titel.getMargin().setTop (200);
page.getParagraphs().add(titel);
doc.Save(outFile);
```

**Metode ContainsUsageRights()** ditambahkan ke dalam kelas **PdfFileSignature**

**Metode RemoveUsageRights()** ditambahkan ke dalam kelas **PdfFileSignature**

Contoh:

Kode berikut menunjukkan cara menghapus fitur hak penggunaan dari dokumen:

```java
PdfFileSignature pdfSign = new PdfFileSignature();

try

{
    String inputFile = "c:\\36908.pdf";

    String outputFile = "c:\\36908_output.pdf";

    pdfSign.bindPdf(inputFile);

    if (pdfSign.containsUsageRights())

    {
        pdfSign.removeUsageRights();
    }

    pdfSign.getDocument().save(outputFile);
}

finally

{
    pdfSign.dispose();
}
```


**isContainSignature()** method diubah namanya menjadi **ContainsSignature(...)**

- Nama metode sebelumnya tidak dihapus tetapi ditandai sebagai usang untuk dihapus di masa depan.
    **isCoversWholeDocument()** method diubah namanya menjadi **CoversWholeDocument(...)**
- Nama metode sebelumnya tidak dihapus tetapi ditandai sebagai usang untuk dihapus di masa depan.

**Measure** class ditambahkan ke dalam paket **com.aspose.pdf**

Kelas ini menjelaskan sistem koordinat Measure. Anggota kelas Measure:

Konstruktor:

- public Measure(Annotation annotation)

get/set Properti:

- ScaleRatio - Sebuah string teks yang menyatakan rasio skala dari gambar.
- XFormat - Sebuah array format angka untuk pengukuran perubahan sepanjang sumbu x dan, jika Y tidak ada, juga sepanjang sumbu y
- YFormat - Sebuah array format angka untuk pengukuran perubahan sepanjang sumbu y.
- DistanceFormat - Sebuah array format angka untuk pengukuran jarak dalam arah mana pun.
- AreaFormat - Sebuah array format angka untuk pengukuran area.

- AngleFormat - Sebuah array format angka untuk pengukuran sudut.
- SlopeFormat - Sebuah array format angka untuk pengukuran kemiringan garis.
- Origin - Titik yang akan menentukan asal dari sistem koordinat pengukuran dalam koordinat ruang pengguna default.
- XYFactor - Sebuah faktor yang akan digunakan untuk mengkonversi satuan terbesar sepanjang sumbu y ke satuan terbesar sepanjang sumbu x.

**NumberFormat** kelas ditambahkan ke dalam kelas **Measure**

Kelas ini mewakili format angka untuk pengukuran.

Konstruktor:

- public NumberFormat(Measure measure)

get/set Properti:

- UnitLabel - Sebuah string teks yang menentukan label untuk menampilkan satuan.
- ConvresionFactor - Faktor konversi yang digunakan untuk mengalikan nilai dalam satuan parsial dari elemen array format angka sebelumnya untuk mendapatkan nilai dalam satuan format angka ini.
- FractionDisplayment - Dalam cara apa nilai pecahan ditampilkan.
- Precision - Jika FractionDisplayment adalah ShowAsDecimal, nilai ini adalah presisi dari nilai pecahan; Ini harus merupakan kelipatan 10. Default adalah 100.
- Denominator - Jika FractionDisplayment adalah ShowAsFraction, nilai ini adalah penyebut dari pecahan.
 Nilai default adalah 16.
- ForceDenominator - Jika FractionDisplayment adalah ShowAsFraction, nilai ini menentukan apakah pecahan dapat disederhanakan atau tidak. Jika nilainya benar, pecahan mungkin tidak disederhanakan.
- ThousandsSeparator - Teks yang akan digunakan antara urutan ribuan dalam tampilan nilai numerik. String kosong menunjukkan bahwa tidak ada teks yang akan ditambahkan. Default adalah koma.
- FractionSeparator - Teks yang akan digunakan sebagai posisi desimal dalam menampilkan nilai numerik. String kosong menunjukkan bahwa default akan digunakan. Default adalah karakter titik.
- BeforeText - Teks yang akan dikonkatenasi di sebelah kiri label.
- AfterText - Teks yang akan dikonkatenasi setelah label.

Enumerasi **FractionStyle** ditambahkan ke dalam kelas **NumberFormat**

Nilai FractionStyle:

- ShowAsDecimal - Menampilkan nilai pecahan sebagai pecahan desimal.
- ShowAsFraction - Menampilkan nilai pecahan sebagai pecahan.
- Round - Membulatkan nilai pecahan ke bilangan bulat terdekat.
- Truncate - Memotong untuk mencapai satuan utuh.

Kelas **NumberFormatList** ditambahkan ke dalam kelas **Measure**
The class represents Represents list of number formats.

Konstruktor:

- public NumberFormatList(Measure measure)

Properti:

- get_Item(int) dan set_Item(int index, NumberFormat value) - Mendapatkan atau mengatur format angka dalam daftar berdasarkan indeksnya.
- getCount()- Menghitung item dalam daftar.

Metode:

- public void add(NumberFormat value)
- Menambahkan format angka ke daftar.
- public void insert(int index, NumberFormat value)
- Menyisipkan format angka ke dalam daftar.
- public void removeAt(int index)
- Menghapus format angka dari daftar.

Properti **Measure** ditambahkan ke kelas **LineAnnotation** dan **PolyLineAnnotation**.

Contoh:

Contoh berikut menunjukkan cara menggunakan Measure dengan LineAnnotation:

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//atur parameter garis ekstensi.
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//atur akhir garis
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//buat elemen Measure
line.setMeasure(new Measure(line));<p>
line.getMeasure().setDistanceFormat(new Measure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//teks garis ukuran
line.setContents("155 mm");
//ini harus diatur untuk menampilkan teks.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


Contoh berikut menunjukkan cara menggunakan Measure dengan PolylineAnnotation:

```java
 Document doc = new Document("source.pdf");

Point[] vertices = new Point[]

{


new Point(100, 600),

new Point(500, 600),

new Point(500, 500),

new Point(400, 300),

new Point(100, 500),

new Point(100, 600)

};

Rectangle rect = new Rectangle(100, 500, 500, 600);
//area atau garis keliling
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
//gaya garis dapat diatur untuk garis keliling.
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

Cuplikan kode berikut menunjukkan cara membaca properti Measure:

```java
//baca properti Measure

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**Perubahan signifikan** - Properti PdfPageEditor.Pages diubah namanya menjadi **ProcessPages**

Cuplikan kode berikut menunjukkan penggunaan properti tersebut (mengatur koefisien zoom untuk halaman #1 dari dokumen):

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**Perubahan besar** - Properti RichTextBoxField.RValue diubah namanya menjadi **RichTextValue**

Cuplikan kode berikut menunjukkan contoh di mana field yang diubah namanya digunakan:

```java
Document doc = new Document("input.pdf");

RichTextBoxField rt = new RichTextBoxField(doc.getPages().get_Item(1), new Rectangle(50, 600, 250, 650));
rt.setPartialName("rt");
doc.getForm().add(rt);
doc.save("34834.pdf");
Document doc1 = new Document("34834.pdf");
((RichTextBoxField)doc1.getForm().get("rt")).setRichTextValue("<p>Ini adalah <b>paragraf</b> saya</p>");

doc1.save("output.pdf");
```

Opsi **InsertBlankColumnAtFirst** ditambahkan ke dalam **kelas ExcelSaveOptions**

Cuplikan kode berikut menunjukkan cara menekan kemunculan kolom kosong pertama:

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

Properti **PageInfo** ditambahkan ke dalam **kelas SvgLoadOptions**.

Cuplikan kode berikut menunjukkan cara menggunakan SvgLoadOptions dan mengatur info margin dengan properti PageInfo:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
options.getPageInfo().getMargin().setTop(0);
options.getPageInfo().getMargin().setLeft(0);
options.getPageInfo().getMargin().setBottom(0);
options.getPageInfo().getMargin().setRight(0);
String inFile = "35730.svg";
String outFile = "35730.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```

Enumerasi **ConversionEngines** ditambahkan ke kelas **SvgLoadOptions**.

Nilai-nilai berikut didefinisikan:

- **LegacyEngine** - mesin lama dari pemrosesan Svg
- **NewEngine** - mesin pemrosesan Svg baru

Properti **ConversionEngine** ditambahkan ke kelas **SvgLoadOptions**

LegacyEngine masih menjadi nilai default karena NewEngine sedang dalam tahap pengujian B. Cuplikan kode berikut menunjukkan contoh cara menggunakan mesin baru:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**Properti ColumnAdjustment** ditambahkan ke dalam kelas **Table**

Enumerasi ColumnAdjustment ditambahkan ke dalam paket com.aspose.pdf

nilai-nilai berikut ditambahkan:

- **Customized** - Pengguna mengatur ColumnWidth secara manual.
- **AutoFitToContent** - Melakukan penyesuaian otomatis ke konten

**Properti ColumnAdjustment** ditambahkan ke dalam kelas **Table**

Nilai default adalah Customized.

Cuplikan kode berikut menunjukkan contoh penggunaan properti ColumnAdjustment:

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**Properti MinimizeTheNumberOfWorksheets** diperkenalkan ke dalam objek **ExcelSaveOptions**.

Cuplikan kode berikut menunjukkan cara meminimalkan jumlah lembar kerja yang mungkin:

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//Tetapkan properti ini ke true
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**Nilai Default** ditambahkan ke enumerasi **PageLayout**.

Cuplikan kode berikut mengatur PageLayout ke nilai Default:

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout (PageLayout.Default);
doc1.save("output.pdf");
```

Dukungan **Ujung Membulat** telah diimplementasikan untuk **InkAnnotation**

Enumerasi **CapStyle** ditambahkan ke dalam paket **com.aspose.pdf**
Nilai-nilai berikut ada

- **Rectangular** - Nilai yang ditentukan sebagai default
- **Rounded** - sudut membulat
- Properti **CapStyle** ditambahkan ke kelas **InkAnnotation**

Cuplikan kode berikut menunjukkan cara mengatur sudut InkAnnotation sebagai membulat:

```java
Document doc = new Document("PdfWithText.pdf");
Page pdfPage = doc.getPages().get_Item(1);
java.awt.Rectangle drect = new java.awt.Rectangle();
drect.height = (int)pdfPage.getRect().getHeight();
drect.width = (int)pdfPage.getRect().getWidth();
drect.x = 0;
drect.y = 0;
com.aspose.pdf.Rectangle arect = com.aspose.pdf.Rectangle.fromRect(drect);
java.util.ArrayList inkList = new java.util.ArrayList();
com.aspose.pdf.Point[] arrpt = new com.aspose.pdf.Point[3];
inkList.add(arrpt);
arrpt[0] = new Point(100, 800);
arrpt[1] = new Point(200, 800);
arrpt[2] = new Point(200, 700);
InkAnnotation ia = new InkAnnotation(pdfPage, arect, inkList);
ia.setTitle("XXX");
ia.setColor(Color.getLightBlue());
ia.setCapStyle(CapStyle.Rounded);
Border border = new Border(ia);
border.setWidth(25);
ia.setOpacity(0.5);
pdfPage.getAnnotations().add(ia);
doc.save("37071.pdf");
```


**PDFNEWJAVA-33498** - Memberikan dukungan untuk menambahkan Gambar dari BufferedImage ke dalam dokumen PDF

Cuplikan kode berikut menunjukkan penambahan Gambar dari BufferedImage:

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - Konversi PDF ke HTML: Untuk menentukan folder gambar

Cuplikan kode berikut menunjukkan cara menentukan folder gambar:

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - Mengatur DPI/PPI gambar dalam PDF

Cuplikan kode berikut menunjukkan cara mengubah resolusi gambar dalam file pdf:

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
//menguji pembuatan pdf
Document doc = new Document();
Page page = doc.getPages().add();
com.aspose.pdf.Image image1 = new com.aspose.pdf.Image();
image1.setImageStream(in);
image1.setFixHeight(page.getMediaBox().getHeight()/4);
image1.setFixWidth(page.getMediaBox().getWidth()/2);
NewParagraphPlacementInfo placementInfo = new NewParagraphPlacementInfo();
placementInfo.setStartNewPage(true);
page.getParagraphs().add(image1, placementInfo);
page.getPageInfo().getMargin().setLeft(5);
page.getPageInfo().getMargin().setRight(0);
page.getPageInfo().getMargin().setTop(0);
page.getPageInfo().getMargin().setBottom(0);
doc.save(out);
```


```java
//perubahan resolusi gambar internal
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//definisikan resolusi horizontal dan vertikal
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**Ringkasan:**

**Kelas yang Ditambahkan:**

- com.aspose.pdf.drawing.Ellipse
- com.aspose.pdf.drawing.Path
com.aspose.pdf.generator.legacyxmlmodel.BookmarkIncludeType
- com.aspose.pdf.generator.legacyxmlmodel.BorderSide
- com.aspose.pdf.generator.legacyxmlmodel.ColumnInfo
- com.aspose.pdf.generator.legacyxmlmodel.HeaderFooterType
- com.aspose.pdf.generator.legacyxmlmodel.HtmlInfo
- com.aspose.pdf.generator.legacyxmlmodel.ImportOptions
- com.aspose.pdf.generator.legacyxmlmodel.MediaType
- com.aspose.pdf.generator.legacyxmlmodel.PathArea
- com.aspose.pdf.generator.legacyxmlmodel.TableFormatInfo

- com.aspose.pdf.AutoDetectedFormatLoadOptions

- com.aspose.pdf.CapStyle
- com.aspose.pdf.ColumnAdjustment
- com.aspose.pdf.ComHelper
- com.aspose.pdf.EpubLoadOptions
- com.aspose.pdf.EpubSaveOptions
- com.aspose.pdf.FileFontSource
- com.aspose.pdf.FontAbsorber
- com.aspose.pdf.HtmlFragment
- com.aspose.pdf.Measure
- com.aspose.pdf.MemoryFontSource

## Perubahan dalam kelas:

**com.aspose.pdf.facades.Form**

Perubahan:

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**
Ditambahkan:

- public int getCoordinateType()
- public void setCoordinateType(int value)
  Tidak digunakan lagi:
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**
Perubahan:

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value

**com.aspose.pdf.facades.PdfFileSignature**
Deprikasi:

- public boolean isContainSignature()
- public boolean isCoversWholeDocument(String signName)
  Ditambahkan:
- public boolean containsSignature()
- public boolean containsUsageRights()
- public void removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor**
Perubahan:

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages()
- public void setPages(int[] value) -> public void setProcessPages(int[] value)
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations()
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer**
Deprikasi:

- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)
  Ditambahkan:
- public int getCoordinateType()
- public void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata**
Perubahan:

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment** Ditambahkan:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo** Ditambahkan:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- Status Deprecated dihapus dari kelas

**com.aspose.pdf.generator.legacyxmlmodel.Cell** Ditambahkan:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter** Ditambahkan:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading** Status Deprecated dihapus dari:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image** Ditambahkan:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts** Ditambahkan:

- public void remove(Cell jsToRemove)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
Ditambahkan:

- public boolean DigitSubstitution
- public boolean IsAutoFontAdjusted
- public boolean IsBuffered
- public InputStream TruetypeFontMapStream
- public boolean IsImageNotFoundErrorIgnored
- public boolean Linearized;
- public int getPageCount()
- public void save(OutputStream output)
- public byte[] getBuffer()
- public void save(String pdfFile)
- public void bindXML(String xmlFile, String xslFileIfAny)
- public void bindXML(InputStream xmlStream, InputStream xslStream)
- public void setUnicode()
- public Object getObjectByID(String ID)
- public HtmlInfo HtmlInfo

Ditambahkan yang Tidak Digunakan Lagi:

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**
Ditambahkan:

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**
Ditambahkan:

- public void add(Paragraph paragraph)
- void addHeading(Paragraf paragraf)
- public int indexOf(Paragraf paragraf)
- public void copyTo(Paragraf[] paraArray, int index)
- public void insert(Paragraf paragrafUntukDisisipkanSetelah, Paragraf paragrafBaru)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
Diubah:

- DefaultCellTextInfo menjadi bidang getter dan setter  
  Ditambahkan:
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public Object deepClone()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
Ditambahkan:

- public ColumnInfo ColumnInfo
- public int getPageCount()
- public void setPageCount(int value)
- public String BreakParaText
- public Object deepClone()
- public Object completeClone()
- public HeaderFooter insertHeader(int type)
- public HeaderFooter insertFooter(int type)
- public Object getObjectByID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
Ditambahkan:

- public Sections()
- public Section add()
- public void insert(int index, Section section)

- public void insert(Section sectionUntukDisisipkanSetelah, Section sectionBaru)
- public void remove(Section sectionToRemove)  
- public void copyTo(Section[] secArray, int index)  
- public int indexOf(Section section)  
- public void set_Item(int index, Section value)  
- public Section get_Item(String sectionID)  
- public void set_Item(String sectionID, Section value)  

**com.aspose.pdf.generator.legacyxmlmodel.Security**  
Ditambahkan:  

- public boolean isDefaultAllAllowed()  
- public void setDefaultAllAllowed(boolean value)  

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**  
Ditambahkan:  

- public void add(Shape shape)  
- public void remove(Shape shapeToRemove)  
- public void copyTo(Shape[] shapeArray, int index)  
- public int indexOf(Shape shape)  

**com.aspose.pdf.generator.legacyxmlmodel.Table**  
Diubah:  

- FixedWidth menjadi field getter dan setter  
- DefaultCellTextInfo menjadi field getter dan setter  
  Ditambahkan:  
- public float getFixedWidth()  
- public void setFixedWidth(float value)  
- public TextInfo getDefaultCellTextInfo()  
- public void setDefaultCellTextInfo(TextInfo value)  

- public Cell getCell(int row, int column, boolean isTableChanged)  
 - public void formatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)
- public void formatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)
- public void formatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)
- public void setColumnWidth(int columnNumber, float width)
- public String getColumnWidths()
- public void setColumnWidths(String value)

**com.aspose.pdf.generator.legacyxmlmodel.TabStops**  
Ditambahkan:

- public int getCapacity()
- public void setCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
Diubah:

- Daftar berikut dari bidang diubah menjadi bidang getter dan setter terpisah:

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


Ditambahkan:

- public float getFontSize()
- public void setFontSize(float value)
- public String getFontName()
- public void setFontName(String value)
- public String getTruetypeFontFileName()
- public void setTruetypeFontFileName(String value)
- public boolean isUnicode()
- public void setUnicode(boolean value)
- public String getFontAfmFile()
- public void setFontAfmFile(String value)
- public String getFontPfmFile()
- public void setFontPfmFile(String value)
- public String getFontOutlineFile()
- public void setFontOutlineFile(String value)
- public String getFontEncodingFile()
- public void setFontEncodingFile(String value)
- public boolean isTrueTypeFontBold()
- public void setTrueTypeFontBold(boolean value)
- public boolean isTrueTypeFontItalic()
- public void setTrueTypeFontItalic(boolean value)
- public String getFontEncoding()
- public void setFontEncoding(String value)
- public boolean isFontEmbedded()
- public void setFontEmbedded(boolean value)
- public boolean isUnderline()

- public void setUnderline(boolean value)
- publik boolean isOverline()
- publik void setOverline(boolean value)
- publik float getCharSpace()
- publik void setCharSpace(float value)
- publik float getWordSpace()
- publik void setWordSpace(float value)
- publik float getLineSpacing()
- publik void setLineSpacing(float value)
- publik float getOverlineOffset()
- publik void setOverlineOffset(float value)
- publik float getUnderlineOffset()
- publik void setUnderlineOffset(float value)
- publik int getRenderingMode()
- publik void setRenderingMode(int value)
- publik Color getColor()
- publik void setColor(Color value)
- publik Color getBackgroundColor()
- publik void setBackgroundColor(Color value)
- publik boolean isRightToLeft()
- publik void setRightToLeft(boolean value)
- publik float getStrokeWidth()
- publik void setStrokeWidth(float value)
- publik Color getStrokeColor()
- publik void setStrokeColor(Color value)
- publik boolean isBaseline()
- publik void setBaseline(boolean value)
- publik int getAlignment()

- publik void setAlignment(int value)

**com.aspose.pdf.BaseOperatorCollection**  
Perubahan:

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border**  
Perubahan:

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value)  
  Ditambahkan Deprecated:
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils**  
Perubahan:

- Internalized

**com.aspose.pdf.ExcelSaveOptions**  
Ditambahkan:

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font**  
Ditambahkan:

- public void save(OutputStream stream)

**com.aspose.pdf.Form**  
Ditambahkan:

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:**  
Ditambahkan:


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**
Ditambahkan:

- public int getCapStyle()
- public void setCapStyle(int value)

**com.aspose.pdf.LineAnnotation**
Ditambahkan:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.LoadFormat:**
Perubahan:

- public static final int InfoPath - dihapus
- public static final int AutoDetect - Ditambahkan

**com.aspose.pdf.Metadata**
Perubahan:

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields() 

**com.aspose.pdf.PageLayout**
Ditambahkan:

- public static final int Default

**com.aspose.pdf.PolylineAnnotation**
Ditambahkan:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.PopupAnnotation**
Ditambahkan:

- public MarkupAnnotation getParent()
- public void setParent(MarkupAnnotation value)

**com.aspose.pdf.RichTextBoxField**
Perubahan:

- public String getRValue() -> public String getRichTextValue()

- public void setRValue(String value) -> public void setRichTextValue(String value)

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
Ditambahkan:

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
Ditambahkan:

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
Ditambahkan:

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
Ditambahkan:

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
Ditambahkan:

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
Ditambahkan:

- public void setFieldImage(String fieldName, InputStream image)