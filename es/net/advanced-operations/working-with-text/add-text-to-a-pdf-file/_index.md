---
title: Añadir texto a PDF usando C#
linktitle: Añadir texto a PDF
type: docs
weight: 10
url: /es/net/add-text-to-pdf-file/
description: Este artículo describe varios aspectos del trabajo con texto en Aspose.PDF. Aprende cómo añadir texto a PDF, añadir fragmentos HTML o usar fuentes OTF personalizadas.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir texto a PDF usando C#",
    "alternativeHeadline": "Cómo añadir texto a PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, añadir texto a pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo describe varios aspectos del trabajo con texto en Aspose.PDF. Aprende cómo añadir texto a PDF, añadir fragmentos HTML o usar fuentes OTF personalizadas."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Para agregar texto a un archivo PDF existente:

1. Abre el PDF de entrada usando el objeto Document.
2. Obtén la página específica a la que deseas agregar el texto.
3. Crea un objeto TextFragment con el texto de entrada junto con otras propiedades del texto. El objeto TextBuilder creado de esa página en particular – a la que deseas agregar el texto – te permite añadir el objeto TextFragment a la página usando el método AppendText.
4. Llama al método Save del objeto Document y guarda el archivo PDF de salida.

## Agregar Texto

El siguiente fragmento de código te muestra cómo agregar texto en un archivo PDF existente.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "input.pdf");

// Obtener página específica
Page pdfPage = (Page)pdfDocument.Pages[1];

// Crear fragmento de texto
TextFragment textFragment = new TextFragment("texto principal");
textFragment.Position = new Position(100, 600);

// Establecer propiedades del texto
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// Crear objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);

// Añadir el fragmento de texto a la página PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Cargando Fuente desde un Flujo

El siguiente fragmento de código muestra cómo cargar una fuente desde un objeto Stream al añadir texto a un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// Cargar archivo PDF de entrada
Document doc = new Document(dataDir + "input.pdf");
// Crear objeto constructor de texto para la primera página del documento
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Crear fragmento de texto con una cadena de ejemplo
TextFragment textFragment = new TextFragment("Hola mundo");

if (fontFile != "")
{
    // Cargar la fuente TrueType en el objeto de flujo
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // Establecer el nombre de la fuente para la cadena de texto
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Especificar la posición para el Fragmento de Texto
        textFragment.Position = new Position(10, 10);
        // Añadir el texto al TextBuilder para que pueda colocarse sobre el archivo PDF
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // Guardar el documento PDF resultante.
    doc.Save(dataDir);
}
```
## Agregar texto usando TextParagraph

El siguiente fragmento de código te muestra cómo agregar texto en un documento PDF utilizando la clase [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Abrir documento
Document doc = new Document();
// Añadir página a la colección de páginas del objeto Document
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// Crear párrafo de texto
TextParagraph paragraph = new TextParagraph();
// Establecer la indentación de las líneas subsiguientes
paragraph.SubsequentLinesIndent = 20;
// Especificar la ubicación para añadir TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// Especificar el modo de ajuste de palabras
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// Crear fragmento de texto
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// Añadir fragmento al párrafo
paragraph.AppendLine(fragment1);
// Añadir párrafo
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// Guardar el documento PDF resultante.
doc.Save(dataDir);
```
## Agregar Hipervínculo a TextSegment

