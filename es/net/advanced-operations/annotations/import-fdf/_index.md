---
title: Importar anotaciones en formato FDF a PDF a través de C#
linktitle: Importar anotaciones en formato FDF a PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/import-fdf/
description: Utilice los métodos existentes Form.ImportFdf() o PdfAnnotationEditor.ImportAnnotationsFromFdf() para importar anotaciones en formato FDF a PDF con Aspose.PDF for .NET.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "Importe anotaciones en formato FDF a archivos PDF sin problemas utilizando Aspose.PDF for .NET, mejorando sus capacidades de gestión de PDF. Con los métodos Form.ImportFdf() y PdfAnnotationEditor.ImportAnnotationsFromFdf(), puede integrar sin esfuerzo los datos del formulario y los comentarios de archivos FDF ligeros en sus documentos PDF, agilizando los procesos de envío de datos y anotaciones.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

FDF (Forms Data Format) es un formato de archivo que almacena y transmite datos de formularios y anotaciones en documentos PDF. Es una versión ligera de PDF que contiene solo los valores de los campos del formulario o comentarios, sin el contenido completo del archivo PDF original. Los archivos FDF se utilizan a menudo al enviar datos de formularios a un servidor, o al intercambiar anotaciones sin necesidad de enviar todo el archivo PDF. Pueden ser importados de nuevo a un PDF para completar campos de formulario o aplicar comentarios.

{{% /alert %}}

La clase [PDFAnnotationEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfannotationeditor/) contiene métodos para trabajar con la importación de anotaciones desde un archivo FDF. El método [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) proporciona la funcionalidad para importar anotaciones de un documento FDF a un archivo PDF.

Además, la [Clase Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/) incluye el método [Form.ImportFdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/importfdf/) - importa el contenido de los campos del archivo FDF y los coloca en el nuevo PDF.

El siguiente fragmento de código le muestra cómo importar anotaciones en formato FDF a PDF con el método Form.ImportFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

El siguiente fragmento de código muestra cómo importar anotaciones en formato FDF a PDF con el método PdfAnnotationEditor.ImportAnnotationsFromFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```