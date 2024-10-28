---
title: Cambios en la API Pública en Aspose.PDF para Java 9.5.0
type: docs
weight: 70
url: /java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página enumera los cambios en la API pública introducidos en [Aspose.PDF para Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx). Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pueda considerarse una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}}

**Se agregó la propiedad CoordinateType a PdfViewer y PdfConverter**<p>
La propiedad CoordinateType permite establecer el área imprimible a MediaBox o CropBox (valor predeterminado)

**Se agregó el método SetFieldImage a la clase XFA:** 

public void SetFieldImage(string fieldName, Stream image)

Ejemplo:

El siguiente fragmento de código muestra cómo establecer una imagen para el campo de formulario XFA:

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

La enumeración **ReplaceAdjustment** se agrega a la clase **TextReplaceOptions**

Este enum proporciona los siguientes valores:

- **None** - Sin acción, la longitud de la línea puede cambiar
- **AdjustSpaceWidth** - Intenta ajustar los espacios entre palabras para mantener la longitud de la línea

Se agrega la propiedad **ReplaceAdjustmentAction** en la clase **TextReplaceOptions**

La clase **TextReplaceOptions** tiene un nuevo constructor que permite establecer el parámetro **ReplaceAdjustment**:

TextReplaceOptions(int adjustment, int scope)

Se agrega la propiedad **TextReplaceOptions** en la clase **TextFragmentAbsorber**

Se implementa la clase **Ellipse**:

Constructor:

public Ellipse(float left, float bottom, float width, float height)

Propiedades:

- Left - valor flotante que indica la posición izquierda de la elipse.

- Bottom - valor flotante que indica la posición inferior de la elipse.

- Width - valor de punto flotante que indica el ancho de la elipse.
- Height - valor de punto flotante que indica la altura de la elipse.

Ejemplo: El siguiente fragmento de código muestra cómo agregar una Elipse:

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

La clase **Path** fue implementada

Constructores:

public Path()
public Path(Shape[] shapes)

Propiedad:

- Shapes - colección de formas

Ejemplo: el siguiente fragmento de código muestra cómo agregar un Path:

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


**HtmlFragment** class fue añadida al paquete com.aspose.pdf*

Constructor:

- public HtmlFragment(string text)

Parámetro:

- Text - texto HTML
  Propiedad:
- Text - texto HTML

Ejemplo:
El siguiente fragmento de código muestra cómo agregar un fragmento HTML:

```java
Document doc = new Document();
Page page = doc.getPages().add();
HtmlFragment titulo = new HtmlFragment("<fontsize=10><b><i>Tabla</i></b></fontsize>");
titulo.setKeptWithNext (true);
titulo.getMargin().setBottom (10);
titulo.getMargin().setTop (200);
page.getParagraphs().add(titulo);
doc.Save(outFile);
```

Se añadió el método **ContainsUsageRights()** a la clase **PdfFileSignature**

Se añadió el método **RemoveUsageRights()** a la clase **PdfFileSignature**

Ejemplo:

El siguiente código muestra cómo eliminar la característica de derechos de uso del documento:

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


**isContainSignature()** método fue renombrado a **ContainsSignature(...)**

- El nombre del método anterior no fue eliminado pero se marcó como obsoleto para ser eliminado en el futuro.
    **isCoversWholeDocument()** método fue renombrado a **CoversWholeDocument(...)**
- El nombre del método anterior no fue eliminado pero se marcó como obsoleto para ser eliminado en el futuro.

La clase **Measure** fue añadida al paquete **com.aspose.pdf**

La clase describe el sistema de coordenadas Measure. Miembros de la clase Measure:

Constructor:

- public Measure(Annotation annotation)

Propiedades get/set:

- ScaleRatio - Una cadena de texto que expresa la relación de escala del dibujo.
- XFormat - Un arreglo de formato numérico para la medición del cambio a lo largo del eje x y, si Y no está presente, a lo largo del eje y también.
- YFormat - Un arreglo de formato numérico para la medición del cambio a lo largo del eje y.
- DistanceFormat - Un arreglo de formato numérico para la medición de la distancia en cualquier dirección.
- AreaFormat - Un arreglo de formato numérico para la medición de área.

