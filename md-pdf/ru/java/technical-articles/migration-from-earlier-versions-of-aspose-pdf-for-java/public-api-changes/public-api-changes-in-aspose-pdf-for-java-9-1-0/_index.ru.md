---
title: Изменения в общедоступном API в Aspose.PDF для Java 9.1.0
type: docs
weight: 40
url: /java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения в общедоступном API, введенные в Aspose.PDF для Java 9.1.0. Они включают не только новые и устаревшие общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, которое может быть воспринято как регрессия и изменяет существующее поведение, особенно важно и документировано здесь.

{{% /alert %}}

## Перемещено

com.aspose.pdf.Text.FontSourceCollection перемещено в com.aspose.pdf.FontSourceCollection

## Добавлены следующие классы:

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

**Изменены названия классов:**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**В классе SaveFormat, поле переименовано:**
SaveFormat.None -> SaveFormat.Pdf

**В классе XForm, метод переименован:**
public Rectangle getRectangle_Rename_Namesake () -> public Rectangle getRectangle()

**В классе PdfFileEditor добавлены следующие методы:**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**В классе PdfFileSignature добавлены следующие методы:**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**В классе Stamp добавлены следующие методы:**
public int getQuality()
public void setQuality(int value)

**В классе Document добавлены следующие методы:**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**В классе Annotation добавлены следующие методы:**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**В классе BaseParagraph добавлены следующие методы:**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**В классе DocSaveOptions изменения:**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- добавлено поле:

public ConversionProgressEventHandler CustomProgressHandler

**В классе HtmlConverter следующие методы переименованы:**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**В классе HtmlSaveOptions изменения:**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- добавлено поле:
  public ConversionProgressEventHandler CustomProgressHandler
- добавлены внутренние классы:

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**В классе ImageStamp добавлены следующие методы:**
public int getQuality()
public void setQuality(int value)

**В классе Signature добавлены следующие методы:**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**Изменения в классе MobiXmlSaveOptions:**
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**Изменения в классе OperatorCollection:**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**В класс PdfFormat был добавлен следующий элемент:**
public static final int PDF_X_3 = 10;

**Изменения в классе TextBuilder:**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Изменения в классе Watermark:**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
добавлен конструктор: public Watermark(BufferedImage nativeImage, Rectangle rect)
добавлен метод: public BufferedImage getImage()

**Изменения в классе XImageCollection:**
добавлен метод: public void add(InputStream image, int quality)

**Изменения в классе XpsSaveOptions:**

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions