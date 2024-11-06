---
title: Изменения публичного API в Aspose.PDF для Java 10.0.0
type: docs
weight: 90
url: ru/java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Эта страница перечисляет изменения публичного API, введенные в [Aspose.PDF для Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx). Она включает не только новые и устаревшие публичные методы, но и описание любых изменений в поведении за кулисами в Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, которое может рассматриваться как регрессия и изменяет существующее поведение, особенно важно и документировано здесь.

{{% /alert %}}

## Публичный API и Обратимые Несовместимые Изменения

**класс com.aspose.pdf.facades.Form:**

Устаревшие методы:

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

Устаревший конструктор:

- public Form(InputStream srcStream, OutputStream destStream)


**класс com.aspose.pdf.facades.PdfFileEdito:**

Добавлен внутренний класс:

- public static class PageBreak

Добавлены методы:

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**Класс com.aspose.pdf.facades.PdfFileStamp:**

Устаревшие методы:

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**Класс com.aspose.pdf.facades.AutoFiller:**

Устаревшие методы:

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**Класс com.aspose.pdf.facades.FormEditor:**

Устаревшие конструкторы:

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. класс com.aspose.pdf.facades.PdfFileMend:

Устаревшие конструкторы:

- public PdfFileMend(IDocument document, String outputFileName)

**класс com.aspose.pdf.facades.PdfFileSecurity:**

Устаревшие методы:

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

Устаревшие конструкторы:

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## Добавлен новый класс PdfPrintPageInfo

**класс com.aspose.pdf.generator.legacyxmlmodel.PathArea:**

Добавлен метод:

- public java.util.Map getShapes()

**класс com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern:**

Добавлен метод:

- public java.awt.Color getColor()

**класс com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory:**

Добавлен метод:

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**класс com.aspose.pdf.Document:**

Добавлены методы:

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact класс:**

Добавлены методы:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection класс:**

Добавлены методы:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact класс:**

Добавлены методы:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph класс:**

Добавлены методы:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph класс:**

Изменения в методах:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) -> public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions класс:**

Изменения в методах:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**com.aspose.pdf.Color class:**

Добавлены методы:

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**com.aspose.pdf.ComHelper class:**

Добавлены методы:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**com.aspose.pdf.ComHelper class:**

Добавлены конструкторы:

- public ContentsAppender(XForm form)

**com.aspose.pdf.ComHelper class:**

Добавлены методы:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

## Добавлен enum класс com.aspose.pdf.FileEncoding

**класс com.aspose.pdf.FileParams:**

Добавлены методы:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

Добавлен конструктор:

- public FileParams(FileSpecification spec)

**класс com.aspose.pdf.FileParams:**

Добавлены методы:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**класс com.aspose.pdf.FloatingBox:**

Изменения:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() и public void setVerticalAlignment_Rename_Namesake(int value)

**класс com.aspose.pdf.IIndexBitmapConverte:**

Добавлены методы:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**класс com.aspose.pdf.Image:**

Изменения:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

Добавлены методы:

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**Класс com.aspose.pdf.Layer:**

Добавлены методы:

- public java.util.List<Operator> getContents()

**Класс com.aspose.pdf.LevelFormat:**

Изменения:

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value) -> public void setMargin(com.aspose.pdf.MarginInfo value)

## Добавлен класс com.aspose.pdf.Note

**Класс com.aspose.pdf.Page:**

Добавлены методы:

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**Класс com.aspose.pdf.Page:**

Добавлены поля:

- public boolean SupressErrors;

**Класс com.aspose.pdf.PKCS7 Detached:**

Добавлен конструктор:

- public PKCS7Detached(InputStream pfx, String password)

**Класс com.aspose.pdf.SoundData:**

Добавлены методы:

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions class:**

Добавленные методы:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment class:**

Добавленные методы:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState class:**

Добавленные методы:

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp class:**

Добавленные методы:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp class:**

Добавленные методы:

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo class:**

Добавленные методы:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()
 
**com.aspose.pdf.XImage class:**

Добавленные методы:

- public boolean containsTransparency()
- public int getColorType()