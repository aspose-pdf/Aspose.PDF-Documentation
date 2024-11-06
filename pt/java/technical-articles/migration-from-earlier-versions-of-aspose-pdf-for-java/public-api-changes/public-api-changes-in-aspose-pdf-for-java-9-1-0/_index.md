---
title: Mudanças na API Pública no Aspose.PDF para Java 9.1.0
type: docs
weight: 40
url: pt/java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no Aspose.PDF para Java 9.1.0. Inclui não apenas novos métodos públicos e métodos obsoletos, mas também uma descrição de quaisquer mudanças no comportamento nos bastidores no Aspose.PDF para Java que possam afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifique o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

## Movido

com.aspose.pdf.Text.FontSourceCollection movido para com.aspose.pdf.FontSourceCollection

## Adicionadas as seguintes classes:

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

**Nomes de classes alterados:**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**Na classe SaveFormat, o campo foi renomeado:**
SaveFormat.None -> SaveFormat.Pdf

**Na classe XForm, o método foi renomeado:**
public Rectangle getRectangle_Rename_Namesake () ->
public Rectangle getRectangle()

**Na classe PdfFileEditor, os seguintes métodos foram adicionados:**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**Na classe PdfFileSignature, os seguintes métodos foram adicionados:**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**Na classe Stamp, os seguintes métodos foram adicionados:**
public int getQuality()
public void setQuality(int value)

**Na classe Document, os seguintes métodos foram adicionados:**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**Na classe Annotation, os seguintes métodos foram adicionados:**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**Na classe BaseParagraph, os seguintes métodos foram adicionados:**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**Alterações na classe DocSaveOptions:**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- campo adicionado:

public ConversionProgressEventHandler CustomProgressHandler

**Na classe HtmlConverter, os seguintes métodos foram renomeados:**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**Alterações na classe HtmlSaveOptions:**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- campo adicionado:
  public ConversionProgressEventHandler CustomProgressHandler
- classes internas adicionadas:

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**Na classe ImageStamp, os seguintes métodos foram adicionados:**
public int getQuality()
public void setQuality(int value)

**Na classe Signature, os seguintes métodos foram adicionados:**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**Mudanças na classe MobiXmlSaveOptions:**
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**Mudanças na classe OperatorCollection:**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**Foi adicionado o próximo elemento à classe PdfFormat:**
public static final int PDF_X_3 = 10;

**Mudanças na classe TextBuilder:**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Mudanças na classe Watermark:**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
construtor adicionado: public Watermark(BufferedImage nativeImage, Rectangle rect)
método adicionado: public BufferedImage getImage()

**Mudanças na classe XImageCollection:**
método adicionado: public void add(InputStream image, int quality)

**Mudanças na classe XpsSaveOptions:**

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions