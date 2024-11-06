---
title: Aspose.PDF for Java 9.1.0における公開APIの変更
type: docs
weight: 40
url: ja/java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、Aspose.PDF for Java 9.1.0で導入された公開APIの変更を一覧表示しています。新しい公開メソッドや廃止された公開メソッドだけでなく、既存のコードに影響を与える可能性のあるAspose.PDF for Javaの背後の動作の変更についても説明しています。既存の動作を修正し、回帰と見なされる可能性のある動作は特に重要であり、ここに記録されています。

{{% /alert %}}

## 移動

com.aspose.pdf.Text.FontSourceCollection は com.aspose.pdf.FontSourceCollection に移動されました

## 以下のクラスが追加されました:

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

**クラス名の変更:**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**クラス SaveFormat で、フィールドが名前変更されました:**
SaveFormat.None -> SaveFormat.Pdf

**クラス XForm で、メソッドが名前変更されました:**
public Rectangle getRectangle_Rename_Namesake () -> 
public Rectangle getRectangle()

**PdfFileEditor クラスに、以下のメソッドが追加されました:**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**PdfFileSignature クラスに、以下のメソッドが追加されました:**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**Stamp クラスに、以下のメソッドが追加されました:**
public int getQuality()
public void setQuality(int value)

**Document クラスに、以下のメソッドが追加されました:**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**Annotation クラスに、以下のメソッドが追加されました:**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**In BaseParagraph class, following methods are added:**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**In DocSaveOptions class changes:**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- フィールドが追加されました:

public ConversionProgressEventHandler CustomProgressHandler

**In HtmlConverter class, following methods are renamed:**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**In HtmlSaveOptions class changes:**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- フィールドが追加されました:
  public ConversionProgressEventHandler CustomProgressHandler
- 内部クラスが追加されました:

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**In ImageStamp class, following methods added:**
public int getQuality()
public void setQuality(int value)

**Signature class, following methods are added:**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**MobiXmlSaveOptions クラスの変更:**
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**OperatorCollection クラスの変更:**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**PdfFormat クラスに次の要素が追加されました:**
public static final int PDF_X_3 = 10;

**TextBuilder クラスの変更:**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Watermark クラスの変更:**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
コンストラクタが追加されました: public Watermark(BufferedImage nativeImage, Rectangle rect)
メソッドが追加されました: public BufferedImage getImage()

**XImageCollection クラスの変更:**
メソッドが追加されました: public void add(InputStream image, int quality)

**XpsSaveOptions クラスの変更:**

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions