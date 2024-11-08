---
title: Perubahan API Publik di Aspose.PDF untuk Java 10.0.0
type: docs
weight: 90
url: /id/java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan di [Aspose.PDF untuk Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx). Ini termasuk tidak hanya metode publik baru dan yang sudah usang, tetapi juga deskripsi perubahan dalam perilaku di balik layar di Aspose.PDF untuk Java yang mungkin mempengaruhi kode yang ada. Setiap perilaku yang diperkenalkan yang dapat dianggap sebagai regresi dan memodifikasi perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

## Perubahan API Publik dan Tidak Kompatibel dengan Versi Sebelumnya

**kelas com.aspose.pdf.facades.Form:**

Metode yang sudah usang:

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

Konstruktor yang sudah usang:

- public Form(InputStream srcStream, OutputStream destStream)


**kelas com.aspose.pdf.facades.PdfFileEdito:**

Ditambahkan kelas internal:

- public static class PageBreak

Ditambahkan metode:

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**kelas com.aspose.pdf.facades.PdfFileStamp:**

Metode yang tidak digunakan lagi:

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**kelas com.aspose.pdf.facades.AutoFiller:**

Metode yang tidak digunakan lagi:

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**kelas com.aspose.pdf.facades.FormEditor:**

Konstruktor yang tidak digunakan lagi:

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. com.aspose.pdf.facades.PdfFileMend kelas:

Konstruktor yang tidak digunakan lagi:

- public PdfFileMend(IDocument document, String outputFileName)

**com.aspose.pdf.facades.PdfFileSecurity kelas:**

Metode yang tidak digunakan lagi:

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

Konstruktor yang tidak digunakan lagi:

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## Ditambahkan kelas baru PdfPrintPageInfo

**com.aspose.pdf.generator.legacyxmlmodel.PathArea kelas:**

Metode yang ditambahkan:

- public java.util.Map getShapes()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern kelas:**

Metode yang ditambahkan:

- public java.awt.Color getColor()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory kelas:**

Metode yang ditambahkan:

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**com.aspose.pdf.Document kelas:**

Metode yang ditambahkan:

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact class:**

Metode yang ditambahkan:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection class:**

Metode yang ditambahkan:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact class:**

Metode yang ditambahkan:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph class:**

Metode yang ditambahkan:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph class:**

Perubahan dalam metode:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) -> public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions class:**

Perubahan dalam metode:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**com.aspose.pdf.Color class:**

Metode yang ditambahkan:

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**com.aspose.pdf.ComHelper class:**

Metode yang ditambahkan:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**com.aspose.pdf.ComHelper class:**

Konstruktor yang ditambahkan:

- public ContentsAppender(XForm form)

**com.aspose.pdf.ComHelper class:**

Metode yang ditambahkan:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)


## Kelas enum yang ditambahkan com.aspose.pdf.FileEncoding

**com.aspose.pdf.FileParams class:**

Metode yang ditambahkan:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

Konstruktor yang ditambahkan:

- public FileParams(FileSpecification spec)

**com.aspose.pdf.FileParams class:**

Metode yang ditambahkan:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**com.aspose.pdf.FloatingBox class:**

Perubahan:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() dan public void setVerticalAlignment_Rename_Namesake(int value)

**com.aspose.pdf.IIndexBitmapConverte class:**

Metode yang ditambahkan:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**com.aspose.pdf.Image class:**

Perubahan:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

Metode yang ditambahkan:

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**kelas com.aspose.pdf.Layer:**

Metode yang ditambahkan:

- public java.util.List<Operator> getContents()

**kelas com.aspose.pdf.LevelFormat:**

Perubahan:

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value) -> public void setMargin(com.aspose.pdf.MarginInfo value) 

## Kelas yang ditambahkan com.aspose.pdf.Note

**kelas com.aspose.pdf.Page:**

Metode yang ditambahkan:

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**kelas com.aspose.pdf.Page:**

Bidang yang ditambahkan:

- public boolean SupressErrors;

**kelas com.aspose.pdf.PKCS7 Detached:**

Konstruktor yang ditambahkan:

- public PKCS7Detached(InputStream pfx, String password)

**kelas com.aspose.pdf.SoundData:**

Metode yang ditambahkan:

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions class:**

Metode yang ditambahkan:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment class:**

Metode yang ditambahkan:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState class:**

Metode yang ditambahkan:

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp class:**

Metode yang ditambahkan:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp class:**

Metode yang ditambahkan:

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo class:**

Metode yang ditambahkan:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()
 
**com.aspose.pdf.XImage class:**

Metode yang ditambahkan:

- public boolean containsTransparency()
- public int getColorType()