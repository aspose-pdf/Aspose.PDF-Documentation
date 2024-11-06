---
title: Changements de l'API publique dans Aspose.PDF pour Java 9.3.0
type: docs
weight: 50
url: fr/java/public-api-changes-in-aspose-pdf-for-java-9-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page répertorie les changements de l'API publique introduits dans [Aspose.PDF pour Java 9.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry559320.aspx). Elle inclut non seulement les nouvelles méthodes publiques et celles obsolètes, mais aussi une description de tout changement dans le comportement en coulisse dans Aspose.PDF pour Java qui pourrait affecter le code existant. Tout comportement introduit qui pourrait être perçu comme une régression et modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

## Classes ajoutées :

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

## Classes d'énumération ajoutées :

com.aspose.pdf.generator.legacyxmlmodel.enums.FunctionType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PaintType  
com.aspose.pdf.generator.legacyxmlmodel.enums.PatternType  
com.aspose.pdf.generator.legacyxmlmodel.enums.ShadingGradientType  
com.aspose.pdf.generator.legacyxmlmodel.enums.TilingType  
Utilisation implémentée des classes d'énumération : **TextEncodingInternal** et **ImageFormatInternal**

## Classes supprimées :

La classe obsolète com.aspose.pdf.generator.legacyxmlmodel.enums.TextAlignmentType a été supprimée.

## Classes déplacées :

Les classes du package **com.aspose.pdf.generator.legacyxmlmodel.enums** sont déplacées vers le package **com.aspose.pdf.generator.legacyxmlmodel**

## Classes internalisées :

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

## Modifications dans les classes :

Dans la classe **PdfExtractor**, une méthode a été ajoutée  
public extractText(java.nio.charset.Charset value)  

Dans la classe **PdfFileEditor**, une méthode a été ajoutée  
public static void validateAnotations(IDocument doc)  

Dans la classe **BorderInfo**, de nouveaux constructeurs ont été ajoutés :  
public BorderInfo(int borderSide)  
public BorderInfo(int borderSide, GraphInfo borderFormat)  
public BorderInfo(int borderSide, float borderWidth)  
public BorderInfo(int borderSide, float borderWidth, Color borderColor)  
public BorderInfo(int borderSide, Color borderColor)  

Dans la classe **Canvas**, une méthode a été ajoutée  
public Object deepClone()  

Dans la classe **Cell**, des méthodes ont été ajoutées :  
public boolean isNoBorder()  
public void setNoBorder(boolean value)  

public Object completeClone()  

Dans la classe **DocumentAttachment**, méthode ajoutée  
public Object completeClone()

Dans la classe **FloatingBox**, méthode ajoutée  
public Object completeClone()

Dans la classe **FormField**, méthode ajoutée  
public Object completeClone()

Dans la classe **Graph**, méthodes ajoutées :  
public float getRotatingAngle()  
public void setRotatingAngle(float value)  
public ClippingPath getClipping()  
public void setClipping(ClippingPath value)  
public Object completeClone()

Dans la classe **Image**, constructeurs et méthodes ajoutés :  
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

Dans la classe **ImageInfo**, champs et méthodes ajoutés :

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

Dans la classe **Paragraph**, des champs et méthodes ont été ajoutés :
public float FixedHeight;

public float FixedWidth;

public /**BookmarkIncludeType**/int getBookmarked()
public void setBookmarked(/**BookmarkIncludeType**/int value)
public void copyTo(Paragraph par)

Dans la classe **RadioButton**, méthode ajoutée
public Object completeClone()

Dans la classe **Row**, méthode ajoutée
public Object completeClone()

Dans la classe **Segment**, méthode ajoutée
public Object completeClone()

Dans la classe **Shape**, méthode ajoutée
public float getOpacity()
public void setOpacity(float value)
public float getStrokeOpacity() 
public void setStrokeOpacity(float value)  

Dans la classe **Shapes**, certaines méthodes ont été internalisées :
void add(Shape shape)
void remove(Shape shapeToRemove)
void copyTo(Shape[] shapeArray, int index)
int indexOf(Shape shape)

Dans la classe **Table**, méthode ajoutée
public /**override**/ Object completeClone()

Dans la classe **Text**, méthode ajoutée
public /**override**/ Object completeClone()

Dans la classe **XslFoLoadOptions**, méthode ajoutée
public String getBasePath() 
public void setBasePath(String value) 

Dans la classe **PdfBookmarkEditor**, méthode ajoutée

public Bookmarks extractBookmarks(boolean upperLevel)


In **XslFoLoadOptions** classe, méthode ajoutée

In **XslFoLoadOptions** classe, méthode ajoutée

In **XslFoLoadOptions** classe, méthode ajoutée

In **XslFoLoadOptions** classe, méthode ajoutée

**Tous les noms de méthodes setter booléennes qui commençaient par is ont été renommés en set**

par exemple :

com.aspose.pdf.facades.ReplaceTextStrategy.isRegularExpressionUsed(boolean value) -> com.aspose.pdf.facades.ReplaceTextStrategy.setRegularExpressionUsed(boolean value)