---
title: Aspose.PDF for Java 10.0.0의 공개 API 변경 사항
type: docs
weight: 90
url: /java/public-api-changes-in-aspose-pdf-for-java-10-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 [Aspose.PDF for Java 10.0.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry608514.aspx)에서 도입된 공개 API 변경 사항을 나열합니다. 여기에는 새로운 공개 메서드와 구식 메서드뿐만 아니라 Aspose.PDF for Java의 내부 동작 변화로 인해 기존 코드에 영향을 미칠 수 있는 모든 변경 사항의 설명도 포함되어 있습니다. 회귀로 볼 수 있는 행동과 기존 행동을 수정하는 모든 변경 사항은 특히 중요하며 여기 문서화되어 있습니다.

{{% /alert %}}

## 공개 API 및 하위 호환성 없는 변경 사항

**com.aspose.pdf.facades.Form 클래스:**

사용되지 않는 메서드:

- public OutputStream getDestStream() 
- public void setDestStream(OutputStream value)

사용되지 않는 생성자:

- public Form(InputStream srcStream, OutputStream destStream)

**com.aspose.pdf.facades.PdfFileEdito 클래스:**

내부 클래스 추가됨:

- public static class PageBreak

메서드 추가됨:

- public void addPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
- public void addPageBreak(String src, String dest, PageBreak[] pageBreaks)

**com.aspose.pdf.facades.PdfFileStamp 클래스:**

사용 중단된 메서드:

- public String getInputFile() 
- public void setInputFile(String value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)
- public String getOutputFile() 
- public void setOutputFile(String value)
- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)

**com.aspose.pdf.facades.AutoFiller 클래스:**

사용 중단된 메서드:

- public OutputStream getOutputStream() 
- public void setOutputStream(OutputStream value)
- public InputStream getInputStream() 
- public void setInputStream(InputStream value)

**com.aspose.pdf.facades.FormEditor 클래스:**

사용 중단된 생성자:

- public FormEditor(IDocument document, OutputStream destStream)

- public FormEditor(IDocument document, String destFileName)
- public FormEditor(InputStream srcStream, OutputStream destStream)

h34. com.aspose.pdf.facades.PdfFileMend 클래스:

사용되지 않는 생성자:

- public PdfFileMend(IDocument document, String outputFileName)

**com.aspose.pdf.facades.PdfFileSecurity 클래스:**

사용되지 않는 메서드:

- public void setInputStream(InputStream value)
- public void setOutputStream(OutputStream value)

사용되지 않는 생성자:

- public PdfFileSecurity(InputStream inputStream, OutputStream outputStream)

## 새로운 클래스 PdfPrintPageInfo 추가

**com.aspose.pdf.generator.legacyxmlmodel.PathArea 클래스:**

메서드 추가:

- public java.util.Map getShapes()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern 클래스:**

메서드 추가:

- public java.awt.Color getColor()

**com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory 클래스:**

메서드 추가:

- public static ShadingPattern getShadingPattern(int level,java.awt.Color color)

**com.aspose.pdf.Document 클래스:**

메서드 추가:

- public boolean getAllowReusePageContent()

- public void setAllowReusePageContent(boolean value)

**com.aspose.pdf.Artifact 클래스:**

추가된 메서드:

- public void setImage(InputStream imageStream)

**com.aspose.pdf.ArtifactCollection 클래스:**

추가된 메서드:

- public java.util.List<Artifact> findByValue(String name, String expectedValue)

**com.aspose.pdf.BackgroundArtifact 클래스:**

추가된 메서드:

- public InputStream getBackgroundImage()

**com.aspose.pdf.BaseParagraph 클래스:**

추가된 메서드:

- public boolean isInLineParagraph()
- public void setInLineParagraph(boolean value)

**com.aspose.pdf.BaseParagraph 클래스:**

메서드 변경:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()
- public void setPageSize(java.awt.geom.Point2D.Float value) -> public void setPageSize(java.awt.geom.Dimension2D value)

**com.aspose.pdf.CgmLoadOptions 클래스:**

메서드 변경:

- public java.awt.geom.Point2D.Float getPageSize() -> public java.awt.geom.Dimension2D getPageSize()

- public CgmLoadOptions(java.awt.geom.Point2D.Float pageSize) -> public CgmLoadOptions(java.awt.geom.Dimension2D pageSize)

