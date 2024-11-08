---
title: Aspose.PDF for Java 9.3.0의 공개 API 변경 사항
type: docs
weight: 50
url: /ko/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 [Aspose.PDF for Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx)에서 도입된 공개 API 변경 사항을 나열합니다. 여기에는 새로운 공개 메서드와 사용 중지된 공개 메서드뿐만 아니라 Aspose.PDF for Java에서의 동작 변화가 포함되어 있으며, 이는 기존 코드에 영향을 미칠 수 있습니다. 회귀로 간주될 수 있고 기존 동작을 수정하는 모든 동작이 특히 중요하며 여기에 문서화되어 있습니다.

{{% /alert %}}

## 추가된 클래스:

com.aspose.pdf.MemoryCleaner
com.aspose.pdf.generator.legacy.CmykColorSpace
com.aspose.pdf.generator.legacy.GrayColorSpace
com.aspose.pdf.generator.legacyxmlmodel.ClippingPath
com.aspose.pdf.generator.legacyxmlmodel.ColouredTilingPattern

com.aspose.pdf.generator.legacyxmlmodel.CompareValidator
com.aspose.pdf.generator.legacyxmlmodel.CrossHatchPattern  
com.aspose.pdf.generator.legacyxmlmodel.CustomValidator  
com.aspose.pdf.generator.legacyxmlmodel.Function  
com.aspose.pdf.generator.legacyxmlmodel.FunctionExpInterpolation  
com.aspose.pdf.generator.legacyxmlmodel.GradientAxialShading  
com.aspose.pdf.generator.legacyxmlmodel.GradientRadialShading  
com.aspose.pdf.generator.legacyxmlmodel.HatchingPattern  
com.aspose.pdf.generator.legacyxmlmodel.ImagePattern  
com.aspose.pdf.generator.legacyxmlmodel.PointsPattern  
com.aspose.pdf.generator.legacyxmlmodel.RangeValidator  
com.aspose.pdf.generator.legacyxmlmodel.RegularExpressionValidator  
com.aspose.pdf.generator.legacyxmlmodel.RequiredFieldValidator  
com.aspose.pdf.generator.legacyxmlmodel.ShadingGradientPattern  
com.aspose.pdf.generator.legacyxmlmodel.ShadingPattern  
com.aspose.pdf.generator.legacyxmlmodel.ShadingPatternFactory  
com.aspose.pdf.generator.legacyxmlmodel.TilingPattern  
com.aspose.pdf.generator.legacyxmlmodel.UncolouredTilingPattern  

com.aspose.pdf.Artifact.ArtifactType
com.aspose.pdf.Artifact.ArtifactSubtype  
com.aspose.pdf.ILicenseProvider  
com.aspose.pdf.Layer  
com.aspose.pdf.LettersPositioningMethods

## 열거형 클래스 추가됨:

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
열거형 클래스의 사용 구현됨: **TextEncodingInternal** 및 **ImageFormatInternal**

## 클래스 제거됨:

폐기된 com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType 클래스가 제거되었습니다.

## 클래스 이동됨:

패키지 **com.aspose.pdf.generator.legacyxmlmodel.enums** 에서의 클래스들이 패키지 **com.aspose.pdf.generator.legacyxmlmodel** 로 이동되었습니다.

## 클래스 내부화됨:

com.aspose.pdf.XfdfTags  
com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape  
com.aspose.pdf.generator.legacyxmlmodel.ComplexShape

com.aspose.pdf.generator.legacyxmlmodel.Circle
com.aspose.pdf.generator.legacyxmlmodel.Curve  
com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape  
com.aspose.pdf.generator.legacyxmlmodel.Ellipse  
com.aspose.pdf.generator.legacyxmlmodel.PolyDashArray  
com.aspose.pdf.generator.legacyxmlmodel.PathArea  
com.aspose.pdf.generator.legacyxmlmodel.Rectangle  

## 클래스의 변경 사항:

**PdfExtractor** 클래스에 메서드가 추가되었습니다.
public extractText(java.nio.charset.Charset value)  

**PdfFileEditor** 클래스에 메서드가 추가되었습니다.
public static void validateAnotations(IDocument doc)  

**BorderInfo** 클래스에 새로운 생성자가 추가되었습니다:
public BorderInfo(int borderSide)  
public BorderInfo(int borderSide, GraphInfo borderFormat)  
public BorderInfo(int borderSide, float borderWidth)  
public BorderInfo(int borderSide, float borderWidth, Color borderColor)  
public BorderInfo(int borderSide, Color borderColor)  

