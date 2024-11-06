---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF for Java 10.0.0
type: docs
weight: 90
url: ar/java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة المقدمة في [Aspose.PDF for Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx). يتضمن ذلك ليس فقط الطرق العامة الجديدة والمحذوفة، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF for Java والتي قد تؤثر على الكود الحالي. أي سلوك مُعَرَّف يمكن اعتباره تراجعًا ويعدل السلوك الحالي مهم بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

## تغييرات واجهة برمجة التطبيقات العامة وغير المتوافقة مع الإصدارات السابقة

**فئة com.aspose.pdf.facades.Form:**

الطرق التي تم إهمالها:

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

المُنشئ الذي تم إهماله:

- public Form(InputStream srcStream, OutputStream destStream)

**فئة com.aspose.pdf.facades.PdfFileEdito:**

تمت إضافة فئة داخلية:

- public static class PageBreak

تمت إضافة طرق:

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**فئة com.aspose.pdf.facades.PdfFileStamp:**

الطرق المهملة:

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**فئة com.aspose.pdf.facades.AutoFiller:**

الطرق المهملة:

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**فئة com.aspose.pdf.facades.FormEditor:**

البناؤون المهملون:

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. فئة com.aspose.pdf.facades.PdfFileMend:

البناءات المتوقفة:

- public PdfFileMend(IDocument document, String outputFileName)

**فئة com.aspose.pdf.facades.PdfFileSecurity:**

الأساليب المتوقفة:

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

البناءات المتوقفة:

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## إضافة فئة جديدة PdfPrintPageInfo

**فئة com.aspose.pdf.generator.legacyxmlmodel.PathArea:**

تمت إضافة طريقة:

- public java.util.Map getShapes()

**فئة com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern:**

تمت إضافة طريقة:

- public java.awt.Color getColor()

**فئة com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory:**

تمت إضافة طريقة:

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**فئة com.aspose.pdf.Document:**

تمت إضافة طرق:

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact class:**

تمت إضافة طرق:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection class:**

تمت إضافة طرق:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact class:**

تمت إضافة طرق:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph class:**

تمت إضافة طرق:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph class:**

التغييرات في الطرق:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) - > public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions class:**

التغييرات في الطرق:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**فئة com.aspose.pdf.Color:**

تمت إضافة طرق:

- public PatternColorSpace getPatternColorSpace() 
- public void setPatternColorSpace(PatternColorSpace value)

**فئة com.aspose.pdf.ComHelper:**

تمت إضافة طرق:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**فئة com.aspose.pdf.ComHelper:**

تمت إضافة منشئين:

- public ContentsAppender(XForm form)

**فئة com.aspose.pdf.ComHelper:**

تمت إضافة طرق:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

## تمت إضافة فئة التعداد com.aspose.pdf.FileEncoding

**com.aspose.pdf.FileParams class:**

تمت إضافة طرق:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

تمت إضافة مُنشئ:

- public FileParams(FileSpecification spec)

**com.aspose.pdf.FileParams class:**

تمت إضافة طرق:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**com.aspose.pdf.FloatingBox class:**

التغييرات:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() and public void setVerticalAlignment_Rename_Namesake(int value)

**com.aspose.pdf.IIndexBitmapConverte class:**

تمت إضافة طرق:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**com.aspose.pdf.Image class:**

التغييرات:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

تمت إضافة طرق:

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**فئة com.aspose.pdf.Layer:**

تمت إضافة طرق:

- public java.util.List<Operator> getContents()

**فئة com.aspose.pdf.LevelFormat:**

التغييرات:

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value) -> public void setMargin(com.aspose.pdf.MarginInfo value)

## تمت إضافة فئة com.aspose.pdf.Note

**فئة com.aspose.pdf.Page:**

تمت إضافة طرق:

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**فئة com.aspose.pdf.Page:**

تمت إضافة حقول:

- public boolean SupressErrors;

**فئة com.aspose.pdf.PKCS7 Detached:**

تمت إضافة منشئ:

- public PKCS7Detached(InputStream pfx, String password)

**فئة com.aspose.pdf.SoundData:**

تمت إضافة طرق:

- public InputStream getContents()


**com.aspose.pdf.TextExtractionOptions class:**

تمت إضافة الطرق:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment class:**

تمت إضافة الطرق:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState class:**

تمت إضافة الطرق:

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp class:**

تمت إضافة الطرق:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp class:**

تمت إضافة الطرق:

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo class:**

تمت إضافة الطرق:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()
 
**com.aspose.pdf.XImage class:**

تمت إضافة الطرق:

- public boolean containsTransparency()
- public int getColorType()