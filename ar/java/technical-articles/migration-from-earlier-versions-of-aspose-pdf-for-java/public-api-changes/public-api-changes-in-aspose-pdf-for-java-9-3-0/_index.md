---
title: التغييرات في واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 9.3.0
type: docs
weight: 50
url: /ar/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة التغييرات في واجهة برمجة التطبيقات العامة المقدمة في [Aspose.PDF لـ Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx). لا يشمل ذلك فقط الأساليب العامة الجديدة والمهملة، بل يتضمن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF لـ Java والتي قد تؤثر على الكود الحالي. أي سلوك تم تقديمه قد يُنظر إليه على أنه تراجع ويعدّل السلوك الحالي هو أمر مهم بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

## الفئات المضافة:

com.aspose.pdf.MemoryCleaner  
com.aspose.pdf.generator.legacy.CmykColorSpace  
com.aspose.pdf.generator.legacy.GrayColorSpace  
com.aspose.pdf.generator.legacyxmlmodel.ClippingPath  
com.aspose.pdf.generator.legacyxmlmodel.ColouredTilingPattern  

com.aspose.pdf.generator.legacyxmlmodel.CompareValidator
com.aspose.pdf.generator.legacyxmlmodel.نمط التظليل المتقاطع  
com.aspose.pdf.generator.legacyxmlmodel.المحقق المخصص  
com.aspose.pdf.generator.legacyxmlmodel.وظيفة  
com.aspose.pdf.generator.legacyxmlmodel.دالة التداخل الأسي  
com.aspose.pdf.generator.legacyxmlmodel.تظليل التدرج المحوري  
com.aspose.pdf.generator.legacyxmlmodel.تظليل التدرج الشعاعي  
com.aspose.pdf.generator.legacyxmlmodel.نمط التظليل  
com.aspose.pdf.generator.legacyxmlmodel.نمط الصورة  
com.aspose.pdf.generator.legacyxmlmodel.نمط النقاط  
com.aspose.pdf.generator.legacyxmlmodel.محقق النطاق  
com.aspose.pdf.generator.legacyxmlmodel.محقق التعبير النظامي  
com.aspose.pdf.generator.legacyxmlmodel.محقق الحقل المطلوب  
com.aspose.pdf.generator.legacyxmlmodel.نمط التدرج التظليلي  
com.aspose.pdf.generator.legacyxmlmodel.نمط التظليل  
com.aspose.pdf.generator.legacyxmlmodel.مصنع نمط التظليل  
com.aspose.pdf.generator.legacyxmlmodel.نمط التبليط  
com.aspose.pdf.generator.legacyxmlmodel.نمط التبليط غير الملون  

com.aspose.pdf.Artifact.نوع الأداة
com.aspose.pdf.Artifact.ArtifactSubtype  
com.aspose.pdf.ILicenseProvider  
com.aspose.pdf.Layer  
com.aspose.pdf.LettersPositioningMethods  

## فئات التعداد المضافة:

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
تم تنفيذ استخدام فئات التعداد: **TextEncodingInternal** و **ImageFormatInternal**

## الفئات المحذوفة:

تمت إزالة الفئة المتوقفة com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType.

## الفئات المنقولة:

تم نقل الفئات من الحزمة **com.aspose.pdf.generator.legacyxmlmodel.enums** إلى الحزمة **com.aspose.pdf.generator.legacyxmlmodel**

## الفئات المحولة إلى داخلية:

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

## تغييرات في الفئات:

في فئة **PdfExtractor** تمت إضافة طريقة  
public extractText(java.nio.charset.Charset value)  

في فئة **PdfFileEditor** تمت إضافة طريقة  
public static void validateAnotations(IDocument doc)  

في فئة **BorderInfo** أضيفت مُنشئات جديدة:  
public BorderInfo(int borderSide)  
public BorderInfo(int borderSide, GraphInfo borderFormat)  
public BorderInfo(int borderSide, float borderWidth)  
public BorderInfo(int borderSide, float borderWidth, Color borderColor)  
public BorderInfo(int borderSide, Color borderColor)  

