---
title: Aspose.PDF for Java 10.0.0 的公共 API 变更
type: docs
weight: 90
url: zh/java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了在 [Aspose.PDF for Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx) 中引入的公共 API 变更。它不仅包括新的和已废弃的公共方法，还包括对 Aspose.PDF for Java 中可能影响现有代码的行为更改的描述。任何被视为回归并修改现有行为的行为尤其重要，并在此处记录。

{{% /alert %}}

## 公共 API 和向后不兼容的更改

**com.aspose.pdf.facades.Form 类：**

已废弃的方法：

- public OutputStream getDestStream()
- public void setDestStream(OutputStream value)

已废弃的构造函数：

- public Form(InputStream srcStream, OutputStream destStream)

**com.aspose.pdf.facades.PdfFileEdito 类：**

添加了内部类：

- public static class PageBreak

添加了方法：

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**com.aspose.pdf.facades.PdfFileStamp 类：**

已弃用的方法：

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**com.aspose.pdf.facades.AutoFiller 类：**

已弃用的方法：

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**com.aspose.pdf.facades.FormEditor 类：**

已弃用的构造函数：

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. com.aspose.pdf.facades.PdfFileMend 类：

已弃用的构造函数：

- public PdfFileMend(IDocument document, String outputFileName)

**com.aspose.pdf.facades.PdfFileSecurity 类：**

已弃用的方法：

- public void setInputStream(InputStream value)  
- public void setOutputStream(OutputStream value)

已弃用的构造函数：

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## 新增类 PdfPrintPageInfo

**com.aspose.pdf.generator.legacyxmlmodel.PathArea 类：**

新增方法：

- public java.util.Map getShapes()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern 类：**

新增方法：

- public java.awt.Color getColor()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory 类：**

新增方法：

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**com.aspose.pdf.Document 类：**

新增方法：

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact 类:**

添加的方法:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection 类:**

添加的方法:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact 类:**

添加的方法:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph 类:**

添加的方法:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph 类:**

方法的变更:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) -> public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions 类:**

方法的变更:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**com.aspose.pdf.Color 类:**

新增方法:

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**com.aspose.pdf.ComHelper 类:**

新增方法:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**com.aspose.pdf.ComHelper 类:**

新增构造函数:

- public ContentsAppender(XForm form)

**com.aspose.pdf.ComHelper 类:**

新增方法:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

## 新增枚举类 com.aspose.pdf.FileEncoding

**com.aspose.pdf.FileParams 类:**

添加的方法:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

添加的构造函数:

- public FileParams(FileSpecification spec)

**com.aspose.pdf.FileParams 类:**

添加的方法:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**com.aspose.pdf.FloatingBox 类:**

更改:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() 和 public void setVerticalAlignment_Rename_Namesake(int value)

**com.aspose.pdf.IIndexBitmapConverte 类:**

添加的方法:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**com.aspose.pdf.Image 类:**

更改:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

添加的方法：

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**com.aspose.pdf.Layer 类:**

添加的方法：

- public java.util.List<Operator> getContents()

**com.aspose.pdf.LevelFormat 类:**

更改：

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value) -> public void setMargin(com.aspose.pdf.MarginInfo value)

## 添加类 com.aspose.pdf.Note

**com.aspose.pdf.Page 类:**

添加的方法：

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**com.aspose.pdf.Page 类:**

添加的字段：

- public boolean SupressErrors;

**com.aspose.pdf.PKCS7 Detached 类:**

添加的构造函数：

- public PKCS7Detached(InputStream pfx, String password)

**com.aspose.pdf.SoundData 类:**

添加的方法：

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions 类:**

添加的方法:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment 类:**

添加的方法:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState 类:**

添加的方法:

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp 类:**

添加的方法:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp 类:**

添加的方法:

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo 类:**

添加的方法:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()
 
**com.aspose.pdf.XImage 类:**

添加的方法:

- public boolean containsTransparency()
- public int getColorType()