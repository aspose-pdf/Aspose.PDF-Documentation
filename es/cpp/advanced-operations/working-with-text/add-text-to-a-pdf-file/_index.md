---
title: Añadir Texto a PDF usando C++
linktitle: Añadir Texto a PDF
type: docs
weight: 10
url: /es/cpp/add-text-to-pdf-file/
description: Este artículo describe varios aspectos del trabajo con texto en Aspose.PDF. Aprenda cómo añadir texto a PDF, añadir fragmentos HTML o usar fuentes OTF personalizadas.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadiendo Texto

Para añadir texto a un archivo PDF existente:

1. Abra el PDF de entrada usando el objeto Document.
2. Obtenga la página específica a la que desea añadir el texto.
3. Cree un objeto TextFragment con el texto de entrada junto con otras propiedades de texto. El objeto TextBuilder creado a partir de esa página específica, a la que desea añadir el texto, le permite añadir el objeto TextFragment a la página utilizando el método AppendText.
4. Llame al método Save del objeto Document y guarde el archivo PDF de salida.

El siguiente fragmento de código le muestra cómo añadir texto en un archivo PDF existente.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String para nombre de archivo de entrada
    String inputFileName("sample.pdf");
    // String para nombre de archivo de salida
    String outputFileName("AddingText_out.pdf");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // obtener página particular
    auto pdfPage = document->get_Pages()->idx_get(1);

    // crear fragmento de texto
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // establecer propiedades de texto
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // crear objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // añadir el fragmento de texto a la página PDF
    textBuilder->AppendText(textFragment);

    // Guardar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Cargando Fuente desde Stream

El siguiente fragmento de código muestra cómo cargar una fuente desde un objeto Stream al agregar texto a un documento PDF.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // Cargar archivo PDF de entrada
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear objeto de constructor de texto para la primera página del documento
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // Crear fragmento de texto con cadena de muestra
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // Cargar la fuente TrueType en el objeto stream
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // Establecer el nombre de la fuente para la cadena de texto
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // Especificar la posición para el fragmento de texto
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // Agregar el texto al TextBuilder para que pueda colocarse sobre el archivo PDF
        textBuilder->AppendText(textFragment);

        // Guardar el documento PDF resultante.
        document->Save(_dataDir + outputFileName);
    }
}
```

## Añadir Texto usando TextParagraph

El siguiente fragmento de código muestra cómo agregar texto en un documento PDF usando la clase [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // Add page to pages collection of Document object
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // Create text paragraph
    auto paragraph = MakeObject<TextParagraph>();

    // Set subsequent lines indent
    paragraph->set_SubsequentLinesIndent(20);

    // Specify the location to add TextParagraph
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // Specify word wraping mode
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // Create text fragment
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // Add fragment to paragraph
    paragraph->AppendLine(fragment1);
    // Add paragraph
    builder->AppendParagraph(paragraph);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}

```

## Añadir Hipervínculo a TextSegment

