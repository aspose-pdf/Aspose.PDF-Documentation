---
title: Mudanças na API Pública no Aspose.PDF para Java 10.0.0
type: docs
weight: 90
url: /java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no [Aspose.PDF para Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx). Inclui não apenas métodos públicos novos e obsoletos, mas também uma descrição de quaisquer alterações no comportamento nos bastidores do Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifica o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

## Mudanças na API Pública e Incompatibilidades com Versões Anteriores

**classe com.aspose.pdf.facades.Form:**

Métodos obsoletos:

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

Construtor obsoleto:

- public Form(InputStream srcStream, OutputStream destStream)


**classe com.aspose.pdf.facades.PdfFileEdito:**

Classe interna adicionada:

- public static class PageBreak

Métodos adicionados:

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**classe com.aspose.pdf.facades.PdfFileStamp:**

Métodos obsoletos:

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**classe com.aspose.pdf.facades.AutoFiller:**

Métodos obsoletos:

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**classe com.aspose.pdf.facades.FormEditor:**

Construtores obsoletos:

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. classe com.aspose.pdf.facades.PdfFileMend:

Construtores obsoletos:

- public PdfFileMend(IDocument document, String outputFileName)

**classe com.aspose.pdf.facades.PdfFileSecurity:**

Métodos obsoletos:

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

Construtores obsoletos:

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## Nova classe adicionada PdfPrintPageInfo

**classe com.aspose.pdf.generator.legacyxmlmodel.PathArea:**

Método adicionado:

- public java.util.Map getShapes()

**classe com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern:**

Método adicionado:

- public java.awt.Color getColor()

**classe com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory:**

Método adicionado:

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**classe com.aspose.pdf.Document:**

Métodos adicionados:

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact class:**

Métodos adicionados:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection class:**

Métodos adicionados:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact class:**

Métodos adicionados:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph class:**

Métodos adicionados:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph class:**

Alterações nos métodos:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) -> public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions class:**

Alterações nos métodos:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**classe com.aspose.pdf.Color:**

Métodos adicionados:

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**classe com.aspose.pdf.ComHelper:**

Métodos adicionados:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**classe com.aspose.pdf.ComHelper:**

Construtores adicionados:

- public ContentsAppender(XForm form)

**classe com.aspose.pdf.ComHelper:**

Métodos adicionados:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

## Classe enum adicionada com.aspose.pdf.FileEncoding

**classe com.aspose.pdf.FileParams:**

Métodos adicionados:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

Construtor adicionado:

- public FileParams(FileSpecification spec)

**classe com.aspose.pdf.FileParams:**

Métodos adicionados:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**classe com.aspose.pdf.FloatingBox:**

Alterações:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() e public void setVerticalAlignment_Rename_Namesake(int value)

**classe com.aspose.pdf.IIndexBitmapConverte:**

Métodos adicionados:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**classe com.aspose.pdf.Image:**

Alterações:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

Métodos adicionados:

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**classe com.aspose.pdf.Layer:**

Métodos adicionados:

- public java.util.List<Operator> getContents()

**classe com.aspose.pdf.LevelFormat:**

Alterações:

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value) -> public void setMargin(com.aspose.pdf.MarginInfo value) 

## Classe adicionada com.aspose.pdf.Note

**classe com.aspose.pdf.Page:**

Métodos adicionados:

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**classe com.aspose.pdf.Page:**

Campos adicionados:

- public boolean SupressErrors;

**classe com.aspose.pdf.PKCS7 Detached:**

Construtor adicionado:

- public PKCS7Detached(InputStream pfx, String password)

**classe com.aspose.pdf.SoundData:**

Métodos adicionados:

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions class:**

Métodos adicionados:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment class:**

Métodos adicionados:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState class:**

Métodos adicionados:

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp class:**

Métodos adicionados:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp class:**

Métodos adicionados:

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo class:**

Métodos adicionados:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()

**com.aspose.pdf.XImage class:**

Métodos adicionados:

- public boolean containsTransparency()
- public int getColorType()