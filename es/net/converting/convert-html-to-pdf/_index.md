---
title: Convertir HTML a PDF en .NET
linktitle: Convertir archivo HTML a PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Este tema te muestra cómo convertir HTML a PDF y MHTML a PDF usando Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "La función de conversión en Aspose.PDF for .NET permite la transformación sin problemas de documentos HTML y MHTML en archivos PDF de alta calidad. Con opciones de personalización avanzadas, los usuarios pueden controlar la incrustación de fuentes, consultas de medios y gestión de recursos externos, asegurando que las páginas web o archivos HTML locales se representen con precisión en formato PDF con flexibilidad adaptada a sus necesidades específicas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1980",
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
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Resumen 

Este artículo explica cómo **convertir HTML a PDF usando C#**. Cubre los siguientes temas.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

- [Convertir HTML a PDF](#csharp-html-to-pdf)
- [Convertir Página Web a PDF](#csharp-webpage-to-pdf)
- [Convertir MHTML a PDF](#csharp-mhtml-to-pdf)

**Aspose.PDF for .NET** es una API de manipulación de PDF que te permite convertir cualquier documento HTML existente a PDF sin problemas. El proceso de conversión de HTML a PDF se puede personalizar de manera flexible.

## Convertir HTML a PDF

El siguiente ejemplo de código C# muestra cómo convertir un documento HTML a un PDF.

<a name="csharp-html-to-pdf"><strong>Convertir HTML a PDF</strong></a>

1. Crea una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions/).
2. Inicializa el objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/).
3. Guarda el documento PDF de salida llamando al método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Intenta convertir HTML a PDF en línea**

Aspose te presenta una aplicación gratuita en línea ["HTML a PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión HTML a PDF usando la aplicación gratuita](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Conversión avanzada de HTML a PDF

El motor de conversión HTML tiene varias opciones que nos permiten controlar el proceso de conversión.

### Soporte para consultas de medios

Las consultas de medios son una técnica popular para ofrecer una hoja de estilo adaptada a diferentes dispositivos. Podemos establecer el tipo de dispositivo utilizando la propiedad [`HtmlMediaType`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### Habilitar (deshabilitar) la incrustación de fuentes

Las páginas HTML a menudo utilizan fuentes (por ejemplo, fuentes de la carpeta local, Google Fonts, etc.). También podemos controlar la incrustación de fuentes en un documento utilizando la propiedad [`IsEmbedFonts`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### Gestionar la carga de recursos externos

El motor de conversión proporciona un mecanismo que te permite controlar la carga de ciertos recursos asociados con el documento HTML. La clase [`HtmlLoadOptions`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions) tiene la propiedad [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) con la que podemos definir el comportamiento del cargador de recursos. Supongamos que necesitamos reemplazar todas las imágenes PNG con una sola imagen `test.jpg` y reemplazar la URL externa por interna para otros recursos. Para hacer esto, podemos definir un cargador personalizado `SamePictureLoader` y apuntar [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) a este nombre.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## Convertir Página Web a PDF

Convertir una página web es ligeramente diferente de convertir un documento HTML local. Para convertir el contenido de una página web a formato PDF, primero podemos obtener el contenido de la página HTML utilizando una instancia de HttpClient, crear un objeto Stream, pasar el contenido al objeto Document y renderizar la salida en formato PDF.

Al convertir una página web alojada en un servidor web a PDF:

<a name="csharp-webpage-to-pdf"><strong>Convertir Página Web a PDF</strong></a>

1. Lee el contenido de la página utilizando un objeto HttpClient.
1. Instancia el objeto [HtmlLoadOptions](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions) y establece la URL base.
1. Inicializa un objeto Document pasando el objeto stream.
1. Opcionalmente, establece el tamaño de la página y/o la orientación.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Proporcionar credenciales para la conversión de Página Web a PDF

A veces necesitamos realizar la conversión de archivos HTML que requieren autenticación y privilegios de acceso, de modo que solo los usuarios auténticos puedan obtener el contenido de la página. También incluye el escenario en el que algunos recursos/datos referenciados dentro de HTML se obtienen de algún servidor externo que requiere autenticación y, para atender este requisito, se ha añadido la propiedad [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) a la clase [`HtmlLoadOptions`](https://reference.aspose.com/pdf/es/net/aspose.pdf/htmlloadoptions). El siguiente fragmento de código muestra los pasos para pasar credenciales para solicitar HTML y sus respectivos recursos mientras se convierte un archivo HTML a PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Renderizar todo el contenido HTML en una sola página

Aspose.PDF for .NET proporciona la capacidad de renderizar todo el contenido en una sola página al convertir un archivo HTML a formato PDF. Por ejemplo, si tienes algún contenido HTML cuyo tamaño de salida es mayor que una página, puedes usar la opción para renderizar los datos de salida en una sola página PDF. Para usar esta opción, la clase HtmlLoadOptions se amplió con la bandera IsRenderToSinglePage. El siguiente fragmento de código muestra cómo usar esta funcionalidad.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### Renderizar HTML con datos SVG

Aspose.PDF for .NET proporciona la capacidad de convertir una página HTML a un documento PDF. Dado que HTML permite agregar elementos gráficos SVG como una etiqueta en la página, Aspose.PDF también admite la conversión de dichos datos en el archivo PDF resultante. El siguiente fragmento de código muestra cómo convertir archivos HTML con etiquetas gráficas SVG a Documentos PDF Etiquetados.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## Convertir MHTML a PDF 

{{% alert color="success" %}}
**Intenta convertir MHTML a PDF en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["MHTML a PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión MHTML a PDF usando la aplicación gratuita](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, abreviatura de MIME HTML, es un formato de archivo de archivo de página web utilizado para combinar recursos que normalmente se representan mediante enlaces externos (como imágenes, animaciones Flash, applets de Java y archivos de audio) con código HTML en un solo archivo. El contenido de un archivo MHTML está codificado como si fuera un mensaje de correo electrónico HTML, utilizando el tipo MIME multipart/related. Aspose.PDF for .NET puede convertir archivos HTML a formato PDF y con el lanzamiento de Aspose.PDF for .NET 9.0.0, hemos introducido una nueva función que te permite convertir archivos MHTML a formato PDF. El siguiente fragmento de código muestra cómo convertir archivos MHTML a formato PDF con C#:

<a name="csharp-mhtml-to-pdf"><strong>Convertir MHTML a PDF</strong></a>

1. Crea una instancia de la clase [MhtLoadOptions](https://reference.aspose.com/pdf/es/net/aspose.pdf/mhtloadoptions/).
2. Inicializa el objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/).
3. Guarda el documento PDF de salida llamando al método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```