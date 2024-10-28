---
title: Perubahan API Publik di Aspose.PDF untuk Java 9.1.0
type: docs
weight: 40
url: /java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan di Aspose.PDF untuk Java 9.1.0. Ini mencakup tidak hanya metode publik baru dan yang tidak digunakan lagi, tetapi juga deskripsi perubahan dalam perilaku di balik layar di Aspose.PDF untuk Java yang dapat memengaruhi kode yang ada. Setiap perilaku yang diperkenalkan yang dapat dilihat sebagai regresi dan memodifikasi perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

## Dipindahkan

com.aspose.pdf.Text.FontSourceCollection dipindahkan ke com.aspose.pdf.FontSourceCollection

## Ditambahkan kelas-kelas berikut:

- BaseOperatorCollection
- DocMDPAccessPermissions
- DocMDPSignature
- LightweightOperatorCollection
- OcspSettings
- PclConverter
- PclSaveOptions
- TextParagraphAbsorber
- TextParagraphCollection
- TimestampSettings
- UnifiedSaveOptions

**Nama kelas yang diubah:**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**Dalam kelas SaveFormat, field diubah namanya:**
SaveFormat.None -> SaveFormat.Pdf

**Dalam kelas XForm, metode diubah namanya:**
public Rectangle getRectangle_Rename_Namesake () ->
public Rectangle getRectangle()

**Dalam kelas PdfFileEditor, metode berikut ditambahkan:**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**Dalam kelas PdfFileSignature, metode berikut ditambahkan:**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**Dalam kelas Stamp, metode berikut ditambahkan:**
public int getQuality()
public void setQuality(int value)

**Dalam kelas Document, metode berikut ditambahkan:**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**Dalam kelas Annotation, metode berikut ditambahkan:**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**Di kelas BaseParagraph, metode berikut ditambahkan:**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**Perubahan di kelas DocSaveOptions:**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- ditambahkan field:

public ConversionProgressEventHandler CustomProgressHandler

**Di kelas HtmlConverter, metode berikut diganti namanya:**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**Perubahan di kelas HtmlSaveOptions:**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- ditambahkan field:
  public ConversionProgressEventHandler CustomProgressHandler
- ditambahkan kelas internal:

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**Di kelas ImageStamp, metode berikut ditambahkan:**
public int getQuality()
public void setQuality(int value)

**Kelas Signature, metode berikut ditambahkan:**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**Perubahan kelas MobiXmlSaveOptions:**
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**Perubahan kelas OperatorCollection:**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**Kelas PdfFormat ditambahkan elemen berikut:**
public static final int PDF_X_3 = 10;

**Perubahan kelas TextBuilder:**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Perubahan kelas Watermark:**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
ditambahkan konstruktor: public Watermark(BufferedImage nativeImage, Rectangle rect)
ditambahkan metode: public BufferedImage getImage()

**Perubahan kelas XImageCollection:**
ditambahkan metode: public void add(InputStream image, int quality)

**Perubahan kelas XpsSaveOptions:**

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions