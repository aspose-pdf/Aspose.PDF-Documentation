---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 9.1.0
type: docs
weight: 40
url: ar/java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة المقدمة في Aspose.PDF لـ Java 9.1.0. لا يتضمن ذلك الأساليب العامة الجديدة والمستهلكة فقط، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.PDF لـ Java التي قد تؤثر على الكود الحالي. أي سلوك مقدم يمكن اعتباره تراجعًا ويعدل السلوك الحالي يعتبر مهمًا بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

## تم النقل

تم نقل com.aspose.pdf.Text.FontSourceCollection إلى com.aspose.pdf.FontSourceCollection

## تمت إضافة الفئات التالية:

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

**تم تغيير أسماء الفئات:**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**في فئة SaveFormat، تم إعادة تسمية الحقل:**
SaveFormat.None -> SaveFormat.Pdf

**في فئة XForm، تم إعادة تسمية الطريقة:**
public Rectangle getRectangle_Rename_Namesake () ->
public Rectangle getRectangle()

**في فئة PdfFileEditor، تم إضافة الطرق التالية:**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**في فئة PdfFileSignature، تم إضافة الطرق التالية:**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**في فئة Stamp، تم إضافة الطرق التالية:**
public int getQuality()
public void setQuality(int value)

**في فئة Document، تم إضافة الطرق التالية:**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**في فئة Annotation، تم إضافة الطرق التالية:**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
 public void setColor_Rename_Namesake(Color value)

**في فئة BaseParagraph، تمت إضافة الطرق التالية:**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**تغييرات في فئة DocSaveOptions:**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- تم إضافة الحقل:

public ConversionProgressEventHandler CustomProgressHandler

**في فئة HtmlConverter، تم إعادة تسمية الطرق التالية:**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**تغييرات في فئة HtmlSaveOptions:**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- تم إضافة الحقل:
  public ConversionProgressEventHandler CustomProgressHandler
- إضافة الفئات الداخلية:

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**في فئة ImageStamp، تمت إضافة الطرق التالية:**
public int getQuality()
public void setQuality(int value)

**في فئة Signature، تمت إضافة الطرق التالية:**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**تغييرات فئة MobiXmlSaveOptions:**
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**تغييرات فئة OperatorCollection:**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**تمت إضافة العنصر التالي لفئة PdfFormat:**
public static final int PDF_X_3 = 10;

**تغييرات فئة TextBuilder:**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**تغييرات فئة Watermark:**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
تمت إضافة المنشئ: public Watermark(BufferedImage nativeImage, Rectangle rect)
تمت إضافة الطريقة: public BufferedImage getImage()

**تغييرات فئة XImageCollection:**
تمت إضافة الطريقة: public void add(InputStream image, int quality)

**تغييرات فئة XpsSaveOptions:**

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions