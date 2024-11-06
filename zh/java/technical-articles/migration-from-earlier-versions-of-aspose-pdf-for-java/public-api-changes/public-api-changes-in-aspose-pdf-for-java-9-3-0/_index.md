---
title: Aspose.PDF for Java 9.3.0 中的公共 API 更改
type: docs
weight: 50
url: zh/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了在 [Aspose.PDF for Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx) 中引入的公共 API 更改。它不仅包括新的和已废弃的公共方法，还包括对 Aspose.PDF for Java 背后行为的任何更改的描述，这些更改可能会影响现有代码。任何被视为回归且修改现有行为的行为都特别重要，并在此记录。

{{% /alert %}}

## 添加的类：

com.aspose.pdf.MemoryCleaner  
com.aspose.pdf.generator.legacy.CmykColorSpace  
com.aspose.pdf.generator.legacy.GrayColorSpace  
com.aspose.pdf.generator.legacyxmlmodel.ClippingPath  
com.aspose.pdf.generator.legacyxmlmodel.ColouredTilingPattern  

com.aspose.pdf.generator.legacyxmlmodel.CompareValidator
com.aspose.pdf.generator.legacyxmlmodel.交叉影线图案
com.aspose.pdf.generator.legacyxmlmodel.自定义验证器
com.aspose.pdf.generator.legacyxmlmodel.函数
com.aspose.pdf.generator.legacyxmlmodel.指数插值函数
com.aspose.pdf.generator.legacyxmlmodel.渐变轴向阴影
com.aspose.pdf.generator.legacyxmlmodel.渐变径向阴影
com.aspose.pdf.generator.legacyxmlmodel.影线图案
com.aspose.pdf.generator.legacyxmlmodel.图像图案
com.aspose.pdf.generator.legacyxmlmodel.点图案
com.aspose.pdf.generator.legacyxmlmodel.范围验证器
com.aspose.pdf.generator.legacyxmlmodel.正则表达式验证器
com.aspose.pdf.generator.legacyxmlmodel.必填字段验证器
com.aspose.pdf.generator.legacyxmlmodel.阴影渐变图案
com.aspose.pdf.generator.legacyxmlmodel.阴影图案
com.aspose.pdf.generator.legacyxmlmodel.阴影图案工厂
com.aspose.pdf.generator.legacyxmlmodel.平铺图案
com.aspose.pdf.generator.legacyxmlmodel.无色平铺图案

com.aspose.pdf.Artifact.工件类型

com.aspose.pdf.Artifact.ArtifactSubtype  
com.aspose.pdf.ILicenseProvider  
com.aspose.pdf.Layer  
com.aspose.pdf.LettersPositioningMethods  

## 枚举类已添加：

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
实现了枚举类的使用：**TextEncodingInternal** 和 **ImageFormatInternal**

## 类已移除：

已弃用的 com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType 类被移除。

## 类已移动：

包 **com.aspose.pdf.generator.legacyxmlmodel.enums** 中的类已移动到包 **com.aspose.pdf.generator.legacyxmlmodel**

## 类已内部化：

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

## 类的更改：

在 **PdfExtractor** 类中添加了方法  
public extractText(java.nio.charset.Charset value)  

在 **PdfFileEditor** 类中添加了方法  
public static void validateAnotations(IDocument doc)  

在 **BorderInfo** 类中添加了新的构造函数：  
public BorderInfo(int borderSide)  
public BorderInfo(int borderSide, GraphInfo borderFormat)  
public BorderInfo(int borderSide, float borderWidth)  
public BorderInfo(int borderSide, float borderWidth, Color borderColor)  
public BorderInfo(int borderSide, Color borderColor)  

在 **Canvas** 类中添加了方法  
public Object deepClone()  

在 **Cell** 类中添加了方法：  
public boolean isNoBorder()  
public void setNoBorder(boolean value)  

public Object completeClone()  

在 **DocumentAttachment** 类中添加了方法  
public Object completeClone()

在 **FloatingBox** 类中添加了方法  
public Object completeClone()

在 **FormField** 类中添加了方法  
public Object completeClone()

在 **Graph** 类中添加了方法：  
public float getRotatingAngle()  
public void setRotatingAngle(float value)  
public ClippingPath getClipping()  
public void setClipping(ClippingPath value)  
public Object completeClone()

在 **Image** 类中添加了构造函数和方法：  
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

在 **ImageInfo** 类中添加了字段和方法：  

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

在**Paragraph**类中添加了字段和方法：
public float FixedHeight;

public float FixedWidth;
public /**BookmarkIncludeType**/int getBookmarked()  
public void setBookmarked(/**BookmarkIncludeType**/int value)  
public void copyTo(Paragraph par)  

在 **RadioButton** 类中添加了方法  
public Object completeClone()  

在 **Row** 类中添加了方法  
public Object completeClone()  

在 **Segment** 类中添加了方法  
public Object completeClone()  

在 **Shape** 类中添加了方法  
public float getOpacity()  
public void setOpacity(float value)  
public float getStrokeOpacity()  
public void setStrokeOpacity(float value)  

在 **Shapes** 类中，一些方法被内部化:  
void add(Shape shape)  
void remove(Shape shapeToRemove)  
void copyTo(Shape[] shapeArray, int index)  
int indexOf(Shape shape)  

在 **Table** 类中添加了方法  
public /**override**/ Object completeClone()  

在 **Text** 类中添加了方法  
public /**override**/ Object completeClone()  

在 **XslFoLoadOptions** 类中添加了方法  
public String getBasePath()  
public void setBasePath(String value)  

在 **PdfBookmarkEditor** 类中添加了方法  

public Bookmarks extractBookmarks(boolean upperLevel)

In **XslFoLoadOptions** 类中添加了方法

In **XslFoLoadOptions** 类中添加了方法

In **XslFoLoadOptions** 类中添加了方法

In **XslFoLoadOptions** 类中添加了方法

**所有以 is 开头的布尔设置器方法名称已重命名为 set**

例如：

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)