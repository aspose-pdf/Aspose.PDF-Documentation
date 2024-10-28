---
title: Changements de l'API Publique dans Aspose.PDF pour Java 9.5.0
type: docs
weight: 70
url: /java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page liste les changements de l'API publique introduits dans [Aspose.PDF pour Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx). Elle inclut non seulement les méthodes publiques nouvelles et obsolètes, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.PDF pour Java qui pourrait affecter le code existant. Tout comportement introduit qui pourrait être vu comme une régression et modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

**La propriété CoordinateType est ajoutée à PdfViewer et PdfConverter**<p>
La propriété CoordinateType permet de définir la zone imprimable sur MediaBox ou CropBox (valeur par défaut)

**La méthode SetFieldImage a été ajoutée à la classe XFA :** 

public void SetFieldImage(string fieldName, Stream image)

Exemple :

Le snippet de code suivant montre comment définir une image pour le champ de formulaire XFA :

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

**ReplaceAdjustment** énumération est ajoutée à la classe **TextReplaceOptions**

Cet enum fournit les valeurs suivantes :

- **None** - Aucune action, la longueur de la ligne peut être modifiée
- **AdjustSpaceWidth** - Essayer d'ajuster les espaces entre les mots pour maintenir la longueur de la ligne

La propriété **ReplaceAdjustmentAction** est ajoutée dans la classe **TextReplaceOptions**

La classe **TextReplaceOptions** a un nouveau constructeur qui permet de définir le paramètre **ReplaceAdjustment** :

TextReplaceOptions(int adjustment, int scope)

La propriété **TextReplaceOptions** est ajoutée dans la classe **TextFragmentAbsorber**

La classe **Ellipse** est implémentée :

Constructeur :

public Ellipse(float left, float bottom, float width, float height)

Propriétés :

- Left - valeur flottante qui indique la position gauche de l'ellipse.

- Bottom - valeur flottante qui indique la position inférieure de l'ellipse.
- Width - valeur flottante qui indique la largeur de l'ellipse.
- Height - valeur flottante qui indique la hauteur de l'ellipse.

Exemple : 
Le snippet de code suivant montre comment ajouter une ellipse :

```java
String outFile = "Ellipse.pdf";
Document doc = new Document();
Page page = doc.getPages().add();
Graph canvas = new Graph(400, 100);
page.getParagraphs().add(canvas);
Ellipse ellipse1 = new Ellipse(50, 10, 100, 50);
canvas.getShapes().add(ellipse1);
doc.save(outFile);
```

La classe **Path** a été implémentée

Constructeurs :

public Path()
public Path(Shape[] shapes)

Propriété :

- Shapes - collection de formes

Exemple : 
Le snippet de code suivant montre comment ajouter un chemin :

```java
Document doc = new Document();
Page page = doc.getPages().add();
Graph graph = new Graph(100, 400);
page.getParagraphs().add(graph);

Path path = new Path();
path.getGraphInfo().setFillColor ( Color.getRed());
graph.getShapes().add(path);

Line line = new Line(new float[] { 200, 80, 200, 100 });
path.getShapes().add(line);
Arc arc = new Arc(200, 50, 50, 90, 270);
path.getShapes().add(arc);
float[] curPos = arc.getEndPosition();
line = new Line(new float[] { curPos[0], curPos[1], 200, 20 });
path.getShapes().add(line);
arc = new Arc(200, 50, 30, 270, 90);
path.getShapes().add(arc);
doc.Save(outFile);
```


**Classe HtmlFragment** a été ajoutée dans le package com.aspose.pdf*

Constructeur :

- public HtmlFragment(string text)

Paramètre :

- Text - texte HTML
  Propriété :
- Text - texte HTML

Exemple :
Le code suivant montre comment ajouter un fragment HTML :

```java
Document doc = new Document();
Page page = doc.getPages().add();
HtmlFragment titre = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
titre.setKeptWithNext (true);
titre.getMargin().setBottom (10);
titre.getMargin().setTop (200);
page.getParagraphs().add(titre);
doc.Save(outFile);
```

**Méthode ContainsUsageRights()** a été ajoutée dans la classe **PdfFileSignature**

**Méthode RemoveUsageRights()** a été ajoutée dans la classe **PdfFileSignature**

Exemple :

Le code suivant montre comment supprimer la fonctionnalité de droits d'usage du document :

