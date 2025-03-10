---
title: Extraire des annotations d'un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/extract-annotation/
description: Cette section explique comment extraire des annotations d'un fichier PDF vers XFDF avec Aspose.PDF Facades.
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
    "abstract": "Déverrouillez le potentiel de vos documents PDF avec la nouvelle fonctionnalité d'extraction d'annotations, qui permet une extraction transparente des annotations au format XFDF en utilisant Aspose.PDF for .NET. Cette fonctionnalité permet une récupération facile de types d'annotations spécifiques, améliorant l'efficacité de la gestion des documents et de la collaboration. Découvrez comment rationaliser vos flux de travail PDF en extrayant et en enregistrant facilement des données d'annotations importantes.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

La méthode [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) vous permet d'extraire des annotations d'un fichier PDF. Pour extraire des annotations, vous devez créer un objet [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) et lier le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez extraire du fichier PDF.

Vous pouvez ensuite utiliser la méthode [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) pour extraire les annotations dans un ArrayList. Après cela, vous pouvez parcourir cette liste et obtenir des annotations individuelles. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de l'objet [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor). Le code suivant vous montre comment extraire des annotations d'un fichier PDF.

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