في فئة **Canvas** أضيفت طريقة  
public Object deepClone()  

في فئة **Cell** أضيفت طرق:  
public boolean isNoBorder()  
public void setNoBorder(boolean value)  

public Object completeClone()

في فئة **DocumentAttachment** تمت إضافة الطريقة  
public Object completeClone()

في فئة **FloatingBox** تمت إضافة الطريقة  
public Object completeClone()

في فئة **FormField** تمت إضافة الطريقة  
public Object completeClone()

في فئة **Graph** تمت إضافة الطرق:  
public float getRotatingAngle()  
public void setRotatingAngle(float value)  
public ClippingPath getClipping()  
public void setClipping(ClippingPath value)  
public Object completeClone()

في فئة **Image** تمت إضافة المنشئات والطرق:  
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

في فئة **ImageInfo** تمت إضافة الحقول والطرق:  

public TextInfo TextInfo

public String Title
public BorderInfo ImageBorder

public /**ImageFileType**/int _ImageFileType
public InputStream getImageStream()
public void setImageStream(InputStream value)
public BufferedImage getSystemImage()
public void setSystemImage(BufferedImage value)  
public /**Byte**/byte[] getMemoryData() 
public void setMemoryData(/**Byte**/byte[] value) 
public boolean isFixImgWidthSettedInXML() 
public void setFixImgWidthSettedInXML(boolean value) 
public boolean isFixImgHeightSettedInXML()
public void setFixImgHeightSettedInXML(boolean value) 
public boolean isAllFramesInNewPage() 
public void setAllFramesInNewPage(boolean value)
public boolean isStencilMask() 
public void setStencilMask(boolean value)
public com.aspose.pdf.generator.legacyxmlmodel.Color getBackgroundColor() 
public void setBackgroundColor(com.aspose.pdf.generator.legacyxmlmodel.Color value)
public java.awt.Color getPatternColor()
public void setPatternColor(java.awt.Color value) 

في **فئة الفقرة** تمت إضافة الحقول والطرق:
public float FixedHeight;

public float FixedWidth;
public /**BookmarkIncludeType**/int getBookmarked()
public void setBookmarked(/**BookmarkIncludeType**/int value)
public void copyTo(Paragraph par)

في فئة **RadioButton** تمت إضافة طريقة
public Object completeClone()

في فئة **Row** تمت إضافة طريقة
public Object completeClone()

في فئة **Segment** تمت إضافة طريقة
public Object completeClone()

في فئة **Shape** تمت إضافة طريقة
public float getOpacity()
public void setOpacity(float value)
public float getStrokeOpacity() 
public void setStrokeOpacity(float value)  

في فئة **Shapes** بعض الطرق تم جعلها داخلية:
void add(Shape shape)
void remove(Shape shapeToRemove)
void copyTo(Shape[] shapeArray, int index)
int indexOf(Shape shape)

في فئة **Table** تمت إضافة طريقة
public /**override**/ Object completeClone()

في فئة **Text** تمت إضافة طريقة
public /**override**/ Object completeClone()

في فئة **XslFoLoadOptions** تمت إضافة طريقة
public String getBasePath() 
public void setBasePath(String value)  

في فئة **PdfBookmarkEditor** تمت إضافة طريقة

public Bookmarks extractBookmarks(boolean upperLevel)


In **XslFoLoadOptions** class added method

في فئة **XslFoLoadOptions** تمت إضافة طريقة

In **XslFoLoadOptions** class added method

في فئة **XslFoLoadOptions** تمت إضافة طريقة

In **XslFoLoadOptions** class added method

في فئة **XslFoLoadOptions** تمت إضافة طريقة

In **XslFoLoadOptions** class added method

في فئة **XslFoLoadOptions** تمت إضافة طريقة

**All the boolean setter method names that were started from is was renamed ro set**

**تمت إعادة تسمية جميع أسماء طرق تعيين القيم البوليانية التي كانت تبدأ بـ is إلى set**

for example:

على سبيل المثال:

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)