Una página PDF puede constar de uno o más objetos TextFragment, donde cada objeto TextFragment puede tener una o más instancias de TextSegment. Para establecer un hipervínculo para TextSegment, se puede utilizar la propiedad Hyperlink de la clase [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) proporcionando el objeto de la instancia Aspose.Pdf.WebHyperlink. Por favor, intente usar el siguiente fragmento de código para lograr este requisito.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear instancia de documento
Document doc = new Document();
// Agregar página a la colección de páginas del archivo PDF
Page page1 = doc.Pages.Add();
// Crear instancia de TextFragment
TextFragment tf = new TextFragment("Fragmento de Texto de Ejemplo");
// Establecer alineación horizontal para TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// Crear un textsegment con texto de ejemplo
TextSegment segment = new TextSegment(" ... Texto Segmento 1...");
// Agregar segmento a la colección de segmentos de TextFragment
tf.Segments.Add(segment);
// Crear un nuevo TextSegment
segment = new TextSegment("Enlace a Google");
// Agregar segmento a la colección de segmentos de TextFragment
tf.Segments.Add(segment);
// Establecer hipervínculo para TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// Establecer color de primer plano para el segmento de texto
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// Establecer formato de texto como cursiva
segment.TextState.FontStyle = FontStyles.Italic;
// Crear otro objeto TextSegment
segment = new TextSegment("TextSegment sin hipervínculo");
// Agregar segmento a la colección de segmentos de TextFragment
tf.Segments.Add(segment);
// Agregar TextFragment a la colección de párrafos del objeto de página
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// Guardar el documento PDF resultante.
doc.Save(dataDir);
```
## Utilizar fuente OTF

Aspose.PDF para .NET ofrece la característica de utilizar fuentes personalizadas/TrueType mientras se crea o se manipula el contenido de archivos PDF de modo que los contenidos del archivo se muestren utilizando fuentes distintas a las predeterminadas del sistema. A partir de la versión de Aspose.PDF para .NET 10.3.0, hemos proporcionado soporte para fuentes de tipo abierto.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear una nueva instancia de documento
Document pdfDocument = new Document();
// Añadir página a la colección de páginas del archivo PDF
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// Crear instancia de TextFragment con texto de muestra
TextFragment fragment = new TextFragment("Texto de muestra en fuente OTF");
// Buscar fuente dentro del directorio de fuentes del sistema
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// O incluso puede especificar la ruta de la fuente OTF en el directorio del sistema
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// Especificar para embeber la fuente dentro del archivo PDF, de modo que se muestre correctamente,
// Incluso si la fuente específica no está instalada/presente en la máquina objetivo
fragment.TextState.Font.IsEmbedded = true;
// Añadir TextFragment a la colección de párrafos de la instancia de Page
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Agregar cadena HTML usando DOM

La clase Aspose.Pdf.Generator.Text contiene una propiedad llamada IsHtmlTagSupported que permite agregar etiquetas/contenidos HTML en archivos PDF. El contenido agregado se representa en etiquetas HTML nativas en lugar de aparecer como una cadena de texto simple. Para admitir una función similar en el nuevo Modelo de Objeto de Documento (DOM) del espacio de nombres Aspose.Pdf, se ha introducido la clase HtmlFragment.

La instancia [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) se puede utilizar para especificar los contenidos HTML que deben colocarse dentro del archivo PDF. Similar a TextFragment, HtmlFragment es un objeto a nivel de párrafo y se puede agregar a la colección de párrafos del objeto Page. Los siguientes fragmentos de código muestran los pasos para colocar contenidos HTML dentro del archivo PDF utilizando el enfoque DOM.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Instanciar objeto Document
Document doc = new Document();
// Agregar una página a la colección de páginas del archivo PDF
Page page = doc.Pages.Add();
// Instanciar HtmlFragment con contenidos HTML
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Tabla</i></b></fontsize>");
// Establecer información del margen inferior
title.Margin.Bottom = 10;
// Establecer información del margen superior
title.Margin.Top = 200;
// Agregar Fragmento HTML a la colección de párrafos de la página
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// Guardar archivo PDF
doc.Save(dataDir);
```
El siguiente fragmento de código demuestra los pasos sobre cómo agregar listas ordenadas HTML en el documento:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// La ruta al documento de salida.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// Instancia del objeto Document
Document doc = new Document();
// Instancia del objeto HtmlFragment con el fragmento HTML correspondiente
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>Primero</li><li>Segundo</li><li>Tercero</li><li>Cuarto</li><li>Quinto</li></ul>Texto después de la lista.<br/>Siguiente línea<br/>Última línea</body>`");
// Añadir página en la colección de páginas
Page page = doc.Pages.Add();
// Añadir HtmlFragment dentro de la página
page.Paragraphs.Add(t);
// Guardar el archivo PDF resultante
doc.Save(outFile);
```