```java
PdfFileSignature pdfSign = new PdfFileSignature();

try

{
    String inputFile = "c:\\36908.pdf";

    String outputFile = "c:\\36908_output.pdf";

    pdfSign.bindPdf(inputFile);

    if (pdfSign.containsUsageRights())

    {
        pdfSign.removeUsageRights();
    }

    pdfSign.getDocument().save(outputFile);
}

finally

{
    pdfSign.dispose();
}
```


**isContainSignature()** méthode a été renommée en **ContainsSignature(...)**

- Le nom de la méthode précédente n'a pas été supprimé mais marqué comme obsolète pour être supprimé à l'avenir.
    **isCoversWholeDocument()** méthode a été renommée en **CoversWholeDocument(...)**
- Le nom de la méthode précédente n'a pas été supprimé mais marqué comme obsolète pour être supprimé à l'avenir.

La classe **Measure** a été ajoutée au package **com.aspose.pdf**

La classe décrit le système de coordonnées Measure. Membres de la classe Measure :

Constructeur :

- public Measure(Annotation annotation)

Propriétés get/set :

- ScaleRatio - Une chaîne de texte exprimant le rapport d'échelle du dessin.
- XFormat - Un tableau de format numérique pour la mesure du changement le long de l'axe x et, si Y n'est pas présent, également le long de l'axe y.
- YFormat - Un tableau de format numérique pour la mesure du changement le long de l'axe y.
- DistanceFormat - Un tableau de format numérique pour la mesure de la distance dans n'importe quelle direction.
- AreaFormat - Un tableau de format numérique pour la mesure de la superficie.

- AngleFormat - Un tableau de format numérique pour la mesure des angles.
- SlopeFormat - Un tableau de format numérique pour la mesure de la pente d'une ligne.
- Origin - Point qui doit spécifier l'origine du système de coordonnées de mesure dans les coordonnées de l'espace utilisateur par défaut.
- XYFactor - Un facteur qui doit être utilisé pour convertir les plus grandes unités le long de l'axe y en les plus grandes unités le long de l'axe x.

La classe **NumberFormat** a été ajoutée à la classe **Measure**

La classe représente le format numérique pour la mesure.

Constructeur :

- public NumberFormat(Measure measure)

Propriétés get/set :

- UnitLabel - Une chaîne de texte spécifiant une étiquette pour afficher les unités.
- ConvresionFactor - Le facteur de conversion utilisé pour multiplier une valeur en unités partielles de l'élément précédent du tableau de format numérique pour obtenir une valeur dans les unités de ce format numérique.
- FractionDisplayment - La manière dont les valeurs fractionnaires sont affichées.
- Precision - Si FractionDisplayment est ShowAsDecimal, cette valeur est la précision de la valeur fractionnaire ; Elle doit être un multiple de 10. La valeur par défaut est 100.
- Denominator - Si FractionDisplayment est ShowAsFraction, cette valeur est le dénominateur de la fraction.
 Valeur par défaut est 16.  
- ForceDenominator - Si FractionDisplayment est ShowAsFraction, cette valeur détermine si la fraction peut ou non être réduite. Si la valeur est vraie, la fraction ne peut pas être réduite.  
- ThousandsSeparator - Texte qui doit être utilisé entre les ordres de milliers dans l'affichage des valeurs numériques. Une chaîne vide indique qu'aucun texte ne doit être ajouté. Par défaut, c'est une virgule.  
- FractionSeparator - Texte qui doit être utilisé comme position décimale dans l'affichage des valeurs numériques. Une chaîne vide indique que la valeur par défaut doit être utilisée. Par défaut, c'est le caractère de point.  
- BeforeText - Texte qui doit être concaténé à gauche de l'étiquette.  
- AfterText - Texte qui doit être concaténé après l'étiquette  

L'énumération **FractionStyle** a été ajoutée à la classe **NumberFormat**  

Valeurs de FractionStyle :

- ShowAsDecimal - Afficher les valeurs fractionnaires comme fraction décimale.  
- ShowAsFraction - Afficher la valeur fractionnaire comme une fraction.  
- Round - Arrondir les valeurs fractionnaires à l'entier le plus proche.  
- Truncate - Tronquer pour obtenir des unités entières.  

La classe **NumberFormatList** a été ajoutée à la classe **Measure**  
La classe représente une liste de formats de nombres.

Constructeur :

- public NumberFormatList(Measure measure)

Propriétés :

- get_Item(int) et set_Item(int index, NumberFormat value) - Obtient ou définit le format de nombre dans la liste par son index.
- getCount() - Compte le nombre d'éléments dans la liste.

