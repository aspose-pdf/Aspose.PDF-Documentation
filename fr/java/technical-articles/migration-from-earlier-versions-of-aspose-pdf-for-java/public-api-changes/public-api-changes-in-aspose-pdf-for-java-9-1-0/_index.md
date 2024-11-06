---
title: Changements de l'API Publique dans Aspose.PDF pour Java 9.1.0
type: docs
weight: 40
url: fr/java/public-api-changes-in-aspose-pdf-for-java-9-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page répertorie les changements de l'API publique introduits dans Aspose.PDF pour Java 9.1.0. Elle inclut non seulement les méthodes publiques nouvelles et obsolètes, mais aussi une description de tous les changements dans le comportement en coulisse dans Aspose.PDF pour Java qui peuvent affecter le code existant. Tout comportement introduit qui pourrait être vu comme une régression et modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

## Déplacé

com.aspose.pdf.Text.FontSourceCollection déplacé vers com.aspose.pdf.FontSourceCollection

## Ajout des classes suivantes :

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

**Changement des noms de classes :**

MhtToPdfConverter -> MhtConverter
XpsToPdfConverter -> XpsConverter

**Dans la classe SaveFormat, le champ est renommé :**
SaveFormat.None -> SaveFormat.Pdf

**Dans la classe XForm, la méthode est renommée :**
public Rectangle getRectangle_Rename_Namesake () ->
public Rectangle getRectangle()

**Dans la classe PdfFileEditor, les méthodes suivantes sont ajoutées :**
public boolean getCopyLogicalStructure()
public void setCopyLogicalStructure(boolean value)

**Dans la classe PdfFileSignature, les méthodes suivantes sont ajoutées :**
public boolean isCertified()
public int getAccessPermissions()
public void certify(int page, String SigReason, String SigContact, String SigLocation, boolean visible, java.awt.Rectangle annotRect, DocMDPSignature docMdpSignature)

**Dans la classe Stamp, les méthodes suivantes sont ajoutées :**
public int getQuality()
public void setQuality(int value)

**Dans la classe Document, les méthodes suivantes sont ajoutées :**
public Copier getDefaultCopier()
public Object getCatalogValue(String key)

**Dans la classe Annotation, les méthodes suivantes sont ajoutées :**
public static boolean getUseFontSubset()

public static void setUseFontSubset(boolean value)
public void setColor_Rename_Namesake(Color value)

**Dans la classe BaseParagraph, les méthodes suivantes sont ajoutées :**
public boolean isInNewPage()
public void isInNewPage(boolean value)

**Dans les changements de la classe DocSaveOptions :**
DocSaveOptions extends SaveOptions -> DocSaveOptions extends UnifiedSaveOptions

- champ ajouté :

public ConversionProgressEventHandler CustomProgressHandler

**Dans la classe HtmlConverter, les méthodes suivantes sont renommées :**
saveReferencedHtml (..)->saveOneHtmlPageMarkup (..)

**Dans les changements de la classe HtmlSaveOptions :**
HtmlSaveOptions extends SaveOptions -> HtmlSaveOptions extends UnifiedSaveOptions

- champ ajouté :
  public ConversionProgressEventHandler CustomProgressHandler
- classes internes ajoutées :

public static class HtmlPageMarkupSavingInfo
public static final class HtmlMarkupGenerationModes

**Dans la classe ImageStamp, les méthodes suivantes sont ajoutées :**
public int getQuality()
public void setQuality(int value)

**Dans la classe Signature, les méthodes suivantes sont ajoutées :**
public TimestampSettings getTimestampSettings()

public void setTimestampSettings(TimestampSettings value)

**Changements de la classe MobiXmlSaveOptions :**
MobiXmlSaveOptions extends SaveOptions -> MobiXmlSaveOptions extends UnifiedSaveOptions

**Changements de la classe OperatorCollection :**
public final class OperatorCollection implements ICollection -> public class OperatorCollection extends BaseOperatorCollection implements ICollection

**La classe PdfFormat a été ajoutée avec l'élément suivant :**
public static final int PDF_X_3 = 10;

**Changements de la classe TextBuilder :**
public TextBuilder(Page page, OperatorCollection operatorCollection) -> public TextBuilder(Page page, BaseOperatorCollection operatorCollection)

**Changements de la classe Watermark :**
public Watermark(com.aspose.ms.System.Drawing.Image image) -> public Watermark(BufferedImage nativeImage)
constructeur ajouté : public Watermark(BufferedImage nativeImage, Rectangle rect)
méthode ajoutée : public BufferedImage getImage()

**Changements de la classe XImageCollection :**
méthode ajoutée : public void add(InputStream image, int quality)

**Changements de la classe XpsSaveOptions :**

XpsSaveOptions extends SaveOptions -> XpsSaveOptions extends UnifiedSaveOptions