Una página PDF puede estar compuesta por uno o más objetos TextFragment, donde cada objeto TextFragment puede tener una o más instancias de TextSegment. Para establecer un hipervínculo para TextSegment, se puede usar la propiedad Hyperlink de la clase [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment) mientras se proporciona el objeto de la instancia Aspose.Pdf.WebHyperlink. Por favor, intente usar el siguiente fragmento de código para lograr este requisito.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // Crear instancia de documento
    auto document = MakeObject<Document>();

    // Añadir página a la colección de páginas del archivo PDF
    auto page1 = document->get_Pages()->Add();

    // Crear instancia de TextFragment
    auto tf = MakeObject<TextFragment>("Fragmento de Texto de Muestra");
    // Establecer alineación horizontal para TextFragment
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // Crear un textsegment con texto de muestra
    auto segment = MakeObject<TextSegment>(" ... Segmento de Texto 1...");
    // Añadir segmento a la colección de segmentos de TextFragment
    tf->get_Segments()->Add(segment);

    // Crear un nuevo TextSegment
    segment = MakeObject<TextSegment>("Enlace a Google");
    // Añadir segmento a la colección de segmentos de TextFragment

    tf->get_Segments()->Add(segment);

    // Establecer hipervínculo para TextSegment
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // Establecer color de primer plano para el segmento de texto
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // Establecer formato de texto como cursiva
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // Crear otro objeto TextSegment
    segment = MakeObject<TextSegment>(u"Segmento de Texto sin hipervínculo");

    // Añadir segmento a la colección de segmentos de TextFragment
    tf->get_Segments()->Add(segment);

    // Añadir TextFragment a la colección de párrafos del objeto página
    page1->get_Paragraphs()->Add(tf);

    // Guardar documento PDF resultante.
    document->Save(_dataDir + outputFileName);

}
```

## Usar Fuente OTF

Aspose.PDF para C++ ofrece la característica de usar fuentes Personalizadas/TrueType al crear/manipular contenidos de archivos PDF para que los contenidos del archivo se muestren usando fuentes distintas a las fuentes predeterminadas del sistema.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // Crear una nueva instancia de documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear instancia de TextFragment con texto de ejemplo
    auto fragment = MakeObject<TextFragment>("Texto de ejemplo en fuente OTF");

    // O incluso puedes especificar la ruta de la fuente OTF en el directorio del sistema
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // Especificar incrustar la fuente dentro del archivo PDF, para que se muestre correctamente,
    // Incluso si la fuente específica no está instalada/presente en la máquina de destino
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // Agregar TextFragment a la colección de párrafos de la instancia de Página
    page->get_Paragraphs()->Add(fragment);
    // Guardar el documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Añadir Cadena HTML usando DOM

La clase Aspose.Pdf.Generator.Text contiene una propiedad llamada IsHtmlTagSupported que hace posible agregar etiquetas/contenidos HTML en archivos PDF. El contenido añadido se representa en etiquetas HTML nativas en lugar de aparecer como una simple cadena de texto. Para soportar una característica similar en el nuevo Modelo de Objetos de Documento (DOM) del espacio de nombres Aspose.Pdf, se ha introducido la clase HtmlFragment.

La instancia [HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) puede ser utilizada para especificar los contenidos HTML que deben colocarse dentro del archivo PDF. Similar a TextFragment, HtmlFragment es un objeto de nivel de párrafo y puede ser añadido a la colección de párrafos del objeto Page. Los siguientes fragmentos de código muestran los pasos para colocar contenidos HTML dentro del archivo PDF usando el enfoque DOM.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String inputFileName("sample.pdf");

    // Cadena para el nombre del archivo de salida
    String outputFileName("sample_html_out.pdf");

    // crear instancia de Document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Añadir una página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Instanciar HtmlFragment con contenidos HTML
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // establecer MarginInfo para detalles de margen
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Establecer información de margen
    title->set_Margin(margin);

    // Añadir Fragmento HTML a la colección de párrafos de la página
    page->get_Paragraphs()->Add(title);
    // Guardar archivo PDF
    document->Save(_dataDir + outputFileName);
}
```

El siguiente fragmento de código demuestra los pasos para agregar listas ordenadas HTML en el documento:

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de salida
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>();

    // Instanciar objeto HtmlFragment con el fragmento HTML correspondiente
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Agregar Página en la Colección de Páginas
    auto page = document->get_Pages()->Add();

    // Agregar HtmlFragment dentro de la página
    page->get_Paragraphs()->Add(htmlFragment);

    // Guardar archivo PDF resultante
    document->Save(_dataDir + outputFileName);
}
```

También puedes configurar el formato de cadena HTML usando el objeto TextState de la siguiente manera:

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de salida
    String outputFileName("sample_html_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>();

    // Agregar Página en la Colección de Páginas
    auto page = document->get_Pages()->Add();

    // Instanciar HtmlFragment con contenido HTML
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // Agregar Fragmento HTML a la colección de párrafos de la página
    page->get_Paragraphs()->Add(title);
    // Guardar archivo PDF
    document->Save(_dataDir + outputFileName);
}
```

