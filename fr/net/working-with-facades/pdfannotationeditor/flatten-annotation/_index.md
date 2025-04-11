---
title: Aplatir l'annotation du PDF vers XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/flatten-annotation/
description: Cette section explique comment exporter des annotations d'un fichier PDF vers XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Flatten Annotation from PDF to XFDF",
    "alternativeHeadline": "Export PDF Annotations as Non-Editable XFDF Format",
    "abstract": "La fonctionnalité Aplatir l'annotation du PDF vers XFDF permet aux utilisateurs d'exporter des annotations de fichiers PDF au format XFDF tout en préservant leur représentation visuelle. Cette fonctionnalité garantit que les annotations restent visibles dans le document mais deviennent non modifiables, offrant un moyen d'appliquer de manière permanente des notes ou des commentaires pour les visualisateurs qui peuvent ne pas prendre en charge les fonctionnalités d'annotation.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "191",
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
    "url": "/net/flatten-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/flatten-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Le processus d'aplatissement signifie que lorsqu'une annotation est supprimée d'un document, sa représentation visuelle est conservée intacte. Une annotation aplatie est toujours visible mais n'est plus modifiable par vos utilisateurs ou par votre application. Cela peut être utilisé, par exemple, pour appliquer de manière permanente des annotations à votre document ou pour rendre les annotations visibles aux visualisateurs qui ne peuvent autrement pas afficher les annotations. Si cela n'est pas spécifié, une exportation conservera toutes les annotations telles qu'elles sont.

Lorsque cette option est sélectionnée, vos annotations seront incluses dans votre PDF exporté en tant qu'annotations standard PDF.

Vérifiez comment la méthode [flatteningAnnotations](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) utilisée dans l'extrait de code suivant. 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Create FlattenSettings
        var flattenSettings = new Aspose.Pdf.Forms.Form.FlattenSettings
        {
            ApplyRedactions = true,
            CallEvents = false,
            HideButtons = true,
            UpdateAppearances = true
        };
        annotationEditor.FlatteningAnnotations(flattenSettings);
        // Save PDF document
        annotationEditor.Save(dataDir + "FlattenAnnotation_out.pdf");
    }
}
```