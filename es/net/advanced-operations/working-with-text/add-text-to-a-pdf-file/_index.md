---
title: Agregar texto a PDF usando C#
linktitle: Agregar texto a PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/add-text-to-pdf-file/
description: Aprenda cómo agregar texto a un documento PDF en .NET usando Aspose.PDF para mejorar el contenido y editar documentos.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text to PDF using C#",
    "alternativeHeadline": "Add Custom Text to Existing PDFs with C#",
    "abstract": "La función Agregar texto a PDF usando C# en Aspose.PDF permite a los desarrolladores integrar y manipular texto sin problemas dentro de documentos PDF existentes. Con capacidades como agregar fragmentos de texto, utilizar fuentes OTF personalizadas y agregar contenido HTML, esta funcionalidad mejora el formato y la presentación del documento, facilitando la creación de PDFs profesionales y personalizados programáticamente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "5625",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "dateModified": "2024-11-26",
    "description": "Este artículo describe varios aspectos de trabajar con texto en Aspose.PDF. Aprenda cómo agregar texto a PDF, agregar fragmentos HTML o usar fuentes OTF personalizadas."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Para agregar texto a un archivo PDF existente:

1. Abra el PDF de entrada usando el objeto Document.
2. Obtenga la página particular a la que desea agregar el texto.
3. Cree un objeto TextFragment con el texto de entrada junto con otras propiedades de texto. El objeto TextBuilder creado a partir de esa página particular – a la que desea agregar el texto – le permite agregar el objeto TextFragment a la página usando el método AppendText.
4. Llame al método Save del objeto Document y guarde el archivo PDF de salida.

## Agregar texto

El siguiente fragmento de código le muestra cómo agregar texto en un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();

        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddText_out.pdf");
    }
}
```

## Cargar fuente desde Stream

El siguiente fragmento de código muestra cómo cargar una fuente desde un objeto Stream al agregar texto a un documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LoadingFontFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    var fontFile = dataDir + "HPSimplified.ttf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "LoadFonts.pdf"))
    {
        // Create text builder object for first page of document
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (File.Exists(fontFile))
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(10, 10);
                // Add the text to TextBuilder so that it can be placed over the PDF file
                textBuilder.AppendText(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "LoadingFontFromStream_out.pdf");
        }
    }
}
```

## Agregar texto usando TextParagraph

El siguiente fragmento de código le muestra cómo agregar texto en un documento PDF usando la clase [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextWithTextParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document object
        var page = document.Pages.Add();
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Create text paragraph
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Set subsequent lines indent
        paragraph.SubsequentLinesIndent = 20;
        // Specify the location to add TextParagraph
        paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
        // Specify word wraping mode
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        // Create text fragment
        var fragment = new Aspose.Pdf.Text.TextFragment("the quick brown fox jumps over the lazy dog");
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        fragment.TextState.FontSize = 12;
        // Add fragment to paragraph
        paragraph.AppendLine(fragment);
        // Add paragraph
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "AddTextUsingTextParagraph_out.pdf");
    }
}
```

## Agregar hipervínculo a TextSegment

Una página PDF puede constar de uno o más objetos TextFragment, donde cada objeto TextFragment puede tener una o más instancias de TextSegment. Para establecer un hipervínculo para TextSegment, se puede usar la propiedad Hyperlink de la clase [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) mientras se proporciona el objeto de la instancia Aspose.Pdf.WebHyperlink. Intente usar el siguiente fragmento de código para lograr este requisito.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkToTextSegment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text Fragment");
        // Set horizontal alignment for TextFragment
        fragment.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        // Create a textsegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" ... Text Segment 1...");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Create a new TextSegment
        segment = new Aspose.Pdf.Text.TextSegment("Link to Google");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Set hyperlink for TextSegment
        segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
        // Set forground color for text segment
        segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
        // Set text formatting as italic
        segment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create another TextSegment object
        segment = new Aspose.Pdf.Text.TextSegment("TextSegment without hyperlink");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Add TextFragment to paragraphs collection of page object
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHyperlinkToTextSegment_out.pdf");
    }
}
```

## Usar fuente OTF