También puedes configurar el formato de cadena HTML usando el objeto TextState como se muestra a continuación:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("algún texto");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
En caso de que establezca algunos valores de atributos de texto a través de marcado HTML y luego proporcione los mismos valores en las propiedades de TextState, estos sobrescribirán los parámetros HTML por propiedades del instancia de TextState. Los siguientes fragmentos de código muestran el comportamiento descrito.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instanciar objeto Document
Document doc = new Document();
// Agregar una página a la colección de páginas del archivo PDF
Page page = doc.Pages.Add();
// Instanciar HtmlFragment con contenidos HTML
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>La tabla contiene texto</i></b></p>");
// La fuente 'Verdana' se restablecerá a 'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// Establecer información del margen inferior
title.Margin.Bottom = 10;
// Establecer información del margen superior
title.Margin.Top = 400;
// Agregar fragmento HTML a la colección de párrafos de la página
page.Paragraphs.Add(title);
// Guardar archivo PDF
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// Guardar archivo PDF
doc.Save(dataDir);
```
## Notas al pie y notas finales (DOM)

Las notas al pie indican notas en el texto de su documento utilizando números en superíndice consecutivos. La nota real está sangrada y puede aparecer como una nota al pie en la parte inferior de la página.

### Agregar una Nota al pie

En un sistema de referencias con notas al pie, indique una referencia:

- colocando un número pequeño sobre la línea de texto justo después del material fuente. Este número se llama identificador de nota. Se sitúa ligeramente por encima de la línea de texto.
- colocando el mismo número, seguido de una cita de su fuente, en la parte inferior de la página. Las notas al pie deben ser numéricas y cronológicas: la primera referencia es 1, la segunda es 2, y así sucesivamente.

La ventaja de usar notas al pie es que el lector puede simplemente bajar la vista hacia la página para descubrir la fuente de una referencia que le interese.

Por favor, siga los pasos especificados a continuación para crear una Nota al pie:

- Cree una instancia de Documento
- Cree un objeto Página
- Cree un objeto Fragmento de Texto
- Cree una instancia de Nota y pase su valor a la propiedad TextFragment.FootNote
- Crear una instancia de Note y pasar su valor a la propiedad TextFragment.FootNote
- Añadir TextFragment a la colección de párrafos de una instancia de página

### Estilo de línea personalizado para FootNote

El siguiente ejemplo demuestra cómo añadir Footnotes al final de la página Pdf y definir un estilo de línea personalizado.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear instancia de Document
Document doc = new Document();
// Añadir página a la colección de páginas del PDF
Page page = doc.Pages.Add();
// Crear objeto GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Establecer el ancho de línea como 2
graph.LineWidth = 2;
// Establecer el color para el objeto gráfico
graph.Color = Aspose.Pdf.Color.Red;
// Establecer el valor de la matriz de guiones como 3
graph.DashArray = new int[] { 3 };
// Establecer el valor de fase de guión como 1
graph.DashPhase = 1;
// Establecer el estilo de línea de la nota al pie para la página como gráfico
page.NoteLineStyle = graph;
// Crear instancia de TextFragment
TextFragment text = new TextFragment("Hello World");
// Establecer el valor de FootNote para TextFragment
text.FootNote = new Note("foot note for test text 1");
// Añadir TextFragment a la colección de párrafos de la primera página del documento
page.Paragraphs.Add(text);
// Crear segundo TextFragment
text = new TextFragment("Aspose.Pdf for .NET");
// Establecer FootNote para el segundo fragmento de texto
text.FootNote = new Note("foot note for test text 2");
// Añadir el segundo fragmento de texto a la colección de párrafos del archivo PDF
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// Guardar el documento PDF resultante.
doc.Save(dataDir);
```
Podemos configurar el formato del identificador de la nota al pie (etiqueta de nota al pie) utilizando el objeto TextState de la siguiente manera:

```csharp
TextFragment text = new TextFragment("texto de prueba 1");
text.FootNote = new Note("nota al pie para texto de prueba 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### Personalizar la etiqueta de la nota al pie

Por defecto, el número de FootNote es incremental comenzando desde 1. Sin embargo, podemos tener el requisito de establecer una etiqueta de FootNote personalizada. Para lograr este requisito, intente usar el siguiente fragmento de código

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear instancia de Documento
Document doc = new Document();
// Agregar página a la colección de páginas de PDF
Page page = doc.Pages.Add();
// Crear objeto GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Establecer el ancho de línea como 2
graph.LineWidth = 2;
// Establecer el color para el objeto gráfico
graph.Color = Aspose.Pdf.Color.Red;
// Establecer el valor del array de guiones como 3
graph.DashArray = new int[] { 3 };
// Establecer el valor de la fase de guiones como 1
graph.DashPhase = 1;
// Establecer el estilo de línea de la nota al pie para la página como gráfico
page.NoteLineStyle = graph;
// Crear instancia de TextFragment
TextFragment text = new TextFragment("Hola Mundo");
// Establecer el valor de FootNote para TextFragment
text.FootNote = new Note("nota al pie para texto de prueba 1");
// Especificar etiqueta personalizada para FootNote
text.FootNote.Text = " Aspose(2015)";
// Agregar TextFragment a la colección de párrafos de la primera página del documento
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## Añadiendo Imagen y Tabla a la Nota al Pie

En versiones anteriores, el soporte para Notas al Pie estaba disponible pero solo era aplicable al objeto TextFragment. Sin embargo, a partir de la versión Aspose.PDF para .NET 10.7.0, también puedes añadir Notas al Pie a otros objetos dentro del documento PDF como Tablas, Celdas, etc. El siguiente fragmento de código muestra los pasos para añadir una Nota al Pie al objeto TextFragment y luego añadir objetos de Imagen y Tabla a la colección de párrafos de la sección de Nota al Pie.

```csharp

// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("algún texto");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("texto de la nota al pie");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Fila 1 Celda 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// Guardar el documento PDF resultante.
doc.Save(dataDir);
```
## Cómo Crear Notas al Final

Una Nota al Final es una cita de fuente que remite a los lectores a un lugar específico al final del documento donde pueden averiguar la fuente de la información o palabras citadas o mencionadas en el documento. Cuando se utilizan notas al final, la frase citada o parafraseada o el material resumido es seguido por un número en superíndice.

El siguiente ejemplo demuestra cómo añadir una Nota al Final en la página de un PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear una instancia de Documento
Document doc = new Document();
// Añadir página a la colección de páginas del PDF
Page page = doc.Pages.Add();
// Crear instancia de TextFragment
TextFragment text = new TextFragment("Hola Mundo");
// Establecer valor de FootNote para TextFragment
text.EndNote = new Note("nota al final de ejemplo");
// Especificar etiqueta personalizada para FootNote
text.EndNote.Text = " Aspose(2015)";
// Añadir TextFragment a la colección de párrafos de la primera página del documento
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// Guardar el documento PDF resultante.
doc.Save(dataDir);
```
## Texto e Imagen como Párrafos en Línea

El diseño predeterminado del archivo PDF es de flujo (de Arriba-Izquierda a Abajo-Derecha). Por lo tanto, cada nuevo elemento que se añade al archivo PDF se añade en el flujo inferior derecho. Sin embargo, podemos tener la necesidad de mostrar varios elementos de la página, es decir, Imagen y Texto al mismo nivel (uno tras otro). Un enfoque puede ser crear una instancia de Tabla y añadir ambos elementos a objetos de celda individuales. Sin embargo, otro enfoque puede ser el párrafo en línea. Al establecer la propiedad IsInLineParagraph de Imagen y Texto como verdadero, estos párrafos aparecerán en línea con otros elementos de la página.