- AngleFormat - Un arreglo de formato numérico para la medición de ángulos.
- SlopeFormat - Una matriz de formato numérico para medir la pendiente de una línea.
- Origin - Punto que especificará el origen del sistema de coordenadas de medición en coordenadas de espacio de usuario predeterminadas.
- XYFactor - Un factor que se usará para convertir las unidades más grandes a lo largo del eje y a las unidades más grandes a lo largo del eje x.

**NumberFormat** clase fue añadida a la clase **Measure**

La clase representa el formato numérico para la medida.

Constructor:

- public NumberFormat(Measure measure)

get/set Propiedades:

- UnitLabel - Una cadena de texto que especifica una etiqueta para mostrar las unidades.
- ConvresionFactor - El factor de conversión utilizado para multiplicar un valor en unidades parciales del elemento anterior de la matriz de formato numérico para obtener un valor en las unidades de este formato numérico.
- FractionDisplayment - De qué manera se muestran los valores fraccionarios.
- Precision - Si FractionDisplayment es ShowAsDecimal, este valor es la precisión del valor fraccional; debe ser múltiplo de 10. El valor predeterminado es 100.
- Denominator - Si FractionDisplayment es ShowAsFraction, este valor es el denominador de la fracción.
 El valor predeterminado es 16.
- ForceDenominator - Si FractionDisplayment es ShowAsFraction, este valor determina si la fracción puede o no ser reducida. Si el valor es verdadero, la fracción puede no ser reducida.
- ThousandsSeparator - Texto que se utilizará entre órdenes de miles en la visualización de valores numéricos. Una cadena vacía indica que no se añadirá texto. El valor predeterminado es una coma.
- FractionSeparator - Texto que se utilizará como la posición decimal al mostrar valores numéricos. Una cadena vacía indica que se usará el valor predeterminado. El valor predeterminado es el carácter de punto.
- BeforeText - Texto que se concatenará a la izquierda de la etiqueta.
- AfterText - Texto que se concatenará después de la etiqueta.

Se agregó la enumeración **FractionStyle** en la clase **NumberFormat**

Valores de FractionStyle:

- ShowAsDecimal - Mostrar valores fraccionarios como fracción decimal.
- ShowAsFraction - Mostrar valor fraccionario como fracción.
- Round - Redondear valores fraccionarios al entero más cercano.
- Truncate - Truncar para lograr unidades completas.

La clase **NumberFormatList** fue agregada a la clase **Measure**
La clase representa representa la lista de formatos de números.

Constructor:

- public NumberFormatList(Measure measure)

Propiedades:

- get_Item(int) y set_Item(int index, NumberFormat value) - Obtiene o establece el formato de número en la lista por su índice.
- getCount()- Cuenta si los elementos en la lista.

Métodos:

- public void add(NumberFormat value)
- Añade el formato de número a la lista.
- public void insert(int index, NumberFormat value)
- Inserta el formato de número en la lista.
- public void removeAt(int index)
- Elimina el formato de número de la lista.

La propiedad **Measure** fue añadida a las clases **LineAnnotation** y **PolyLineAnnotation**.

Ejemplos:

