---
title: Agregar sellos de texto en PDF C#
linktitle: Sellos de texto en archivo PDF
type: docs
weight: 20
url: /net/text-stamps-in-the-pdf-file/
description: Agregar un sello de texto a un documento PDF utilizando la clase TextStamp con la biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Agregar sellos de texto en PDF C#",
    "alternativeHeadline": "Agregar sellos de texto en PDF C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, c#, generación de documentos",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Agregar un sello de texto a un documento PDF utilizando la clase TextStamp con la biblioteca Aspose.PDF para .NET."
}
</script>
## Añadir sello de texto con C#

Puedes usar la clase [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) para añadir un sello de texto en un archivo PDF. La clase TextStamp proporciona propiedades necesarias para crear un sello basado en texto como el tamaño de fuente, el estilo de fuente y el color de la fuente, etc. Para añadir un sello de texto, necesitas crear un objeto Document y un objeto TextStamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Página para añadir el sello en el PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente fragmento de código te muestra cómo añadir un sello de texto en el archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// Crear sello de texto
TextStamp textStamp = new TextStamp("Sello de muestra");
// Establecer si el sello es de fondo
textStamp.Background = true;
// Establecer origen
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// Rotar sello
textStamp.Rotate = Rotation.on90;
// Establecer propiedades del texto
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// Añadir sello a la página específica
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// Guardar documento de salida
pdfDocument.Save(dataDir);
```
## Definir la alineación para el objeto TextStamp

Agregar marcas de agua a documentos PDF es una de las características frecuentemente demandadas y Aspose.PDF para .NET es completamente capaz de agregar marcas de agua de imagen así como de texto. Tenemos una clase llamada [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) que proporciona la funcionalidad de agregar sellos de texto sobre el archivo PDF. Recientemente, ha surgido la necesidad de soportar la funcionalidad para especificar la alineación del texto cuando se utiliza el objeto TextStamp. Por lo tanto, para cumplir con esta necesidad, hemos introducido la propiedad TextAlignment en la clase TextStamp. Usando esta propiedad, podemos especificar la alineación horizontal del texto.

El siguiente fragmento de código muestra un ejemplo sobre cómo cargar un documento PDF existente y agregar un TextStamp sobre él.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instanciar objeto Document con archivo de entrada
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// Instanciar objeto FormattedText con cadena de muestra
FormattedText text = new FormattedText("This");
// Agregar nueva línea de texto a FormattedText
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// Crear objeto TextStamp usando FormattedText
TextStamp stamp = new TextStamp(text);
// Especificar la Alineación Horizontal del sello de texto como centrada
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// Especificar la Alineación Vertical del sello de texto como centrada
stamp.VerticalAlignment = VerticalAlignment.Center;
// Especificar la Alineación Horizontal del Texto del TextStamp como centrada
stamp.TextAlignment = HorizontalAlignment.Center;
// Establecer margen superior para el objeto sello
stamp.TopMargin = 20;
// Agregar el objeto sello sobre la primera página del documento
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
```
## Rellenar texto de trazo como sello en archivo PDF

Hemos implementado la configuración del modo de renderizado para escenarios de adición y edición de texto. Para renderizar texto de trazo, por favor cree un objeto TextState y establezca RenderingMode en TextRenderingMode.StrokeText y también seleccione color para la propiedad StrokingColor. Luego, vincule TextState al sello utilizando el método BindTextState().

El siguiente fragmento de código demuestra cómo agregar texto de relleno y trazo:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// Crear objeto TextState para transferir propiedades avanzadas
TextState ts = new TextState();
// Establecer color para el trazo
ts.StrokingColor = Color.Gray;
// Establecer modo de renderizado de texto
ts.RenderingMode = TextRenderingMode.StrokeText;
// Cargar un documento PDF de entrada
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAGADO COMPLETAMENTE", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// Vincular TextState
stamp.BindTextState(ts);
// Establecer origen X,Y
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// Agregar sello
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
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

