---
title: Rotar Texto Dentro de PDF usando Python
linktitle: Rotar Texto Dentro de PDF
type: docs
weight: 50
url: es/python-net/rotate-text-inside-pdf/
description: Aprenda diferentes maneras de rotar texto en PDF. Aspose.PDF le permite rotar texto a cualquier ángulo, rotar un fragmento de texto o un párrafo completo.
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotar Texto Dentro de PDF usando Python",
    "alternativeHeadline": "Cómo rotar Texto en un Archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, generación de documentos",
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
    "url": "/python-net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Aprenda diferentes maneras de rotar texto en PDF. Aspose.PDF le permite rotar texto a cualquier ángulo, rotar un fragmento de texto o un párrafo completo."
}
</script>


## Rotar Texto Dentro de un PDF usando la Propiedad de Rotación

Usando la propiedad de Rotación de la Clase [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment), puedes rotar texto en varios ángulos. La rotación de texto se puede utilizar en diferentes escenarios de generación de documentos. Puedes especificar el ángulo de rotación en grados para rotar el texto según tu requerimiento. Por favor, revisa los siguientes diferentes escenarios, en los cuales puedes implementar la rotación de texto.

## Implementar Rotación usando TextFragment y TextBuilder

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializar objeto de documento
Document pdfDocument = new Document();
// Obtener una página en particular
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Crear fragmento de texto
TextFragment textFragment1 = new TextFragment("texto principal");
textFragment1.Position = new Position(100, 600);
// Establecer propiedades del texto
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Crear fragmento de texto rotado
TextFragment textFragment2 = new TextFragment("texto rotado");
textFragment2.Position = new Position(200, 600);
// Establecer propiedades del texto
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// Crear fragmento de texto rotado
TextFragment textFragment3 = new TextFragment("texto rotado");
textFragment3.Position = new Position(300, 600);
// Establecer propiedades del texto
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// crear objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Añadir el fragmento de texto a la página PDF
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// Guardar documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```


## Implementar Rotación usando TextParagraph y TextBuilder (Fragmentos Rotados)

```csharp
// Para obtener ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializar objeto de documento
Document pdfDocument = new Document();
// Obtener página particular
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// Crear fragmento de texto
TextFragment textFragment1 = new TextFragment("texto rotado");
// Establecer propiedades de texto
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Establecer rotación
textFragment1.TextState.Rotation = 45;
// Crear fragmento de texto
TextFragment textFragment2 = new TextFragment("texto principal");
// Establecer propiedades de texto
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Crear fragmento de texto
TextFragment textFragment3 = new TextFragment("otro texto rotado");
// Establecer propiedades de texto
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Establecer rotación
textFragment3.TextState.Rotation = -45;
// Añadir los fragmentos de texto al párrafo
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// Crear objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Añadir el párrafo de texto a la página PDF
textBuilder.AppendParagraph(paragraph);
// Guardar documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```


## Implementar Rotación usando TextFragment y Page.Paragraphs

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializar objeto documento
Document pdfDocument = new Document();
// Obtener página particular
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Crear fragmento de texto
TextFragment textFragment1 = new TextFragment("texto principal");
// Establecer propiedades de texto
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Crear fragmento de texto
TextFragment textFragment2 = new TextFragment("texto rotado");
// Establecer propiedades de texto
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Establecer rotación
textFragment2.TextState.Rotation = 315;
// Crear fragmento de texto
TextFragment textFragment3 = new TextFragment("texto rotado");
// Establecer propiedades de texto
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Establecer rotación
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// Guardar documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```


## Implementar Rotación usando TextParagraph y TextBuilder (Párrafo Completo Rotado)

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializar objeto de documento
Document pdfDocument = new Document();
// Obtener página particular
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // Especificar rotación
    paragraph.Rotation = i * 90 + 45;
    // Crear fragmento de texto
    TextFragment textFragment1 = new TextFragment("Texto del Párrafo");
    // Crear fragmento de texto
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Crear fragmento de texto
    TextFragment textFragment2 = new TextFragment("Segunda línea de texto");
    // Establecer propiedades del texto
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Crear fragmento de texto
    TextFragment textFragment3 = new TextFragment("Y algo más de texto...");
    // Establecer propiedades del texto
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // Crear objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Añadir el fragmento de texto a la página del PDF
    textBuilder.AppendParagraph(paragraph);
}
// Guardar documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
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