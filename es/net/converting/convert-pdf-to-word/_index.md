---
title: Convertir PDF a Documentos de Microsoft Word en .NET
linktitle: Convertir PDF a Word
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Aprende cómo escribir código C# para la conversión de formatos PDF a Microsoft Word con Aspose.PDF for .NET. y ajustar la conversión de PDF a DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET presenta una poderosa función para convertir archivos PDF a formatos de Microsoft Word (DOC y DOCX) usando C#. Esta funcionalidad no solo mejora la edición de documentos, sino que también proporciona opciones flexibles para el reconocimiento y formato de texto, asegurando alta fidelidad entre el PDF de origen y el documento de Word resultante.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1495",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Resumen

Este artículo explica cómo **convertir PDF a Documentos de Microsoft Word usando C#**. Cubre estos temas.

_Formato_: **DOC**

- [C# PDF a DOC](#csharp-pdf-to-doc)
- [C# Convertir PDF a DOC](#csharp-pdf-to-doc)
- [C# Cómo convertir archivo PDF a DOC](#csharp-pdf-to-doc)

_Formato_: **DOCX**

- [C# PDF a DOCX](#csharp-pdf-to-docx)
- [C# Convertir PDF a DOCX](#csharp-pdf-to-docx)
- [C# Cómo convertir archivo PDF a DOCX](#csharp-pdf-to-docx)

_Formato_: **Word**

- [C# PDF a Word](#csharp-pdf-to-docx)
- [C# Convertir PDF a Word](#csharp-pdf-to-doc)
- [C# Cómo convertir archivo PDF a Word](#csharp-pdf-to-docx)

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Conversión de PDF a DOC y DOCX

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, que facilita la gestión de contenido. **Aspose.PDF for .NET** te permite convertir archivos PDF a formato DOC y DOCX de manera rápida y eficiente.

## Convertir archivo PDF a DOC (Microsoft Word 97-2003)

Convierte archivos PDF a formato DOC con facilidad y control total. Aspose.PDF for .NET es flexible y admite una amplia variedad de conversiones. Convertir páginas de documentos PDF a imágenes, por ejemplo, es una característica muy popular.

Muchos de nuestros clientes han solicitado una conversión de PDF a DOC: convertir un archivo PDF a un documento de Microsoft Word. Los clientes quieren esto porque los archivos PDF no se pueden editar fácilmente, mientras que los documentos de Word sí. Algunas empresas quieren que sus usuarios puedan manipular texto, tablas e imágenes en archivos que comenzaron como PDFs.

Manteniendo viva la tradición de hacer las cosas simples y comprensibles, Aspose.PDF for .NET te permite transformar un archivo PDF de origen en un archivo DOC con dos líneas de código. Para lograr esta función, hemos introducido una enumeración llamada SaveFormat y su valor .Doc te permite guardar el archivo de origen en formato de Microsoft Word.

El siguiente fragmento de código C# muestra cómo convertir un archivo PDF en formato DOC.

<a name="csharp-pdf-to-doc"><strong>Pasos: Convertir PDF a DOC en C#</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) con el documento PDF de origen.
2. Guárdalo en formato **SaveFormat.Doc** llamando al método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### Usando la Clase DocSaveOptions

La clase [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) proporciona numerosas propiedades que mejoran la conversión de archivos PDF a formato DOC. Entre estas propiedades, Mode te permite especificar el modo de reconocimiento para el contenido PDF. Puedes seleccionar cualquier valor de la enumeración RecognitionMode para esta propiedad. Cada uno de estos valores tiene beneficios y limitaciones específicas:

- El modo [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) es rápido y bueno para preservar la apariencia original del archivo PDF, pero la editabilidad del documento resultante podría ser limitada. Cada bloque de texto visualmente agrupado en el PDF original se convierte en un cuadro de texto en el documento de salida. Esto logra una máxima semejanza con el original, por lo que el documento de salida se ve bien, pero consiste completamente en cuadros de texto, que podrían ser editados en Microsoft Word, lo cual es bastante complicado.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) es el modo de reconocimiento completo, donde el motor realiza agrupamiento y análisis multinivel para restaurar el documento original según la intención del autor mientras produce un documento fácilmente editable. La limitación es que el documento de salida podría verse diferente del original.

La propiedad [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) se puede usar para controlar la proximidad relativa entre elementos textuales. Esto significa que la distancia se normaliza por el tamaño de la fuente. Las fuentes más grandes pueden tener espacios más grandes entre las sílabas y aún ser consideradas un todo único. Se especifica como un porcentaje del tamaño de la fuente; por ejemplo, 1 = 100%. Esto significa que dos caracteres de 12pt colocados a 12 pt de distancia son proximales.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) se utiliza para activar el reconocimiento de viñetas durante la conversión.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes investigar la funcionalidad y calidad con la que trabaja.

[![Convertir PDF a DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir archivo PDF a DOCX (Microsoft Word 2007-2024)

La API de Aspose.PDF for .NET te permite leer y convertir documentos PDF a DOCX usando C# y cualquier lenguaje .NET. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura cambió de binaria simple a una combinación de archivos XML y binarios. Los archivos Docx se pueden abrir con Word 2007 y versiones posteriores, pero no con versiones anteriores de MS Word, que admiten extensiones de archivo DOC.

El siguiente fragmento de código C# muestra cómo convertir un archivo PDF en formato DOCX.

<a name="csharp-pdf-to-docx"><strong>Pasos: Convertir PDF a DOCX en C#</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) con el documento PDF de origen.
2. Guárdalo en formato **SaveFormat.DocX** llamando al método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### Convertir PDF a DOCX en Modo Mejorado

Para obtener mejores resultados en la conversión de PDF a DOCX, puedes usar el modo `EnhancedFlow`.
La principal diferencia entre Flow y Enhanced Flow es que las tablas (tanto con como sin bordes) se reconocen como tablas reales, no como texto con una imagen de fondo.
También hay reconocimiento de listas numeradas y muchas otras cosas menores.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puedes investigar la funcionalidad y calidad con la que trabaja.

[![Aplicación gratuita de conversión PDF a Word de Aspose.PDF](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que los anteriores.

_Formato_: **Word**

- [C# PDF a Código de Word](#csharp-pdf-to-docx)
- [C# PDF a API de Word](#csharp-pdf-to-docx)
- [C# PDF a Word Programáticamente](#csharp-pdf-to-docx)
- [C# PDF a Biblioteca de Word](#csharp-pdf-to-docx)
- [C# Guardar PDF como Word](#csharp-pdf-to-docx)
- [C# Generar Word desde PDF](#csharp-pdf-to-docx)
- [C# Crear Word desde PDF](#csharp-pdf-to-docx)
- [C# Convertidor de PDF a Word](#csharp-pdf-to-docx)

_Formato_: **DOC**

- [C# PDF a Código de DOC](#csharp-pdf-to-doc)
- [C# PDF a API de DOC](#csharp-pdf-to-doc)
- [C# PDF a DOC Programáticamente](#csharp-pdf-to-doc)
- [C# PDF a Biblioteca de DOC](#csharp-pdf-to-doc)
- [C# Guardar PDF como DOC](#csharp-pdf-to-doc)
- [C# Generar DOC desde PDF](#csharp-pdf-to-doc)
- [C# Crear DOC desde PDF](#csharp-pdf-to-doc)
- [C# Convertidor de PDF a DOC](#csharp-pdf-to-doc)

_Formato_: **DOCX**

- [C# PDF a Código de DOCX](#csharp-pdf-to-docx)
- [C# PDF a API de DOCX](#csharp-pdf-to-docx)
- [C# PDF a DOCX Programáticamente](#csharp-pdf-to-docx)
- [C# PDF a Biblioteca de DOCX](#csharp-pdf-to-docx)
- [C# Guardar PDF como DOCX](#csharp-pdf-to-docx)
- [C# Generar DOCX desde PDF](#csharp-pdf-to-docx)
- [C# Crear DOCX desde PDF](#csharp-pdf-to-docx)
- [C# Convertidor de PDF a DOCX](#csharp-pdf-to-docx)