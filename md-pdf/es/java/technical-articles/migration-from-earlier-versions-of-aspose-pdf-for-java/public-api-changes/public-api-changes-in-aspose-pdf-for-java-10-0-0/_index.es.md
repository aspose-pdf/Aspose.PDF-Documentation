---
title: Cambios en la API Pública en Aspose.PDF para Java 10.0.0
type: docs
weight: 90
url: /java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página enumera los cambios en la API pública introducidos en [Aspose.PDF para Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx). Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento tras bambalinas en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pueda verse como una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}}

## Cambios en la API Pública e Incompatibilidades

**clase com.aspose.pdf.facades.Form:**

Métodos obsoletos:

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

Constructor obsoleto:

- public Form(InputStream srcStream, OutputStream destStream)


**clase com.aspose.pdf.facades.PdfFileEdito:**

Added internal class:

- public static class PageBreak

Added methods:

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**com.aspose.pdf.facades.PdfFileStamp class:**

Métodos obsoletos:

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**com.aspose.pdf.facades.AutoFiller class:**

Métodos obsoletos:

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**com.aspose.pdf.facades.FormEditor class:**

Constructores obsoletos:

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. com.aspose.pdf.facades.PdfFileMend class:

Constructores obsoletos:

- public PdfFileMend(IDocument document, String outputFileName)

**com.aspose.pdf.facades.PdfFileSecurity class:**

Métodos obsoletos:

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

Constructores obsoletos:

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## Añadida nueva clase PdfPrintPageInfo

**com.aspose.pdf.generator.legacyxmlmodel.PathArea class:**

Método añadido:

- public java.util.Map getShapes()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern class:**

Método añadido:

- public java.awt.Color getColor()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory class:**

Método añadido:

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**com.aspose.pdf.Document class:**

Métodos añadidos:

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact class:**

Métodos añadidos:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection class:**

Métodos añadidos:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact class:**

Métodos añadidos:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph class:**

Métodos añadidos:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph class:**

Cambios en métodos:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) -> public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions class:**

Cambios en métodos:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**com.aspose.pdf.Color class:**

Métodos añadidos:

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**com.aspose.pdf.ComHelper class:**

Métodos añadidos:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**com.aspose.pdf.ComHelper class:**

Constructores añadidos:

- public ContentsAppender(XForm form)

**com.aspose.pdf.ComHelper class:**

Métodos añadidos:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)


## Clase enum añadida com.aspose.pdf.FileEncoding

**com.aspose.pdf.FileParams class:**

Métodos añadidos:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

Constructor añadido:

- public FileParams(FileSpecification spec)

**com.aspose.pdf.FileParams class:**

Métodos añadidos:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**com.aspose.pdf.FloatingBox class:**

Cambios:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() and public void setVerticalAlignment_Rename_Namesake(int value)

**com.aspose.pdf.IIndexBitmapConverte class:**

Métodos añadidos:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**com.aspose.pdf.Image class:**

Cambios:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

Métodos añadidos:

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**com.aspose.pdf.Layer class:**

Métodos añadidos:

- public java.util.List<Operator> getContents()

**com.aspose.pdf.LevelFormat class:**

Cambios:

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value) -> public void setMargin(com.aspose.pdf.MarginInfo value) 

## Clase añadida com.aspose.pdf.Note

**com.aspose.pdf.Page class:**

Métodos añadidos:

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**com.aspose.pdf.Page class:**

Campos añadidos:

- public boolean SupressErrors;

**com.aspose.pdf.PKCS7 Detached class:**

Constructor añadido:

- public PKCS7Detached(InputStream pfx, String password)

**com.aspose.pdf.SoundData class:**

Métodos añadidos:

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions class:**

Métodos añadidos:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment class:**

Métodos añadidos:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState class:**

Métodos añadidos:

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp class:**

Métodos añadidos:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp class:**

Métodos añadidos:

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo class:**

Métodos añadidos:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()

**com.aspose.pdf.XImage class:**

Métodos añadidos:

- public boolean containsTransparency()
- public int getColorType()