Aspose.PDF for .NET ofrece la función de usar fuentes personalizadas/TrueType al crear/manipular el contenido de archivos PDF para que el contenido del archivo se muestre utilizando contenidos distintos de las fuentes del sistema predeterminadas. Desde el lanzamiento de Aspose.PDF for .NET 10.3.0, hemos proporcionado soporte para fuentes Open Type.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UseOTFFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instnace with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text in OTF font");
        // Find font inside system font directory
        // Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
        // Or you can even specify the path of OTF font in system directory
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(dataDir + "space age.otf");
        // Specify to emend font inside PDF file, so that its displayed properly,
        // Even if specific font is not installed/present over target machine
        fragment.TextState.Font.IsEmbedded = true;
        // Add TextFragment to paragraphs collection of Page instance
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "OTFFont_out.pdf");
    }
}
```

## Agregar cadena HTML usando DOM

La clase Aspose.Pdf.Generator.Text contiene una propiedad llamada IsHtmlTagSupported que hace posible agregar etiquetas/contenidos HTML en archivos PDF. El contenido agregado se renderiza en etiquetas HTML nativas en lugar de aparecer como una simple cadena de texto. Para soportar una característica similar en el nuevo Modelo de Objetos de Documento (DOM) del espacio de nombres Aspose.Pdf, se ha introducido la clase HtmlFragment.

La instancia de [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) se puede usar para especificar los contenidos HTML que deben colocarse dentro del archivo PDF. Similar a TextFragment, HtmlFragment es un objeto a nivel de párrafo y se puede agregar a la colección de párrafos del objeto Page. Los siguientes fragmentos de código muestran los pasos para colocar contenidos HTML dentro del archivo PDF usando el enfoque DOM.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLStringUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 200;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);

        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOM_out.pdf");
    }
}
```

El siguiente fragmento de código demuestra los pasos sobre cómo agregar listas ordenadas HTML en el documento:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLOrderedListIntoDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Instantiate HtmlFragment object with corresponding HTML fragment 
        var fragment = new Aspose.Pdf.HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
    }
}
```

También puede establecer el formato de cadena HTML usando el objeto TextState de la siguiente manera:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetHTMLStringFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var fragment = new Aspose.Pdf.HtmlFragment("some text");
        fragment.TextState = new Aspose.Pdf.Text.TextState();
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "SetHTMLStringFormatting_out.pdf");
    }
}
```

En caso de que establezca algunos valores de atributos de texto a través de la marca HTML y luego proporcione los mismos valores en las propiedades de TextState, sobrescribirán los parámetros HTML por las propiedades del objeto TextState. Los siguientes fragmentos de código muestran el comportamiento descrito.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLUsingDOMAndOverwrite()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
        //Font-family from 'Verdana' will be reset to 'Arial'
        title.TextState = new Aspose.Pdf.Text.TextState("Arial");
        title.TextState.FontSize = 20;
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 400;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);
        
        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
    }
}
```

## Notas al pie y Notas finales (DOM)

Las notas al pie indican notas en el texto de su documento utilizando números en superíndice consecutivos. La nota real está indentada y puede aparecer como una nota al pie en la parte inferior de la página.

### Agregar Nota al pie

En un sistema de referencia de notas al pie, indique una referencia mediante:

- Colocar un pequeño número sobre la línea de tipo directamente después del material fuente. Este número se llama identificador de nota. Se sitúa ligeramente por encima de la línea de texto.
- Colocar el mismo número, seguido de una cita de su fuente, en la parte inferior de la página. Las notas al pie deben ser numéricas y cronológicas: la primera referencia es 1, la segunda es 2, y así sucesivamente.

La ventaja de las notas al pie es que el lector puede simplemente mirar hacia abajo en la página para descubrir la fuente de una referencia que le interese.

Siga los pasos especificados a continuación para crear una Nota al pie:

- Cree una instancia de Document.
- Cree un objeto Page.
- Cree un objeto TextFragment.
- Cree una instancia de Nota y pase su valor a la propiedad TextFragment.FootNote.
- Agregue TextFragment a la colección de párrafos de una instancia de página.

### Estilo de línea personalizado para Nota al pie

El siguiente ejemplo demuestra cómo agregar notas al pie a la parte inferior de la página PDF y definir un estilo de línea personalizado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomLineStyleForFootNote()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);
        // Create second TextFragment
        text = new Aspose.Pdf.Text.TextFragment("Aspose.PDF for .NET");
        // Set FootNote for second text fragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 2");
        // Add second text fragment to paragraphs collection of PDF file
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomLineStyleForFootNote_out.pdf");
    }
}
```

