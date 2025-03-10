---
title: Importar y Exportar Anotaciones a XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/import-export-annotations/
description: Esta sección explica cómo importar y exportar anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Import and Export PDF Annotations with XFDF",
    "abstract": "Aspose.PDF for .NET introduce una poderosa funcionalidad para importar y exportar anotaciones a XFDF, mejorando las capacidades de manipulación de PDF. Esta característica permite a los usuarios transferir selectivamente datos de anotaciones en formato XML Forms Data Format, permitiendo una integración y archivo sin problemas para una mejor gestión de documentos. Con métodos dedicados para especificar tipos de anotaciones, los usuarios pueden gestionar eficientemente sus anotaciones PDF con precisión",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/import-export-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

XFDF significa XML Forms Data Format. Es un formato de archivo basado en XML. Este formato de archivo se utiliza para representar datos de formularios o anotaciones contenidas en un formulario PDF. XFDF se puede utilizar para muchos propósitos diferentes, pero en nuestro caso, se puede utilizar para enviar o recibir datos de formularios o anotaciones a otros ordenadores o servidores, etc., o se puede utilizar para archivar los datos de formularios o anotaciones. En este artículo, veremos cómo Aspose.Pdf.Facades ha tenido en cuenta este concepto y cómo podemos importar y exportar datos de anotaciones a un archivo XFDF.

## Importando y Exportando Anotaciones a XFDF

[Aspose.PDF for .NET](/pdf/net/) es un componente rico en características cuando se trata de editar documentos PDF. Como sabemos, XFDF es un aspecto importante de la manipulación de formularios PDF, el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF for .NET](/pdf/net/) lo ha considerado muy bien y ha proporcionado métodos para importar y exportar datos de anotaciones a archivos XFDF.

La clase [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contiene dos métodos para trabajar con la importación y exportación de anotaciones a un archivo XFDF. El método [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) proporciona la funcionalidad para exportar anotaciones de un documento PDF a un archivo XFDF, mientras que el método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) permite importar anotaciones de un archivo XFDF existente. Para importar o exportar anotaciones, necesitamos especificar los tipos de anotaciones. Podemos especificar estos tipos en forma de una enumeración y luego pasar esta enumeración como un argumento a cualquiera de estos métodos. De esta manera, solo se importarán o exportarán las anotaciones de los tipos especificados a un archivo XFDF.

El siguiente fragmento de código muestra cómo importar anotaciones a un archivo XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Sources of PDF with annotations           
    var sources = new string[] { dataDir + "ImportAnnotations.pdf" };
            
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "input.pdf");
        annotationEditor.ImportAnnotations(sources);
        // Save PDF document
        annotationEditor.Save(dataDir + "ImportAnnotations_out.pdf");
    }
}
```

El siguiente fragmento de código describe cómo importar/exportar anotaciones a un archivo XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
        }

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "exportannotations_out.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_out.pdf");
        }
    }
}
```

De esta manera, solo se importarán o exportarán las anotaciones de los tipos especificados a un archivo XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");

        // Export annotations
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            var annotationTypes = new[] {AnnotationType.FreeText, AnnotationType.Text};
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 1, 5, annotationTypes);
        }

        // Import annotations
        using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "annotations.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_XFDF02_out.pdf");
        }
    }
}
```