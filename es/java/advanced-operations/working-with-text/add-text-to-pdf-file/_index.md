---
title: Agregar Texto al Archivo PDF 
linktitle: Agregar Texto al Archivo PDF
type: docs
weight: 10
url: es/java/add-text-to-pdf-file/
description: Este artículo describe varios aspectos del trabajo con texto en Aspose.PDF. Aprende cómo agregar texto a PDF, agregar fragmentos HTML o usar fuentes OTF personalizadas.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para agregar texto a un archivo PDF existente:

1. Abre el PDF de entrada usando el objeto Document.
2. Obtén la página particular a la que deseas agregar el texto.
3. Crea un objeto TextFragment con el texto de entrada junto con otras propiedades del texto. El objeto TextBuilder creado a partir de esa página particular – a la que deseas agregar el texto – te permite agregar el objeto TextFragment a la página usando el método AppendText.
4. Llama al método Save del objeto Document y guarda el archivo PDF de salida.

## Agregar Texto

El siguiente fragmento de código te muestra cómo agregar texto en un archivo PDF existente.

```java
public static void AddingText() {
    // Cargar el archivo PDF
    Document document = new Document(_dataDir + "sample.pdf");

    // obtener la página particular
    Page pdfPage = document.getPages().get_Item(1);
    // crear fragmento de texto
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // establecer propiedades del texto
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // crear objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // agregar el fragmento de texto a la página PDF
    textBuilder.appendText(textFragment);

    // Guardar el documento PDF resultante.
    document.save(_dataDir + "AddText_out.pdf");
}
```


## Cargando Fuente desde Stream