El siguiente ejemplo demuestra cómo usar Measure con LineAnnotation:

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//establecer los parámetros de la línea de extensión.
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//establecer los finales de las líneas
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//crear elemento Measure
line.setMeasure(new Measure(line));<p>
line.getMeasure().setDistanceFormat(newMeasure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//texto de la línea de medida
line.setContents("155 mm");
//esto debe establecerse para mostrar el texto.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


El siguiente ejemplo demuestra cómo usar Measure con PolylineAnnotation:

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
//área o línea de perímetro
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
//los extremos de línea pueden configurarse para la línea de perímetro.
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

El siguiente fragmento de código demuestra cómo leer las propiedades de Measure:

```java
//leer propiedades de Medida

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**Cambio radical** - La propiedad PdfPageEditor.Pages fue renombrada a **ProcessPages**

El siguiente fragmento de código muestra el uso de la propiedad (establece el coeficiente de zoom para la página #1 del documento):

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**Cambio importante** - La propiedad RichTextBoxField.RValue fue renombrada a **RichTextValue**

El siguiente fragmento de código muestra un ejemplo donde se utilizaba el campo renombrado:

```java
Document doc = new Document("input.pdf");

RichTextBoxField rt = new RichTextBoxField(doc.getPages().get_Item(1), new Rectangle(50, 600, 250, 650));
rt.setPartialName("rt");
doc.getForm().add(rt);
doc.save("34834.pdf");
Document doc1 = new Document("34834.pdf");
((RichTextBoxField)doc1.getForm().get("rt")).setRichTextValue("<p>This is my <b>paragraph</b></p>");

doc1.save("output.pdf");
```

Se añadió la opción **InsertBlankColumnAtFirst** en la clase **ExcelSaveOptions**

El siguiente fragmento de código muestra cómo suprimir la aparición de la primera columna en blanco:

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

Se añadió la propiedad **PageInfo** a la clase **SvgLoadOptions**.

El siguiente fragmento de código muestra cómo usar SvgLoadOptions y establecer la información de margen con la propiedad PageInfo:

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

Se añadió la enumeración **ConversionEngines** a la clase **SvgLoadOptions**.

Se definen los siguientes valores:

- **LegacyEngine** - motor heredado de procesamiento de Svg
- **NewEngine** - nuevo motor de procesamiento de Svg

Se añadió la propiedad **ConversionEngine** a la clase **SvgLoadOptions**

El LegacyEngine sigue siendo el valor predeterminado porque el NewEngine está en etapas de pruebas B.
El siguiente fragmento de código muestra un ejemplo de cómo utilizar el nuevo motor:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**Propiedad ColumnAdjustment** fue añadida a la clase **Table**

La enumeración ColumnAdjustment fue añadida al paquete com.aspose.pdf

Se añadieron los siguientes valores:

- **Customized** - El usuario establece manualmente el ColumnWidth.
- **AutoFitToContent** - Realiza un ajuste automático al contenido

**Propiedad ColumnAdjustment** fue añadida a la clase **Table**

El valor predeterminado es Customized.

El siguiente fragmento de código muestra un ejemplo del uso de la propiedad ColumnAdjustment:

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**Propiedad MinimizeTheNumberOfWorksheets** fue introducida en el objeto **ExcelSaveOptions**.

El siguiente fragmento de código muestra cómo minimizar el posible número de hojas de cálculo:

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//Establezca esta propiedad en true
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**Valor predeterminado** se agregó a la enumeración **PageLayout**.

El siguiente fragmento de código establece PageLayout al valor predeterminado:

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout (PageLayout.Default);
doc1.save("output.pdf");
```

Se implementó soporte de **Extremos Redondeados** para **InkAnnotation**

La enumeración **CapStyle** se agregó al paquete **com.aspose.pdf**
Los siguientes valores están presentes

- **Rectangular** - Valor predeterminado especificado
- **Redondeado** - esquinas redondeadas
- Se agregó la propiedad **CapStyle** a la clase **InkAnnotation**

El siguiente fragmento de código muestra cómo establecer las esquinas de InkAnnotation como redondeadas:

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


**PDFNEWJAVA-33498** - Proporcionar soporte para agregar Imagen desde BufferedImage en el documento PDF

El siguiente fragmento de código muestra cómo agregar una Imagen desde BufferedImage:

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - Conversión de PDF a HTML: Especificar la carpeta de imágenes

El siguiente fragmento de código muestra cómo especificar la carpeta de imágenes:

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - Configuración de DPI/PPI de imágenes en PDF

El siguiente fragmento de código muestra cómo cambiar la resolución de imagen en el archivo pdf:

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
//prueba de creación de pdf
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
// cambio de resolución de imagen interna
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//definir resoluciones horizontal y vertical
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**Resumen:**

**Clases añadidas:**

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

## Cambios en las clases:

**com.aspose.pdf.facades.Form**

Cambios:

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**
Añadido:

- public int getCoordinateType()
- public void setCoordinateType(int value)
  Obsoleto:
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**
Cambios:

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value

**com.aspose.pdf.facades.PdfFileSignature**
Depricado:

- public boolean isContainSignature()
- public boolean isCoversWholeDocument(String signName)
  Agregado:
- public boolean containsSignature()
- public boolean containsUsageRights()
- public void removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor**
Cambios:

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages()
- public void setPages(int[] value) -> public void setProcessPages(int[] value)
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations()
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer**
Depricado:

- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)
  Agregado:
- public int getCoordinateType()
- public void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata**
Cambios:

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment** Añadido:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo** Añadido:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- Eliminado el estado Obsoleto de la clase

