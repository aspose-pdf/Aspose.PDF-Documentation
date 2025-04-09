---
title: Convertir PDF a HTML en .NET
linktitle: Convertir PDF a formato HTML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Este tema te muestra cómo convertir un archivo PDF a formato HTML con la biblioteca Aspose.PDF C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "Presentando una nueva característica poderosa en Aspose.PDF for .NET que permite la conversión sin problemas de documentos PDF a formato HTML. Esta funcionalidad admite salida de varias páginas, gestión de imágenes SVG y opciones para renderizado de texto transparente, permitiendo a los desarrolladores transformar fácilmente PDFs en contenido listo para la web con solo unas pocas líneas de código C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1588",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Resumen

Este artículo explica cómo **convertir PDF a HTML usando C#**. Cubre estos temas.

- [Convertir PDF a HTML](#csharp-pdf-to-html)

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Convertir PDF a HTML

**Aspose.PDF for .NET** proporciona muchas características para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo discute cómo convertir un archivo PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for .NET proporciona la capacidad de convertir archivos HTML en formato PDF utilizando el enfoque InLineHtml. Hemos recibido muchas solicitudes para una funcionalidad que convierta un archivo PDF en formato HTML y hemos proporcionado esta característica. Ten en cuenta que esta función también admite XHTML 1.0.

**Aspose.PDF for .NET** admite las características para convertir un archivo PDF en HTML. Las principales tareas que puedes realizar con la biblioteca Aspose.PDF están listadas:

- Convertir PDF a HTML.
- Dividir la salida en HTML de varias páginas.
- Especificar la carpeta para almacenar archivos SVG.
- Comprimir imágenes SVG durante la conversión.
- Guardar imágenes como fondo PNG.
- Especificar la carpeta de imágenes.
- Crear archivos subsiguientes solo con el contenido del cuerpo.
- Renderizado de texto transparente.
- Renderizado de capas de documentos PDF.

{{% alert color="success" %}}
**Intenta convertir PDF a HTML en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a HTML con aplicación gratuita](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET proporciona un código de dos líneas para transformar un archivo PDF de origen a HTML. La [`enumeración SaveFormat`](https://reference.aspose.com/pdf/es/net/aspose.pdf/saveformat) contiene el valor Html que te permite guardar el archivo de origen en HTML. El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF en HTML.

<a name="csharp-pdf-to-html" id="cshart-pdf-to-html"><strong>Convertir PDF a HTML</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/) con el documento PDF de origen.
2. Guárdalo en formato **SaveFormat.Html** llamando al método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### Dividir la salida en HTML de varias páginas

Al convertir un archivo PDF grande con varias páginas a formato HTML, la salida aparece como una sola página HTML. Puede terminar siendo muy larga. Para controlar el tamaño de la página, es posible dividir la salida en varias páginas durante la conversión de PDF a HTML. Por favor, intenta usar el siguiente fragmento de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### Especificar la carpeta para almacenar archivos SVG

Durante la conversión de PDF a HTML, es posible especificar la carpeta en la que se deben guardar las imágenes SVG. Usa la [`clase HtmlSaveOption`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlsaveoptions) [`propiedad SpecialFolderForSvgImages`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages) para especificar un directorio especial para imágenes SVG. Esta propiedad obtiene o establece la ruta al directorio en el que se deben guardar las imágenes SVG cuando se encuentran durante la conversión. Si el parámetro está vacío o es nulo, entonces cualquier archivo SVG se guarda junto con otros archivos de imagen.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### Comprimir imágenes SVG durante la conversión

Para comprimir imágenes SVG durante la conversión de PDF a HTML, por favor intenta usar el siguiente código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### Guardar imágenes como fondo PNG

El formato de salida predeterminado para guardar imágenes es SVG. Durante la conversión, algunas imágenes del PDF se transforman en imágenes vectoriales SVG. Esto podría ser lento. En su lugar, las imágenes podrían transformarse en un archivo de fondo PNG para cada página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### Especificar la carpeta de imágenes

También podemos especificar la carpeta a la que se guardarán las imágenes durante la conversión de PDF a HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### Crear archivos subsiguientes solo con el contenido del cuerpo

Recientemente, se nos pidió que introdujéramos una característica donde los archivos PDF se convierten a HTML y el usuario puede obtener solo el contenido de la etiqueta `<body>` para cada página. Esto produciría un archivo con detalles de CSS, `<html>`, `<head>` y todas las páginas en otros archivos solo con el contenido de `<body>`.

Para cumplir con este requisito, se introdujo una nueva propiedad, HtmlMarkupGenerationMode, en la clase HtmlSaveOptions.

Con el siguiente fragmento de código simple, puedes dividir la salida HTML en páginas. En las páginas de salida, todos los objetos HTML deben ir exactamente donde van ahora (procesamiento y salida de fuentes, creación y salida de CSS, creación y salida de imágenes), excepto que el HTML de salida contendrá contenidos actualmente colocados dentro de las etiquetas (ahora las etiquetas “body” serán omitidas). Sin embargo, al usar este enfoque, el enlace al CSS es responsabilidad de tu código, porque cosas como serán eliminadas. Para este propósito, puedes leer el CSS a través de File.ReadAllText() y enviarlo a través de AJAX a una página web donde se aplicará mediante jQuery.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### Renderizado de texto transparente

En caso de que el archivo PDF de origen/entrada contenga textos transparentes sombreados por imágenes de primer plano, entonces podría haber problemas de renderizado de texto. Así que, para atender tales escenarios, se pueden usar las propiedades SaveShadowedTextsAsTransparentTexts y SaveTransparentTexts.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### Renderizado de capas de documentos PDF

Podemos renderizar capas de documentos PDF en un elemento de tipo capa separado durante la conversión de PDF a HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```