Méthodes :

- public void add(NumberFormat value)
- Ajoute un format de nombre à la liste.
- public void insert(int index, NumberFormat value)
- Insère un format de nombre dans la liste.
- public void removeAt(int index)
- Supprime un format de nombre de la liste.

La propriété **Measure** a été ajoutée aux classes **LineAnnotation** et **PolyLineAnnotation**.

Exemples :

L'exemple suivant montre comment utiliser Measure avec LineAnnotation :

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//définir les paramètres de la ligne d'extension.
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//définir les terminaisons de ligne
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//créer un élément Measure
line.setMeasure(new Measure(line));<p>
line.getMeasure().setDistanceFormat(newMeasure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//texte de la ligne de mesure
line.setContents("155 mm");
//cela doit être réglé pour afficher le texte.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


L'exemple suivant démontre comment utiliser Measure avec PolylineAnnotation :

```java
 Document doc = new Document("source.pdf");

Point[] vertices = new Point[]

{


new Point(100, 600),

new Point(500, 600),

new Point(500, 500),

new Point(400, 300),

new Point(100, 500),

new Point(100, 600)

};

Rectangle rect = new Rectangle(100, 500, 500, 600);
//ligne de périmètre ou zone
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
//les extrémités de ligne peuvent être définies pour la ligne de périmètre.
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

Le snippet de code suivant démontre comment lire les propriétés Measure :

```java
//lire les propriétés de mesure

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**Changement majeur** - La propriété PdfPageEditor.Pages a été renommée en **ProcessPages**

Le snippet de code suivant montre l'utilisation de la propriété (définit le coefficient de zoom pour la page #1 du document) :

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**Changement majeur** - La propriété RichTextBoxField.RValue a été renommée en **RichTextValue**

Le fragment de code suivant montre un exemple où le champ renommé a été utilisé :

```java
Document doc = new Document("input.pdf");

RichTextBoxField rt = new RichTextBoxField(doc.getPages().get_Item(1), new Rectangle(50, 600, 250, 650));
rt.setPartialName("rt");
doc.getForm().add(rt);
doc.save("34834.pdf");
Document doc1 = new Document("34834.pdf");
((RichTextBoxField)doc1.getForm().get("rt")).setRichTextValue("<p>Ceci est mon <b>paragraphe</b></p>");

doc1.save("output.pdf");
```

L'option **InsertBlankColumnAtFirst** a été ajoutée à la classe **ExcelSaveOptions**

Le fragment de code suivant montre comment supprimer l'apparition de la première colonne vide :

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

La propriété **PageInfo** a été ajoutée à la classe **SvgLoadOptions**.

Le fragment de code suivant montre comment utiliser SvgLoadOptions et définir les informations de marge avec la propriété PageInfo :

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
options.getPageInfo().getMargin().setTop(0);
options.getPageInfo().getMargin().setLeft(0);
options.getPageInfo().getMargin().setBottom(0);
options.getPageInfo().getMargin().setRight(0);
String inFile = "35730.svg";
String outFile = "35730.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```

L'énumération **ConversionEngines** a été ajoutée à la classe **SvgLoadOptions**.

Les valeurs suivantes sont définies :

- **LegacyEngine** - moteur hérité du traitement Svg
- **NewEngine** - nouveau moteur de traitement Svg

La propriété **ConversionEngine** a été ajoutée à la classe **SvgLoadOptions**

Le LegacyEngine est toujours la valeur par défaut car NewEngine est en phase de B-test. Le code suivant montre un exemple d'utilisation du nouveau moteur :

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**Propriété ColumnAdjustment** a été ajoutée à la classe **Table**

L'énumération ColumnAdjustment a été ajoutée au package com.aspose.pdf

les valeurs suivantes ont été ajoutées :

- **Customized** - L'utilisateur définit la largeur de la colonne manuellement.
- **AutoFitToContent** - Effectue un ajustement automatique au contenu

**Propriété ColumnAdjustment** a été ajoutée à la classe **Table**

La valeur par défaut est Customized.

L'extrait de code suivant montre un exemple d'utilisation de la propriété ColumnAdjustment :

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**Propriété MinimizeTheNumberOfWorksheets** a été introduite dans l'objet **ExcelSaveOptions**.

L'extrait de code suivant montre comment minimiser le nombre possible de feuilles de calcul :

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//Définissez cette propriété sur true
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**Valeur** par défaut a été ajoutée à l'énumération **PageLayout**.

L'extrait de code suivant définit PageLayout à la valeur par défaut :

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout(PageLayout.Default);
doc1.save("output.pdf");
```

Le support des **Extrémités Arrondies** a été implémenté pour **InkAnnotation**

L'énumération **CapStyle** a été ajoutée au package **com.aspose.pdf**
Les valeurs suivantes sont présentes

- **Rectangular** - Valeur par défaut spécifiée
- **Rounded** - coins arrondis
- La propriété **CapStyle** a été ajoutée à la classe **InkAnnotation**

L'extrait de code suivant montre comment définir les coins de l'InkAnnotation comme arrondis :

```java
Document doc = new Document("PdfWithText.pdf");
Page pdfPage = doc.getPages().get_Item(1);
java.awt.Rectangle drect = new java.awt.Rectangle();
drect.height = (int)pdfPage.getRect().getHeight();
drect.width = (int)pdfPage.getRect().getWidth();
drect.x = 0;
drect.y = 0;
com.aspose.pdf.Rectangle arect = com.aspose.pdf.Rectangle.fromRect(drect);
java.util.ArrayList inkList = new java.util.ArrayList();
com.aspose.pdf.Point[] arrpt = new com.aspose.pdf.Point[3];
inkList.add(arrpt);
arrpt[0] = new Point(100, 800);
arrpt[1] = new Point(200, 800);
arrpt[2] = new Point(200, 700);
InkAnnotation ia = new InkAnnotation(pdfPage, arect, inkList);
ia.setTitle("XXX");
ia.setColor(Color.getLightBlue());
ia.setCapStyle(CapStyle.Rounded);
Border border = new Border(ia);
border.setWidth(25);
ia.setOpacity(0.5);
pdfPage.getAnnotations().add(ia);
doc.save("37071.pdf");
```


**PDFNEWJAVA-33498** - Fournir un support pour ajouter une image à partir de BufferedImage dans un document PDF

Le code suivant montre comment ajouter une image à partir de BufferedImage :

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - Conversion PDF en HTML : spécifier le dossier d'images

Le code suivant montre comment spécifier le dossier d'images :

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - Réglage du DPI/PPI des images dans le PDF

Le code suivant montre comment changer la résolution de l'image dans le fichier pdf :

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
//test de création de pdf
Document doc = new Document();
Page page = doc.getPages().add();
com.aspose.pdf.Image image1 = new com.aspose.pdf.Image();
image1.setImageStream(in);
image1.setFixHeight(page.getMediaBox().getHeight()/4);
image1.setFixWidth(page.getMediaBox().getWidth()/2);
NewParagraphPlacementInfo placementInfo = new NewParagraphPlacementInfo();
placementInfo.setStartNewPage(true);
page.getParagraphs().add(image1, placementInfo);
page.getPageInfo().getMargin().setLeft(5);
page.getPageInfo().getMargin().setRight(0);
page.getPageInfo().getMargin().setTop(0);
page.getPageInfo().getMargin().setBottom(0);
doc.save(out);
```


```java
//changement de résolution d'image interne
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//définir les résolutions horizontale et verticale
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**Résumé :**

**Classes ajoutées :**

- com.aspose.pdf.drawing.Ellipse
- com.aspose.pdf.drawing.Path
com.aspose.pdf.generator.legacyxmlmodel.BookmarkIncludeType
- com.aspose.pdf.generator.legacyxmlmodel.BorderSide
- com.aspose.pdf.generator.legacyxmlmodel.ColumnInfo
- com.aspose.pdf.generator.legacyxmlmodel.HeaderFooterType
- com.aspose.pdf.generator.legacyxmlmodel.HtmlInfo
- com.aspose.pdf.generator.legacyxmlmodel.ImportOptions
- com.aspose.pdf.generator.legacyxmlmodel.MediaType
- com.aspose.pdf.generator.legacyxmlmodel.PathArea
- com.aspose.pdf.generator.legacyxmlmodel.TableFormatInfo

- com.aspose.pdf.AutoDetectedFormatLoadOptions

- com.aspose.pdf.CapStyle
- com.aspose.pdf.ColumnAdjustment
- com.aspose.pdf.ComHelper
- com.aspose.pdf.EpubLoadOptions
- com.aspose.pdf.EpubSaveOptions
- com.aspose.pdf.FileFontSource
- com.aspose.pdf.FontAbsorber
- com.aspose.pdf.HtmlFragment
- com.aspose.pdf.Measure
- com.aspose.pdf.MemoryFontSource

## Changements dans les classes :

**com.aspose.pdf.facades.Form**

Changements :

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**
Ajouté :

- public int getCoordinateType()
- public void setCoordinateType(int value)
  Obsolète :
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**
Changements :

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value

**com.aspose.pdf.facades.PdfFileSignature**
Deprécié :

- public boolean isContainSignature()
- public boolean isCoversWholeDocument(String signName)
  Ajouté :
- public boolean containsSignature()
- public boolean containsUsageRights()
- public void removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor**
Modifications :

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages()
- public void setPages(int[] value) -> public void setProcessPages(int[] value)
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations()
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer**
Déprécié :

- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)
  Ajouté :
- public int getCoordinateType()
- public void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata**
Modifications :

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment**  
Ajouté :

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo**  
Ajouté :

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- Statut obsolète retiré de la classe

**com.aspose.pdf.generator.legacyxmlmodel.Cell**  
Ajouté :

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter**  
Ajouté :

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading**  
Statut obsolète retiré de :

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image**  
Ajouté :

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts**  
Ajouté :

- public void remove(Cell jsToRemove)


**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
Ajouté :

- public boolean DigitSubstitution
- public boolean IsAutoFontAdjusted
- public boolean IsBuffered
- public InputStream TruetypeFontMapStream
- public boolean IsImageNotFoundErrorIgnored
- public boolean Linearized;
- public int getPageCount()
- public void save(OutputStream output)
- public byte[] getBuffer()
- public void save(String pdfFile)
- public void bindXML(String xmlFile, String xslFileIfAny)
- public void bindXML(InputStream xmlStream, InputStream xslStream)
- public void setUnicode()
- public Object getObjectByID(String ID)
- public HtmlInfo HtmlInfo

Ajouté Obsolète :

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**  
Ajouté :

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**  
Ajouté :

- public void add(Paragraph paragraph)
- void ajouterEn-tête(Paragraph paragraph)
- public int indexDe(Paragraph paragraph)
- public void copierVers(Paragraph[] paraArray, int index)
- public void insérer(Paragraph paragraphToInsertAfter, Paragraph newParagraph)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
Changé :

- DefaultCellTextInfo en champ getter et setter  
  Ajouté :
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public Object deepClone()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
Ajouté :

- public ColumnInfo ColumnInfo
- public int getPageCount()
- public void setPageCount(int value)
- public String BreakParaText
- public Object deepClone()
- public Object completeClone()
- public HeaderFooter insertHeader(int type)
- public HeaderFooter insertFooter(int type)
- public Object getObjectByID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
Ajouté :

- public Sections()
- public Section ajouter()
- public void insérer(int index, Section section)

- public void insérer(Section sectionToInsertAfter, Section newSection)
- public void remove(Section sectionToRemove) // public void supprimer(Section sectionASupprimer)
- public void copyTo(Section[] secArray, int index) // public void copierVers(Section[] secArray, int index)
- public int indexOf(Section section) // public int indiceDe(Section section)
- public void set_Item(int index, Section value) // public void définir_Élément(int index, Section valeur)
- public Section get_Item(String sectionID) // public Section obtenir_Élément(String sectionID)
- public void set_Item(String sectionID, Section value) // public void définir_Élément(String sectionID, Section valeur)

**com.aspose.pdf.generator.legacyxmlmodel.Security**
Ajouté :

- public boolean isDefaultAllAllowed() // public boolean estDéfautToutAutorisé()
- public void setDefaultAllAllowed(boolean value) // public void définirDéfautToutAutorisé(boolean valeur)

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**
Ajouté :

- public void add(Shape shape) // public void ajouter(Shape forme)
- public void remove(Shape shapeToRemove) // public void supprimer(Shape formeASupprimer)
- public void copyTo(Shape[] shapeArray, int index) // public void copierVers(Shape[] tableauFormes, int index)
- public int indexOf(Shape shape) // public int indiceDe(Shape forme)

**com.aspose.pdf.generator.legacyxmlmodel.Table**
Changé :

- FixedWidth en champ getter et setter // LargeurFixe en champ getter et setter
- DefaultCellTextInfo en champ getter et setter // InfoTexteCelluleDéfaut en champ getter et setter
  Ajouté :
- public float getFixedWidth() // public float obtenirLargeurFixe()
- public void setFixedWidth(float value) // public void définirLargeurFixe(float valeur)
- public TextInfo getDefaultCellTextInfo() // public TextInfo obtenirInfoTexteCelluleDéfaut()
- public void setDefaultCellTextInfo(TextInfo value) // public void définirInfoTexteCelluleDéfaut(TextInfo valeur)

- public Cell getCell(int row, int column, boolean isTableChanged) // public Cell obtenirCellule(int ligne, int colonne, boolean estTableModifiée)
- public void formatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)
- public void formatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)
- public void formatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)
- public void setColumnWidth(int columnNumber, float width)
- public String getColumnWidths()
- public void setColumnWidths(String value)

**com.aspose.pdf.generator.legacyxmlmodel.TabStops**  
Ajouté :

- public int getCapacity()
- public void setCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
Modifié :

- La liste suivante des champs a été modifiée pour inclure un champ getter et setter séparé :

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic, {color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline, {color}
 {color:#222222}IsOverline, {color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


Ajouté :

- public float getFontSize()  
- public void setFontSize(float value)  
- public String getFontName()  
- public void setFontName(String value)  
- public String getTruetypeFontFileName()  
- public void setTruetypeFontFileName(String value)  
- public boolean isUnicode()  
- public void setUnicode(boolean value)  
- public String getFontAfmFile()  
- public void setFontAfmFile(String value)  
- public String getFontPfmFile()  
- public void setFontPfmFile(String value)  
- public String getFontOutlineFile()  
- public void setFontOutlineFile(String value)  
- public String getFontEncodingFile()  
- public void setFontEncodingFile(String value)  
- public boolean isTrueTypeFontBold()  
- public void setTrueTypeFontBold(boolean value)  
- public boolean isTrueTypeFontItalic()  
- public void setTrueTypeFontItalic(boolean value)  
- public String getFontEncoding()  
- public void setFontEncoding(String value)  
- public boolean isFontEmbedded()  
- public void setFontEmbedded(boolean value)  
- public boolean isUnderline()  

- public void setUnderline(boolean value)
- public boolean isOverline()  
- public void setOverline(boolean value)  
- public float getCharSpace()  
- public void setCharSpace(float value)  
- public float getWordSpace()  
- public void setWordSpace(float value)  
- public float getLineSpacing()  
- public void setLineSpacing(float value)  
- public float getOverlineOffset()  
- public void setOverlineOffset(float value)  
- public float getUnderlineOffset()  
- public void setUnderlineOffset(float value)  
- public int getRenderingMode()  
- public void setRenderingMode(int value)  
- public Color getColor()  
- public void setColor(Color value)  
- public Color getBackgroundColor()  
- public void setBackgroundColor(Color value)  
- public boolean isRightToLeft()  
- public void setRightToLeft(boolean value)  
- public float getStrokeWidth()  
- public void setStrokeWidth(float value)  
- public Color getStrokeColor()  
- public void setStrokeColor(Color value)  
- public boolean isBaseline()  
- public void setBaseline(boolean value)  
- public int getAlignment()  

- public void setAlignment(int value)  

**com.aspose.pdf.BaseOperatorCollection**  
Modifications :

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border**  
Modifications :

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value)  
  Ajouté Obsolète :
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils**  
Modifications :

- Internalisé

**com.aspose.pdf.ExcelSaveOptions**  
Ajouté :

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font**  
Ajouté :

- public void save(OutputStream stream)

**com.aspose.pdf.Form**  
Ajouté :

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:**  
Ajouté :


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
Ajouté :

- public int getCapStyle()
- public void setCapStyle(int value)

**com.aspose.pdf.LineAnnotation**  
Ajouté :

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.LoadFormat :**  
Changements :

- public static final int InfoPath - a été supprimé
- public static final int AutoDetect - Ajouté

**com.aspose.pdf.Metadata**  
Changements :

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields() 

**com.aspose.pdf.PageLayout**  
Ajouté :

- public static final int Default

**com.aspose.pdf.PolylineAnnotation**  
Ajouté :

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.PopupAnnotation**  
Ajouté :

- public MarkupAnnotation getParent()
- public void setParent(MarkupAnnotation value)

**com.aspose.pdf.RichTextBoxField**  
Changements :

- public String getRValue() -> public String getRichTextValue()

- public void setRValue(String value) -> public void setRichTextValue(String value)

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
Ajouté :

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
Ajouté :

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
Ajouté :

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
Ajouté :

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
Ajouté :

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
Ajouté :

- public void setFieldImage(String fieldName, InputStream image)