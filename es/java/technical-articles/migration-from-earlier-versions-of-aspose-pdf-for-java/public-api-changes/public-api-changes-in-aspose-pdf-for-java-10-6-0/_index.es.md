---
title: Cambios en la API Pública en Aspose.PDF para Java 10.6.0
type: docs
weight: 120
url: /java/public-api-changes-in-aspose-pdf-for-java-10-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página enumera los cambios en la API pública introducidos en [Aspose.PDF para Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx). No solo incluye nuevos métodos públicos y los obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar al código existente. Cualquier comportamiento introducido que pueda ser visto como una regresión y modifique el comportamiento existente es especialmente importante y está documentado aquí.

{{% /alert %}}

**Cambios en la API Pública 10.6.0**

Clases añadidas:

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

Clases eliminadas:

- com.aspose.pdf.**NewParagraphPlacementInfo**

Cambios en la clase com.aspose.pdf.drawind.**Circle**:

- public float getPosX() -> public double getPosX() 
- public void setPosX(float value) -> public void setPosX(double value)
- public float getPosY() -> public double getPosY()
- public void setPosY(float value) -> public void setPosY(double value)
- public float getRadius() -> public double getRadius()
- public void setRadius(float value) -> public void setRadius(double value)

Cambios en la clase com.aspose.pdf.drawind.**Curve**:
Añadido:

- public float[] getPositionArray()
- public void setPositionArray(float[] value)

Eliminado:

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

Cambios en la clase com.aspose.pdf.drawind.**Ellipse**:

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

Cambios en la clase com.aspose.pdf.drawing.**Graph**:  
Añadido:

- public GraphInfo getGraphInfo()

Eliminado:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  
- public double getRotationAngle()  
- public void setRotationAngle(double value)  

Cambios en la clase com.aspose.pdf.**GraphInfo**:  
Añadido:

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

Cambios en la clase com.aspose.pdf.drawind.**Rectangle**:

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

Añadido:

- public Rectangle()  

Cambios en la clase com.aspose.pdf.**PdfFileEditor**:

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

Añadido:

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

Cambios en la clase com.aspose.pdf.ReplaceTextStrategy.**Scope**:

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

Clase com.aspose.pdf.**ImageFormatInternal** *renombrada a com.aspose.pdf.*ImageType**

Cambios en la clase com.aspose.pdf.**Document**:

- public void loadXml(String file) -> public void bindXml(String file)

Añadido:

- public void bindXml(String xmlFile, String xslFile)

Cambios en la clase com.aspose.pdf.**EpubLoadOptions**:
Campo añadido:

- public int MarginsAreaUsageMode

Cambios en la clase com.aspose.pdf.**FontAbsorber**:
Añadido:

- public void visit(Document pdf, int startPage, int pageCount)

Cambios en la clase com.aspose.pdf.**Heading**:
Añadido:

- public int getStartNumber()

- public void setStartNumber(int value)

Cambios en la clase com.aspose.pdf.**HtmlSaveOptions**:
Campos añadidos:

- public boolean SaveTransparentTexts
- public boolean SaveShadowedTextsAsTransparentTexts

Cambios en la clase com.aspose.pdf.**Image**:
Añadido:

- public TextFragment getTitle()
- public void setTitle(TextFragment value)

Cambios en la clase com.aspose.pdf.**Matrix**:
Añadido:

- public static Matrix scale(double x, double y)
- public Matrix add(Matrix other)

Cambios en la clase com.aspose.pdf.**Note**:
Añadido:

- public Note()

Cambios en la clase com.aspose.pdf.**PageCollection**:
Añadido:

- public void clear()

Cambios en la clase com.aspose.pdf.**Paragraphs**:
Eliminado:

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)

Cambios en la clase com.aspose.pdf.**RadioButtonOptionField**:
Añadido:

- public /* BoxStyle */int getStyle()
- public void setStyle(/* BoxStyle */int value)

Cambios en la clase com.aspose.pdf.**TextFragment**:
Eliminado:

- public NewParagraphPlacementInfo getPlacementInfo()

- public void setPlacementInfo(NewParagraphPlacementInfo value)

Cambios en la clase com.aspose.pdf.**UnifiedSaveOptions**:  
Campo añadido:

- public boolean TryMergeAdjacentSameBackgroundImages