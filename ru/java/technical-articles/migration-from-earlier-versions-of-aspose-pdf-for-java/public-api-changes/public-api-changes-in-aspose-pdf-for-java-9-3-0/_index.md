---
title: Изменения публичного API в Aspose.PDF для Java 9.3.0
type: docs
weight: 50
url: /ru/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения публичного API, введенные в [Aspose.PDF для Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx). Здесь включены не только новые и устаревшие публичные методы, но и описание любых изменений в поведении за кулисами в Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, которое может восприниматься как регрессия и изменяет существующее поведение, особенно важно и документировано здесь.

{{% /alert %}}

## Добавленные классы:

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

## Добавлены классы перечислений:

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
Реализовано использование классов перечислений: **TextEncodingInternal** и **ImageFormatInternal**  

## Удаленные классы:

Устаревший класс com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType был удален.

## Перемещенные классы:

Классы из пакета **com.aspose.pdf.generator.legacyxmlmodel.enums** перемещены в пакет **com.aspose.pdf.generator.legacyxmlmodel**

## Внутренние классы:

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

## Изменения в классах:

В классе **PdfExtractor** был добавлен метод  
public extractText(java.nio.charset.Charset value)  

В классе **PdfFileEditor** был добавлен метод  
public static void validateAnotations(IDocument doc)  

В классе **BorderInfo** добавлены новые конструкторы:  
public BorderInfo(int borderSide)  
public BorderInfo(int borderSide, GraphInfo borderFormat)  
public BorderInfo(int borderSide, float borderWidth)  
public BorderInfo(int borderSide, float borderWidth, Color borderColor)  
public BorderInfo(int borderSide, Color borderColor)  

В классе **Canvas** добавлен метод  
public Object deepClone()  

В классе **Cell** добавлены методы:  
public boolean isNoBorder()  
public void setNoBorder(boolean value)  

public Object completeClone()

In классе **DocumentAttachment** добавлен метод 
public Object completeClone()

В классе **FloatingBox** добавлен метод
public Object completeClone()

В классе **FormField** добавлен метод
public Object completeClone()

В классе **Graph** добавлены методы:
public float getRotatingAngle() 
public void setRotatingAngle(float value) 
public ClippingPath getClipping() 
public void setClipping(ClippingPath value) 
public Object completeClone()

В классе **Image** добавлены конструкторы и методы:
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

В классе **ImageInfo** добавлены поля и методы:

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

В классе **Paragraph** добавлены поля и методы:
public float FixedHeight;

public float FixedWidth;
public /**BookmarkIncludeType**/int getBookmarked()
public void setBookmarked(/**BookmarkIncludeType**/int value)
public void copyTo(Paragraph par)

В классе **RadioButton** добавлен метод
public Object completeClone()

В классе **Row** добавлен метод
public Object completeClone()

В классе **Segment** добавлен метод
public Object completeClone()

В классе **Shape** добавлен метод
public float getOpacity()
public void setOpacity(float value)
public float getStrokeOpacity()
public void setStrokeOpacity(float value)

В классе **Shapes** некоторые методы были сделаны внутренними:
void add(Shape shape)
void remove(Shape shapeToRemove)
void copyTo(Shape[] shapeArray, int index)
int indexOf(Shape shape)

В классе **Table** добавлен метод
public /**override**/ Object completeClone()

В классе **Text** добавлен метод
public /**override**/ Object completeClone()

В классе **XslFoLoadOptions** добавлен метод
public String getBasePath()
public void setBasePath(String value)

В классе **PdfBookmarkEditor** добавлен метод

public Bookmarks extractBookmarks(boolean upperLevel)


In **XslFoLoadOptions** класс добавлен метод

In **XslFoLoadOptions** класс добавлен метод

In **XslFoLoadOptions** класс добавлен метод

In **XslFoLoadOptions** класс добавлен метод

**Все имена методов установки логических значений, которые начинались с is, были переименованы на set**

например:

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)