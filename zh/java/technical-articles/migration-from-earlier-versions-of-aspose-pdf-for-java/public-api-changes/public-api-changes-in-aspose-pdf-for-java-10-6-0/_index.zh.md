---
title: Aspose.PDF for Java 10.6.0 中的公共 API 变更
type: docs
weight: 120
url: /java/public-api-changes-in-aspose-pdf-for-java-10-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了在 [Aspose.PDF for Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx) 中引入的公共 API 更改。它不仅包括新的和废弃的公共方法，还包括 Aspose.PDF for Java 背后可能影响现有代码的行为变化的描述。任何被视为回归并修改现有行为的行为引入都特别重要，并在此记录。

{{% /alert %}}

**公共 API 更改 10.6.0**

新增类:

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

移除的类：  

- com.aspose.pdf.**NewParagraphPlacementInfo**  

com.aspose.pdf.drawind.**Circle** 类的更改：  

- public float getPosX() -> public double getPosX()  
- public void setPosX(float value) -> public void setPosX(double value)  
- public float getPosY() -> public double getPosY()  
- public void setPosY(float value) -> public void setPosY(double value)  
- public float getRadius() -> public double getRadius()  
- public void setRadius(float value) -> public void setRadius(double value)  

com.aspose.pdf.drawind.**Curve** 类的更改：  
新增：  

- public float[] getPositionArray()  
- public void setPositionArray(float[] value)  

移除：  

- public float getPosition1Y()  
- public void setPosition1Y(float value)  
- public float getPosition2X()  
- public void setPosition2X(float value)  
- public float getPosition2Y()  
- public void setPosition2Y(float value)  

- public float getPosition3X()  
- public void 设置位置3X(float 值)
- public float 获取位置3Y()
- public void 设置位置3Y(float 值)
- public float 获取位置4X()
- public void 设置位置4X(float 值)
- public float 获取位置4Y()
- public void 设置位置4Y(float 值)

com.aspose.pdf.drawind.**Ellipse** 类的更改：

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

com.aspose.pdf.drawing.**Graph** 类的更改：
新增：

- public GraphInfo 获取图形信息()

移除：

- public double 获取倾斜角度X()
- public void 设置倾斜角度X(double 值)
- public double 获取倾斜角度Y()
- public void 设置倾斜角度Y(double 值)
- public double 获取旋转角度() 
- public void 设置旋转角度(double 值)

com.aspose.pdf.**GraphInfo** 类的更改：
新增：

- public double 获取倾斜角度X()
- public void 设置倾斜角度X(double 值)
- public double 获取倾斜角度Y()
- public void 设置倾斜角度Y(double 值)

- public double 获取旋转角度()
- public void setRotationAngle(double value)  
- public double getScalingRateX()  
- public void setScalingRateX(double value)  
- public double getScalingRateY()  
- public void setScalingRateY(double value)  

在 com.aspose.pdf.drawind.**Rectangle** 类中的更改：

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

新增：

- public Rectangle()  

在 com.aspose.pdf.**PdfFileEditor** 类中的更改：

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

新增:

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

在 com.aspose.pdf.ReplaceTextStrategy.**Scope** 类中的更改:

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

类 com.aspose.pdf.**ImageFormatInternal* 重命名为 com.aspose.pdf.*ImageType**

在 com.aspose.pdf.**Document** 类中的更改:

- public void loadXml(String file) -> public void bindXml(String file)

新增:

- public void bindXml(String xmlFile, String xslFile)

在 com.aspose.pdf.**EpubLoadOptions** 类中的更改:
新增字段:

- public int MarginsAreaUsageMode

在 com.aspose.pdf.**FontAbsorber** 类中的更改:
新增:

- public void visit(Document pdf,int startPage, int pageCount)

在 com.aspose.pdf.**Heading** 类中的更改:
新增:

- public int getStartNumber()

- public void setStartNumber(int value)

在 com.aspose.pdf.**HtmlSaveOptions** 类中的更改：  
新增字段：

- public boolean SaveTransparentTexts
- public boolean SaveShadowedTextsAsTransparentTexts

在 com.aspose.pdf.**Image** 类中的更改：  
新增：

- public TextFragment getTitle()
- public void setTitle(TextFragment value)

在 com.aspose.pdf.**Matrix** 类中的更改：  
新增：

- public static Matrix scale(double x, double y)
- public Matrix add(Matrix other)

在 com.aspose.pdf.**Note** 类中的更改：  
新增：

- public Note()

在 com.aspose.pdf.**PageCollection** 类中的更改：  
新增：

- public void clear()

在 com.aspose.pdf.**Paragraphs** 类中的更改：  
移除：

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)

在 com.aspose.pdf.**RadioButtonOptionField** 类中的更改：  
新增：

- public /* BoxStyle */int getStyle()
- public void setStyle(/* BoxStyle */int value)

在 com.aspose.pdf.**TextFragment** 类中的更改：  
移除：

- public NewParagraphPlacementInfo getPlacementInfo()

- public void setPlacementInfo(NewParagraphPlacementInfo value)

Changes in com.aspose.pdf.**UnifiedSaveOptions** 类：  
添加字段：  

- public boolean 尝试合并相邻相同背景图像