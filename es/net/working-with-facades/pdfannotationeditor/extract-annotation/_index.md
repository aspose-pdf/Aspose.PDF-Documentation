---
title: Extraer Anotaciones de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/extract-annotation/
description: Esta sección explica cómo extraer anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Annotations from PDF",
    "alternativeHeadline": "Effortlessly Extract PDF Annotations to XFDF Format",
    "abstract": "Desbloquee el potencial de sus documentos PDF con la nueva función de Extraer Anotaciones, que permite la extracción sin problemas de anotaciones al formato XFDF utilizando Aspose.PDF for .NET. Esta funcionalidad permite la recuperación fácil de tipos específicos de anotaciones, mejorando la gestión de documentos y la eficiencia de colaboración. Descubra cómo optimizar sus flujos de trabajo PDF extrayendo y guardando datos de anotaciones importantes sin esfuerzo.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "254",
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
    "url": "/net/extract-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

[ExtractAnnotations](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) método permite extraer anotaciones de un archivo PDF. Para extraer anotaciones, necesita crear un objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfannotationeditor) y vincular el archivo PDF utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesita crear una enumeración de los tipos de anotaciones que desea extraer del archivo PDF.

Luego puede usar el método [ExtractAnnotations](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) para extraer las anotaciones a un ArrayList. Después de eso, puede recorrer esta lista y obtener anotaciones individuales. Y finalmente, guarde el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save) del objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfannotationeditor). El siguiente fragmento de código le muestra cómo extraer anotaciones de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Extract annotations
            var annotationTypes = new[] { Aspose.Pdf.Annotations.AnnotationType.FreeText, Aspose.Pdf.Annotations.AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
    }
}
```