El siguiente fragmento de código te muestra cómo añadir texto e Imagen como párrafos en línea en el archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instancia de Documento
Document doc = new Document();
// Añadir página a la colección de páginas de la instancia de Documento
Page page = doc.Pages.Add();
// Crear Fragmento de Texto
TextFragment text = new TextFragment("Hello World.. ");
// Añadir fragmento de texto a la colección de párrafos del objeto Página
page.Paragraphs.Add(text);
// Crear una instancia de imagen
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// Establecer la imagen como párrafo en línea para que aparezca justo después
// Del objeto de párrafo anterior (Fragmento de Texto)
image.IsInLineParagraph = true;
// Especificar ruta del archivo de imagen
image.File = dataDir + "aspose-logo.jpg";
// Establecer la altura de la imagen (opcional)
image.FixHeight = 30;
// Establecer el ancho de la imagen (opcional)
image.FixWidth = 100;
// Añadir imagen a la colección de párrafos del objeto de página
page.Paragraphs.Add(image);
// Re-inicializar el objeto Fragmento de Texto con diferentes contenidos
text = new TextFragment(" Hello Again..");
// Establecer Fragmento de Texto como párrafo en línea
text.IsInLineParagraph = true;
// Añadir el Fragmento de Texto recién creado a la colección de párrafos de la página
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## Especificar el espaciado de caracteres al agregar texto

Un texto puede ser agregado dentro de la colección de párrafos de archivos PDF utilizando la instancia TextFragment o mediante el objeto TextParagraph e incluso puedes estampar el texto dentro del PDF usando la clase TextStamp. Al agregar el texto, podemos tener el requisito de especificar el espaciado de caracteres para los objetos de texto. Para lograr este requisito, se ha introducido una nueva propiedad llamada propiedad CharacterSpacing. Por favor, echa un vistazo a los siguientes enfoques para cumplir con este requisito.

Los siguientes enfoques muestran los pasos para especificar el espaciado de caracteres al agregar texto dentro de un documento PDF.

### Usando TextBuilder y TextFragment

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear instancia de Document
Document pdfDocument = new Document();
// Añadir página a la colección de páginas de Document
Page page = pdfDocument.Pages.Add();
// Crear instancia de TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Crear instancia de fragmento de texto con contenidos de muestra
TextFragment wideFragment = new TextFragment("Texto con espaciado de caracteres aumentado");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// Especificar el espaciado de caracteres para TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// Especificar la posición de TextFragment
wideFragment.Position = new Position(100, 650);
// Añadir TextFragment a la instancia de TextBuilder
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
### Usando TextParagraph

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear instancia de Document
Document pdfDocument = new Document();
// Agregar página a la colección de páginas del Documento
Page page = pdfDocument.Pages.Add();
// Crear instancia de TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Instanciar TextParagraph
TextParagraph paragraph = new TextParagraph();
// Crear instancia de TextState para especificar el nombre y tamaño de la fuente
TextState state = new TextState("Arial", 12);
// Especificar el espaciado de caracteres
state.CharacterSpacing = 1.5f;
// Agregar texto al objeto TextParagraph
paragraph.AppendLine("Este es un párrafo con espaciado de caracteres", state);
// Especificar la posición para TextParagraph
paragraph.Position = new Position(100, 550);
// Agregar TextParagraph a la instancia de TextBuilder
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
### Usando TextStamp

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear instancia de Document
Document pdfDocument = new Document();
// Agregar página a la colección de páginas del Documento
Page page = pdfDocument.Pages.Add();
// Instanciar TextStamp con texto de muestra
TextStamp stamp = new TextStamp("Este es un sello de texto con espaciado de caracteres");
// Especificar el nombre de la fuente para el objeto Stamp
stamp.TextState.Font = FontRepository.FindFont("Arial");
// Especificar el tamaño de la fuente para TextStamp
stamp.TextState.FontSize = 12;
// Especificar el espaciado de caracteres como 1f
stamp.TextState.CharacterSpacing = 1f;
// Establecer el XIndent para Stamp
stamp.XIndent = 100;
// Establecer el YIndent para Stamp
stamp.YIndent = 500;
// Agregar sello de texto a la instancia de página
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Crear documento PDF de múltiples columnas

