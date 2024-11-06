---
title: Perubahan API Publik di Aspose.PDF untuk Java 10.6.0
type: docs
weight: 120
url: id/java/public-api-changes-in-aspose-pdf-for-java-10-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan di [Aspose.PDF untuk Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx). Ini termasuk tidak hanya metode publik baru dan usang, tetapi juga deskripsi tentang setiap perubahan dalam perilaku di balik layar di Aspose.PDF untuk Java yang dapat mempengaruhi kode yang ada. Perilaku apa pun yang diperkenalkan yang dapat dianggap sebagai regresi dan memodifikasi perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

**Perubahan API Publik 10.6.0**

Kelas yang ditambahkan:

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

Kelas yang dihapus:

- com.aspose.pdf.**NewParagraphPlacementInfo**

Perubahan dalam kelas com.aspose.pdf.drawind.**Circle**:

- public float getPosX() -> public double getPosX() 
- public void setPosX(float value) -> public void setPosX(double value)
- public float getPosY() -> public double getPosY()
- public void setPosY(float value) -> public void setPosY(double value)
- public float getRadius() -> public double getRadius()
- public void setRadius(float value) -> public void setRadius(double value)

Perubahan dalam kelas com.aspose.pdf.drawind.**Curve**:
Ditambahkan:

- public float[] getPositionArray()
- public void setPositionArray(float[] value)

Dihapus:

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

Perubahan dalam kelas com.aspose.pdf.drawind.**Ellipse**:

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

Perubahan dalam kelas com.aspose.pdf.drawing.**Graph**:  
Ditambahkan:

- public GraphInfo getGraphInfo()

Dihapus:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  
- public double getRotationAngle()  
- public void setRotationAngle(double value)  

Perubahan dalam kelas com.aspose.pdf.**GraphInfo**:  
Ditambahkan:

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  

- public double getRotationAngle()  
- public void setRotationAngle(double value) - public double getScalingRateX() - public void setScalingRateX(double value) - public double getScalingRateY() - public void setScalingRateY(double value)

Perubahan dalam kelas com.aspose.pdf.drawind.**Rectangle**:

- public float getRadiusForRoundCorner() -> public double getRoundedCornerRadius() - public void setRadiusForRoundCorner(float value) -> public void setRoundedCornerRadius(double value) - public float getLeft() -> public double getLeft() - public void setLeft(float value) -> public void setLeft(double value) - public float getBottom() -> public double getBottom() - public void setBottom(float value) -> public void setBottom(double value) - public float getWidth() -> public double getWidth() - public void setWidth(float value) -> public void setWidth(double value) - public float getHeight() -> public double getHeight() - public void setHeight(float value) -> public void setHeight(double value)

Ditambahkan:

- public Rectangle()

Perubahan dalam kelas com.aspose.pdf.**PdfFileEditor**:

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

Ditambahkan:

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

Perubahan dalam kelas com.aspose.pdf.ReplaceTextStrategy.**Scope**:

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

Kelas com.aspose.pdf.**ImageFormatInternal *diubah namanya menjadi com.aspose.pdf.*ImageType**

Perubahan dalam kelas com.aspose.pdf.**Document**:

- public void loadXml(String file) -> public void bindXml(String file)

Ditambahkan:

- public void bindXml(String xmlFile, String xslFile)

Perubahan dalam kelas com.aspose.pdf.**EpubLoadOptions**:
Ditambahkan field:

- public int MarginsAreaUsageMode

Perubahan dalam kelas com.aspose.pdf.**FontAbsorber**:
Ditambahkan:

- public void visit(Document pdf, int startPage, int pageCount)

Perubahan dalam kelas com.aspose.pdf.**Heading**:
Ditambahkan:

- public int getStartNumber()

- public void setStartNumber(int value)

Perubahan dalam kelas com.aspose.pdf.**HtmlSaveOptions**:
Bidang yang ditambahkan:

- public boolean SaveTransparentTexts
- public boolean SaveShadowedTextsAsTransparentTexts

Perubahan dalam kelas com.aspose.pdf.**Image**:
Ditambahkan:

- public TextFragment getTitle()
- public void setTitle(TextFragment value)

Perubahan dalam kelas com.aspose.pdf.**Matrix**:
Ditambahkan:

- public static Matrix scale(double x, double y)
- public Matrix add(Matrix other)

Perubahan dalam kelas com.aspose.pdf.**Note**:
Ditambahkan:

- public Note()

Perubahan dalam kelas com.aspose.pdf.**PageCollection**:
Ditambahkan:

- public void clear()

Perubahan dalam kelas com.aspose.pdf.**Paragraphs**:
Dihapus:

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)

Perubahan dalam kelas com.aspose.pdf.**RadioButtonOptionField**:
Ditambahkan:

- public /* BoxStyle */int getStyle()
- public void setStyle(/* BoxStyle */int value)

Perubahan dalam kelas com.aspose.pdf.**TextFragment**:
Dihapus:

- public NewParagraphPlacementInfo getPlacementInfo()

- public void setPlacementInfo(NewParagraphPlacementInfo value)

Perubahan dalam kelas com.aspose.pdf.**UnifiedSaveOptions**:  
Menambahkan bidang:

- public boolean CobaGabungkanGambarLatarBelakangYangSamaBerdekatan