**com.aspose.pdf.Color 클래스:**

메소드 추가됨:

- public PatternColorSpace getPatternColorSpace()
- public void setPatternColorSpace(PatternColorSpace value)

**com.aspose.pdf.ComHelper 클래스:**

메소드 추가됨:

- public Document openStream(InputStream input)
- public Document openStream(InputStream input, String password)
- public Document openStream(InputStream input, boolean isManagedStream)
- public Document openStream(InputStream input, String password, boolean isManagedStream)
- public Document openStream(InputStream input, LoadOptions options)

**com.aspose.pdf.ComHelper 클래스:**

생성자 추가됨:

- public ContentsAppender(XForm form)

**com.aspose.pdf.ComHelper 클래스:**

메소드 추가됨:

- public void setCreationDate(java.util.Date value)
- public double getCreationTimeZone()
- public void setCreationTimeZone(double value)
- public double getModTimeZone()
- public void setModTimeZone(double value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

## 열거형 클래스 com.aspose.pdf.FileEncoding 추가됨

**com.aspose.pdf.FileParams class:**

메서드 추가:

- public java.util.Date getCreationDate()
- public void setCreationDate(java.util.Date value)
- public java.util.Date getModDate()
- public void setModDate(java.util.Date value)

생성자 추가:

- public FileParams(FileSpecification spec)

**com.aspose.pdf.FileParams class:**

메서드 추가:

- public int getEncoding()
- public void setEncoding(int value)
- public void setParams(FileParams value)

**com.aspose.pdf.FloatingBox class:**

변경 사항:

- public int VerticalAlignment; -> 
- public int getVerticalAlignment_Rename_Namesake() 및 public void setVerticalAlignment_Rename_Namesake(int value)

**com.aspose.pdf.IIndexBitmapConverte class:**

메서드 추가:

- public java.awt.image.BufferedImage get1BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get4BppImage(java.awt.image.BufferedImage src);
- public java.awt.image.BufferedImage get8BppImage(java.awt.image.BufferedImage src);

**com.aspose.pdf.Image class:**

변경 사항:

- public int getFileType() -> public int getFileType()
- public void setFileType(nt value) -> public void setFileType(int value)

추가된 메서드:

- public boolean isBlackWhite() 
- public void setBlackWhite(boolean value)

**com.aspose.pdf.Layer 클래스:**

추가된 메서드:

- public java.util.List<Operator> getContents()

**com.aspose.pdf.LevelFormat 클래스:**

변경 사항:

- public aspose.pdf.MarginInfo getMargin() -> public com.aspose.pdf.MarginInfo getMargin()
- public void setMargin(aspose.pdf.MarginInfo value)  -> public void setMargin(com.aspose.pdf.MarginInfo value) 

## 추가된 클래스 com.aspose.pdf.Note

**com.aspose.pdf.Page 클래스:**

추가된 메서드:

- public GraphInfo getNoteLineStyle()
- public void setNoteLineStyle(GraphInfo value)

**com.aspose.pdf.Page 클래스:**

추가된 필드:

- public boolean SupressErrors;

**com.aspose.pdf.PKCS7 Detached 클래스:**

추가된 생성자:

- public PKCS7Detached(InputStream pfx, String password)

**com.aspose.pdf.SoundData 클래스:**

추가된 메서드:

- public InputStream getContents()

**com.aspose.pdf.TextExtractionOptions 클래스:**

메소드 추가:

- public double getScaleFactor()
- public void setScaleFactor(double value)

**com.aspose.pdf.TextFragment 클래스:**

메소드 추가:

- public Note getEndNote()
- public void setEndNote(Note value)
- public Note getFootNote()
- public void setFootNote(Note value)

**com.aspose.pdf.TextFragmentState 클래스:**

메소드 추가:

- public float getCharacterSpacing() 

**com.aspose.pdf.TextStamp 클래스:**

메소드 추가:

- public boolean getDraw()
- public void setDraw(boolean value)

**com.aspose.pdf.TextStamp 클래스:**

메소드 추가:

- public float getCharacterSpacing() 

**com.aspose.pdf.TocInfo 클래스:**

메소드 추가:

- public void setLevelIndentation(int value)
- public int getLevelIndentation()
 
**com.aspose.pdf.XImage 클래스:**

메소드 추가:

- public boolean containsTransparency()
- public int getColorType()