**com.aspose.pdf.generator.legacyxmlmodel.Cell** Añadido:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter** Añadido:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading** Estado Obsoleto eliminado de:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image** Añadido:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts** Añadido:

- public void remove(Cell jsToRemove)


**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
Agregado:

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

Agregado Obsoleto:

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**  
Agregado:

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**  
Agregado:

- public void add(Paragraph paragraph)
- void añadirEncabezado(Párrafo párrafo)
- public int índiceDe(Párrafo párrafo)
- public void copiarA(Párrafo[] arrayPara, int índice)
- public void insertar(Párrafo párrafoParaInsertarDespués, Párrafo nuevoPárrafo)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
Cambiado:

- DefaultCellTextInfo en campo getter y setter  
  Añadido:
- public TextInfo obtenerDefaultCellTextInfo()
- public void establecerDefaultCellTextInfo(TextInfo valor)
- public Object clonarProfundamente()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
Añadido:

- public ColumnInfo ColumnInfo
- public int obtenerContadorDePáginas()
- public void establecerContadorDePáginas(int valor)
- public String TextoDeRupturaPara
- public Object clonarProfundamente()
- public Object clonarCompletamente()
- public HeaderFooter insertarEncabezado(int tipo)
- public HeaderFooter insertarPieDePágina(int tipo)
- public Object obtenerObjetoPorID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
Añadido:

- public Sections()
- public Section añadir()
- public void insertar(int índice, Section sección)

- public void insertar(Sección secciónParaInsertarDespués, Sección nuevaSección)
- public void remove(Section secciónParaEliminar)
- public void copyTo(Section[] arraySecciones, int índice)
- public int indexOf(Section sección)
- public void set_Item(int índice, Section valor)
- public Section get_Item(String idSección)
- public void set_Item(String idSección, Section valor)

**com.aspose.pdf.generator.legacyxmlmodel.Security**  
Añadido:

- public boolean isDefaultAllAllowed()
- public void setDefaultAllAllowed(boolean valor)

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**  
Añadido:

- public void add(Shape forma)
- public void remove(Shape formaParaEliminar)
- public void copyTo(Shape[] arrayFormas, int índice)
- public int indexOf(Shape forma)

**com.aspose.pdf.generator.legacyxmlmodel.Table**  
Cambiado:

- FixedWidth en campo de getter y setter
- DefaultCellTextInfo en campo de getter y setter  
  Añadido:
- public float getFixedWidth()
- public void setFixedWidth(float valor)
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo valor)

- public Cell getCell(int fila, int columna, boolean esTablaCambiada)
- public void formatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)
- public void formatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)
- public void formatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)
- public void setColumnWidth(int columnNumber, float width)
- public String getColumnWidths()
- public void setColumnWidths(String value)

**com.aspose.pdf.generator.legacyxmlmodel.TabStops**  
Añadido:

- public int getCapacity()
- public void setCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
Cambiado:

- La siguiente lista de campos se cambió a un campo de getter y setter separado:

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


Añadido:

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
Cambios:

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border**  
Cambios:

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value)  
  Añadido Obsoleto:
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils**  
Cambios:

- Internalizado

**com.aspose.pdf.ExcelSaveOptions**  
Añadido:

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font**  
Añadido:

- public void save(OutputStream stream)

**com.aspose.pdf.Form**  
Añadido:

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:**  
Añadido:


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
Añadido:

- public int getCapStyle()
- public void setCapStyle(int value)

**com.aspose.pdf.LineAnnotation**  
Añadido:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.LoadFormat:**  
Cambios:

- public static final int InfoPath - fue eliminado
- public static final int AutoDetect - Añadido

**com.aspose.pdf.Metadata**  
Cambios:

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields() 

**com.aspose.pdf.PageLayout**  
Añadido:

- public static final int Default

**com.aspose.pdf.PolylineAnnotation**  
Añadido:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.PopupAnnotation**  
Añadido:

- public MarkupAnnotation getParent()
- public void setParent(MarkupAnnotation value)

**com.aspose.pdf.RichTextBoxField**  
Cambios:

- public String getRValue() -> public String getRichTextValue()

- public void setRValue(String value) -> public void setRichTextValue(String value)

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
Añadido:

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
Añadido:

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
Añadido:

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
Añadido:

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
Añadido:

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
Añadido:

- public void setFieldImage(String fieldName, InputStream image)