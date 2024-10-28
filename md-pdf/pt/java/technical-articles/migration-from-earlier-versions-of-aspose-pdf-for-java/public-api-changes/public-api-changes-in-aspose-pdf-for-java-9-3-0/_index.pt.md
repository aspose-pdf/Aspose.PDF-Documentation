---
title: Mudanças na API Pública no Aspose.PDF para Java 9.3.0
type: docs
weight: 50
url: /java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no [Aspose.PDF para Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx). Ela inclui não apenas novos métodos públicos e métodos obsoletos, mas também uma descrição de quaisquer mudanças no comportamento nos bastidores no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifique o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

## Classes Adicionadas:

com.aspose.pdf.MemoryCleaner com.aspose.pdf.generator.legacy.CmykColorSpace com.aspose.pdf.generator.legacy.GrayColorSpace com.aspose.pdf.generator.legacyxmlmodel.ClippingPath com.aspose.pdf.generator.legacyxmlmodel.ColouredTilingPattern

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
com.aspose.pdf.Artifact.ArtifactSubtype com.aspose.pdf.ILicenseProvider com.aspose.pdf.Layer com.aspose.pdf.LettersPositioningMethods

## Classes de Enumeração Adicionadas:

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType Implementado uso de classes de enumeração: **TextEncodingInternal** e **ImageFormatInternal**

## Classes Removidas:

Classe obsoleta com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType foi removida.

## Classes Movidas:

Classes do pacote **com.aspose.pdf.generator.legacyxmlmodel.enums** foram movidas para o pacote **com.aspose.pdf.generator.legacyxmlmodel**

## Classes Internalizadas:

com.aspose.pdf.XfdfTags com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape com.aspose.pdf.generator.legacyxmlmodel.ComplexShape

com.aspose.pdf.generator.legacyxmlmodel.Circle
com.aspose.pdf.generator.legacyxmlmodel.Curve  
com.aspose.pdf.generator.legacyxmlmodel.NonClosedShape  
com.aspose.pdf.generator.legacyxmlmodel.Ellipse  
com.aspose.pdf.generator.legacyxmlmodel.PolyDashArray  
com.aspose.pdf.generator.legacyxmlmodel.PathArea  
com.aspose.pdf.generator.legacyxmlmodel.Rectangle  

## Mudanças nas classes:

Na classe **PdfExtractor** foi adicionado o método  
public extractText(java.nio.charset.Charset value)  

Na classe **PdfFileEditor** foi adicionado o método  
public static void validateAnotations(IDocument doc)  

Na classe **BorderInfo** foram adicionados novos construtores:  
public BorderInfo(int borderSide)  
public BorderInfo(int borderSide, GraphInfo borderFormat)  
public BorderInfo(int borderSide, float borderWidth)  
public BorderInfo(int borderSide, float borderWidth, Color borderColor)  
public BorderInfo(int borderSide, Color borderColor)  

Na classe **Canvas** foi adicionado o método  
public Object deepClone()  

Na classe **Cell** foram adicionados os métodos:  
public boolean isNoBorder()  
public void setNoBorder(boolean value)  

public Object completeClone()  

In **DocumentAttachment** class added method 
public Object completeClone()

Na classe **FloatingBox** foi adicionado o método
public Object completeClone()

Na classe **FormField** foi adicionado o método
public Object completeClone()

Na classe **Graph** foram adicionados os métodos:
public float getRotatingAngle() 
public void setRotatingAngle(float value) 
public ClippingPath getClipping() 
public void setClipping(ClippingPath value) 
public Object completeClone()

Na classe **Image** foram adicionados construtores e métodos:
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

Na classe **ImageInfo** foram adicionados campos e métodos:

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

Na classe **Parágrafo** foram adicionados campos e métodos:
public float FixedHeight;

public float FixedWidth;

public /**BookmarkIncludeType**/int getBookmarked()
public void setBookmarked(/**BookmarkIncludeType**/int value)
public void copyTo(Parágrafo par)

Na classe **RadioButton** foi adicionado o método
public Object completeClone()

Na classe **Row** foi adicionado o método
public Object completeClone()

Na classe **Segment** foi adicionado o método
public Object completeClone()

Na classe **Shape** foi adicionado o método
public float getOpacity()
public void setOpacity(float value)
public float getStrokeOpacity() 
public void setStrokeOpacity(float value)

Na classe **Shapes** alguns métodos foram internalizados:
void add(Shape shape)
void remove(Shape shapeToRemove)
void copyTo(Shape[] shapeArray, int index)
int indexOf(Shape shape)

Na classe **Table** foi adicionado o método
public /**override**/ Object completeClone()

Na classe **Text** foi adicionado o método
public /**override**/ Object completeClone()

Na classe **XslFoLoadOptions** foi adicionado o método
public String getBasePath() 
public void setBasePath(String value)

Na classe **PdfBookmarkEditor** foi adicionado o método

public Bookmarks extractBookmarks(boolean upperLevel)

In **XslFoLoadOptions** classe, foi adicionado o método

In **XslFoLoadOptions** classe, foi adicionado o método

In **XslFoLoadOptions** classe, foi adicionado o método

In **XslFoLoadOptions** classe, foi adicionado o método

**Todos os nomes de métodos booleanos setter que começavam com is foram renomeados para set**

por exemplo:

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)