El siguiente fragmento de código muestra cómo cargar una fuente desde un objeto Stream al agregar texto a un documento PDF.

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // Cargar archivo PDF de entrada
    Document doc = new Document(_dataDir + "input.pdf");
    // Crear objeto constructor de texto para la primera página del documento
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // Crear fragmento de texto con cadena de ejemplo
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // Cargar la fuente TrueType en el objeto stream
        FileInputStream fontStream = new FileInputStream(fontFile);            
        // Establecer el nombre de la fuente para la cadena de texto
        textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
        // Especificar la posición para el Fragmento de Texto
        textFragment.setPosition(new Position(10, 10));
        // Agregar el texto al TextBuilder para que se pueda colocar sobre el archivo PDF
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // Guardar el documento PDF resultante.
        doc.save(_dataDir); 
    }       
}
```


## Agregar Texto usando TextParagraph

El siguiente fragmento de código muestra cómo agregar texto en un documento PDF usando la clase [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph).

```java
public static void AddTextUsingTextParagraph() {
    // Abrir documento
    Document doc = new Document();
    // Agregar página a la colección de páginas del objeto Document
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // Crear párrafo de texto
    TextParagraph paragraph = new TextParagraph();
    // Establecer la sangría de las líneas subsiguientes
    paragraph.setSubsequentLinesIndent (20);
    // Especificar la ubicación para agregar TextParagraph
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // Especificar el modo de ajuste de palabras
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // Crear fragmento de texto
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // Agregar fragmento al párrafo
    paragraph.appendLine(fragment1);
    // Agregar párrafo
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // Guardar el documento PDF resultante.
    doc.save(_dataDir);        
}
```


## Añadir Hipervínculo a TextSegment

Una página PDF puede constar de uno o más objetos TextFragment, donde cada objeto TextFragment puede tener una o más instancias de TextSegment. Para establecer un hipervínculo en TextSegment, se puede utilizar la propiedad Hyperlink de la clase TextSegment mientras se proporciona el objeto de la instancia de Aspose.Pdf.WebHyperlink. Por favor, intente utilizar el siguiente fragmento de código para cumplir con este requisito.

```java
public static void AddHyperlinkToTextSegment() {
    // Crear instancia de documento
    Document doc = new Document();
    // Agregar página a la colección de páginas del archivo PDF
    Page page1 = doc.getPages().add();

    // Crear instancia de TextFragment
    TextFragment tf = new TextFragment("Fragmento de texto de ejemplo");
    // Establecer alineación horizontal para TextFragment
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // Crear un TextSegment con texto de ejemplo
    TextSegment segment = new TextSegment(" ... Segmento de texto 1...");
    // Agregar segmento a la colección de segmentos de TextFragment
    tf.getSegments().add(segment);

    // Crear un nuevo TextSegment
    segment = new TextSegment("Enlace a Google");
    // Agregar segmento a la colección de segmentos de TextFragment

    tf.getSegments().add(segment);

    // Establecer hipervínculo para TextSegment
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // Establecer color de primer plano para el segmento de texto
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // Establecer formato de texto como cursiva
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // Crear otro objeto TextSegment
    segment = new TextSegment("TextSegment sin hipervínculo");

    // Agregar segmento a la colección de segmentos de TextFragment
    tf.getSegments().add(segment);

    // Agregar TextFragment a la colección de párrafos del objeto página
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // Guardar el documento PDF resultante.
    doc.save(_dataDir);

}
```


## Use OTF Font

Aspose.PDF for Java ofrece la función de usar fuentes Personalizadas/TrueType al crear/manipular contenidos de archivos PDF para que los contenidos del archivo se muestren utilizando fuentes distintas a las fuentes predeterminadas del sistema. A partir del lanzamiento de Aspose.PDF para Java 10.4.0, hemos proporcionado soporte para Fuentes de Tipo Abierto.

```java
public static void UseOTFFont() {
    // Crear una nueva instancia de documento
    Document pdfDocument = new Document();
    // Agregar una página a la colección de páginas del archivo PDF
    Page page = pdfDocument.getPages().add();
    // Crear una instancia de TextFragment con texto de ejemplo
    TextFragment fragment = new TextFragment("Texto de ejemplo en fuente OTF");
    // O incluso puede especificar la ruta de la fuente OTF en el directorio del sistema
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // Especificar que la fuente se incruste dentro del archivo PDF, para que se muestre correctamente,
    // Incluso si la fuente específica no está instalada/presente en la máquina de destino
    fragment.getTextState().getFont().setEmbedded(true);
    // Agregar TextFragment a la colección de párrafos de la instancia de Page
    page.getParagraphs().add(fragment);
    // Guardar el documento PDF resultante.
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## Añadir Cadena HTML usando DOM

La clase Aspose.Pdf.Generator.Text contiene una propiedad llamada IsHtmlTagSupported que permite agregar etiquetas/contenidos HTML en archivos PDF. El contenido añadido se renderiza en etiquetas HTML nativas en lugar de aparecer como una simple cadena de texto. Para admitir una característica similar en el nuevo Modelo de Objeto de Documento (DOM) del espacio de nombres Aspose.Pdf, se ha introducido la clase HtmlFragment.

La instancia [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) se puede usar para especificar los contenidos HTML que deben colocarse dentro del archivo PDF. Similar a TextFragment, HtmlFragment es un objeto a nivel de párrafo y se puede agregar a la colección de párrafos del objeto Page. Los siguientes fragmentos de código muestran los pasos para colocar contenidos HTML dentro del archivo PDF usando el enfoque DOM.

```java
public static void AddingHtmlString() {
    // Instanciar objeto Document
    Document doc = new Document();
    // Añadir una página a la colección de páginas del archivo PDF
    Page page = doc.getPages().add();
    // Instanciar HtmlFragment con contenidos HTML
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>Demostración de Cadena HTML</strong></h1>");
    // establecer MarginInfo para detalles de margen
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // Establecer información de margen
    title.setMargin(Margin);
    // Añadir Fragmento HTML a la colección de párrafos de la página
    page.getParagraphs().add(title);
    // Guardar archivo PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


El siguiente fragmento de código demuestra los pasos para agregar listas ordenadas de HTML en el documento:

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // Instanciar objeto Document
    Document doc = new Document();
    // Instanciar objeto HtmlFragment con el fragmento HTML correspondiente
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>Primero</li><li>Segundo</li><li>Tercero</li><li>Cuarto</li><li>Quinto</li></ul><p>Texto después de la lista.</p><p>Siguiente línea<br/>Última línea</p></div>");
    // Agregar Página en la Colección de Páginas
    Page page = doc.getPages().add();
    // Agregar HtmlFragment dentro de la página
    page.getParagraphs().add(t);
    // Guardar archivo PDF resultante
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

También puede establecer el formato de cadena HTML usando el objeto TextState de la siguiente manera:

```java
public static void AddHTMLStringFormatting() {
    // Instanciar objeto Document
    Document doc = new Document();
    // Agregar una página a la colección de páginas del archivo PDF
    Page page = doc.getPages().add();
    // Instanciar HtmlFragment con contenidos HTML
    HtmlFragment title = new HtmlFragment("<h1><strong>Demostración de Cadena HTML</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // Agregar Fragmento HTML a la colección de párrafos de la página
    page.getParagraphs().add(title);
    // Guardar archivo PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


En caso de que establezcas algunos valores de atributos de texto a través del marcado HTML y luego proporciones los mismos valores en las propiedades de TextState, ellos sobrescribirán los parámetros HTML por las propiedades del formulario de instancia de TextState. Los siguientes fragmentos de código muestran el comportamiento descrito.

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // Instanciar objeto Document
    Document doc = new Document();
    // Agregar una página a la colección de páginas del archivo PDF
    Page page = doc.getPages().add();
    // Instanciar HtmlFragment con contenido HTML
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>La tabla contiene texto</i></b></p>");
    // La fuente 'Verdana' se restablecerá a 'Arial'
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // Establecer información de margen inferior
    title.getMargin().setBottom(10);
    // Establecer información de margen superior
    title.getMargin().setTop(400);
    // Agregar fragmento HTML a la colección de párrafos de la página
    page.getParagraphs().add(title);
    // Guardar archivo PDF
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## FootNotes y EndNotes (DOM)

FootNotes indican notas en el texto de tu documento usando números en superíndice consecutivos. La nota actual está indentada y puede aparecer como una nota al pie en la parte inferior de la página.

### Agregar FootNote

En un sistema de referencia por nota al pie, indica una referencia:

- colocando un número pequeño sobre la línea del tipo directamente después del material de origen. Este número se llama identificador de nota y se sitúa ligeramente por encima de la línea de texto.
- colocando el mismo número, seguido de una cita de tu fuente, en la parte inferior de la página. La numeración de notas al pie debe ser numérica y cronológica: la primera referencia es 1, la segunda es 2, y así sucesivamente.

La ventaja de las notas al pie es que el lector puede simplemente bajar la vista hacia la página para descubrir la fuente de una referencia que les interese.

Por favor, sigue los pasos especificados a continuación para crear una FootNote:

- Crear una instancia de Document
- Crear un objeto Page
- Crear un objeto TextFragment

- Crear una instancia de Note y pasar su valor a la propiedad TextFragment.FootNote
- Agregar TextFragment a la colección de párrafos de una instancia de página

### Estilo de línea personalizado para FootNote

El siguiente ejemplo demuestra cómo agregar notas al pie al final de la página del PDF y definir un estilo de línea personalizado.

```java
public static void AddFootNote() {
    // crear instancia de Document
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // crear instancia de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // establecer valor de FootNote para TextFragment
    text.setFootNote(new Note("nota al pie para texto de prueba 1"));
    // agregar TextFragment a la colección de párrafos de la primera página del documento
    page.getParagraphs().add(text);
    // crear segundo TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // establecer FootNote para el segundo fragmento de texto
    text.setFootNote(new Note("nota al pie para texto de prueba 2"));
    // agregar segundo fragmento de texto a la colección de párrafos del archivo PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


Podemos configurar el formato de la Etiqueta de Nota al Pie (identificador de nota) utilizando el objeto TextState de la siguiente manera:

```java
public static void AddCustomFootNoteLabel() {
    // crear instancia de Document
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // crear instancia de TextFragment
    TextFragment text = new TextFragment("Hola Mundo");
    // establecer valor de Nota al Pie para TextFragment
    text.setFootNote(new Note("nota al pie para texto de prueba 1"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // añadir TextFragment a la colección de párrafos de la primera página del documento
    page.getParagraphs().add(text);
    // crear segundo TextFragment
    text = new TextFragment("Aspose.Pdf para Java");
    // establecer Nota al Pie para el segundo fragmento de texto
    text.setFootNote(new Note("nota al pie para texto de prueba 2"));
    // añadir el segundo fragmento de texto a la colección de párrafos del archivo PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### Personalizar etiqueta de nota al pie

Por defecto, el número de la nota al pie es incremental comenzando desde 1. Sin embargo, podemos tener un requisito para establecer una etiqueta de nota al pie personalizada. Para cumplir con este requisito, intente usar el siguiente fragmento de código

```java
public static void CustomFootNote_Label() {
    // Crear instancia de Documento
    Document document = new Document();
    // Añadir página a la colección de páginas del PDF
    Page page = document.getPages().add();
    // Crear objeto GraphInfo
    GraphInfo graph = new GraphInfo();
    // Establecer el ancho de línea como 2
    graph.setLineWidth(2);
    // Establecer el color para el objeto graph
    graph.setColor(Color.getRed());
    // Establecer el valor de la matriz de guiones como 3
    graph.setDashArray(new int[] { 3 });
    // Establecer el valor de fase de guiones como 1
    graph.setDashPhase(1);
    // Establecer el estilo de línea de nota al pie para la página como graph
    page.setNoteLineStyle(graph);

    // Crear instancia de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // Establecer el valor de la nota al pie para TextFragment
    text.setFootNote(new Note("nota al pie para texto de prueba 1"));
    // Especificar etiqueta personalizada para la nota al pie
    text.getFootNote().setText(" Aspose(2021)");
    // Añadir TextFragment a la colección de párrafos de la primera página del documento
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## Añadiendo Imagen y Tabla a una Nota al Pie

En versiones de lanzamiento anteriores, se proporcionó soporte para Notas al Pie, pero solo era aplicable al objeto TextFragment. Sin embargo, a partir del lanzamiento de Aspose.PDF para Java 10.7.0, también puedes agregar Notas al Pie a otros objetos dentro del documento PDF, como Tabla, Celdas, etc. El siguiente fragmento de código muestra los pasos para agregar una Nota al Pie al objeto TextFragment y luego agregar un objeto Imagen y Tabla a la colección de párrafos de la sección de Nota al Pie.

```java
public static void AddingImageAndTableToFootnote() {
    // Crear instancia de Documento
    Document document = new Document();
    // Agregar página a la colección de páginas del PDF
    Page page = document.getPages().add();
    // Crear instancia de TextFragment
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("texto de la nota al pie");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Fila 1 Celda 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## Cómo Crear Notas al Final

Una Nota al Final es una cita de fuente que remite a los lectores a un lugar específico al final del documento donde pueden encontrar la fuente de la información o las palabras citadas o mencionadas en el documento. Al usar notas al final, la oración citada, parafraseada o resumida va seguida de un número en superíndice.

El siguiente ejemplo demuestra cómo agregar una Nota al Final en la página de un Pdf.

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // añadir página a la colección de páginas del PDF
    Page page = doc.getPages().add();
    // crear instancia de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // establecer valor de FootNote para TextFragment
    text.setEndNote(new Note("nota final de ejemplo"));
    // especificar etiqueta personalizada para FootNote
    text.getEndNote().setText(" Aspose(2021)");
    // añadir TextFragment a la colección de párrafos de la primera página del documento
    page.getParagraphs().add(text);
    // guardar el archivo PDF
    doc.save(_dataDir + "EndNote.pdf");
}
```


## Texto e Imagen como Párrafo en Línea

El diseño predeterminado del archivo PDF es un diseño de flujo (de arriba a la izquierda hacia abajo a la derecha). Por lo tanto, cada nuevo elemento que se agrega al archivo PDF se añade en el flujo de la esquina inferior derecha. Sin embargo, podemos tener un requisito para mostrar varios elementos de la página, es decir, Imagen y Texto al mismo nivel (uno tras otro). Un enfoque puede ser crear una instancia de Tabla y agregar ambos elementos a objetos de celda individuales. Sin embargo, otro enfoque puede ser el párrafo en línea. Al establecer la propiedad IsInLineParagraph de Imagen y Texto como verdadera, estos párrafos aparecerán como en línea con otros elementos de la página.

El siguiente fragmento de código muestra cómo agregar texto e imagen como párrafos en línea en un archivo PDF.

```java
 public static void TextAndImageAsInLineParagraph() {
    // Instanciar la clase Document
    Document doc = new Document();
    // Agregar página a la colección de páginas de la instancia de Document
    Page page = doc.getPages().add();
    // Crear TextFragment
    TextFragment text = new TextFragment("Hola Mundo.. ");
    // Agregar fragmento de texto a la colección de párrafos del objeto Page
    page.getParagraphs().add(text);
    // Crear una instancia de imagen
    Image image = new Image();
    // Configurar la imagen como párrafo en línea para que aparezca justo después
    // del objeto de párrafo anterior (TextFragment)
    image.setInLineParagraph (true);
    // Especificar la ruta del archivo de imagen
    image.setFile(_dataDir + "aspose-logo.jpg");
    // Establecer altura de la imagen (opcional)
    image.setFixHeight(30);
    // Establecer ancho de la imagen (opcional)
    image.setFixWidth(100);
    // Agregar imagen a la colección de párrafos del objeto page
    page.getParagraphs().add(image);
    // Re-inicializar el objeto TextFragment con diferentes contenidos
    text = new TextFragment(" Hola de nuevo..");
    // Configurar TextFragment como párrafo en línea
    text.setInLineParagraph (true);
    // Agregar el nuevo TextFragment creado a la colección de párrafos de la página
    page.getParagraphs().add(text);
    
    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```


## Especificar el Espaciado de Caracteres al Agregar Texto

Se puede agregar texto dentro de una colección de párrafos de archivos PDF utilizando la instancia de TextFragment o mediante el objeto TextParagraph e incluso puede estampar el texto dentro del PDF utilizando la clase TextStamp. Al agregar el texto, podemos tener un requisito para especificar el espaciado de caracteres para los objetos de texto. Para cumplir con este requisito, se ha introducido una nueva propiedad llamada propiedad CharacterSpacing. Por favor, revise los siguientes enfoques para cumplir con este requisito.

Los siguientes enfoques muestran los pasos para especificar el espaciado de caracteres al agregar texto dentro de un documento PDF.

## Usando TextBuilder y TextFragment

```java
 public static void CharacterSpacing_TextFragment(){
    // Crear instancia de Documento
    Document pdfDocument = new Document();
    // Agregar página a la colección de páginas del Documento
    Page page = pdfDocument.getPages().add();
    // Crear instancia de TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Crear instancia de fragmento de texto con contenido de muestra
    TextFragment wideFragment = new TextFragment("Texto con espaciado de caracteres incrementado");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // Especificar espaciado de caracteres para TextFragment
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // Especificar la posición de TextFragment
    wideFragment.setPosition(new Position(100, 650));
    // Añadir TextFragment a la instancia de TextBuilder
    builder.appendText(wideFragment);        
    // Guardar el documento PDF resultante.
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## Usando TextBuilder y TextParagraph

```java
public static void CharacterSpacing_TextParagraph() {
    // Crear instancia de Document
    Document pdfDocument = new Document();
    // Agregar página a la colección de páginas del Documento
    Page page = pdfDocument.getPages().add();
    // Crear instancia de TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Instanciar instancia de TextParagraph
    TextParagraph paragraph = new TextParagraph();
    // Crear instancia de TextState para especificar el nombre y tamaño de la fuente
    TextState state = new TextState("Arial", 12);
    // Especificar el espaciado de caracteres
    state.setCharacterSpacing (1.5f);
    // Añadir texto al objeto TextParagraph
    paragraph.appendLine("Este es un párrafo con espaciado de caracteres", state);
    // Especificar la posición para TextParagraph
    paragraph.setPosition (new Position(100, 550));
    // Añadir TextParagraph a la instancia de TextBuilder
    builder.appendParagraph(paragraph);
    // Guardar el documento PDF resultante.
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## Usando TextStamp

```java
public static void CharacterSpacing_TextStamp() {
    // Crear una instancia de Document
    Document pdfDocument = new Document();
    // Agregar una página a la colección de páginas del Document
    Page page = pdfDocument.getPages().add();
    // Instanciar TextStamp con texto de ejemplo
    TextStamp stamp = new TextStamp("Este es un sello de texto con espaciado de caracteres");
    // Especificar el nombre de la fuente para el objeto Stamp
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // Especificar el tamaño de fuente para TextStamp
    stamp.getTextState().setFontSize(12);
    // Especificar el espaciado de caracteres como 1f
    stamp.getTextState().setCharacterSpacing (1f);
    // Establecer la XIndent para Stamp
    stamp.setXIndent(100);
    // Establecer la YIndent para Stamp
    stamp.setYIndent(500);
    // Agregar el sello textual a la instancia de página
    stamp.put(page);        
    // Guardar el documento PDF resultante.
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## Crear documento PDF de varias columnas

En revistas y periódicos, vemos principalmente que las noticias se muestran en varias columnas en las páginas individuales en lugar de los libros donde los párrafos de texto se imprimen principalmente en toda la página de izquierda a derecha.
 Muchas aplicaciones de procesamiento de documentos como Microsoft Word y Adobe Acrobat Writer permiten a los usuarios crear múltiples columnas en una sola página y luego agregarles datos.

Aspose.PDF para Java también ofrece la función de crear múltiples columnas dentro de las páginas de documentos PDF. Para crear un archivo PDF de múltiples columnas, podemos hacer uso de la clase Aspose.Pdf.FloatingBox ya que proporciona la propiedad ColumnInfo.ColumnCount para especificar el número de columnas dentro de FloatingBox y también podemos especificar el espacio entre columnas y los anchos de las columnas usando las propiedades ColumnInfo.ColumnSpacing y ColumnInfo.ColumnWidths respectivamente. Por favor, tenga en cuenta que FloatingBox es un elemento dentro del Modelo de Objeto de Documento y puede tener un posicionamiento obsoleto en comparación con el posicionamiento relativo (es decir, Texto, Gráfico, Imagen, etc.).
El espaciado entre columnas significa el espacio entre las columnas y el espaciado predeterminado entre las columnas es de 1,25 cm. Si no se especifica el ancho de la columna, entonces Aspose.PDF para Java calcula automáticamente el ancho de cada columna de acuerdo con el tamaño de la página y el espaciado entre columnas.

A continuación se da un ejemplo para demostrar la creación de dos columnas con objetos de Gráficos (Línea) y se añaden a la colección de párrafos de FloatingBox, que luego se añade a la colección de párrafos de la instancia de Page.

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // Especificar la información del margen izquierdo para el archivo PDF
    doc.getPageInfo().getMargin().setLeft(40);
    
    // Especificar la información del margen derecho para el archivo PDF
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // Añadir la línea a la colección de párrafos del objeto sección
    page.getParagraphs().add(graph1);

    // Especificar las coordenadas para la línea
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // Crear variables de cadena con texto que contiene etiquetas html
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> Cómo evitar estafas de dinero</<strong> </span>";
    
    // Crear párrafos de texto que contienen texto HTML

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // Añadir cuatro columnas en la sección
    box.getColumnInfo().setColumnCount(2);
    // Establecer el espaciado entre las columnas
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("Por Un Googler (El Blog Oficial de Google)");
    text1.getTextState().setFontSize(8);
    text1.getTextState().setLineSpacing(2);
    text1.getTextState().setFontSize(10);
    text1.getTextState().setFontStyle(FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // Crear un objeto de gráficos para dibujar una línea
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // Especificar las coordenadas para la línea
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // Añadir la línea a la colección de párrafos del objeto sección
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // Guardar archivo PDF
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## Trabajar con tabulaciones personalizadas

Un tabulador es un punto de parada para la tabulación. En el procesamiento de textos, cada línea contiene una serie de tabulaciones colocadas a intervalos regulares (por ejemplo, cada media pulgada). Sin embargo, se pueden cambiar, ya que la mayoría de los procesadores de texto te permiten establecer tabulaciones donde desees. Cuando presionas la tecla Tab, el cursor o punto de inserción salta al siguiente tabulador, el cual es invisible. Aunque los tabuladores no existen en el archivo de texto, el procesador de texto los rastrea para que pueda reaccionar correctamente a la tecla Tab.

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) permite a los desarrolladores utilizar tabulaciones personalizadas en documentos PDF. La clase Aspose.Pdf.Text.TabStop se usa para establecer tabulaciones personalizadas en la clase [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment).

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) también ofrece algunos tipos de líderes de tabulación predefinidos como una enumeración llamada TabLeaderType cuyos valores predefinidos y sus descripciones se dan a continuación:

|**Tipo de Líder de Tabulación**|**Descripción**|
| :- | :- |
|None|Sin líder de tabulación|
|Solid|Líder de tabulación sólido|
|Dash|Líder de tabulación de guion|
|Dot|Líder de tabulación de punto|

Aquí hay un ejemplo de cómo establecer paradas de TAB personalizadas.

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("Este es un ejemplo de formación de tabla con paradas de TAB", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## Cómo Agregar Texto Transparente en PDF

Un archivo PDF contiene objetos de Imagen, Texto, Gráfico, adjunto, Anotaciones y, al crear TextFragment, puede establecer información de color de primer plano, color de fondo, así como el formato de texto. Aspose.PDF para Java admite la función de agregar texto con canal de color Alpha. El siguiente fragmento de código muestra cómo agregar texto con color transparente.

```java
public static void AddTransparentText() {
    // Crear instancia de Documento
    Document pdfdocument = new Document();
    // Crear página para la colección de páginas del archivo PDF
    Page page = pdfdocument.getPages().add();

    // Crear objeto Gráfico
    Graph canvas = new Graph(100, 400);
    // Crear instancia de rectángulo con ciertas dimensiones
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // Crear objeto de color desde el canal de color Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // Agregar rectángulo a la colección de formas del objeto Gráfico
    canvas.getShapes().add(rect);
    // Agregar objeto gráfico a la colección de párrafos del objeto página
    page.getParagraphs().add(canvas);
    // Configurar valor para no cambiar la posición del objeto gráfico
    canvas.setChangePosition(false);

    // Crear instancia de TextFragment con valor de ejemplo
    TextFragment text = new TextFragment(
            "texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente ");
    // Crear objeto de color desde el canal Alpha
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // Establecer información de color para la instancia de texto
    text.getTextState().setForegroundColor(alphaColor);
    // Agregar texto a la colección de párrafos de la instancia de página
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## Especificar el Espaciado de Línea para Fuentes

Cada fuente tiene un cuadrado abstracto, cuya altura es la distancia prevista entre líneas de texto en el mismo tamaño de fuente. Este cuadrado se llama `cuadrado em` y es la cuadrícula de diseño en la cual se definen los contornos de los glifos. Muchas letras de la fuente de entrada tienen puntos que están colocados fuera de los límites del `cuadrado em` de la fuente, por lo que para mostrar la fuente correctamente, se necesita el uso de una configuración especial. El objeto TextFragment tiene un conjunto de opciones de formato de texto que son accesibles a través del método [TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--).
Este método devuelve la clase [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions).
 Esta clase tiene una enumeración [LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode) que está diseñada para fuentes específicas, por ejemplo, la fuente de entrada "HPSimplified.ttf". También la clase [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) tiene un método [setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-) de tipo LineSpacingMode. Solo necesitas establecer LineSpacing en LineSpacingMode.FullSize. El fragmento de código para que una fuente se muestre correctamente sería el siguiente:

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // Cargar archivo PDF de entrada
    Document doc = new Document();
    // Crear TextFormattingOptions con LineSpacingMode.FullSize
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // Crear objeto TextBuilder para la primera página del documento
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // Crear fragmento de texto con cadena de ejemplo
    TextFragment textFragment = new TextFragment("Hello world");

    // Cargar la fuente TrueType en el objeto stream
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // Establecer el nombre de la fuente para la cadena de texto
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // Especificar la posición para el Fragmento de Texto
    textFragment.setPosition(new Position(100, 600));
    // Establecer TextFormattingOptions del fragmento actual al predefinido (que apunta a
    // LineSpacingMode.FullSize)
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // Agregar el texto a TextBuilder para que pueda colocarse sobre el archivo PDF
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // Guardar el documento PDF resultante
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## Obtener el Ancho del Texto Dinámicamente

A veces, es necesario obtener el ancho del texto de manera dinámica. Aspose.PDF para Java incluye dos métodos para la medición del ancho de cadenas. Puede invocar el método [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) de las clases com.aspose.pdf.Font o com.aspose.pdf.TextState (o ambas). El siguiente fragmento de código muestra cómo utilizar esta funcionalidad.

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("¡Medición inesperada de la cadena de fuente!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("¡Medición inesperada de la cadena de fuente!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("¡La medición de cadena de fuente y estado no coincide!");
        }
}
```