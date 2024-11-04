---  
title: Изменения общедоступного API в Aspose.PDF для Java 10.6.0  
type: docs  
weight: 120  
url: /java/public-api-changes-in-aspose-pdf-for-java-10-6-0/  
lastmod: "2022-01-27"  
---  

{{% alert color="primary" %}}

На этой странице перечислены изменения общедоступного API, введенные в [Aspose.PDF для Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx). Она включает не только новые и устаревшие общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, которое может рассматриваться как регрессия и изменяет существующее поведение, особенно важно и документировано здесь.

{{% /alert %}}

**Изменения общедоступного API 10.6.0**

Добавлены классы:

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

Удаленные классы:

- com.aspose.pdf.**NewParagraphPlacementInfo**  

Изменения в классе com.aspose.pdf.drawind.**Circle**:

- public float getPosX() -> public double getPosX()  
- public void setPosX(float value) -> public void setPosX(double value)  
- public float getPosY() -> public double getPosY()  
- public void setPosY(float value) -> public void setPosY(double value)  
- public float getRadius() -> public double getRadius()  
- public void setRadius(float value) -> public void setRadius(double value)  

Изменения в классе com.aspose.pdf.drawind.**Curve**:  
Добавлено:

- public float[] getPositionArray()  
- public void setPositionArray(float[] value)  

Удалено:

- public float getPosition1Y()  
- public void setPosition1Y(float value)  
- public float getPosition2X()  
- public void setPosition2X(float value)  
- public float getPosition2Y()  
- public void setPosition2Y(float value)  

- public float getPosition3X()  
- public void setPosition3X(float value)  
- public float getPosition3Y()  
- public void setPosition3Y(float value)  
- public float getPosition4X()  
- public void setPosition4X(float value)  
- public float getPosition4Y()  
- public void setPosition4Y(float value)  

Изменения в классе com.aspose.pdf.drawind.**Ellipse**:

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

Изменения в классе com.aspose.pdf.drawing.**Graph**:  
Добавлено:

- public GraphInfo getGraphInfo()

Удалено:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  
- public double getRotationAngle()  
- public void setRotationAngle(double value)  

Изменения в классе com.aspose.pdf.**GraphInfo**:  
Добавлено:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  

- public double getRotationAngle()  
- public void setRotationAngle(double value) - public double getScalingRateX() - public void setScalingRateX(double value) - public double getScalingRateY() - public void setScalingRateY(double value)

Изменения в классе com.aspose.pdf.drawind.**Rectangle**:

- public float getRadiusForRoundCorner() -> public double getRoundedCornerRadius() - public void setRadiusForRoundCorner(float value) -> public void setRoundedCornerRadius(double value) - public float getLeft() -> public double getLeft() - public void setLeft(float value) -> public void setLeft(double value) - public float getBottom() -> public double getBottom() - public void setBottom(float value) -> public void setBottom(double value) - public float getWidth() -> public double getWidth() - public void setWidth(float value) -> public void setWidth(double value) - public float getHeight() -> public double getHeight() - public void setHeight(float value) -> public void setHeight(double value)

Добавлено:

- public Rectangle()

Изменения в классе com.aspose.pdf.**PdfFileEditor**:

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

Добавлено:

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

Изменения в классе com.aspose.pdf.ReplaceTextStrategy.**Scope**:

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

Класс com.aspose.pdf.**ImageFormatInternal** переименован в com.aspose.pdf.**ImageType**

Изменения в классе com.aspose.pdf.**Document**:

- public void loadXml(String file) -> public void bindXml(String file)

Добавлено:

- public void bindXml(String xmlFile, String xslFile)

Изменения в классе com.aspose.pdf.**EpubLoadOptions**:
Добавлено поле:

- public int MarginsAreaUsageMode

Изменения в классе com.aspose.pdf.**FontAbsorber**:
Добавлено:

- public void visit(Document pdf,int startPage, int pageCount)

Изменения в классе com.aspose.pdf.**Heading**:
Добавлено:

- public int getStartNumber()

- public void setStartNumber(int value)

Изменения в классе com.aspose.pdf.**HtmlSaveOptions**:
Добавлены поля:

- public boolean SaveTransparentTexts
- public boolean SaveShadowedTextsAsTransparentTexts

Изменения в классе com.aspose.pdf.**Image**:
Добавлено:

- public TextFragment getTitle()
- public void setTitle(TextFragment value)

Изменения в классе com.aspose.pdf.**Matrix**:
Добавлено:

- public static Matrix scale(double x, double y)
- public Matrix add(Matrix other)

Изменения в классе com.aspose.pdf.**Note**:
Добавлено:

- public Note()

Изменения в классе com.aspose.pdf.**PageCollection**:
Добавлено:

- public void clear()

Изменения в классе com.aspose.pdf.**Paragraphs**:
Удалено:

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)

Изменения в классе com.aspose.pdf.**RadioButtonOptionField**:
Добавлено:

- public /* BoxStyle */int getStyle()
- public void setStyle(/* BoxStyle */int value)

Изменения в классе com.aspose.pdf.**TextFragment**:
Удалено:

- public NewParagraphPlacementInfo getPlacementInfo()

- public void setPlacementInfo(NewParagraphPlacementInfo value)

Changes in com.aspose.pdf.**UnifiedSaveOptions** class:  
Added field:

- public boolean TryMergeAdjacentSameBackgroundImages  

Изменения в классе com.aspose.pdf.**UnifiedSaveOptions**:  
Добавлено поле:  

- public boolean TryMergeAdjacentSameBackgroundImages