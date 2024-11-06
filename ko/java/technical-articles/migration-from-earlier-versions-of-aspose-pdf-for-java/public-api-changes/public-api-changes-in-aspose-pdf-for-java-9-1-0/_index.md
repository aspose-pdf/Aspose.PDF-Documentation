---
title: Aspose.PDF for Java 9.1.0의 공개 API 변경 사항
type: docs
weight: 40
url: ko/java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 Aspose.PDF for Java 9.1.0에 도입된 공개 API 변경 사항을 나열합니다. 여기에는 새로운 공개 메서드와 폐기된 공개 메서드뿐만 아니라, 기존 코드를 영향을 미칠 수 있는 Aspose.PDF for Java의 내부 동작 변경에 대한 설명도 포함됩니다. 회귀로 볼 수 있고 기존 동작을 수정하는 동작이 도입된 경우 특히 중요하며 여기에 문서화되어 있습니다.

{{% /alert %}}

## 이동됨

com.aspose.pdf.Text.FontSourceCollection이 com.aspose.pdf.FontSourceCollection으로 이동됨

## 다음 클래스가 추가되었습니다:

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

**클래스 이름 변경됨:**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**클래스 SaveFormat에서 필드 이름이 변경되었습니다:**
SaveFormat.None -> SaveFormat.Pdf

**클래스 XForm에서 메서드 이름이 변경되었습니다:**
public Rectangle getRectangle_Rename_Namesake () ->
public Rectangle getRectangle()

**PdfFileEditor 클래스에서 다음 메서드가 추가되었습니다:**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**PdfFileSignature 클래스에서 다음 메서드가 추가되었습니다:**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**Stamp 클래스에서 다음 메서드가 추가되었습니다:**
public int getQuality()
public void setQuality(int value)

**Document 클래스에서 다음 메서드가 추가되었습니다:**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**Annotation 클래스에서 다음 메서드가 추가되었습니다:**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**BaseParagraph 클래스에 다음 메서드가 추가되었습니다:**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**DocSaveOptions 클래스 변경 사항:**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- 필드 추가됨:

public ConversionProgressEventHandler CustomProgressHandler

**HtmlConverter 클래스에서 다음 메서드가 이름이 변경되었습니다:**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**HtmlSaveOptions 클래스 변경 사항:**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- 필드 추가됨:
  public ConversionProgressEventHandler CustomProgressHandler
- 내부 클래스 추가됨:

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**ImageStamp 클래스에 다음 메서드가 추가되었습니다:**
public int getQuality()
public void setQuality(int value)

**Signature 클래스에 다음 메서드가 추가되었습니다:**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**MobiXmlSaveOptions 클래스 변경 사항:**
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**OperatorCollection 클래스 변경 사항:**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**PdfFormat 클래스에 다음 요소가 추가되었습니다:**
public static final int PDF_X_3 = 10;

**TextBuilder 클래스 변경 사항:**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Watermark 클래스 변경 사항:**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
생성자 추가: public Watermark(BufferedImage nativeImage, Rectangle rect)
메서드 추가: public BufferedImage getImage()

**XImageCollection 클래스 변경 사항:**
메서드 추가: public void add(InputStream image, int quality)

**XpsSaveOptions 클래스 변경 사항:**

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions