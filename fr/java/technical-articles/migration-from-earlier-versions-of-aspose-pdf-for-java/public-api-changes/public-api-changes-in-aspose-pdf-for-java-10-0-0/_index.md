---
title: Changements de l'API Publique dans Aspose.PDF pour Java 10.0.0
type: docs
weight: 90
url: /fr/java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page liste les changements de l'API publique introduits dans [Aspose.PDF pour Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx). Elle inclut non seulement les nouvelles méthodes publiques et celles obsolètes, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.PDF pour Java qui peut affecter le code existant. Tout comportement introduit qui pourrait être perçu comme une régression et modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

## Changements de l'API Publique et Incompatibilités Rétroactives

**classe com.aspose.pdf.facades.Form :**

Méthodes obsolètes :

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

Constructeur obsolète :

- public Form(InputStream srcStream, OutputStream destStream)


**classe com.aspose.pdf.facades.PdfFileEdito :**

Ajout de classe interne :

- public static class PageBreak

Ajout de méthodes :

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**classe com.aspose.pdf.facades.PdfFileStamp :**

Méthodes obsolètes :

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**classe com.aspose.pdf.facades.AutoFiller :**

Méthodes obsolètes :

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**classe com.aspose.pdf.facades.FormEditor :**

Constructeurs obsolètes :

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. classe com.aspose.pdf.facades.PdfFileMend :

Constructeurs dépréciés :

- public PdfFileMend(IDocument document, String outputFileName)

**classe com.aspose.pdf.facades.PdfFileSecurity :**

Méthodes dépréciées :

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

Constructeurs dépréciés :

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## Nouvelle classe ajoutée PdfPrintPageInfo

**classe com.aspose.pdf.generator.legacyxmlmodel.PathArea :**

Méthode ajoutée :

- public java.util.Map getShapes()

**classe com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern :**

Méthode ajoutée :

- public java.awt.Color getColor()

**classe com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory :**

Méthode ajoutée :

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**classe com.aspose.pdf.Document :**

Méthodes ajoutées :

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact classe :**

Méthodes ajoutées :

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection classe :**

Méthodes ajoutées :

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact classe :**

Méthodes ajoutées :

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph classe :**

Méthodes ajoutées :

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph classe :**

Modifications dans les méthodes :

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) -> public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions classe :**

Modifications dans les méthodes :

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**com.aspose.pdf.Color class :**

Méthodes ajoutées :

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**com.aspose.pdf.ComHelper class :**

Méthodes ajoutées :

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**com.aspose.pdf.ComHelper class :**

Constructeurs ajoutés :

- public ContentsAppender(XForm form)

**com.aspose.pdf.ComHelper class :**

Méthodes ajoutées :

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

## Classe enum ajoutée com.aspose.pdf.FileEncoding

**com.aspose.pdf.FileParams classe :**

Méthodes ajoutées :

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

Constructeur ajouté :

- public FileParams(FileSpecification spec)

**com.aspose.pdf.FileParams classe :**

Méthodes ajoutées :

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**com.aspose.pdf.FloatingBox classe :**

Modifications :

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() et public void setVerticalAlignment_Rename_Namesake(int value)

**com.aspose.pdf.IIndexBitmapConverte classe :**

Méthodes ajoutées :

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**com.aspose.pdf.Image classe :**

Modifications :

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

Méthodes ajoutées :

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**classe com.aspose.pdf.Layer :**

Méthodes ajoutées :

- public java.util.List<Operator> getContents()

**classe com.aspose.pdf.LevelFormat :**

Modifications :

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value)  -> public void setMargin(com.aspose.pdf.MarginInfo value) 

## Classe ajoutée com.aspose.pdf.Note

**classe com.aspose.pdf.Page :**

Méthodes ajoutées :

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**classe com.aspose.pdf.Page :**

Champs ajoutés :

- public boolean SupressErrors;

**classe com.aspose.pdf.PKCS7 Detached :**

Constructeur ajouté :

- public PKCS7Detached(InputStream pfx, String password)

**classe com.aspose.pdf.SoundData :**

Méthodes ajoutées :

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions classe :**

Méthodes ajoutées :

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment classe :**

Méthodes ajoutées :

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState classe :**

Méthodes ajoutées :

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp classe :**

Méthodes ajoutées :

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp classe :**

Méthodes ajoutées :

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo classe :**

Méthodes ajoutées :

- public void setLevelIndentation(int value)
- public int getLevelIndentation()
 
**com.aspose.pdf.XImage classe :**

Méthodes ajoutées :

- public boolean containsTransparency()
- public int getColorType()