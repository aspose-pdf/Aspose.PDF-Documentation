---
title: Formateo de texto dentro de PDF usando C#
linktitle: Formateo de texto dentro de PDF
type: docs
weight: 30
url: /net/text-formatting-inside-pdf/
description: Esta página explica cómo formatear texto dentro de su archivo PDF. Incluye agregar sangría de línea, agregar borde de texto, agregar texto subrayado, y etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formateo de texto dentro de PDF usando C#",
    "alternativeHeadline": "Cómo formatear texto en un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, formatear texto en pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta página explica cómo formatear texto dentro de su archivo PDF. Incluye agregar sangría de línea, agregar borde de texto, agregar texto subrayado, y etc."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Cómo agregar Sangría de Línea a PDF

Aspose.PDF para .NET ofrece la propiedad SubsequentLinesIndent en la clase [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). Que se puede utilizar para especificar la sangría de línea en escenarios de generación de PDF con colección de TextFragment y Paragraphs.

Por favor, utilice el siguiente fragmento de código para usar la propiedad:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear nuevo objeto de documento
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("Un rápido zorro marrón saltó sobre el perro perezoso. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// Inicializar TextFormattingOptions para el fragmento de texto y especificar el valor de SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Línea2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Línea3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Línea4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Línea5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```
## Cómo agregar borde al texto

El siguiente fragmento de código muestra cómo agregar un borde a un texto utilizando TextBuilder y configurando la propiedad DrawTextRectangleBorder de TextState:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crear nuevo objeto de documento
Document pdfDocument = new Document();
// Obtener la página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Crear fragmento de texto
TextFragment textFragment = new TextFragment("texto principal");
textFragment.Position = new Position(100, 600);
// Configurar propiedades del texto
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Configurar la propiedad StrokingColor para dibujar un borde (trazo) alrededor del rectángulo de texto
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Configurar el valor de la propiedad DrawTextRectangleBorder a true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Guardar el documento
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## Cómo agregar texto subrayado

El siguiente fragmento de código te muestra cómo agregar texto subrayado al crear un nuevo archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear objeto de documentación
Document pdfDocument = new Document();
// Agregar página al documento PDF
pdfDocument.Pages.Add();
// Crear TextBuilder para la primera página
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment con texto de ejemplo
TextFragment fragment = new TextFragment("Mensaje de prueba");
// Establecer la fuente para TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// Establecer el formato de texto como Subrayado
fragment.TextState.Underline = true;
// Especificar la posición donde se debe colocar TextFragment
fragment.Position = new Position(10, 800);
// Añadir TextFragment al archivo PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Cómo agregar un borde alrededor del texto añadido

Tienes control sobre la apariencia del texto que agregas. El ejemplo a continuación muestra cómo agregar un borde alrededor de un texto que has añadido dibujando un rectángulo alrededor de él. Descubre más sobre la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

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
## Cómo agregar un salto de línea

TextFragment no admite saltos de línea dentro del texto. Sin embargo, para agregar texto con un salto de línea, use TextFragment con TextParagraph:

- use "\r\n" o Environment.NewLine en TextFragment en lugar de un único "\n";
- cree un objeto TextParagraph. Esto agregará texto con división de línea;
- agregue el TextFragment con TextParagraph.AppendLine;
- agregue el TextParagraph con TextBuilder.AppendParagraph.
Utilice el siguiente fragmento de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inicializa un nuevo TextFragment con texto que contiene los marcadores de línea necesarios
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nombre del solicitante: " + Environment.NewLine + " Joe Smoe");

// Establece las propiedades del fragmento de texto si es necesario
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Crea un objeto TextParagraph
TextParagraph par = new TextParagraph();

// Agrega un nuevo TextFragment al párrafo
par.AppendLine(textFragment);

// Establece la posición del párrafo
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Crea un objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Agrega el TextParagraph usando TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Guarda el documento PDF resultante.
pdfApplicationDoc.Save(dataDir);
```
## Cómo agregar texto tachado

La clase TextState proporciona las capacidades para establecer formato para los TextFragments que se colocan dentro del documento PDF. Puedes usar esta clase para establecer el formato de texto como Negrita, Itálica, Subrayado y a partir de esta versión, la API ha proporcionado las capacidades para marcar el formato de texto como Tachado. Por favor, intenta usar el siguiente fragmento de código para agregar TextFragment con formato tachado.

Por favor, usa el fragmento de código completo:

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Abrir documento
Document pdfDocument = new Document();
// Obtener página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Crear fragmento de texto
TextFragment textFragment = new TextFragment("texto principal");
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
// Adjuntar el fragmento de texto a la página PDF
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Aplicar sombreado degradado al texto

El formato de texto ha sido mejorado en la API para escenarios de edición de texto y ahora puedes agregar texto con espacio de color de patrón dentro de un documento PDF. La clase Aspose.Pdf.Color ha sido mejorada introduciendo una nueva propiedad de PatternColorSpace, que puede ser utilizada para especificar colores de sombreado para el texto. Esta nueva propiedad agrega diferentes sombreados degradados al texto, por ejemplo, sombreado axial, sombreado radial (Tipo 3) como se muestra en el siguiente fragmento de código:

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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
>Para aplicar un Gradiente Radial, puede establecer la propiedad 'PatternColorSpace' igual a 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' en el fragmento de código anterior.

## Cómo alinear texto para flotar contenido

Aspose.PDF admite la configuración de la alineación de texto para contenidos dentro de un elemento Floating Box. Las propiedades de alineación de la instancia Aspose.Pdf.FloatingBox se pueden utilizar para lograr esto como se muestra en el siguiente ejemplo de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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
floatBox2.Border = a new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
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
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
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

