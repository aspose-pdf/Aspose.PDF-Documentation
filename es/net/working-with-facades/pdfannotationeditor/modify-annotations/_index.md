---
title: Modificar Anotaciones en tu PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/modify-annotations/
description: Esta sección explica cómo modificar anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modify Annotations in your PDF",
    "alternativeHeadline": "Enhance Your PDF Annotations with New Modifications",
    "abstract": "La función Modificar Anotaciones permite a los usuarios editar fácilmente atributos clave de las anotaciones en archivos PDF utilizando Aspose.PDF Facades. Esta funcionalidad incluye cambiar el asunto, autor, color y más, junto con opciones para eliminar anotaciones por tipo, optimizando el proceso de gestión de anotaciones PDF. Optimiza tu flujo de trabajo PDF aprovechando estas poderosas capacidades de modificación de anotaciones.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "290",
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
    "url": "/net/modify-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modify-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Modificar anotación

[ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) método permite cambiar atributos básicos de una anotación, es decir, Asunto, Fecha de modificación, Autor, Color de anotación y Bandera de apertura. También puedes establecer el Autor directamente utilizando el método ModifyAnnotations. Esta clase también proporciona dos métodos sobrecargados para eliminar anotaciones. El primer método llamado DeleteAnnotations elimina todas las anotaciones de un archivo PDF.  

Por ejemplo, en el siguiente código, considera cambiar el autor en nuestra anotación utilizando [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotationsAuthor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Modify annotations author
        annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        // Save PDF document
        annotationEditor.Save(dataDir + "ModifyAnnotationsAuthor_out.pdf");
    }
}
```

El segundo método permite modificar anotaciones.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        // Create PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Create a new object of type Annotation
            TextAnnotation newTextAnnotation = new TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
            newTextAnnotation.Title = "Updated title";
            newTextAnnotation.Subject = "Updated subject";
            newTextAnnotation.Contents = "Updated sample contents for the annotation";
            // Modify annotations in the PDF file
            annotationEditor.ModifyAnnotations(1, 1, newTextAnnotation);
            // Save PDF document
            annotationEditor.Save(dataDir + "ModifyAnnotations_out.pdf");
        }
    }
}
```