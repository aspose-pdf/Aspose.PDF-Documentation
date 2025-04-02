---
title: Cómo crear PDF usando C#
linktitle: Crear documento PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/create-pdf-document/
description: Crear y formatear el documento PDF con Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "La nueva funcionalidad en Aspose.PDF for .NET permite a los desarrolladores crear y formatear documentos PDF sin esfuerzo utilizando C#. Con esta API intuitiva, los usuarios pueden generar PDFs buscables, manipular contenido etiquetado para accesibilidad e integrar sin problemas la generación de PDF en varias aplicaciones .NET, mejorando la productividad y optimizando los flujos de trabajo.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Crear y formatear el documento PDF con Aspose.PDF for .NET."
}
</script>

Siempre estamos buscando una manera de generar documentos PDF y trabajar con ellos en proyectos de C# de manera más exacta, precisa y efectiva. Tener funciones fáciles de usar de una biblioteca nos permite concentrarnos más en el trabajo y menos en los detalles que consumen tiempo al intentar generar PDFs, ya sea en .NET.

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Crear (o generar) documento PDF usando el lenguaje C#

La API de Aspose.PDF for .NET te permite crear y leer archivos PDF usando C# y VB.NET. La API se puede utilizar en una variedad de aplicaciones .NET, incluyendo WinForms, ASP.NET y varias otras. En este artículo, vamos a mostrar cómo usar la API de Aspose.PDF for .NET para generar y leer archivos PDF fácilmente en aplicaciones .NET.

### Cómo crear un archivo PDF simple

Para crear un archivo PDF usando C#, se pueden seguir los siguientes pasos.

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document).
1. Agregar un objeto [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page) a la colección [Pages](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/properties/pages) del objeto Document.
1. Agregar [TextFragment](https://reference.aspose.com/pdf/es/net/aspose.pdf.text/textfragment) a la colección [Paragraphs](https://reference.aspose.com/pdf/es/net/aspose.pdf/page/properties/paragraphs) de la página.
1. Guardar el documento PDF resultante.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHelloWorldDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

### Cómo crear un documento PDF buscable

Aspose.PDF for .NET proporciona la función para crear y manipular documentos PDF existentes. Al agregar elementos de texto dentro del archivo PDF, el PDF resultante es buscable. Sin embargo, si estamos convirtiendo una imagen que contiene texto a un archivo PDF, el contenido dentro del PDF no es buscable. Sin embargo, como solución alternativa, podemos usar OCR sobre el archivo resultante, para que se vuelva buscable.

Esta lógica especificada a continuación reconoce texto para imágenes PDF. Para el reconocimiento, puedes usar soportes externos de OCR que cumplan con el estándar HOCR. Para fines de prueba, hemos utilizado un OCR gratuito de Google Tesseract. Por lo tanto, primero necesitas instalar Tesseract-OCR en tu sistema, y tendrás la aplicación de consola de Tesseract.

El siguiente es el código completo para cumplir con este requisito:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateSearchableDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchableDocument.pdf"))
    {
        document.Convert(CallBackGetHocr);

        // Save PDF document
        document.Save(dataDir + "SearchableDocument_out.pdf");
    }
}

private static string CallBackGetHocr(System.Drawing.Image img)
{
    var tmpFile = Path.GetTempFileName();
    try
    {
        using (var bmp = new System.Drawing.Bitmap(img))
        {
            bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        }

        var inputFile = string.Concat('"', tmpFile, '"');
        var outputFile = string.Concat('"', tmpFile, '"');
        var arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        var tesseractProcessName = RunExamples.GetTesseractExePath();

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
            CreateNoWindow = true,
            WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
            WorkingDirectory = Path.GetDirectoryName(tesseractProcessName)
        };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### Cómo crear un PDF accesible usando funciones de bajo nivel

Este fragmento de código trabaja con un documento PDF y su contenido etiquetado, utilizando una biblioteca Aspose.PDF para procesarlo.

El ejemplo crea un nuevo elemento span en el contenido etiquetado de la primera página de un PDF, encuentra todos los elementos BDC y los asocia con el span. El documento modificado se guarda luego.

Puedes crear una declaración bdc especificando mcid, lang y texto de expansión usando el objeto BDCProperties:

```cs
var bdc = new Aspose.Pdf.Operators.BDC("P", new Aspose.Pdf.Facades.BDCProperties(1, "de", "Hallo, welt!"));
```

Después de crear el árbol de estructura, es posible vincular el operador BDC al elemento especificado de la estructura con el método Tag en el objeto del elemento:

```cs
Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

Pasos para crear un PDF accesible:

1. Cargar el documento PDF.
1. Acceder al contenido etiquetado.
1. Crear un elemento Span.
1. Agregar Span al elemento raíz.
1. Iterar sobre el contenido de la página.
1. Verificar elementos BDC y etiquetarlos.
1. Guardar el documento modificado.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create a span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

Este código modifica un PDF creando un elemento span dentro del contenido etiquetado del documento y etiquetando contenido específico (operaciones BDC) de la primera página con este span. El PDF modificado se guarda luego en un nuevo archivo.

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