Podemos establecer el formato de la etiqueta de la Nota al pie (identificador de nota) usando el objeto TextState de la siguiente manera:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FormattingUsingTextStateObject()
{
    var text = new Aspose.Pdf.Text.TextFragment("test text 1");
    text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
    text.FootNote.Text = "21";
    text.FootNote.TextState = new Aspose.Pdf.Text.TextState();
    text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    text.FootNote.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
}
```

### Personalizar etiqueta de Nota al pie

Por defecto, el número de la Nota al pie es incremental comenzando desde 1. Sin embargo, podemos tener la necesidad de establecer una etiqueta de Nota al pie personalizada. Para lograr este requisito, intente usar el siguiente fragmento de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizeFootNoteLabel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Specify custom label for FootNote
        text.FootNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomizeFootNoteLabel_out.pdf");
    }
}
```

## Agregar imagen y tabla a la Nota al pie

En versiones anteriores, se proporcionó soporte para notas al pie, pero solo era aplicable al objeto TextFragment. Sin embargo, desde el lanzamiento de Aspose.PDF for .NET 10.7.0, también puede agregar notas al pie a otros objetos dentro del documento PDF, como Tabla, Celdas, etc. El siguiente fragmento de código muestra los pasos para agregar una Nota al pie al objeto TextFragment y luego agregar un objeto Imagen y Tabla a la colección de párrafos de la sección de Nota al pie.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageAndTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var text = new Aspose.Pdf.Text.TextFragment("some text");
        page.Paragraphs.Add(text);

        text.FootNote = new Aspose.Pdf.Note();
        // Create image
        Aspose.Pdf.Image image = new Aspose.Pdf.Image();
        image.File = dataDir + "aspose-logo.jpg";
        image.FixHeight = 20;
        text.FootNote.Paragraphs.Add(image);

        var footNote = new Aspose.Pdf.Text.TextFragment("footnote text");
        footNote.TextState.FontSize = 20;
        footNote.IsInLineParagraph = true;
        text.FootNote.Paragraphs.Add(footNote);

        var table = new Aspose.Pdf.Table();
        table.Rows.Add().Cells.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Row 1 Cell 1"));
        text.FootNote.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddImageAndTable_out.pdf");
    }
}
```

## Cómo crear Notas finales

Una Nota final es una cita de fuente que refiere a los lectores a un lugar específico al final del documento donde pueden encontrar la fuente de la información o palabras citadas o mencionadas en el documento. Al usar notas finales, su oración citada o parafraseada o material resumido es seguido por un número en superíndice.

El siguiente ejemplo demuestra cómo agregar una Nota final en la página PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateEndNotes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.EndNote = new Aspose.Pdf.Note("sample End note");
        // Specify custom label for FootNote
        text.EndNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateEndNotes_out.pdf");
    }
}
```

## Texto e imagen como párrafo en línea

El diseño predeterminado del archivo PDF es un diseño de flujo (de arriba a abajo, de izquierda a derecha). Por lo tanto, cada nuevo elemento que se agrega al archivo PDF se agrega en el flujo de la parte inferior derecha. Sin embargo, podemos tener la necesidad de mostrar varios elementos de página, es decir, Imagen y Texto al mismo nivel (uno después del otro). Un enfoque puede ser crear una instancia de Tabla y agregar ambos elementos a objetos de celda individuales. Sin embargo, otro enfoque puede ser el párrafo en línea. Al establecer la propiedad IsInLineParagraph de Imagen y Texto como verdadera, estos párrafos aparecerán como en línea con otros elementos de la página.

