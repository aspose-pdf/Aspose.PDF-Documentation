---
title: Importar y Exportar Anotaciones a XFDF
linktitle: Importar y Exportar Anotaciones a XFDF
type: docs
weight: 40
url: es/net/import-export-xfdf/
description: Puede importar y exportar anotaciones en formato XFDF con C# y la biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Importar y Exportar Anotaciones a XFDF",
    "alternativeHeadline": "Métodos para importar y exportar datos de anotaciones a archivos XFDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, importar exportar a XFDF",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Puede importar y exportar anotaciones en formato XFDF con C# y la biblioteca Aspose.PDF para .NET."
}
</script>
{{% alert color="primary" %}}

XFDF significa Formato de Datos de Formularios XML. Es un formato de archivo basado en XML. Este formato de archivo se utiliza para representar datos de formulario o anotaciones contenidas en un formulario PDF. XFDF puede ser usado para muchos propósitos diferentes, pero en nuestro caso, se puede usar para enviar o recibir datos de formulario o anotaciones a otros computadores o servidores, etc., o se puede usar para archivar los datos del formulario o las anotaciones. En este artículo, veremos cómo Aspose.Pdf.Facades ha tomado en cuenta este concepto y cómo podemos importar y exportar datos de anotaciones a archivos XFDF.

{{% /alert %}}

**Aspose.PDF for .NET** es un componente rico en características cuando se trata de editar documentos PDF. Como sabemos, XFDF es un aspecto importante de la manipulación de formularios PDF, el espacio de nombres Aspose.Pdf.Facades en Aspose.PDF for .NET ha considerado esto muy bien y ha proporcionado métodos para importar y exportar datos de anotaciones a archivos XFDF.

La clase [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contiene dos métodos para trabajar con la importación y exportación de anotaciones a archivos XFDF.
[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) la clase contiene dos métodos para trabajar con la importación y exportación de anotaciones a un archivo XFDF.

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente fragmento de código te muestra cómo exportar anotaciones a un archivo XFDF:

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // La ruta al directorio de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// Importando anotaciones desde archivo XFDF
        /// Archivo en Formato de Datos de Formulario XML (XFDF) creado por Adobe Acrobat, una aplicación de autoría de PDF;
        /// almacena descripciones de elementos de formulario de página y sus valores, como los nombres y valores para
        /// campos de texto; utilizado para guardar datos de formulario que pueden ser importados en un documento PDF.
        /// Puedes importar datos de anotación desde el archivo XFDF a PDF usando
        /// el método ImportAnnotationsFromXfdf en la clase PdfAnnotationEditor.
        /// </summary>

        public static void ExportAnnotationXFDF()
        {
            // Crear objeto PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // Vincular documento PDF al Editor de Anotaciones
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));

            // Exportar anotaciones
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
El siguiente fragmento de código describe cómo importar anotaciones a un archivo XFDF:

```csharp
public static void ImportAnnotationXFDF()
{
    // Crear objeto PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Crear un nuevo documento PDF
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importar anotación
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Guardar el PDF de salida
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Otra manera de exportar/importar anotaciones de una sola vez

En el código a continuación, un método ImportAnnotations permite importar anotaciones directamente desde otro documento PDF.

```csharp
        /// <summary>
        /// El método ImportAnnotations permite importar anotaciones directamente desde otro documento PDF
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // Crear objeto PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // Crear un nuevo documento PDF
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // El Editor de Anotaciones permite importar anotaciones de varios documentos PDF,
            // pero en este ejemplo, usamos solo uno.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // Guardar el PDF de salida
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
        }
    }
}
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destacado",
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
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/captura-de-pantalla.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```
Por supuesto, necesitaría ver el contenido del documento para proceder con la traducción al español mientras mantengo el formato original en markdown. Por favor, proporciona el texto o el documento que necesitas traducir.
