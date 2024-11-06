---

title: Changements de l'API Publique dans Aspose.PDF pour Java 10.6.0  
type: docs  
weight: 120  
url: fr/java/public-api-changes-in-aspose-pdf-for-java-10-6-0/  
lastmod: "2022-01-27"  

---

{{% alert color="primary" %}}

Cette page répertorie les changements de l'API publique introduits dans [Aspose.PDF pour Java 10.6.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry649204.aspx). Elle inclut non seulement les nouvelles méthodes publiques et celles obsolètes, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.PDF pour Java qui pourrait affecter le code existant. Tout comportement introduit qui pourrait être perçu comme une régression et qui modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

**Changements de l'API Publique 10.6.0**

Classes ajoutées :

- com.aspose.pdf.printer.**PrinterPaperKind**
- com.aspose.pdf.printer.**PrintPaperSourceKind**
- com.aspose.pdf.**AbsorbedCell**
- com.aspose.pdf.**AbsorbedColumn**
- com.aspose.pdf.**AbsorbedRow**
- com.aspose.pdf.**AbsorbedTable**

- com.aspose.pdf.**ITableElement**
- com.aspose.pdf.LoadOptions.**ModesDUsageDeZoneDeMarges**
- com.aspose.pdf.**AbsorbeurDeTable**
- com.aspose.pdf.**CollectionDElémentsDeTable**

Classes supprimées:

- com.aspose.pdf.**InfoDePlacementDeNouveauParagraphe**

Modifications dans la classe com.aspose.pdf.drawind.**Cercle** :

- public float getPosX() -> public double getPosX() 
- public void setPosX(float value) -> public void setPosX(double value)
- public float getPosY() -> public double getPosY()
- public void setPosY(float value) -> public void setPosY(double value)
- public float getRadius() -> public double getRadius()
- public void setRadius(float value) -> public void setRadius(double value)

Modifications dans la classe com.aspose.pdf.drawind.**Courbe** :
Ajouté :

- public float[] getPositionArray()
- public void setPositionArray(float[] value)

Supprimé :

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

Modifications dans la classe com.aspose.pdf.drawind.**Ellipse** :

- public Ellipse(float left, float bottom, float width, float height) -> public Ellipse(double left, double bottom, double width, double height)  

Modifications dans la classe com.aspose.pdf.drawing.**Graph** :  
Ajouté :  

- public GraphInfo getGraphInfo()  

Supprimé :  

- public double getSkewAngleX()  
- public void setSkewAngleX(double value)  
- public double getSkewAngleY()  
- public void setSkewAngleY(double value)  
- public double getRotationAngle()  
- public void setRotationAngle(double value)  

Modifications dans la classe com.aspose.pdf.**GraphInfo** :  
Ajouté :  

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

Modifications dans la classe com.aspose.pdf.drawind.**Rectangle** :

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

Ajouté :

- public Rectangle()  

Modifications dans la classe com.aspose.pdf.**PdfFileEditor** :

- public boolean concatenate(Document[] src, Document dest) -> public boolean concatenate(IDocument[] src, IDocument dest)

Ajouté :

- public boolean getUseDiskBuffer()
- public void setUseDiskBuffer(boolean value)
- public int getConcatenationPacketSize()
- public void setConcatenationPacketSize(int value)

Modifications dans la classe com.aspose.pdf.ReplaceTextStrategy.**Scope** :

- REPLACE_FIRST -> ReplaceFirst
- REPLACE_ALL -> ReplaceAll

Classe com.aspose.pdf.**ImageFormatInternal *renommée en com.aspose.pdf.*ImageType**

Modifications dans la classe com.aspose.pdf.**Document** :

- public void loadXml(String file) -> public void bindXml(String file)

Ajouté :

- public void bindXml(String xmlFile, String xslFile)

Modifications dans la classe com.aspose.pdf.**EpubLoadOptions** :
Champ ajouté :

- public int MarginsAreaUsageMode

Modifications dans la classe com.aspose.pdf.**FontAbsorber** :
Ajouté :

- public void visit(Document pdf, int startPage, int pageCount)

Modifications dans la classe com.aspose.pdf.**Heading** :
Ajouté :

- public int getStartNumber()

- public void setStartNumber(int value)

Changements dans la classe com.aspose.pdf.**HtmlSaveOptions** :  
Champs ajoutés :

- public boolean SaveTransparentTexts  
- public boolean SaveShadowedTextsAsTransparentTexts  

Changements dans la classe com.aspose.pdf.**Image** :  
Ajouté :

- public TextFragment getTitle()  
- public void setTitle(TextFragment value)  

Changements dans la classe com.aspose.pdf.**Matrix** :  
Ajouté :

- public static Matrix scale(double x, double y)  
- public Matrix add(Matrix other)  

Changements dans la classe com.aspose.pdf.**Note** :  
Ajouté :

- public Note()  

Changements dans la classe com.aspose.pdf.**PageCollection** :  
Ajouté :

- public void clear()  

Changements dans la classe com.aspose.pdf.**Paragraphs** :  
Supprimé :

- public void add(BaseParagraph paragraph, NewParagraphPlacementInfo placementInfo)  

Changements dans la classe com.aspose.pdf.**RadioButtonOptionField** :  
Ajouté :

- public /* BoxStyle */int getStyle()  
- public void setStyle(/* BoxStyle */int value)  

Changements dans la classe com.aspose.pdf.**TextFragment** :  
Supprimé :

- public NewParagraphPlacementInfo getPlacementInfo()  

- public void setPlacementInfo(NewParagraphPlacementInfo value)  

Changes in com.aspose.pdf.**UnifiedSaveOptions** class:  
Ajouté un champ :

- public boolean TryMergeAdjacentSameBackgroundImages