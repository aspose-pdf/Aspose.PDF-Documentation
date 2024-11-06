---
title: Aspose.PDF for Java 9.1.0 中的公共 API 更改
type: docs
weight: 40
url: zh/java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了 Aspose.PDF for Java 9.1.0 中引入的公共 API 更改。它不仅包括新的和废弃的公共方法，还包括对 Aspose.PDF for Java 背后行为的任何更改的描述，这些更改可能会影响现有代码。任何被视为回归并修改现有行为的行为都特别重要，并在此记录。

{{% /alert %}}

## 移动

com.aspose.pdf.Text.FontSourceCollection 移动到 com.aspose.pdf.FontSourceCollection

## 添加了以下类：

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

**更改的类名称：**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**在类 SaveFormat 中，字段被重命名：**
SaveFormat.None -> SaveFormat.Pdf

**在类 XForm 中，方法被重命名：**
public Rectangle getRectangle_Rename_Namesake () ->
public Rectangle getRectangle()

**在 PdfFileEditor 类中，添加了以下方法：**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**在 PdfFileSignature 类中，添加了以下方法：**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**在 Stamp 类中，添加了以下方法：**
public int getQuality()
public void setQuality(int value)

**在 Document 类中，添加了以下方法：**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**在 Annotation 类中，添加了以下方法：**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**在 BaseParagraph 类中，添加了以下方法：**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**在 DocSaveOptions 类的更改：**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- 添加字段：

public ConversionProgressEventHandler CustomProgressHandler

**在 HtmlConverter 类中，以下方法被重命名：**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**在 HtmlSaveOptions 类的更改：**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- 添加字段：
  public ConversionProgressEventHandler CustomProgressHandler
- 添加内部类：

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**在 ImageStamp 类中，添加了以下方法：**
public int getQuality()
public void setQuality(int value)

**Signature 类中，添加了以下方法：**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**MobiXmlSaveOptions 类更改：**  
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**OperatorCollection 类更改：**  
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**PdfFormat 类添加了下一个元素：**  
public static final int PDF_X_3 = 10;

**TextBuilder 类更改：**  
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Watermark 类更改：**  
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)  
添加构造函数: public Watermark(BufferedImage nativeImage, Rectangle rect)  
添加方法: public BufferedImage getImage()

**XImageCollection 类更改：**  
添加方法: public void add(InputStream image, int quality)

**XpsSaveOptions 类更改：**  

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions