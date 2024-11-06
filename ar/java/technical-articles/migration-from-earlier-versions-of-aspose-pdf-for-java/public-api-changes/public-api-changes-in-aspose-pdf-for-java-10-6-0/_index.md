---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 10.6.0
type: docs
weight: 120
url: ar/java/public-api-changes-in-aspose-pdf-for-java-10-6-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة التي تم إدخالها في [Aspose.PDF لـ Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx). إنه يشمل ليس فقط الأساليب العامة الجديدة والمهملة، بل أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF لـ Java والتي قد تؤثر على الشفرة الحالية. أي سلوك تم إدخاله يمكن اعتباره تراجعًا ويعدل السلوك الحالي هو مهم بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

**تغييرات واجهة برمجة التطبيقات العامة 10.6.0**

تمت إضافة الفئات:

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

تم إزالة الفئات:  

- com.aspose.pdf.**NewParagraphPlacementInfo**  

التغييرات في فئة com.aspose.pdf.drawind.**Circle**:  

- public float getPosX() -> public double getPosX()  
- public void setPosX(float value) -> public void setPosX(double value)  
- public float getPosY() -> public double getPosY()  
- public void setPosY(float value) -> public void setPosY(double value)  
- public float getRadius() -> public double getRadius()  
- public void setRadius(float value) -> public void setRadius(double value)  

التغييرات في فئة com.aspose.pdf.drawind.**Curve**:  
تمت الإضافة:  

- public float[] getPositionArray()  
- public void setPositionArray(float[] value)  

تمت الإزالة:  

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

التغييرات في فئة com.aspose.pdf.drawind.**Ellipse**:

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)

التغييرات في فئة com.aspose.pdf.drawing.**Graph**: 
أضيف:

- public GraphInfo getGraphInfo()

أزيل:

- public double getSkewAngleX() 
- public void setSkewAngleX(double value) 
- public double getSkewAngleY() 
- public void setSkewAngleY(double value) 
- public double getRotationAngle()  
- public void setRotationAngle(double value) 

التغييرات في فئة com.aspose.pdf.**GraphInfo**: 
أضيف:

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

التغييرات في فئة com.aspose.pdf.drawind.**Rectangle**:

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

أضيف:

- public Rectangle()  

التغييرات في فئة com.aspose.pdf.**PdfFileEditor**:

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

تمت الإضافة:

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

التغييرات في فئة com.aspose.pdf.ReplaceTextStrategy.**Scope**:

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

فئة com.aspose.pdf.**ImageFormatInternal *renamed to com.aspose.pdf.*ImageType**

التغييرات في فئة com.aspose.pdf.**Document**:

- public void loadXml(String file) -> public void bindXml(String file)

تمت الإضافة:

- public void bindXml(String xmlFile, String xslFile)

التغييرات في فئة com.aspose.pdf.**EpubLoadOptions**:
تمت إضافة حقل:

- public int MarginsAreaUsageMode

التغييرات في فئة com.aspose.pdf.**FontAbsorber**:
تمت الإضافة:

- public void visit(Document pdf,int startPage, int pageCount)

التغييرات في فئة com.aspose.pdf.**Heading**:
تمت الإضافة:

- public int getStartNumber()

- public void setStartNumber(int value)

التغييرات في فئة com.aspose.pdf.**HtmlSaveOptions**:
تمت إضافة الحقول:

- public boolean حفظ النصوص الشفافة
- public boolean حفظ النصوص المظللة كنصوص شفافة

التغييرات في فئة com.aspose.pdf.**Image**:
تمت الإضافة:

- public TextFragment الحصول على العنوان()
- public void تعيين العنوان(TextFragment القيمة)

التغييرات في فئة com.aspose.pdf.**Matrix**:
تمت الإضافة:

- public static Matrix تكبير(double x, double y)
- public Matrix إضافة(Matrix أخرى)

التغييرات في فئة com.aspose.pdf.**Note**:
تمت الإضافة:

- public Note()

التغييرات في فئة com.aspose.pdf.**PageCollection**:
تمت الإضافة:

- public void مسح()

التغييرات في فئة com.aspose.pdf.**Paragraphs**:
تمت الإزالة:

- public void إضافة(BaseParagraph فقرة, NewParagraphPlacementInfo معلومات التمركز)

التغييرات في فئة com.aspose.pdf.**RadioButtonOptionField**:
تمت الإضافة:

- public /* BoxStyle */int الحصول على النمط()
- public void تعيين النمط(/* BoxStyle */int القيمة)

التغييرات في فئة com.aspose.pdf.**TextFragment**:
تمت الإزالة:

- public NewParagraphPlacementInfo الحصول على معلومات التمركز()

- public void تعيين معلومات التمركز(NewParagraphPlacementInfo القيمة)

Changes in com.aspose.pdf.**UnifiedSaveOptions** class:  
تمت إضافة الحقل:

- public boolean TryMergeAdjacentSameBackgroundImages