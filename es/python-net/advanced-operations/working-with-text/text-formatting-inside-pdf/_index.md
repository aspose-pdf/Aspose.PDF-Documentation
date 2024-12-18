---
title: Formato de Texto dentro de PDF usando Python
linktitle: Formato de Texto dentro de PDF
type: docs
weight: 30
url: /es/python-net/text-formatting-inside-pdf/
description: Esta página explica cómo formatear texto dentro de su archivo PDF. Hay adición de sangría de línea, adición de borde de texto, adición de texto subrayado, etc.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formato de Texto dentro de PDF usando Python",
    "alternativeHeadline": "Cómo formatear texto en archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, formatear texto en pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Esta página explica cómo formatear texto dentro de su archivo PDF. Hay adición de sangría de línea, adición de borde de texto, adición de texto subrayado, etc."
}
</script>


## Cómo agregar sangría de línea a PDF

Aspose.PDF para .NET ofrece la propiedad SubsequentLinesIndent en la clase [TextFormattingOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textformattingoptions). Que se puede usar para especificar la sangría de línea en escenarios de generación de PDF con TextFragment y la colección de Párrafos.

Utilice el siguiente fragmento de código para usar la propiedad:

```csharp
// Para obtener ejemplos completos y archivos de datos, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear nuevo objeto de documento
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// Inicializar TextFormattingOptions para el fragmento de texto y especificar el valor de SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```


## Cómo añadir un borde al texto

El siguiente fragmento de código muestra cómo añadir un borde a un texto usando TextBuilder y configurando la propiedad DrawTextRectangleBorder de TextState:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear un nuevo objeto de documento
Document pdfDocument = new Document();
// Obtener una página en particular
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Crear un fragmento de texto
TextFragment textFragment = new TextFragment("texto principal");
textFragment.Position = new Position(100, 600);
// Establecer propiedades del texto
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Establecer la propiedad StrokingColor para dibujar un borde (trazo) alrededor del rectángulo de texto
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Establecer el valor de la propiedad DrawTextRectangleBorder a true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Guardar el documento
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```


## Cómo agregar texto subrayado

El siguiente fragmento de código te muestra cómo agregar texto subrayado mientras creas un nuevo archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear objeto de documentación
Document pdfDocument = new Document();
// Añadir página al documento PDF
pdfDocument.Pages.Add();
// Crear TextBuilder para la primera página
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment con texto de ejemplo
TextFragment fragment = new TextFragment("Mensaje de prueba");
// Establecer la fuente para TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// Establecer el formato del texto como Subrayado
fragment.TextState.Underline = true;
// Especificar la posición donde se necesita colocar TextFragment
fragment.Position = new Position(10, 800);
// Añadir TextFragment al archivo PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```


## Cómo agregar un borde alrededor del texto añadido

Tienes control sobre el aspecto del texto que añades. El ejemplo a continuación muestra cómo añadir un borde alrededor de un fragmento de texto que has añadido dibujando un rectángulo a su alrededor. Descubre más sobre la clase [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// Guarda el documento PDF resultante.
editor.Save(dataDir);
```

## Cómo agregar un salto de línea

TextFragment no admite el salto de línea dentro del texto. Sin embargo, para agregar texto con salto de línea, use TextFragment con TextParagraph:

- use "\r\n" o Environment.NewLine en TextFragment en lugar de un solo "\n";
- cree un objeto TextParagraph. Esto agregará texto con división de líneas;
- agregue el TextFragment con TextParagraph.AppendLine;
- agregue el TextParagraph con TextBuilder.AppendParagraph.
Utilice el siguiente fragmento de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inicializar un nuevo TextFragment con texto que contiene los marcadores de nueva línea requeridos
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// Establecer propiedades del fragmento de texto si es necesario
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Crear un objeto TextParagraph
TextParagraph par = new TextParagraph();

// Agregar nuevo TextFragment al párrafo
par.AppendLine(textFragment);

// Establecer posición del párrafo
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Crear un objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Agregar el TextParagraph usando TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Guardar el documento PDF resultante.
pdfApplicationDoc.Save(dataDir);
```


## Cómo añadir texto tachado

La clase TextState proporciona las capacidades para establecer el formato de TextFragments que se colocan dentro de un documento PDF. Puede usar esta clase para establecer el formato de texto como Negrita, Cursiva, Subrayado y, a partir de esta versión, la API ha proporcionado la capacidad para marcar el formato de texto como Tachado. Por favor, intente usar el siguiente fragmento de código para agregar un TextFragment con formato Tachado.

Por favor, use el fragmento de código completo:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Abrir documento
Document pdfDocument = new Document();
// Obtener página en particular
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Crear fragmento de texto
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// Establecer propiedades de texto
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Establecer propiedad de Tachado
textFragment.TextState.StrikeOut = true;
// Marcar texto como Negrita
textFragment.TextState.FontStyle = FontStyles.Bold;

// Crear objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Añadir el fragmento de texto a la página PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```


## Aplicar sombreado de gradiente al texto

El formato de texto se ha mejorado aún más en la API para escenarios de edición de texto y ahora puede agregar texto con un espacio de color de patrón dentro del documento PDF. La clase Aspose.Pdf.Color se ha mejorado introduciendo una nueva propiedad de PatternColorSpace, que se puede usar para especificar colores de sombreado para el texto. Esta nueva propiedad agrega diferentes sombreados de gradiente al texto, por ejemplo, sombreado axial, sombreado radial (Tipo 3) como se muestra en el siguiente fragmento de código:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // Crear nuevo color con espacio de color de patrón
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```


>Para aplicar un Degradado Radial, puedes establecer la propiedad ‘PatternColorSpace’ igual a ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ en el fragmento de código anterior.

## Cómo alinear texto al contenido flotante

Aspose.PDF admite la configuración de la alineación del texto para los contenidos dentro de un elemento de Caja Flotante. Se pueden utilizar las propiedades de alineación de la instancia Aspose.Pdf.FloatingBox para lograr esto, como se muestra en el siguiente ejemplo de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la Biblioteca .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>