El siguiente fragmento de código le muestra cómo agregar texto e imagen como párrafos en línea en el archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextAndImageAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document instance
        var page = document.Pages.Add();
        // Create TextFragmnet
        var text = new Aspose.Pdf.Text.TextFragment("Hello World.. ");
        // Add text fragment to paragraphs collection of Page object
        page.Paragraphs.Add(text);
        // Create an image instance
        var image = new Aspose.Pdf.Image();
        // Set image as inline paragraph so that it appears right after
        // The previous paragraph object (TextFragment)
        image.IsInLineParagraph = true;
        // Specify image file path
        image.File = dataDir + "aspose-logo.jpg";
        // Set image Height (optional)
        image.FixHeight = 30;
        // Set Image Width (optional)
        image.FixWidth = 100;
        // Add image to paragraphs collection of page object
        page.Paragraphs.Add(image);
        // Re-initialize TextFragment object with different contents
        text = new Aspose.Pdf.Text.TextFragment(" Hello Again..");
        // Set TextFragment as inline paragraph
        text.IsInLineParagraph = true;
        // Add newly created TextFragment to paragraphs collection of page
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "TextAndImageAsParagraph_out.pdf");
    }
}
```

## Especificar espaciado de caracteres al agregar texto

Se puede agregar texto dentro de la colección de párrafos de archivos PDF usando la instancia TextFragment o usando el objeto TextParagraph e incluso puede estampar el texto dentro del PDF usando la clase TextStamp. Al agregar el texto, podemos tener la necesidad de especificar el espaciado de caracteres para los objetos de texto. Para lograr este requisito, se ha introducido una nueva propiedad llamada CharacterSpacing. Por favor, eche un vistazo a los siguientes enfoques para cumplir con este requisito.

Los siguientes enfoques muestran los pasos para especificar el espaciado de caracteres al agregar texto dentro de un documento PDF.

### Usando TextBuilder y TextFragment

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndFragment()
{            
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment instance with sample contents
        var wideFragment = new Aspose.Pdf.Text.TextFragment("Text with increased character spacing");
        wideFragment.TextState.ApplyChangesFrom(new Aspose.Pdf.Text.TextState("Arial", 12));
        // Specify character spacing for TextFragment
        wideFragment.TextState.CharacterSpacing = 2.0f;
        // Specify the position of TextFragment
        wideFragment.Position = new Aspose.Pdf.Text.Position(100, 650);
        // Append TextFragment to TextBuilder instance
        builder.AppendText(wideFragment);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
    }
}
```

### Usando TextParagraph

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Instantiate TextParagraph instance
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Create TextState instance to specify font name and size
        var state = new Aspose.Pdf.Text.TextState("Arial", 12);
        // Specify the character spacing
        state.CharacterSpacing = 1.5f;
        // Append text to TextParagraph object
        paragraph.AppendLine("This is paragraph with character spacing", state);
        // Specify the position for TextParagraph
        paragraph.Position = new Aspose.Pdf.Text.Position(100, 550);
        // Append TextParagraph to TextBuilder instance
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
    }
}
```

### Usando TextStamp

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Instantiate TextStamp instance with sample text
        var stamp = new Aspose.Pdf.TextStamp("This is text stamp with character spacing");
        // Specify font name for Stamp object
        stamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        // Specify Font size for TextStamp
        stamp.TextState.FontSize = 12;
        // Specify character specing as 1f
        stamp.TextState.CharacterSpacing = 1f;
        // Set the XIndent for Stamp
        stamp.XIndent = 100;
        // Set the YIndent for Stamp
        stamp.YIndent = 500;
        // Add textual stamp to page instance
        stamp.Put(page);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextStamp_out.pdf");
    }
}
```

## Crear documento PDF de múltiples columnas

En revistas y periódicos, vemos que las noticias se muestran en múltiples columnas en una sola página en lugar de en libros donde los párrafos de texto se imprimen principalmente en toda la página de izquierda a derecha. Muchas aplicaciones de procesamiento de documentos como Microsoft Word y Adobe Acrobat Writer permiten a los usuarios crear múltiples columnas en una sola página y luego agregar datos a ellas.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) también ofrece la función de crear múltiples columnas dentro de las páginas de documentos PDF. Para crear un archivo PDF de múltiples columnas, podemos utilizar la clase Aspose.Pdf.FloatingBox, ya que proporciona la propiedad ColumnInfo.ColumnCount para especificar el número de columnas dentro de FloatingBox y también podemos especificar el espaciado entre columnas y los anchos de las columnas usando las propiedades ColumnInfo.ColumnSpacing y ColumnInfo.ColumnWidths respectivamente. Tenga en cuenta que FloatingBox es un elemento dentro del Modelo de Objetos de Documento y puede tener posicionamiento obsoleto en comparación con el posicionamiento relativo (es decir, Texto, Gráfico, Imagen, etc.).

El espaciado entre columnas significa el espacio entre las columnas y el espaciado predeterminado entre las columnas es de 1.25 cm. Si no se especifica el ancho de la columna, entonces [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) calcula automáticamente el ancho para cada columna de acuerdo con el tamaño de la página y el espaciado entre columnas.