En caso de que establezca algunos valores de atributos de texto a través de la marca HTML y luego proporcione los mismos valores en las propiedades de TextState, estas sobrescribirán los parámetros HTML mediante las propiedades del formulario de la instancia de TextState. Los siguientes fragmentos de código muestran el comportamiento descrito.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // String para el nombre del archivo de salida
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>();

    // Agregar página en la colección de páginas
    auto page = document->get_Pages()->Add();

    // Instanciar HtmlFragment con contenido HTML
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>La tabla contiene texto</i></b></p>");

    // La fuente 'Verdana' se restablecerá a 'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // Establecer información del margen inferior
    title->get_Margin()->set_Bottom(10);
    // Establecer información del margen superior
    title->get_Margin()->set_Top(400);
    // Agregar fragmento HTML a la colección de párrafos de la página
    page->get_Paragraphs()->Add(title);
    // Guardar archivo PDF
    document->Save(_dataDir + outputFileName);
}
```

## FootNotes and EndNotes (DOM)

FootNotes indican notas en el texto de su documento utilizando números superíndice consecutivos. La nota real está indentada y puede aparecer como una nota al pie al final de la página.

### Adding FootNote

En un sistema de referencia con nota al pie, indique una referencia mediante:

- colocando un número pequeño por encima de la línea de texto directamente después del material de origen. Este número se llama identificador de nota. Se sitúa ligeramente por encima de la línea de texto.
- colocando el mismo número, seguido de una cita de su fuente, al final de la página. La numeración de las notas al pie debe ser numérica y cronológica: la primera referencia es 1, la segunda es 2, y así sucesivamente.

La ventaja de las notas al pie es que el lector puede simplemente bajar la mirada por la página para descubrir la fuente de una referencia que les interese.

Siga los siguientes pasos:

- Crear una instancia de [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
- Crear un objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)

- Crear un objeto [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)
- Crear una instancia de Note y pasar su valor a la propiedad TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219)
- Agregar TextFragment a la colección de párrafos de una instancia de página

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Agregar Página en la Colección de Páginas
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // crear instancia de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // establecer valor de FootNote para TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // agregar TextFragment a la colección de párrafos de la primera página del documento
    page->get_Paragraphs()->Add(text);
    // crear segundo TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // establecer FootNote para el segundo fragmento de texto
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // agregar segundo fragmento de texto a la colección de párrafos del archivo PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Estilo de línea personalizado para nota al pie

El siguiente ejemplo demuestra cómo agregar notas al pie en la parte inferior de la página de PDF y definir un estilo de línea personalizado.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de salida    
    String outputFileName("customFootNote_Line.pdf");

    // Crear instancia de Document
    auto document = MakeObject<Document>();

    // agregar página a la colección de páginas del PDF
    auto page = document->get_Pages()->Add();
    
    // crear objeto GraphInfo
    auto graph = MakeObject<GraphInfo>();
    // establecer el ancho de línea como 2
    graph->set_LineWidth(2);
    // establecer el color para el objeto graph
    graph->set_Color(Color::get_Red());
    // establecer el valor del array de guiones como 3
    graph->set_DashArray(MakeArray<int>(3));
    // establecer el valor fase de guiones como 1
    graph->set_DashPhase(1);
    // establecer el estilo de línea de la nota al pie para la página como graph
    page->set_NoteLineStyle(graph);

    // crear instancia de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // establecer el valor de la nota al pie para TextFragment
    text->set_FootNote(MakeObject<Note>("nota al pie para texto de prueba 1"));
    // agregar TextFragment a la colección de párrafos de la primera página del documento
    page->get_Paragraphs()->Add(text);
    // crear segundo TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // establecer nota al pie para el segundo fragmento de texto
    text->set_FootNote(MakeObject<Note>("nota al pie para texto de prueba 2"));
    // agregar segundo fragmento de texto a la colección de párrafos del archivo PDF
    page->get_Paragraphs()->Add(text);
    // guardar el archivo PDF
    document->Save(_dataDir + outputFileName);
}
```

