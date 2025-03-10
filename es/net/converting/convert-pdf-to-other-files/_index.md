---
title: Convertir PDF a EPUB, LaTeX, Texto, XPS en C#
linktitle: Convertir PDF a otros formatos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /es/net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
description: Este tema te muestra cómo convertir un archivo PDF a otros formatos de archivo como EPUB, LaTeX, Texto, XPS, etc. utilizando C# o .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to EPUB, LaTeX, Text, XPS in C#",
    "alternativeHeadline": "Add PDF format conversion to EPUB, LaTeX, Text, XPS in C#",
    "abstract": "Aspose.PDF for .NET presenta una poderosa característica que permite la conversión sin problemas de archivos PDF a varios formatos, incluidos EPUB, LaTeX, Texto, XPS y Markdown. Esta funcionalidad mejora la accesibilidad y usabilidad de los documentos al permitir que los desarrolladores integren sin esfuerzo diversas conversiones de formatos de archivo en sus aplicaciones C#, atendiendo así a una audiencia más amplia y optimizando el contenido para diferentes plataformas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1419",
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
    "url": "/net/convert-pdf-to-other-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-other-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a EPUB con Aplicación Gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publicación Electrónica">EPUB</abbr>** es un estándar de libro electrónico gratuito y abierto del Foro Internacional de Publicación Digital (IDPF). Los archivos tienen la extensión .epub.
EPUB está diseñado para contenido refluido, lo que significa que un lector de EPUB puede optimizar el texto para un dispositivo de visualización particular. EPUB también admite contenido de diseño fijo. El formato está destinado a ser un formato único que los editores y las casas de conversión pueden usar internamente, así como para distribución y venta. Sustituye el estándar Open eBook.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Aspose.PDF for .NET también admite la función de convertir documentos PDF a formato EPUB. Aspose.PDF for .NET tiene una clase llamada EpubSaveOptions que se puede usar como el segundo argumento del método [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para generar un archivo EPUB.
Por favor, intenta usar el siguiente fragmento de código para cumplir con este requisito con C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoEPUB()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToEPUB.pdf"))
    {
        // Instantiate Epub Save options
        EpubSaveOptions options = new EpubSaveOptions();
        // Specify the layout for contents
        options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;

        // Save ePUB document
        document.Save(dataDir + "PDFToEPUB_out.epub", options);
    }
}
```

## Convertir PDF a LaTeX/TeX

**Aspose.PDF for .NET** admite la conversión de PDF a LaTeX/TeX.
El formato de archivo LaTeX es un formato de archivo de texto con un marcado especial y se utiliza en sistemas de preparación de documentos basados en TeX para una tipografía de alta calidad.

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a LaTeX/TeX con Aplicación Gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) que proporciona la propiedad OutDirectoryPath para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de conversión de archivos PDF al formato TEX con C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTeX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf"))
    {
        // Instantiate LaTex save option          
        LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

        // Specify the output directory
        string pathToOutputDirectory = dataDir;

        // Set the output directory path for save option object
        saveOptions.OutDirectoryPath = pathToOutputDirectory;

        // Save PDF document into LaTex format           
        document.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
    }
}
```

## Convertir PDF a Texto

**Aspose.PDF for .NET** admite la conversión de todo el documento PDF y de una sola página a un archivo de Texto.

### Convertir todo el documento PDF a archivo de Texto

Puedes convertir un documento PDF a un archivo TXT utilizando el método [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) de la clase [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        ta.Visit(document);

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt",ta.Text);
    }
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a Texto en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a Texto con Aplicación Gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convertir página PDF a archivo de texto

Puedes convertir un documento PDF a un archivo TXT con Aspose.PDF for .NET. Debes usar el método `Visit` de la clase `TextAbsorber` para resolver esta tarea.

El siguiente fragmento de código explica cómo extraer los textos de páginas particulares.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        var pages = new [] {1, 3, 4};
        foreach (var page in pages)
        {
            ta.Visit(document.Pages[page]);
        }
    
        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", ta.Text);
    }
}
```

## Convertir PDF a XPS

**Aspose.PDF for .NET** ofrece la posibilidad de convertir archivos PDF a formato <abbr title="Especificación de Papel XML">XPS</abbr>. Intentemos usar el fragmento de código presentado para convertir archivos PDF a formato XPS con C#.

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a XPS con Aplicación Gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

El tipo de archivo XPS está asociado principalmente con la Especificación de Papel XML de Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente conocida como Metro y que abarca el concepto de marketing del Camino de Impresión de Nueva Generación (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) que se utiliza como el segundo argumento del método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para generar el archivo XPS.

Desde la versión 24.2, Aspose.PDF ha implementado la conversión de PDF Buscable a XPS mientras mantiene el Texto Seleccionable en el XPS resultante. Para preservar el texto, es necesario establecer la propiedad XpsSaveOptions.SaveTransparentTexts en true.

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF al formato XPS.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoXPS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var xpsOptions = new XpsSaveOptions
        {
            SaveTransparentTexts = true
        };

        // Save XPS document
        document.Save(dataDir + "PDFtoXPS_out.xps", xpsOptions);
    }
}
```

## Convertir PDF a Markdown

**Aspose.PDF for .NET** ofrece la posibilidad de convertir archivos PDF a formato <abbr title="Markdown">MD</abbr>. Intentemos usar el fragmento de código presentado para convertir archivos PDF a formato MD con C#.

Markdown es un lenguaje de marcado ligero diseñado para representar el formato de texto plano con la máxima legibilidad humana y legibilidad por máquina para lenguajes de publicación avanzados.

### Optimizar el uso de imágenes mediante el convertidor de PDF a Markdown

Puedes notar que en directorios con imágenes, el número de imágenes es menor que el número de imágenes en archivos PDF.

Dado que el archivo markdown no puede establecer el tamaño de la imagen, sin la opción MarkdownSaveOptions.UseImageHtmlTag, el mismo tipo de imágenes con diferentes tamaños se guardan como diferentes.

Para la opción habilitada MarkdownSaveOptions.UseImageHtmlTag se guardarán imágenes únicas, que se escalan en el documento mediante la etiqueta img.

El código abre un documento PDF, configura los parámetros para convertirlo a un archivo Markdown (guardando cualquier imagen en la carpeta llamada "images") y guarda el archivo Markdown resultante en la ruta de salida especificada.

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF al formato MD.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        }
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options   
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

### Convertir PDF a MobiXml

MobiXML es un formato de eBook popular, diseñado para ser utilizado en plataformas móviles.
El siguiente fragmento de código explica cómo convertir un documento PDF a un archivo MobiXML.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void ConvertPdfToMobiXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToXML.pdf"))
    {
        // Save PDF document in XML format
        document.Save(dataDir + "PDFToXML_out.xml", Aspose.Pdf.SaveFormat.MobiXml);
    }
}
```