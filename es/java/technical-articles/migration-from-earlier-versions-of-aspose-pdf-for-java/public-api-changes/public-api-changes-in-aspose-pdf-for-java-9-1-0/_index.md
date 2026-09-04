---
title: Cambios en la API Pública en Aspose.PDF para Java 9.1.0
type: docs
weight: 40
url: /es/java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista los cambios en la API pública introducidos en Aspose.PDF para Java 9.1.0. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pueda ser visto como una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}}

## Movido

com.aspose.pdf.Text.FontSourceCollection movido a com.aspose.pdf.FontSourceCollection

## Se agregaron las siguientes clases:

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

**Nombres de clases cambiados:**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**En la clase SaveFormat, el campo se renombra:**
SaveFormat.None -> SaveFormat.Pdf

**En la clase XForm, el método se renombra:**
public Rectangle getRectangle_Rename_Namesake () -> 
public Rectangle getRectangle()

**En la clase PdfFileEditor, se agregan los siguientes métodos:**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**En la clase PdfFileSignature, se agregan los siguientes métodos:**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**En la clase Stamp, se agregan los siguientes métodos:**
public int getQuality()
public void setQuality(int value)

**En la clase Document, se agregan los siguientes métodos:**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**En la clase Annotation, se agregan los siguientes métodos:**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**En la clase BaseParagraph, se agregan los siguientes métodos:**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**En la clase DocSaveOptions cambios:**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- campo agregado:

public ConversionProgressEventHandler CustomProgressHandler

**En la clase HtmlConverter, los siguientes métodos se renombran:**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**En la clase HtmlSaveOptions cambios:**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- campo agregado:
  public ConversionProgressEventHandler CustomProgressHandler
- clases internas agregadas:

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**En la clase ImageStamp, se agregan los siguientes métodos:**
public int getQuality()
public void setQuality(int value)

**En la clase Signature, se agregan los siguientes métodos:**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**Cambios en la clase MobiXmlSaveOptions:**
MobiXmlSaveOptions extiende SaveOptions -> MobiXmlSaveOptions extiende UnifiedSaveOptions

**Cambios en la clase OperatorCollection:**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extiende BaseOperatorCollection implements ICollection

**Se añadió el siguiente elemento a la clase PdfFormat:**
public static final int PDF_X_3 = 10;

**Cambios en la clase TextBuilder:**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Cambios en la clase Watermark:**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
constructor añadido: public Watermark(BufferedImage nativeImage, Rectangle rect)
método añadido: public BufferedImage getImage()

**Cambios en la clase XImageCollection:**
método añadido: public void add(InputStream image, int quality)

**Cambios en la clase XpsSaveOptions:**

XpsSaveOptions extiende SaveOptions -> XpsSaveOptions extiende UnifiedSaveOptions