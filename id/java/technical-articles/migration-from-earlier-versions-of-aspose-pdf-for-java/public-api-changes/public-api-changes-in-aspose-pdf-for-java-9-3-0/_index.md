---
title: Perubahan API Publik di Aspose.PDF untuk Java 9.3.0
type: docs
weight: 50
url: id/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan di [Aspose.PDF untuk Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx). Ini tidak hanya mencakup metode publik baru dan yang sudah usang, tetapi juga deskripsi perubahan dalam perilaku di belakang layar di Aspose.PDF untuk Java yang dapat mempengaruhi kode yang ada. Setiap perilaku baru yang dapat dilihat sebagai kemunduran dan memodifikasi perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

## Kelas Ditambahkan:

com.aspose.pdf.MemoryCleaner
com.aspose.pdf.generator.legacy.CmykColorSpace
com.aspose.pdf.generator.legacy.GrayColorSpace
com.aspose.pdf.generator.legacyxmlmodel.ClippingPath
com.aspose.pdf.generator.legacyxmlmodel.ColouredTilingPattern

com.aspose.pdf.generator.legacyxmlmodel.CompareValidator
com.aspose.pdf.generator.legacyxmlmodel.PolaSilang
com.aspose.pdf.generator.legacyxmlmodel.ValidatorKustom
com.aspose.pdf.generator.legacyxmlmodel.Fungsi
com.aspose.pdf.generator.legacyxmlmodel.FungsiInterpolasiEksponensial
com.aspose.pdf.generator.legacyxmlmodel.GradasiBayanganAksial
com.aspose.pdf.generator.legacyxmlmodel.GradasiBayanganRadial
com.aspose.pdf.generator.legacyxmlmodel.PolaGoresan
com.aspose.pdf.generator.legacyxmlmodel.PolaGambar
com.aspose.pdf.generator.legacyxmlmodel.PolaTitik
com.aspose.pdf.generator.legacyxmlmodel.ValidatorRentang
com.aspose.pdf.generator.legacyxmlmodel.ValidatorEkspresiReguler
com.aspose.pdf.generator.legacyxmlmodel.ValidatorKolomDiperlukan
com.aspose.pdf.generator.legacyxmlmodel.PolaGradasiBayangan
com.aspose.pdf.generator.legacyxmlmodel.PolaBayangan
com.aspose.pdf.generator.legacyxmlmodel.PabrikPolaBayangan
com.aspose.pdf.generator.legacyxmlmodel.PolaUbin
com.aspose.pdf.generator.legacyxmlmodel.PolaUbinTakBerwarna

com.aspose.pdf.Artifact.ArtifactType
com.aspose.pdf.Artifact.ArtifactSubtype  
com.aspose.pdf.ILicenseProvider  
com.aspose.pdf.Layer  
com.aspose.pdf.LettersPositioningMethods  

## Kelas Enumerasi Ditambahkan:

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
Penggunaan kelas enumerasi yang diterapkan: **TextEncodingInternal** dan **ImageFormatInternal**

## kelas Dihapus:

Kelas com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType yang sudah usang telah dihapus.

## kelas Dipindahkan:

Kelas dari paket **com.aspose.pdf.generator.legacyxmlmodel.enums** dipindahkan ke paket **com.aspose.pdf.generator.legacyxmlmodel**

## Kelas Diinternalisasi:

com.aspose.pdf.XfdfTags  
com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape  
com.aspose.pdf.generator.legacyxmlmodel.ComplexShape  

com.aspose.pdf.generator.legacyxmlmodel.Circle  
com.aspose.pdf.generator.legacyxmlmodel.Curve
com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape
com.aspose.pdf.generator.legacyxmlmodel.Ellipse
com.aspose.pdf.generator.legacyxmlmodel.PolyDashArray
com.aspose.pdf.generator.legacyxmlmodel.PathArea
com.aspose.pdf.generator.legacyxmlmodel.Rectangle

## Perubahan dalam kelas:

Dalam kelas **PdfExtractor** ditambahkan metode
public extractText(java.nio.charset.Charset value)

Dalam kelas **PdfFileEditor** ditambahkan metode
public static void validateAnotations(IDocument doc)

