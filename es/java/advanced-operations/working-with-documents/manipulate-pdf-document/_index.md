---
title: Manipular Documento PDF 
linktitle: Manipular Documento PDF
type: docs
weight: 30
url: /es/java/manipulate-pdf-document/
description: Este artículo contiene información sobre cómo validar un Documento PDF para el Estándar PDF A, cómo trabajar con TOC, cómo establecer la fecha de vencimiento del PDF y cómo determinar el Progreso de la generación del archivo PDF.
lastmod: "2021-06-05"
---

## Validar Documento PDF para el Estándar PDF A (A 1A y A 1B)

Para validar un documento PDF para la compatibilidad con PDF/A-1a o PDF/A-1b, use el método [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este método le permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerido [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) enumeración: PDF_A_1A o PDF_A_1B.

El formato de salida XML es un formato personalizado de Aspose.
 El XML contiene una colección de etiquetas con el nombre Problem; cada etiqueta contiene los detalles de un problema particular. El atributo ObjectID de la etiqueta Problem representa el ID del objeto particular al que este problema está relacionado. El atributo Clause representa una regla correspondiente en la especificación del PDF.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Validar PDF para PDF/A-1a
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // Guardar archivo PDF actualizado
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## Trabajando con TOC

### Agregar TOC a un PDF Existente

La clase ListSection en el paquete aspose.pdf te permite crear una tabla de contenidos al crear un documento PDF desde cero. Para agregar encabezados, que son elementos del TOC, utiliza la clase [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading).

Para agregar un TOC a un archivo PDF existente, utiliza la clase [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) en el paquete com.aspose.pdf. El paquete com.aspose.pdf puede tanto crear como manipular archivos PDF existentes. Para agregar un índice a un PDF existente, utilice el paquete com.aspose.pdf.

El siguiente fragmento de código muestra cómo crear una tabla de contenido dentro de un archivo PDF existente.

```java
public static void AddTOCtoExistingPDF() {
    // Cargar un archivo PDF existente
    Document document = new Document(_dataDir + "sample.pdf");

    // Obtener acceso a la primera página del archivo PDF
    Page tocPage = document.getPages().insert(1);

    // Crear objeto para representar la información del TOC
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("Tabla de Contenidos");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // Establecer el título para el TOC
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // Crear objetos de cadena que se usarán como elementos del TOC
    String[] titles = new String[4];
    titles[0] = "Primera página";
    titles[1] = "Segunda página";
    titles[2] = "Tercera página";
    titles[3] = "Cuarta página";
    for (int i = 0; i < 4; i++) {
      // Crear objeto de encabezado
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // Especificar la página de destino para el objeto de encabezado
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // Página de destino
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // Coordenada de destino
      segment2.setText(titles[i]);

      // Agregar encabezado a la página que contiene el TOC
      tocPage.getParagraphs().add(heading2);
    }
    // Guardar el documento actualizado
    document.save("TOC_Output_Java.pdf");
  }
```
### Establecer diferentes TabLeaderType para diferentes niveles de TOC

Aspose.PDF también permite establecer diferentes TabLeaderType para diferentes niveles de TOC. Necesitas establecer la propiedad LineDash de FormatArray con el valor apropiado del enum TabLeaderType como sigue.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // establecer LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("Tabla de Contenidos");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Añadir la sección de la lista a la colección de secciones del documento Pdf

    tocPage.setTocInfo(tocInfo);

    // Definir el formato de los cuatro niveles de la lista estableciendo los márgenes izquierdos y
    // configuraciones de formato de texto de cada nivel

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Crear una sección en el documento Pdf
    Page page = document.getPages().add();

    // Añadir cuatro encabezados en la sección
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("Encabezado de Ejemplo" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // Añadir el encabezado en la Tabla de Contenidos.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // guardar el PDF
    document.save(outFile);
  }
```

### Ocultar Números de Página en TOC

En caso de que no desees mostrar números de página, junto con los encabezados en TOC, puedes usar la propiedad [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) de la clase [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) como falso. Por favor revisa el siguiente fragmento de código para ocultar los números de página en la tabla de contenidos:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Tabla de Contenidos");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Agregar la sección de la lista a la colección de secciones del documento Pdf
    tocPage.setTocInfo(tocInfo);

    // Definir el formato de la lista de cuatro niveles estableciendo los márgenes izquierdos y
    // configuraciones de formato de texto de cada nivel

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // Agregar cuatro encabezados en la sección
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("este es el encabezado de nivel " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### Personalizar Números de Página al agregar TOC

Es común personalizar la numeración de páginas en el TOC al agregar TOC en un documento PDF. Por ejemplo, puede que necesitemos agregar algún prefijo antes del número de página como P1, P2, P3 y así sucesivamente. En tal caso, Aspose.PDF para Java proporciona la propiedad PageNumbersPrefix de la clase TocInfo que se puede usar para personalizar los números de página como se muestra en el siguiente ejemplo de código.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // Cargar un archivo PDF existente
    Document doc = new Document(inFile);
    // Obtener acceso a la primera página del archivo PDF
    Page tocPage = doc.getPages().insert(1);
    // Crear objeto para representar la información del TOC
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Tabla de Contenidos");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // Establecer el título para TOC
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // Crear objeto Heading
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // Especificar la página de destino para el objeto heading
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // Página de destino
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // Coordenada de destino
      segment2.setText("Página " + i);
      // Agregar heading a la página que contiene el TOC
      tocPage.getParagraphs().add(heading2);
    }

    // Guardar el documento actualizado
    doc.save(outFile);
  }
```


## Añadir Capas al Archivo PDF

Las capas pueden usarse en documentos PDF de muchas maneras. Podrías tener un archivo multilingüe que deseas distribuir y quieres que el texto en cada idioma aparezca en diferentes capas, con el diseño de fondo apareciendo en una capa separada. También podrías crear documentos con animación que aparece en una capa separada. Un ejemplo podría ser agregar un acuerdo de licencia a tu archivo, y no quieres que un usuario vea el contenido hasta que acepte los términos del acuerdo.

Aspose.PDF para Java soporta la adición de capas a archivos PDF.

Para trabajar con capas en archivos PDF, utiliza los siguientes miembros del API.

La clase [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) representa una capa y contiene las siguientes propiedades:

- **Name** – el nombre de la capa.
- **Id** – el ID de la capa.
- **Contents** – una lista de operadores de capa.

Una vez que los objetos [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) han sido definidos, agrégales a la colección Layers del objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 El código a continuación muestra cómo agregar capas a un documento PDF.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "Línea Roja");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "Línea Verde");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "Línea Azul");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## Establecer Expiración del PDF

La función de expiración del PDF establece cuánto tiempo es válido un archivo PDF. En una fecha particular, si alguien intenta acceder a él, se muestra un pop-up explicando que el archivo ha expirado y que necesitan uno nuevo.

Aspose.PDF te permite establecer la expiración al crear y editar archivos PDF.

El fragmento de código a continuación muestra cómo establecer la fecha de expiración para un archivo PDF. Necesitas usar JavaScript ya que los archivos guardados por componentes de terceros (por ejemplo, OwnerGuard) no se pueden ver en otras estaciones de trabajo sin esa utilidad.

El archivo PDF puede ser creado usando PDF OwnerGuard utilizando un archivo existente con una fecha de expiración. Pero el nuevo archivo solo se puede abrir en una estación de trabajo que tenga instalado PDF OwnerGuard. Las estaciones de trabajo sin PDF OwnerGuard darán un ExpirationFeatureError. Por ejemplo, PDF Reader abre el archivo si OwnerGuard está instalado, pero Adobe Acrobat devuelve un error.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```