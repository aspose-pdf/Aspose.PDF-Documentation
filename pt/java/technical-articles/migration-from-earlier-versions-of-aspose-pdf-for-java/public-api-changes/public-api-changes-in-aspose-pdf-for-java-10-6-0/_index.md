---
title: Mudanças na API Pública no Aspose.PDF para Java 10.6.0
type: docs
weight: 120
url: pt/java/public-api-changes-in-aspose-pdf-for-java-10-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no [Aspose.PDF para Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx). Inclui não apenas métodos públicos novos e obsoletos, mas também uma descrição de quaisquer mudanças no comportamento nos bastidores no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifique o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

**Mudanças na API Pública 10.6.0**

Classes adicionadas:

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

Classes removidas:

- com.aspose.pdf.**NewParagraphPlacementInfo**

Alterações na classe com.aspose.pdf.drawind.**Circle**:

- public float getPosX() -> public double getPosX() 
- public void setPosX(float value) -> public void setPosX(double value)
- public float getPosY() -> public double getPosY()
- public void setPosY(float value) -> public void setPosY(double value)
- public float getRadius() -> public double getRadius()
- public void setRadius(float value) -> public void setRadius(double value)

Alterações na classe com.aspose.pdf.drawind.**Curve**:
Adicionado:

- public float[] getPositionArray()
- public void setPositionArray(float[] value)

Removido:

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

Alterações na classe com.aspose.pdf.drawind.**Ellipse**:

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

Alterações na classe com.aspose.pdf.drawing.**Graph**:  
Adicionado:

- public GraphInfo getGraphInfo()

Removido:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  
- public double getRotationAngle()  
- public void setRotationAngle(double value)  

Alterações na classe com.aspose.pdf.**GraphInfo**:  
Adicionado:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  

- public double getRotationAngle()  
- public void setRotationAngle(double value)  
- public double getScalingRateX()  
- public void setScalingRateX(double value)  
- public double getScalingRateY()  
- public void setScalingRateY(double value)  

Alterações na classe com.aspose.pdf.drawind.**Rectangle**:

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

Adicionado:

- public Rectangle()  

Alterações na classe com.aspose.pdf.**PdfFileEditor**:

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

Adicionado:

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

Alterações na classe com.aspose.pdf.ReplaceTextStrategy.**Scope**:

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

Classe com.aspose.pdf.**ImageFormatInternal** *renomeada para com.aspose.pdf.*ImageType**

Alterações na classe com.aspose.pdf.**Document**:

- public void loadXml(String file) -> public void bindXml(String file)

Adicionado:

- public void bindXml(String xmlFile, String xslFile)

Alterações na classe com.aspose.pdf.**EpubLoadOptions**:
Campo adicionado:

- public int MarginsAreaUsageMode

Alterações na classe com.aspose.pdf.**FontAbsorber**:
Adicionado:

- public void visit(Document pdf,int startPage, int pageCount)

Alterações na classe com.aspose.pdf.**Heading**:
Adicionado:

- public int getStartNumber()

- public void setStartNumber(int value)

Mudanças na classe com.aspose.pdf.**HtmlSaveOptions**:
Campos adicionados:

- public boolean SaveTransparentTexts
- public boolean SaveShadowedTextsAsTransparentTexts

Mudanças na classe com.aspose.pdf.**Image**:
Adicionado:

- public TextFragment getTitle()
- public void setTitle(TextFragment value)

Mudanças na classe com.aspose.pdf.**Matrix**:
Adicionado:

- public static Matrix scale(double x, double y)
- public Matrix add(Matrix other)

Mudanças na classe com.aspose.pdf.**Note**:
Adicionado:

- public Note()

Mudanças na classe com.aspose.pdf.**PageCollection**:
Adicionado:

- public void clear()

Mudanças na classe com.aspose.pdf.**Paragraphs**:
Removido:

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)

Mudanças na classe com.aspose.pdf.**RadioButtonOptionField**:
Adicionado:

- public /* BoxStyle */int getStyle()
- public void setStyle(/* BoxStyle */int value)

Mudanças na classe com.aspose.pdf.**TextFragment**:
Removido:

- public NewParagraphPlacementInfo getPlacementInfo()

- public void setPlacementInfo(NewParagraphPlacementInfo value)

Changes in com.aspose.pdf.**UnifiedSaveOptions** class:  
Adicionado campo:

- public boolean TryMergeAdjacentSameBackgroundImages