A continuación se muestra un ejemplo para demostrar la creación de dos columnas con objetos Gráficos (Línea) y se agregan a la colección de párrafos de FloatingBox, que luego se agrega a la colección de párrafos de la instancia de Page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateMultiColumnPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Specify the left margin info for the PDF file
        document.PageInfo.Margin.Left = 40;
        // Specify the Right margin info for the PDF file
        document.PageInfo.Margin.Right = 40;
        var page = document.Pages.Add();

        var graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
        // Add the line to paraphraphs collection of section object
        page.Paragraphs.Add(graph1);

        // Specify the coordinates for the line
        float[] posArr = new float[] { 1, 2, 500, 2 };
        var line1 = new Aspose.Pdf.Drawing.Line(posArr);
        graph1.Shapes.Add(line1);
        // Create string variables with text containing html tags
        string s = "<font face=\"Times New Roman\" size=4>" +

        "<strong> How to Steer Clear of money scams</<strong> "
        + "</font>";
        // Create text paragraphs containing HTML text
        var heading_text = new Aspose.Pdf.HtmlFragment(s);
        page.Paragraphs.Add(heading_text);

        var box = new Aspose.Pdf.FloatingBox();
        // Add four columns in the section
        box.ColumnInfo.ColumnCount = 2;
        // Set the spacing between the columns
        box.ColumnInfo.ColumnSpacing = "5";

        box.ColumnInfo.ColumnWidths = "105 105";
        var text1 = new Aspose.Pdf.Text.TextFragment("By A Googler (The Official Google Blog)");
        text1.TextState.FontSize = 8;
        text1.TextState.LineSpacing = 2;
        box.Paragraphs.Add(text1);
        text1.TextState.FontSize = 10;

        text1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create a graphs object to draw a line
        var graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
        // Specify the coordinates for the line
        float[] posArr2 = new float[] { 1, 10, 100, 10 };
        var line2 = new Aspose.Pdf.Drawing.Line(posArr2);
        graph2.Shapes.Add(line2);

        // Add the line to paragraphs collection of section object
        box.Paragraphs.Add(graph2);

        var text2 = new Aspose.Pdf.Text.TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
        box.Paragraphs.Add(text2);

        page.Paragraphs.Add(box);

        // Save PDF document
        document.Save(dataDir + "CreateMultiColumnPdf_out.pdf");
    }
}
```

## Trabajando con Tab Stops personalizados

Un Tab Stop es un punto de parada para tabular. En el procesamiento de texto, cada línea contiene un número de tab stops colocados a intervalos regulares (por ejemplo, cada media pulgada). Sin embargo, pueden cambiarse, ya que la mayoría de los procesadores de texto permiten establecer tab stops donde desee. Cuando presiona la tecla Tab, el cursor o punto de inserción salta al siguiente tab stop, que en sí mismo es invisible. Aunque los tab stops no existen en el archivo de texto, el procesador de texto los rastrea para que pueda reaccionar correctamente a la tecla Tab.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) permite a los desarrolladores usar tab stops personalizados en documentos PDF. La clase Aspose.Pdf.Text.TabStop se utiliza para establecer tab stops personalizados en la clase [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) también ofrece algunos tipos de tab leader predefinidos como una enumeración llamada TabLeaderType cuyos valores predefinidos y sus descripciones se dan a continuación:

|**Tipo de Tab Leader**|**Descripción**|
| :- | :- |
|Ninguno|Sin tab leader|
|Sólido|Tab leader sólido|
|Guion|Tab leader de guion|
|Punto|Tab leader de punto|

Aquí hay un ejemplo de cómo establecer tab stops personalizados.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomTabStops()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var tabStops = new Aspose.Pdf.Text.TabStops();
        var tabStop1 = tabStops.Add(100);
        tabStop1.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Right;
        tabStop1.LeaderType = Aspose.Pdf.Text.TabLeaderType.Solid;

        var tabStop2 = tabStops.Add(200);
        tabStop2.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Center;
        tabStop2.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dash;

        var tabStop3 = tabStops.Add(300);
        tabStop3.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Left;
        tabStop3.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dot;

        var header = new Aspose.Pdf.Text.TextFragment("This is a example of forming table with TAB stops", tabStops);
        var text0 = new Aspose.Pdf.Text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        var text1 = new Aspose.Pdf.Text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);
        var text2 = new Aspose.Pdf.Text.TextFragment("#$TABdata21 ", tabStops);
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data22 "));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data23"));

        // Add text fragments to page
        page.Paragraphs.Add(header);
        page.Paragraphs.Add(text0);
        page.Paragraphs.Add(text1);
        page.Paragraphs.Add(text2);

        // Save PDF document
        document.Save(dataDir + "CustomTabStops_out.pdf");
    }
}
```

