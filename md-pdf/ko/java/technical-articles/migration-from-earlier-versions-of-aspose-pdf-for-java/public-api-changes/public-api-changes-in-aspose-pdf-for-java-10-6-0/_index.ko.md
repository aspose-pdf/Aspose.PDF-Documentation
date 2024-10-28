---
title: Aspose.PDF for Java 10.6.0의 공개 API 변경 사항
type: docs
weight: 120
url: /java/public-api-changes-in-aspose-pdf-for-java-10-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 [Aspose.PDF for Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx)에 도입된 공개 API 변경 사항을 나열합니다. 새로운 공개 메서드와 사용되지 않는 메서드뿐만 아니라 Aspose.PDF for Java의 내부 동작 변화로 인해 기존 코드에 영향을 미칠 수 있는 변경 사항에 대한 설명도 포함되어 있습니다. 회귀로 볼 수 있는 동작을 도입하고 기존 동작을 수정하는 것은 특히 중요하며 여기 문서화되어 있습니다.

{{% /alert %}}

**공개 API 변경 사항 10.6.0**

추가된 클래스:

- com.aspose.pdf.printer.**PrinterPaperKind**
- com.aspose.pdf.printer.**PrintPaperSourceKind**
- com.aspose.pdf.**AbsorbedCell**
- com.aspose.pdf.**AbsorbedColumn**
- com.aspose.pdf.**AbsorbedRow**
- com.aspose.pdf.**AbsorbedTable**

- com.aspose.pdf.**ITableElement**
- com.aspose.pdf.LoadOptions.**MarginsAreaUsageModes**  
- com.aspose.pdf.**TableAbsorber**  
- com.aspose.pdf.**TableElementCollection**  

제거된 클래스:  

- com.aspose.pdf.**NewParagraphPlacementInfo**  

com.aspose.pdf.drawind.**Circle** 클래스의 변경 사항:  

- public float getPosX() -> public double getPosX()  
- public void setPosX(float value) -> public void setPosX(double value)  
- public float getPosY() -> public double getPosY()  
- public void setPosY(float value) -> public void setPosY(double value)  
- public float getRadius() -> public double getRadius()  
- public void setRadius(float value) -> public void setRadius(double value)  

com.aspose.pdf.drawind.**Curve** 클래스의 변경 사항:  
추가됨:  

- public float[] getPositionArray()  
- public void setPositionArray(float[] value)  

제거됨:  

- public float getPosition1Y()  
- public void setPosition1Y(float value)  
- public float getPosition2X()  
- public void setPosition2X(float value)  
- public float getPosition2Y()  
- public void setPosition2Y(float value)  

- public float getPosition3X()  
- public void setPosition3X(float value) // public void setPosition3X(float 값)
- public float getPosition3Y() // public float getPosition3Y()
- public void setPosition3Y(float value) // public void setPosition3Y(float 값)
- public float getPosition4X() // public float getPosition4X()
- public void setPosition4X(float value) // public void setPosition4X(float 값)
- public float getPosition4Y() // public float getPosition4Y()
- public void setPosition4Y(float value) // public void setPosition4Y(float 값)

com.aspose.pdf.drawind.**Ellipse** 클래스의 변경 사항:

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

com.aspose.pdf.drawing.**Graph** 클래스의 변경 사항:
추가됨:

- public GraphInfo getGraphInfo() // public GraphInfo getGraphInfo()

제거됨:

- public double getSkewAngleX() // public double getSkewAngleX()
- public void setSkewAngleX(double value) // public void setSkewAngleX(double 값)
- public double getSkewAngleY() // public double getSkewAngleY()
- public void setSkewAngleY(double value) // public void setSkewAngleY(double 값)
- public double getRotationAngle() // public double getRotationAngle()
- public void setRotationAngle(double value) // public void setRotationAngle(double 값)

com.aspose.pdf.**GraphInfo** 클래스의 변경 사항:
추가됨:

- public double getSkewAngleX() // public double getSkewAngleX()
- public void setSkewAngleX(double value) // public void setSkewAngleX(double 값)
- public double getSkewAngleY() // public double getSkewAngleY()
- public void setSkewAngleY(double value) // public void setSkewAngleY(double 값)

- public double getRotationAngle() // public double getRotationAngle()
- public void setRotationAngle(double value)  
- public double getScalingRateX()  
- public void setScalingRateX(double value)  
- public double getScalingRateY()  
- public void setScalingRateY(double value)  

com.aspose.pdf.drawind.**Rectangle** 클래스의 변경 사항:

- public float getRadiusForRoundCorner() -> public double getRoundedCornerRadius()  
- public void setRadiusForRoundCorner(float value) -> public void setRoundedCornerRadius(double value)  
- public float getLeft() -> public double getLeft()  
- public void setLeft(float value) -> public void setLeft(double value)  
- public float getBottom() -> public double getBottom()  
- public void setBottom(float value) -> public void setBottom(double value)  
- public float getWidth() -> public double getWidth()  
- public void setWidth(float value) -> public void setWidth(double value)  
- public float getHeight() -> public double getHeight()  
- public void setHeight(float value) -> public void setHeight(double value)  

추가됨:

- public Rectangle()  

com.aspose.pdf.**PdfFileEditor** 클래스의 변경 사항:

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

추가됨:

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

com.aspose.pdf.ReplaceTextStrategy.**Scope** 클래스의 변경 사항:

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

com.aspose.pdf.**ImageFormatInternal** 클래스의 이름이 com.aspose.pdf.**ImageType**로 변경됨

com.aspose.pdf.**Document** 클래스의 변경 사항:

- public void loadXml(String file) -> public void bindXml(String file)

추가됨:

- public void bindXml(String xmlFile, String xslFile)

com.aspose.pdf.**EpubLoadOptions** 클래스의 변경 사항:
필드 추가:

- public int MarginsAreaUsageMode

com.aspose.pdf.**FontAbsorber** 클래스의 변경 사항:
추가됨:

- public void visit(Document pdf,int startPage, int pageCount)

com.aspose.pdf.**Heading** 클래스의 변경 사항:
추가됨:

- public int getStartNumber()

- public void setStartNumber(int value)

com.aspose.pdf.**HtmlSaveOptions** 클래스의 변경 사항:
필드 추가:

- public boolean SaveTransparentTexts
- public boolean SaveShadowedTextsAsTransparentTexts

com.aspose.pdf.**Image** 클래스의 변경 사항:
추가:

- public TextFragment getTitle()
- public void setTitle(TextFragment value)

com.aspose.pdf.**Matrix** 클래스의 변경 사항:
추가:

- public static Matrix scale(double x, double y)
- public Matrix add(Matrix other)

com.aspose.pdf.**Note** 클래스의 변경 사항:
추가:

- public Note()

com.aspose.pdf.**PageCollection** 클래스의 변경 사항:
추가:

- public void clear()

com.aspose.pdf.**Paragraphs** 클래스의 변경 사항:
제거됨:

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)

com.aspose.pdf.**RadioButtonOptionField** 클래스의 변경 사항:
추가:

- public /* BoxStyle */int getStyle()
- public void setStyle(/* BoxStyle */int value)

com.aspose.pdf.**TextFragment** 클래스의 변경 사항:
제거됨:

- public NewParagraphPlacementInfo getPlacementInfo()

- public void setPlacementInfo(NewParagraphPlacementInfo value)

Changes in com.aspose.pdf.**UnifiedSaveOptions** 클래스:  
필드 추가됨:

- public boolean TryMergeAdjacentSameBackgroundImages