**Canvas** 클래스에 메서드가 추가되었습니다.
public Object deepClone()  

**Cell** 클래스에 메서드가 추가되었습니다:
public boolean isNoBorder()  
public void setNoBorder(boolean value)  

public Object completeClone()  

In **DocumentAttachment** 클래스에 메서드 추가됨  
public Object completeClone()

In **FloatingBox** 클래스에 메서드 추가됨  
public Object completeClone()

In **FormField** 클래스에 메서드 추가됨  
public Object completeClone()

In **Graph** 클래스에 메서드 추가됨:  
public float getRotatingAngle()  
public void setRotatingAngle(float value)  
public ClippingPath getClipping()  
public void setClipping(ClippingPath value)  
public Object completeClone()

In **Image** 클래스에 생성자와 메서드 추가됨:  
public Image()  
public Image(Section section)  
public int getAutoNumber()  
public void setAutoNumber(int value)  
public float getImageHeight()  
public void setImageHeight(float value)  
public float getImageWidth()  
public void setImageWidth(float value)  
public float getVectorGraphicsRenderingDPI()  
public void setVectorGraphicsRenderingDPI(float value)  
public float getImageScale()  
public void setImageScale(float value)  
public Object completeClone()  

In **ImageInfo** 클래스에 필드와 메서드 추가됨:  

public TextInfo TextInfo

public String Title
public BorderInfo 이미지경계

public /**ImageFileType**/int _이미지파일유형 public InputStream getImageStream() public void setImageStream(InputStream value) public BufferedImage getSystemImage() public void setSystemImage(BufferedImage value) public /**Byte**/byte[] getMemoryData() public void setMemoryData(/**Byte**/byte[] value) public boolean isFixImgWidthSettedInXML() public void setFixImgWidthSettedInXML(boolean value) public boolean isFixImgHeightSettedInXML() public void setFixImgHeightSettedInXML(boolean value) public boolean isAllFramesInNewPage() public void setAllFramesInNewPage(boolean value) public boolean isStencilMask() public void setStencilMask(boolean value) public com.aspose.pdf.generator.legacyxmlmodel.Color getBackgroundColor() public void setBackgroundColor(com.aspose.pdf.generator.legacyxmlmodel.Color value) public java.awt.Color getPatternColor() public void setPatternColor(java.awt.Color value)

**Paragraph** 클래스에 추가된 필드와 메서드: public float 고정높이;

public float 고정너비;
public /**BookmarkIncludeType**/int getBookmarked()
public void setBookmarked(/**BookmarkIncludeType**/int value)
public void copyTo(Paragraph par)

**RadioButton** 클래스에 메서드가 추가되었습니다.
public Object completeClone()

**Row** 클래스에 메서드가 추가되었습니다.
public Object completeClone()

**Segment** 클래스에 메서드가 추가되었습니다.
public Object completeClone()

**Shape** 클래스에 메서드가 추가되었습니다.
public float getOpacity()
public void setOpacity(float value)
public float getStrokeOpacity() 
public void setStrokeOpacity(float value)  

**Shapes** 클래스의 일부 메서드가 내부화되었습니다:
void add(Shape shape)
void remove(Shape shapeToRemove)
void copyTo(Shape[] shapeArray, int index)
int indexOf(Shape shape)

**Table** 클래스에 메서드가 추가되었습니다.
public /**override**/ Object completeClone()

**Text** 클래스에 메서드가 추가되었습니다.
public /**override**/ Object completeClone()

**XslFoLoadOptions** 클래스에 메서드가 추가되었습니다.
public String getBasePath() 
public void setBasePath(String value) 

**PdfBookmarkEditor** 클래스에 메서드가 추가되었습니다.

public Bookmarks extractBookmarks(boolean upperLevel)


In **XslFoLoadOptions** 클래스에 메서드가 추가되었습니다

In **XslFoLoadOptions** 클래스에 메서드가 추가되었습니다

In **XslFoLoadOptions** 클래스에 메서드가 추가되었습니다

In **XslFoLoadOptions** 클래스에 메서드가 추가되었습니다

**is로 시작했던 모든 boolean 설정자 메서드 이름이 set으로 변경되었습니다**

예를 들어:

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)