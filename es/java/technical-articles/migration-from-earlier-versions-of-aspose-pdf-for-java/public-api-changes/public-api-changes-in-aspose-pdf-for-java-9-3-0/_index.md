---
title: Cambios en la API Pública en Aspose.PDF para Java 9.3.0
type: docs
weight: 50
url: es/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página enumera los cambios en la API pública introducidos en [Aspose.PDF para Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx). Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pueda ser visto como una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}}

## Clases Añadidas:

com.aspose.pdf.MemoryCleaner
com.aspose.pdf.generator.legacy.CmykColorSpace
com.aspose.pdf.generator.legacy.GrayColorSpace
com.aspose.pdf.generator.legacyxmlmodel.ClippingPath
com.aspose.pdf.generator.legacyxmlmodel.ColouredTilingPattern

com.aspose.pdf.generator.legacyxmlmodel.CompareValidator
com.aspose.pdf.generator.legacyxmlmodel.PatrónDeRayadoCruzado  
com.aspose.pdf.generator.legacyxmlmodel.ValidadorPersonalizado  
com.aspose.pdf.generator.legacyxmlmodel.Función  
com.aspose.pdf.generator.legacyxmlmodel.FunciónInterpolaciónExponencial  
com.aspose.pdf.generator.legacyxmlmodel.SombreadoDeGradienteAxial  
com.aspose.pdf.generator.legacyxmlmodel.SombreadoDeGradienteRadial  
com.aspose.pdf.generator.legacyxmlmodel.PatrónDeRayado  
com.aspose.pdf.generator.legacyxmlmodel.PatrónDeImagen  
com.aspose.pdf.generator.legacyxmlmodel.PatrónDePuntos  
com.aspose.pdf.generator.legacyxmlmodel.ValidadorDeRango  
com.aspose.pdf.generator.legacyxmlmodel.ValidadorDeExpresiónRegular  
com.aspose.pdf.generator.legacyxmlmodel.ValidadorDeCampoRequerido  
com.aspose.pdf.generator.legacyxmlmodel.PatrónDeGradienteDeSombreado  
com.aspose.pdf.generator.legacyxmlmodel.PatrónDeSombreado  
com.aspose.pdf.generator.legacyxmlmodel.FábricaDePatronesDeSombreado  
com.aspose.pdf.generator.legacyxmlmodel.PatrónDeMosaico  
com.aspose.pdf.generator.legacyxmlmodel.PatrónDeMosaicoSinColor  

com.aspose.pdf.Artifact.TipoDeArtefacto
com.aspose.pdf.Artifact.ArtifactSubtype  
com.aspose.pdf.ILicenseProvider  
com.aspose.pdf.Layer  
com.aspose.pdf.LettersPositioningMethods  

## Clases de Enumeración Añadidas:

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
Implementado el uso de clases de enumeración: **TextEncodingInternal** y **ImageFormatInternal**

## Clases Eliminadas:

La clase obsoleta com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType fue eliminada.

## Clases Movidas:

Las clases del paquete **com.aspose.pdf.generator.legacyxmlmodel.enums** se movieron al paquete **com.aspose.pdf.generator.legacyxmlmodel**

## Clases Internalizadas:

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

## Cambios en las clases:

En la clase **PdfExtractor** se añadió el método 
public extractText(java.nio.charset.Charset value) 

En la clase **PdfFileEditor** se añadió el método 
public static void validateAnotations(IDocument doc)

En la clase **BorderInfo** se añadieron nuevos constructores:
public BorderInfo(int borderSide)
public BorderInfo(int borderSide, GraphInfo borderFormat)
public BorderInfo(int borderSide, float borderWidth)
public BorderInfo(int borderSide, float borderWidth, Color borderColor)
public BorderInfo(int borderSide, Color borderColor)

En la clase **Canvas** se añadió el método 
public Object deepClone()

En la clase **Cell** se añadieron métodos:
public boolean isNoBorder()
public void setNoBorder(boolean value)

public Object completeClone()

En la clase **DocumentAttachment** se agregó el método  
public Object completeClone()

En la clase **FloatingBox** se agregó el método  
public Object completeClone()

En la clase **FormField** se agregó el método  
public Object completeClone()

En la clase **Graph** se agregaron métodos:  
public float getRotatingAngle()  
public void setRotatingAngle(float value)  
public ClippingPath getClipping()  
public void setClipping(ClippingPath value)  
public Object completeClone()

En la clase **Image** se agregaron constructores y métodos:  
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

En la clase **ImageInfo** se agregaron campos y métodos:

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

En la clase **Paragraph** se añadieron campos y métodos:
public float FixedHeight;

public float FixedWidth;
public /**BookmarkIncludeType**/int getBookmarked()  
public void setBookmarked(/**BookmarkIncludeType**/int value)  
public void copyTo(Paragraph par)

En la clase **RadioButton** se añadió el método  
public Object completeClone()

En la clase **Row** se añadió el método  
public Object completeClone()

En la clase **Segment** se añadió el método  
public Object completeClone()

En la clase **Shape** se añadió el método  
public float getOpacity()  
public void setOpacity(float value)  
public float getStrokeOpacity()   
public void setStrokeOpacity(float value)  

En la clase **Shapes** algunos métodos fueron internalizados:  
void add(Shape shape)  
void remove(Shape shapeToRemove)  
void copyTo(Shape[] shapeArray, int index)  
int indexOf(Shape shape)

En la clase **Table** se añadió el método  
public /**override**/ Object completeClone()

En la clase **Text** se añadió el método  
public /**override**/ Object completeClone()

En la clase **XslFoLoadOptions** se añadió el método  
public String getBasePath()   
public void setBasePath(String value)  

En la clase **PdfBookmarkEditor** se añadió el método  

public Bookmarks extractBookmarks(boolean upperLevel)

In **XslFoLoadOptions** clase se añadió el método

In **XslFoLoadOptions** clase se añadió el método

In **XslFoLoadOptions** clase se añadió el método

In **XslFoLoadOptions** clase se añadió el método

**Todos los nombres de los métodos set booleanos que comenzaban con is fueron renombrados a set**

por ejemplo:

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)