## Cómo agregar texto transparente en PDF

Un archivo PDF contiene objetos de Imagen, Texto, Gráfico, adjuntos, Anotaciones y al crear TextFragment, puede establecer información de color de primer plano, color de fondo, así como formato de texto. Aspose.PDF for .NET admite la función de agregar texto con canal de color Alpha. El siguiente fragmento de código muestra cómo agregar texto con color transparente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTransparentText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create page to pages collection of PDF file
        var page = document.Pages.Add();

        // Create Graph object
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
        // Create rectangle instance with certain dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
        // Create color object from Alpha color channel
        rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
        // Add rectanlge to shapes collection of Graph object
        canvas.Shapes.Add(rect);
        // Add graph object to paragraphs collection of page object
        page.Paragraphs.Add(canvas);
        // Set value to not change position for graph object
        canvas.IsChangePosition = false;

        // Create TextFragment instance with sample value
        var text = new Aspose.Pdf.Text.TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
        // Create color object from Alpha channel
        Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
        // Set color information for text instance
        text.TextState.ForegroundColor = color;
        // Add text to paragraphs collection of page instance
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "AddTransparentText_out.pdf");
    }
}
```

## Especificar LineSpacing para fuentes

Cada fuente tiene un cuadrado abstracto, cuya altura es la distancia prevista entre líneas de tipo en el mismo tamaño de tipo. Este cuadrado se llama el cuadrado em y es la cuadrícula de diseño en la que se definen los contornos de los glifos. Muchas letras de la fuente de entrada tienen puntos que se colocan fuera de los límites del cuadrado em de la fuente, por lo que para mostrar la fuente correctamente, se necesita el uso de una configuración especial. El objeto TextFragment tiene un conjunto de opciones de formato de texto que son accesibles a través de las propiedades TextState.FormattingOptions. La última propiedad de este camino es una propiedad de tipo Aspose.Pdf.Text.TextFormattingOptions. Esta clase tiene una enumeración [LineSpacingMode](https://reference.aspose.com/pdf/net/aspose.pdf.text.textformattingoptions/linespacingmode) que está diseñada para fuentes específicas, por ejemplo, la fuente de entrada "HPSimplified.ttf". También la clase [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions) tiene una propiedad [LineSpacing](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions/properties/linespacing) de tipo LineSpacingMode. Solo necesita establecer LineSpacing en LineSpacingMode.FullSize. El fragmento de código para mostrar una fuente correctamente sería como sigue:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyLineSpacing()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    string fontFile = dataDir + "HPSimplified.TTF";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        //Create TextFormattingOptions with LineSpacingMode.FullSize
        var formattingOptions = new Aspose.Pdf.Text.TextFormattingOptions();
        formattingOptions.LineSpacing = Aspose.Pdf.Text.TextFormattingOptions.LineSpacingMode.FullSize;

        // Create text builder object for first page of document
        //TextBuilder textBuilder = new TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (fontFile != "")
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
                //Set TextFormattingOptions of current fragment to predefined(which points to LineSpacingMode.FullSize)
                textFragment.TextState.FormattingOptions = formattingOptions;
                // Add the text to TextBuilder so that it can be placed over the PDF file
                //textBuilder.AppendText(textFragment);
                var page = document.Pages.Add();
                page.Paragraphs.Add(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "SpecifyLineSpacing_out.pdf");
        }
    }
}
```

## Obtener el ancho del texto dinámicamente

A veces, es necesario obtener el ancho del texto dinámicamente. Aspose.PDF for .NET incluye dos métodos para medir el ancho de la cadena. Puede invocar el método [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) de las clases Aspose.Pdf.Text.Font o Aspose.Pdf.Text.TextState (o ambas). El siguiente fragmento de código muestra cómo usar esta funcionalidad.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextWidthDynamically()
{            
    var font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
    var textState = new Aspose.Pdf.Text.TextState();
    textState.Font = font;
    textState.FontSize = 14;

    if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    if (Math.Abs(textState.MeasureString("z") - 7.0) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++)
    {
        double fontMeasure = font.MeasureString(c.ToString(), 14);
        double textStateMeasure = textState.MeasureString(c.ToString());

        if (Math.Abs(fontMeasure - textStateMeasure) > 0.001)
        {
            Console.WriteLine("Font and state string measuring doesn't match!");
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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