Dalam kelas **BorderInfo** ditambahkan konstruktor baru:
public BorderInfo(int borderSide)
public BorderInfo(int borderSide, GraphInfo borderFormat)
public BorderInfo(int borderSide, float borderWidth)
public BorderInfo(int borderSide, float borderWidth, Color borderColor)
public BorderInfo(int borderSide, Color borderColor)

Dalam kelas **Canvas** ditambahkan metode
public Object deepClone()

Dalam kelas **Cell** ditambahkan metode:
public boolean isNoBorder()
public void setNoBorder(boolean value)

public Object completeClone()

Dalam kelas **DocumentAttachment** ditambahkan metode  
public Object completeClone()

Dalam kelas **FloatingBox** ditambahkan metode  
public Object completeClone()

Dalam kelas **FormField** ditambahkan metode  
public Object completeClone()

Dalam kelas **Graph** ditambahkan metode:  
public float getRotatingAngle()  
public void setRotatingAngle(float value)  
public ClippingPath getClipping()  
public void setClipping(ClippingPath value)  
public Object completeClone()

Dalam kelas **Image** ditambahkan konstruktor dan metode:  
public Image()  
public Image(Section section)  
public int getAutoNumber()  
public void setAutoNumber(int value)  
public float getImageHeight()  
public void setImageHeight(float value)  
public float getImageWidth()  
public void setImageWidth(float value)  
public float getVectorGraphicsRenderingDPI()  
public void setVectorGraphicsRenderingDPI(float value)  
public float getImageScale()  
public void setImageScale(float value)  
public Object completeClone()        

Dalam kelas **ImageInfo** ditambahkan bidang dan metode:

public TextInfo TextInfo

public String Title
public BorderInfo ImageBorder

public /**ImageFileType**/int _ImageFileType
public InputStream getImageStream()
public void setImageStream(InputStream value)
public BufferedImage getSystemImage()
public void setSystemImage(BufferedImage value)  
public /**Byte**/byte[] getMemoryData() 
public void setMemoryData(/**Byte**/byte[] value) 
public boolean isFixImgWidthSettedInXML() 
public void setFixImgWidthSettedInXML(boolean value) 
public boolean isFixImgHeightSettedInXML()
public void setFixImgHeightSettedInXML(boolean value) 
public boolean isAllFramesInNewPage() 
public void setAllFramesInNewPage(boolean value)
public boolean isStencilMask() 
public void setStencilMask(boolean value)
public com.aspose.pdf.generator.legacyxmlmodel.Color getBackgroundColor() 
public void setBackgroundColor(com.aspose.pdf.generator.legacyxmlmodel.Color value)
public java.awt.Color getPatternColor()
public void setPatternColor(java.awt.Color value) 

Dalam kelas **Paragraph** ditambahkan bidang dan metode:
public float FixedHeight;

public float FixedWidth;

public /**BookmarkIncludeType**/int getBookmarked()
public void setBookmarked(/**BookmarkIncludeType**/int value)
public void copyTo(Paragraph par)

Dalam kelas **RadioButton** ditambahkan metode
public Object completeClone()

Dalam kelas **Row** ditambahkan metode
public Object completeClone()

Dalam kelas **Segment** ditambahkan metode
public Object completeClone()

Dalam kelas **Shape** ditambahkan metode
public float getOpacity()
public void setOpacity(float value)
public float getStrokeOpacity() 
public void setStrokeOpacity(float value)  

Dalam kelas **Shapes** beberapa metode diinternalisasi:
void add(Shape shape)
void remove(Shape shapeToRemove)
void copyTo(Shape[] shapeArray, int index)
int indexOf(Shape shape)

Dalam kelas **Table** ditambahkan metode
public /**override**/ Object completeClone()

Dalam kelas **Text** ditambahkan metode
public /**override**/ Object completeClone()

Dalam kelas **XslFoLoadOptions** ditambahkan metode
public String getBasePath() 
public void setBasePath(String value) 

Dalam kelas **PdfBookmarkEditor** ditambahkan metode

public Bookmarks extractBookmarks(boolean upperLevel)


In **XslFoLoadOptions** kelas ditambahkan metode

In **XslFoLoadOptions** kelas ditambahkan metode

In **XslFoLoadOptions** kelas ditambahkan metode

In **XslFoLoadOptions** kelas ditambahkan metode

**Semua nama metode setter boolean yang dimulai dengan is diubah namanya menjadi set**

sebagai contoh:

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)