Podemos establecer el formato de la Etiqueta de Nota al Pie (identificador de nota) usando el objeto TextState de la siguiente manera:

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada    
    String inputFileName("sample.pdf");

    // String para el nombre del archivo de salida    
    String outputFileName("sample_footnote.pdf");

    // Crear instancia de Documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // crear instancia de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // establecer valor de Nota al Pie para TextFragment
    text->set_FootNote(MakeObject<Note>("nota al pie para texto de prueba 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // añadir TextFragment a la colección de párrafos de la primera página del documento
    page->get_Paragraphs()->Add(text);
    // crear segundo TextFragment
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // establecer Nota al Pie para el segundo fragmento de texto
    text->set_FootNote(MakeObject<Note>("nota al pie para texto de prueba 2"));
    // añadir segundo fragmento de texto a la colección de párrafos del archivo PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Personalizar etiqueta de pie de nota

Por defecto, el número de pie de nota es incremental comenzando desde 1. Sin embargo, podemos tener un requisito para establecer una etiqueta de pie de nota personalizada. Para cumplir con este requisito, intente usar el siguiente fragmento de código

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // String para el nombre del archivo de salida    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Crear instancia de Documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto GraphInfo
    auto graph = MakeObject<GraphInfo>();

    // Establecer el ancho de línea como 2
    graph->set_LineWidth(2);

    // Establecer el color para el objeto gráfico
    graph->set_Color(Color::get_Red());

    // Establecer el valor del array de guiones como 3
    graph->set_DashArray(MakeArray<int>(3));

    // Establecer el valor de la fase de guiones como 1
    graph->set_DashPhase(1);

    // Establecer el estilo de línea de pie de nota para la página como gráfico
    page->set_NoteLineStyle(graph);

    // Crear instancia de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // Establecer valor de pie de nota para TextFragment
    text->set_FootNote(MakeObject<Note>("nota al pie para texto de prueba 1"));
    // Especificar etiqueta personalizada para el pie de nota
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // Agregar TextFragment a la colección de párrafos de la primera página del documento
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Agregar Imagen y Tabla a la Nota al Pie

El siguiente fragmento de código muestra los pasos para agregar [Nota al Pie](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722) al objeto [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) y luego agregar objeto Imagen y Tabla a la colección de párrafos de la sección de Nota al Pie.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de salida    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Crear instancia de Document
    auto document = new Document();
    // Agregar página a la colección de páginas del PDF
    auto page = document->get_Pages()->Add();

    // Crear instancia de TextFragment
    auto text = MakeObject<TextFragment>("Hola Mundo");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("texto de nota al pie");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Fila 1 Celda 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Cómo Crear Notas Finales

Una Nota Final es una cita de fuente que remite a los lectores a un lugar específico al final del documento donde pueden encontrar la fuente de la información o las palabras citadas o mencionadas en el documento. Al usar notas finales, tu oración citada o parafraseada o el material resumido es seguido por un número en superíndice.

El siguiente ejemplo demuestra cómo agregar una Nota Final en la página Pdf.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida    
    String outputFileName("endNote_out.pdf");

    // Crear instancia de Documento
    auto document = new Document();
    // Añadir página a la colección de páginas del PDF
    auto page = document->get_Pages()->Add();

    // crear instancia de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    // establecer valor de FootNote para TextFragment
    text->set_EndNote(MakeObject<Note>("sample End note"));

    // especificar etiqueta personalizada para FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // añadir TextFragment a la colección de párrafos de la primera página del documento
    page->get_Paragraphs()->Add(text);
    // guardar el archivo PDF
    document->Save(_dataDir + outputFileName);
}
```

## Texto e Imagen como Párrafo en Línea

El diseño predeterminado del archivo PDF es un diseño de flujo (de arriba a la izquierda a abajo a la derecha). Por lo tanto, cada nuevo elemento que se agrega al archivo PDF se añade en el flujo de la parte inferior derecha. Sin embargo, podemos tener un requisito para mostrar varios elementos de la página, es decir, Imagen y Texto al mismo nivel (uno tras otro). Un enfoque puede ser crear una instancia de Tabla y agregar ambos elementos a objetos de celda individuales. Sin embargo, otro enfoque puede ser el párrafo en línea. Al configurar la propiedad IsInLineParagraph de Imagen y Texto como verdadera, estos párrafos aparecerán en línea con otros elementos de la página.

El siguiente fragmento de código te muestra cómo agregar texto e Imagen como párrafos en línea en un archivo PDF.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Instanciar la instancia de Documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas de la instancia de Documento
    auto page = document->get_Pages()->Add();

    // Crear TextFragment
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // Agregar fragmento de texto a la colección de párrafos del objeto Page
    page->get_Paragraphs()->Add(text);

    // Crear una instancia de imagen
    auto image = MakeObject<Image>();

    // Configurar imagen como párrafo en línea para que aparezca justo después
    // Del objeto de párrafo anterior (TextFragment)
    image->set_IsInLineParagraph(true);

    // Especificar la ruta del archivo de imagen
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // Establecer la altura de la imagen (opcional)
    image->set_FixHeight(30);
    // Establecer el ancho de la imagen (opcional)
    image->set_FixWidth(100);
    // Agregar imagen a la colección de párrafos del objeto de página
    page->get_Paragraphs()->Add(image);
    // Re-inicializar el objeto TextFragment con diferentes contenidos
    text = MakeObject<TextFragment>(" Hello Again..");
    // Configurar TextFragment como párrafo en línea
    text->set_IsInLineParagraph(true);
    // Agregar el TextFragment recién creado a la colección de párrafos de la página
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Especificar el Espaciado de Caracteres al Agregar Texto

El texto se puede agregar a la colección de párrafos de un PDF usando una instancia de TextFragment o un objeto TextParagraph, e incluso se puede estampar texto dentro de un PDF usando la clase TextStamp. Al agregar texto, es posible que debamos especificar el espaciado entre caracteres para los objetos de texto. Para cumplir con este requisito, se ha introducido una nueva propiedad llamada CharacterSpacing.

Considere los siguientes enfoques para cumplir con este requisito.

Los siguientes enfoques muestran los pasos para especificar el espaciado de caracteres al agregar texto dentro de un documento PDF.

### Usando TextBuilder y TextFragment

```cpp
// Especificar el Espaciado de Caracteres al agregar Texto usando TextBuilder y TextFragment
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Crear una instancia de Document
    auto document = MakeObject<Document>();
    // Agregar página a la colección de páginas del Documento
    auto page = document->get_Pages()->Add();

    // Crear una instancia de TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Crear una instancia de fragmento de texto con contenido de muestra
    auto wideFragment = MakeObject<TextFragment>("Texto con espaciado de caracteres aumentado");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // Especificar el espaciado de caracteres para TextFragment
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // Especificar la posición de TextFragment
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // Añadir TextFragment a la instancia de TextBuilder
    builder->AppendText(wideFragment);

    // Guardar el documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

### Usando TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Crear una instancia de Document
    auto document = MakeObject<Document>();

    // Añadir una página a la colección de páginas del Documento
    auto page = document->get_Pages()->Add();

    // Crear una instancia de TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Instanciar una instancia de TextParagraph
    auto paragraph = MakeObject<TextParagraph>();

    // Crear una instancia de TextState para especificar el nombre y tamaño de la fuente
    auto state = MakeObject<TextState>("Arial", 12);

    // Especificar el espaciado entre caracteres
    state->set_CharacterSpacing(1.5f);

    // Añadir texto al objeto TextParagraph
    paragraph->AppendLine(u"Este es un párrafo con espaciado entre caracteres", state);

    // Especificar la posición para TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // Añadir TextParagraph a la instancia de TextBuilder
    builder->AppendParagraph(paragraph);

    // Guardar el documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

### Using TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Crear instancia de Documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del Documento    
    auto page = document->get_Pages()->Add();

    // Instanciar objeto TextStamp con texto de ejemplo
    auto stamp = MakeObject<TextStamp>("Este es un sello de texto con espaciado de caracteres");

    // Especificar nombre de fuente para el objeto Stamp
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // Especificar tamaño de fuente para TextStamp
    stamp->get_TextState()->set_FontSize(12);
    // Especificar espaciado de caracteres como 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // Establecer la XIndent para Stamp
    stamp->set_XIndent(100);
    // Establecer la YIndent para Stamp
    stamp->set_YIndent(500);
    // Añadir sello textual a la instancia de página
    stamp->Put(page);
    // Guardar el documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Crear documento PDF de múltiples columnas

Este tema muestra cómo puedes crear un PDF de múltiples columnas usando Aspose.Pdf para C++.

Hoy en día, a menudo vemos noticias mostradas en múltiples columnas en páginas separadas, en lugar de en libros, donde los párrafos de texto se imprimen principalmente en todas las páginas de izquierda a derecha. Muchas aplicaciones de procesamiento de documentos, como Microsoft Word y Adobe Acrobat Writer, permiten a los usuarios crear múltiples columnas en una sola página y luego agregar datos a ellas.

Aspose.Pdf para C++ también ofrece la capacidad de crear múltiples columnas en las páginas de documentos PDF. Para crear un PDF con múltiples columnas, podemos usar la clase [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) ya que proporciona una propiedad ColumnInfo.ColumnCount para especificar el número de columnas dentro de FloatingBox, y también podemos especificar el espaciado de columnas y los anchos de columnas usando ColumnInfo.ColumnSpacing y ColumnInfo.ColumnWidths respectivamente.

Se da un ejemplo a continuación para demostrar la creación de dos columnas con objetos de Gráficos (Línea) y se agregan a la colección de párrafos de FloatingBox, que luego se agrega a la colección de párrafos de la instancia de Página.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // Crear nueva instancia de documento
    auto document = MakeObject<Document>();

    // Especificar la información del margen izquierdo para el archivo PDF
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // Especificar la información del margen derecho para el archivo PDF
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // Agregar la línea a la colección de párrafos del objeto sección
    page->get_Paragraphs()->Add(graph1);

    // Especificar las coordenadas para la línea
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // Crear variables de cadena con texto que contiene etiquetas html
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> Cómo evitar las estafas de dinero</<strong> </span>");

    // Crear párrafos de texto que contienen texto HTML

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // Agregar cuatro columnas en la sección
    box->get_ColumnInfo()->set_ColumnCount(2);
    // Establecer el espacio entre las columnas
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("Por A Googler (El Blog Oficial de Google)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // Crear un objeto de gráficos para dibujar una línea
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // Especificar las coordenadas para la línea
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // Agregar la línea a la colección de párrafos del objeto sección
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // Guardar archivo PDF
    document->Save(_dataDir + outputFileName);
}
```

## Trabajando con tabulaciones personalizadas

Una tabulación es un punto de parada para tabular. En el procesamiento de texto, cada línea contiene una serie de tabulaciones colocadas a intervalos regulares (por ejemplo, cada media pulgada). Sin embargo, pueden ser cambiadas, ya que la mayoría de los procesadores de texto te permiten establecer tabulaciones donde quieras. Cuando presionas la tecla Tab, el cursor o punto de inserción salta a la siguiente tabulación, que en sí misma es invisible. Aunque las tabulaciones no existen en el archivo de texto, el procesador de texto las sigue para poder reaccionar correctamente a la tecla Tab.

Aquí hay un ejemplo de cómo establecer tabulaciones personalizadas.

```cpp
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("This is a example of forming table with TAB stops", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## Cómo Agregar Texto Transparente en PDF

PDF 1.4 (un formato de archivo compatible con Acrobat 5) fue la primera versión de PDF que admitió la transparencia. Este PDF salió al mercado al mismo tiempo que Adobe Illustrator 9.

Un archivo PDF contiene objetos de Imagen, Texto, Gráfico, adjunto y Anotaciones, y al crear TextFragment, puedes establecer información de color de primer plano, fondo, así como el formato de texto. Aspose.PDF para C++ admite la función de agregar texto con canal de color Alpha. El siguiente fragmento de código muestra cómo agregar texto con color transparente.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Crear instancia de Documento
    auto document = MakeObject<Document>();    
    // Crear página para la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto Gráfico
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Crear instancia de rectángulo con ciertas dimensiones
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Crear objeto de color desde el canal de color Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Agregar rectángulo a la colección de formas del objeto Gráfico
    canvas->get_Shapes()->Add(rect);

    // Agregar objeto gráfico a la colección de párrafos del objeto página
    page->get_Paragraphs()->Add(canvas);

    // Establecer valor para no cambiar la posición del objeto gráfico
    canvas->set_IsChangePosition(false);

    // Crear instancia de TextFragment con valor de ejemplo
    auto text = MakeObject<TextFragment>(
        "texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente ");
    // Crear objeto de color desde el canal Alpha
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Establecer información de color para la instancia de texto
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Agregar texto a la colección de párrafos de la instancia de página
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Especificar el Espaciado de Línea para Fuentes

La clase [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) tiene una enumeración [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91) que está diseñada para fuentes específicas, por ejemplo, la fuente de entrada "HPSimplified.ttf". También la clase [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) tiene una propiedad [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) del tipo LineSpacingMode. Solo necesitas establecer LineSpacing en LineSpacingMode.FullSize. El fragmento de código para obtener una fuente mostrada correctamente sería el siguiente:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // Cargar el archivo PDF de entrada
    auto document = MakeObject<Document>();
    
    // Crear TextFormattingOptions con LineSpacingMode.FullSize
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // Crear fragmento de texto con cadena de ejemplo
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // Cargar la fuente TrueType en el objeto de flujo
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // Establecer el nombre de la fuente para la cadena de texto
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // Especificar la posición para el Fragmento de Texto
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // Establecer TextFormattingOptions del fragmento actual al predefinido (que apunta a
    // LineSpacingMode.FullSize)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // Agregar el texto a TextBuilder para que pueda ser colocado sobre el archivo PDF    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // Guardar el documento PDF resultante
    document->Save(_dataDir + outputFileName);
}
```

## Obtener el Ancho del Texto Dinámicamente

La clase [Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) muestra cómo obtener el ancho del texto dinámicamente en un documento PDF.

A veces, es necesario obtener el ancho del texto de forma dinámica. Aspose.PDF para C++ incluye dos métodos para medir el ancho de una cadena. Puede invocar el método [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) de las clases Aspose.Pdf.Text.Font o Aspose.Pdf.Text.TextState (o ambos). El fragmento de código a continuación muestra cómo usar esta funcionalidad.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"¡Medida de cadena de fuente inesperada!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"¡Medida de cadena de fuente inesperada!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"¡La medición de la cadena de fuente y estado no coincide!");
    }
}
```