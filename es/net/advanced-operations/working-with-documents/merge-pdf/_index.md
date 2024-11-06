---
title: Cómo fusionar PDF usando C#
linktitle: Fusionar archivos PDF
type: docs
weight: 50
url: es/net/merge-pdf-documents/
keywords: "merge multiple pdf into single pdf c#, combine multiple pdf into one c#, merge multiple pdf into one c#"
description: Esta página explica cómo fusionar documentos PDF en un único archivo PDF con C# o VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cómo fusionar PDF usando C#",
    "alternativeHeadline": "Combinar documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "manipulación de documentos PDF",
    "keywords": "pdf, c#, merge pdf, concatenate, combine pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta página explica cómo fusionar documentos PDF en un único archivo PDF con C# o VB.NET."
}
</script>
## Fusionar o combinar múltiples PDF en un único PDF en C#

Fusionar PDF en C# no es una tarea sencilla sin utilizar una biblioteca de terceros.
Este artículo muestra cómo fusionar múltiples archivos PDF en un único documento PDF utilizando Aspose.PDF para .NET. El ejemplo está escrito en C#, pero la API también puede ser utilizada en otros lenguajes de programación .NET como VB.NET. Los archivos PDF se fusionan de tal manera que el primero se une al final del otro documento.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Fusionar archivos PDF usando C# y DOM

Para concatenar dos archivos PDF:

1. Crea dos objetos [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), cada uno conteniendo uno de los archivos PDF de entrada.
1. Luego llama al método Add de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) para el objeto Document al que quieres añadir el otro archivo PDF.
1.
1. Finalmente, guarde el archivo PDF de salida utilizando el método [Guardar](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código muestra cómo concatenar archivos PDF.

```csharp
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Abrir el primer documento
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// Abrir el segundo documento
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// Agregar páginas del segundo documento al primero
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// Guardar el archivo de salida concatenado
pdfDocument1.Save(dataDir);
```

## Ejemplo en vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de fusión de presentaciones.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Ver también

- [Dividir PDF usando DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Dividir PDF usando DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Concatenar documentos PDF usando Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Dividir PDF usando Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

