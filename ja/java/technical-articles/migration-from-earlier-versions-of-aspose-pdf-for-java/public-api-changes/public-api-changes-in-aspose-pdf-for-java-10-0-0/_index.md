---
title: Aspose.PDF for Java 10.0.0のパブリックAPIの変更
type: docs
weight: 90
url: ja/java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、[Aspose.PDF for Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx)に導入されたパブリックAPIの変更を一覧にしています。新しいパブリックメソッドや廃止されたメソッドだけでなく、Aspose.PDF for Javaの内部動作における変更で既存のコードに影響を与える可能性があるものも含まれています。既存の動作を変更する可能性があり、回帰と見なされる動作は特に重要であり、ここに記録されています。

{{% /alert %}}

## パブリックAPIと後方互換性のない変更

**com.aspose.pdf.facades.Form クラス:**

非推奨のメソッド:

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

非推奨のコンストラクタ:

- public Form(InputStream srcStream, OutputStream destStream)


**com.aspose.pdf.facades.PdfFileEdito クラス:**

内部クラスが追加されました：

- public static class PageBreak

メソッドが追加されました：

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**com.aspose.pdf.facades.PdfFileStamp クラス：**

非推奨メソッド：

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**com.aspose.pdf.facades.AutoFiller クラス：**

非推奨メソッド：

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**com.aspose.pdf.facades.FormEditor クラス：**

非推奨コンストラクタ：

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. com.aspose.pdf.facades.PdfFileMend クラス:

非推奨のコンストラクタ:

- public PdfFileMend(IDocument document, String outputFileName)

**com.aspose.pdf.facades.PdfFileSecurity クラス:**

非推奨のメソッド:

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

非推奨のコンストラクタ:

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## 新しいクラス PdfPrintPageInfo を追加

**com.aspose.pdf.generator.legacyxmlmodel.PathArea クラス:**

追加されたメソッド:

- public java.util.Map getShapes()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern クラス:**

追加されたメソッド:

- public java.awt.Color getColor()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory クラス:**

追加されたメソッド:

- public static ShadingPattern getShadingPattern(int level, java.awt.Color color)

**com.aspose.pdf.Document クラス:**

追加されたメソッド:

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact クラス:**

追加されたメソッド:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection クラス:**

追加されたメソッド:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact クラス:**

追加されたメソッド:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph クラス:**

追加されたメソッド:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph クラス:**

メソッドの変更:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) - > public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions クラス:**

メソッドの変更:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**com.aspose.pdf.Color クラス:**

メソッドを追加:

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**com.aspose.pdf.ComHelper クラス:**

メソッドを追加:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**com.aspose.pdf.ComHelper クラス:**

コンストラクタを追加:

- public ContentsAppender(XForm form)

**com.aspose.pdf.ComHelper クラス:**

メソッドを追加:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)


## 列挙クラス com.aspose.pdf.FileEncoding を追加

**com.aspose.pdf.FileParams クラス:**

追加されたメソッド:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

追加されたコンストラクター:

- public FileParams(FileSpecification spec)

**com.aspose.pdf.FileParams クラス:**

追加されたメソッド:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**com.aspose.pdf.FloatingBox クラス:**

変更点:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() と public void setVerticalAlignment_Rename_Namesake(int value)

**com.aspose.pdf.IIndexBitmapConverte クラス:**

追加されたメソッド:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**com.aspose.pdf.Image クラス:**

変更点:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

追加されたメソッド:

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**com.aspose.pdf.Layer クラス:**

追加されたメソッド:

- public java.util.List<Operator> getContents()

**com.aspose.pdf.LevelFormat クラス:**

変更点:

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value)  -> public void setMargin(com.aspose.pdf.MarginInfo value) 

## 追加されたクラス com.aspose.pdf.Note

**com.aspose.pdf.Page クラス:**

追加されたメソッド:

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**com.aspose.pdf.Page クラス:**

追加されたフィールド:

- public boolean SupressErrors;

**com.aspose.pdf.PKCS7 Detached クラス:**

追加されたコンストラクタ:

- public PKCS7Detached(InputStream pfx, String password)

**com.aspose.pdf.SoundData クラス:**

追加されたメソッド:

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions クラス:**

メソッドが追加されました:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment クラス:**

メソッドが追加されました:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState クラス:**

メソッドが追加されました:

- public float getCharacterSpacing()

**com.aspose.pdf.TextStamp クラス:**

メソッドが追加されました:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp クラス:**

メソッドが追加されました:

- public float getCharacterSpacing()

**com.aspose.pdf.TocInfo クラス:**

メソッドが追加されました:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()

**com.aspose.pdf.XImage クラス:**

メソッドが追加されました:

- public boolean containsTransparency()
- public int getColorType()