En revistas y periódicos, generalmente vemos que las noticias se muestran en múltiples columnas en las páginas individuales en lugar de los libros donde los párrafos de texto se imprimen mayormente en toda la página de izquierda a derecha. Muchas aplicaciones de procesamiento de documentos como Microsoft Word y Adobe Acrobat Writer permiten a los usuarios crear múltiples columnas en una sola página y luego agregar datos a ellas.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) también ofrece la característica de crear múltiples columnas dentro de las páginas de documentos PDF.
[Aspose.PDF para .NET](https://docs.aspose.com/pdf/net/) también ofrece la funcionalidad de crear múltiples columnas dentro de las páginas de documentos PDF.

El espaciado entre columnas significa el espacio entre las columnas y el espaciado predeterminado entre las columnas es de 1.25cm. Si no se especifica el ancho de la columna, entonces [Aspose.PDF para .NET](https://docs.aspose.com/pdf/net/) calcula automáticamente el ancho de cada columna de acuerdo al tamaño de la página y el espaciado entre columnas.

A continuación se ofrece un ejemplo para demostrar la creación de dos columnas con objetos Gráficos (Línea) y estos se añaden a la colección de párrafos de FloatingBox, que luego se añade a la colección de párrafos de una instancia de Página.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// Especifique la información del margen izquierdo para el archivo PDF
doc.PageInfo.Margin.Left = 40;
// Especifique la información del margen derecho para el archivo PDF
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// Añadir la línea a la colección de párrafos del objeto de sección
page.Paragraphs.Add(graph1);

// Especifique las coordenadas para la línea
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// Crear variables de cadena con texto que contiene etiquetas html

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> Cómo evitar estafas de dinero</<strong> "
+ "</font>";
// Crear párrafos de texto que contienen texto HTML

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// Añadir cuatro columnas en la sección
box.ColumnInfo.ColumnCount = 2;
// Establecer el espaciado entre las columnas
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("Por A Googler (El Blog Oficial de Google)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// Crear un objeto gráficos para dibujar una línea
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// Especificar las coordenadas para la línea
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// Añadir la línea a la colección de párrafos del objeto de sección
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// Guardar el archivo PDF
doc.Save(dataDir);
```
## Trabajando con Tabuladores personalizados

Un Tabulador es un punto de detención para el tabulado. En el procesamiento de texto, cada línea contiene una serie de tabuladores colocados a intervalos regulares (por ejemplo, cada media pulgada). Sin embargo, pueden ser modificados, ya que la mayoría de los procesadores de texto permiten establecer tabuladores donde desee. Cuando presiona la tecla Tab, el cursor o punto de inserción salta al siguiente tabulador, que en sí mismo es invisible. Aunque los tabuladores no existen en el archivo de texto, el procesador de texto hace un seguimiento de ellos para poder reaccionar correctamente a la tecla Tab.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) permite a los desarrolladores utilizar tabuladores personalizados en documentos PDF. La clase Aspose.Pdf.Text.TabStop se utiliza para establecer tabuladores personalizados en la clase [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) también ofrece algunos tipos de guías de tabulación predefinidos como una enumeración llamada, TabLeaderType cuyos valores predefinidos y sus descripciones se dan a continuación:
[Aspose.PDF para .NET](https://docs.aspose.com/pdf/net/) también ofrece algunos tipos predefinidos de líderes de tabulación como una enumeración llamada, TabLeaderType cuyos valores predefinidos y sus descripciones se detallan a continuación:

|**Tipo de Líder de Tabulación**|**Descripción**|
| :- | :- |
|None|Sin líder de tabulación|
|Solid|Líder de tabulación sólido|
|Dash|Líder de tabulación de guiones|
|Dot|Líder de tabulación de puntos|

Aquí hay un ejemplo de cómo configurar detenciones de TAB personalizadas.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("Este es un ejemplo de formación de tabla con detenciones de TAB", ts);
TextFragment text0 = new TextFragment("#$TABEncabezado1 #$TABEncabezado2 #$TABEncabezado3", ts);

TextFragment text1 = new TextFragment("#$TABdato11 #$TABdato12 #$TABdato13", ts);
TextFragment text2 = new TextFragment("#$TABdato21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("dato22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("dato23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## Cómo Agregar Texto Transparente en PDF

Un archivo PDF contiene objetos de Imagen, Texto, Gráfico, adjunto, Anotaciones y al crear TextFragment, puedes establecer información de color de fondo y de primer plano, así como formato de texto. Aspose.PDF para .NET soporta la característica de agregar texto con canal de color Alfa. El siguiente fragmento de código muestra cómo agregar texto con color transparente.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear instancia de Documento
Document doc = new Document();
// Crear página para la colección de páginas del archivo PDF
Aspose.Pdf.Page page = doc.Pages.Add();

// Crear objeto Graph
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Crear instancia de rectángulo con ciertas dimensiones
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// Crear objeto de color desde el canal de color Alfa
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Añadir rectángulo a la colección de formas del objeto Graph
canvas.Shapes.Add(rect);
// Añadir objeto graph a la colección de párrafos del objeto de página
page.Paragraphs.Add(canvas);
// Establecer valor para no cambiar la posición para el objeto graph
canvas.IsChangePosition = false;

// Crear instancia de TextFragment con valor de muestra
TextFragment text = new TextFragment("texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente ");
// Crear objeto de color desde el canal Alfa
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// Establecer información de color para la instancia de texto
text.TextState.ForegroundColor = color;
// Añadir texto a la colección de párrafos de la instancia de página
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## Especificar el Interlineado para Fuentes

Cada fuente tiene un cuadro abstracto, cuya altura es la distancia prevista entre líneas del mismo tamaño de tipo.
Cada fuente tiene un cuadrado abstracto, cuya altura es la distancia prevista entre líneas de texto del mismo tamaño de fuente.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// Cargar archivo PDF de entrada
Document doc = new Document();
//Crear TextFormattingOptions con LineSpacingMode.FullSize
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// Crear objeto constructor de texto para la primera página del documento
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Crear fragmento de texto con cadena de ejemplo
TextFragment textFragment = new TextFragment("Hola mundo");

if (fontFile != "")
{
    // Cargar la fuente TrueType en el objeto de flujo
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // Establecer el nombre de la fuente para la cadena de texto
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Especificar la posición para el Fragmento de Texto
        textFragment.Position = new Position(100, 600);
        //Establecer TextFormattingOptions del fragmento actual a predefinido(que apunta a LineSpacingMode.FullSize)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // Agregar el texto al TextBuilder para que pueda ser colocado sobre el archivo PDF
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // Guardar el documento PDF resultante
    doc.Save(dataDir);
}
```
## Obtener el Ancho del Texto Dinámicamente

A veces, es necesario obtener el ancho del texto de manera dinámica. Aspose.PDF para .NET incluye dos métodos para la medición del ancho de las cadenas. Puedes invocar el método [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) de las clases Aspose.Pdf.Text.Font o Aspose.Pdf.Text.TextState (o ambas). El fragmento de código a continuación muestra cómo usar esta funcionalidad.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("¡Medida de cadena de fuente inesperada!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("¡Medida de cadena de fuente inesperada!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("¡La medición de la cadena de fuente y estado no coincide!");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

