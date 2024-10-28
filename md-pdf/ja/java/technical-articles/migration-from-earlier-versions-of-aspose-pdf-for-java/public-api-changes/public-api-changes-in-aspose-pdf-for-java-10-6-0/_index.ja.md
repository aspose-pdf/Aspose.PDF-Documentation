---
title: Aspose.PDF for Java 10.6.0における公開APIの変更
type: docs
weight: 120
url: /java/public-api-changes-in-aspose-pdf-for-java-10-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、[Aspose.PDF for Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx)で導入された公開APIの変更を一覧にしています。新しく追加された公開メソッドや廃止されたメソッドだけでなく、Aspose.PDF for Javaの裏側の動作における変更で既存のコードに影響を及ぼす可能性のあるものについても記載しています。既存の動作を変更するような回帰として見られる可能性のある動作は特に重要であり、ここに記録されています。

{{% /alert %}}

**公開APIの変更 10.6.0**

追加されたクラス:

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

削除されたクラス:  

- com.aspose.pdf.**NewParagraphPlacementInfo**  

com.aspose.pdf.drawind.**Circle** クラスの変更:  

- public float getPosX() -> public double getPosX()  
- public void setPosX(float value) -> public void setPosX(double value)  
- public float getPosY() -> public double getPosY()  
- public void setPosY(float value) -> public void setPosY(double value)  
- public float getRadius() -> public double getRadius()  
- public void setRadius(float value) -> public void setRadius(double value)  

com.aspose.pdf.drawind.**Curve** クラスの変更:  
追加:  

- public float[] getPositionArray()  
- public void setPositionArray(float[] value)  

削除:  

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

com.aspose.pdf.drawind.**Ellipse** クラスの変更:

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

com.aspose.pdf.drawing.**Graph** クラスの変更:  
追加:

- public GraphInfo getGraphInfo()

削除:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  
- public double getRotationAngle()  
- public void setRotationAngle(double value)  

com.aspose.pdf.**GraphInfo** クラスの変更:  
追加:

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

com.aspose.pdf.drawind.**Rectangle** クラスの変更点:

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

追加:

- public Rectangle()  

com.aspose.pdf.**PdfFileEditor** クラスの変更点:

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

追加:

- public boolean getUseDiskBuffer()  
- public void setUseDiskBuffer(boolean value)  
- public int getConcatenationPacketSize()  
- public void setConcatenationPacketSize(int value)  

com.aspose.pdf.ReplaceTextStrategy.**Scope** クラスの変更:

- REPLACE_FIRST -> ReplaceFirst  
- REPLACE_ALL -> ReplaceAll  

クラス com.aspose.pdf.**ImageFormatInternal** は **com.aspose.pdf.ImageType** に改名されました

com.aspose.pdf.**Document** クラスの変更:

- public void loadXml(String file) -> public void bindXml(String file)

追加:

- public void bindXml(String xmlFile, String xslFile)

com.aspose.pdf.**EpubLoadOptions** クラスの変更:  
追加されたフィールド:

- public int MarginsAreaUsageMode

com.aspose.pdf.**FontAbsorber** クラスの変更:  
追加:

- public void visit(Document pdf, int startPage, int pageCount)

com.aspose.pdf.**Heading** クラスの変更:  
追加:

- public int getStartNumber()

- public void setStartNumber(int value)

com.aspose.pdf.**HtmlSaveOptions** クラスの変更:
フィールドが追加されました:

- public boolean SaveTransparentTexts
- public boolean SaveShadowedTextsAsTransparentTexts

com.aspose.pdf.**Image** クラスの変更:
追加されました:

- public TextFragment getTitle()
- public void setTitle(TextFragment value)

com.aspose.pdf.**Matrix** クラスの変更:
追加されました:

- public static Matrix scale(double x, double y)
- public Matrix add(Matrix other)

com.aspose.pdf.**Note** クラスの変更:
追加されました:

- public Note()

com.aspose.pdf.**PageCollection** クラスの変更:
追加されました:

- public void clear()

com.aspose.pdf.**Paragraphs** クラスの変更:
削除されました:

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)

com.aspose.pdf.**RadioButtonOptionField** クラスの変更:
追加されました:

- public /* BoxStyle */int getStyle()
- public void setStyle(/* BoxStyle */int value)

com.aspose.pdf.**TextFragment** クラスの変更:
削除されました:

- public NewParagraphPlacementInfo getPlacementInfo()

- public void setPlacementInfo(NewParagraphPlacementInfo value)

Changes in com.aspose.pdf.**UnifiedSaveOptions** クラス:  
追加されたフィールド:

- public boolean TryMergeAdjacentSameBackgroundImages