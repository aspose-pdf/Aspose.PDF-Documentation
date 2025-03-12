---
title: Enregistrer un document PDF par programmation
linktitle: Enregistrer PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/save-pdf-document/
description: Apprenez à enregistrer un fichier PDF dans la bibliothèque PDF C# Aspose.PDF for .NET. Enregistrez le document PDF dans le système de fichiers, dans un flux et dans des applications Web.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "Découvrez comment les développeurs enregistrent par programmation des documents PDF avec facilité en utilisant Aspose.PDF for .NET. Cette fonctionnalité prend en charge l'enregistrement des PDF dans le système de fichiers, les flux et directement dans les applications Web, s'adaptant à divers cas d'utilisation tout en garantissant la conformité aux normes PDF/A et PDF/X pour l'archivage à long terme et l'échange graphique. Optimisez vos capacités de gestion des PDF avec ce mécanisme d'enregistrement robuste.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

Le prochain extrait de code fonctionne également avec la bibliothèque [Aspose.Drawing](/pdf/fr/net/drawing/).

## Enregistrer un document PDF dans le système de fichiers

Vous pouvez enregistrer le document PDF créé ou manipulé dans le système de fichiers en utilisant la méthode `Save` de la classe `Document`.
Lorsque vous ne fournissez pas le type de format (options), le document est enregistré au format Aspose.PDF v.1.7 (*.pdf).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## Enregistrer un document PDF dans un flux

Vous pouvez également enregistrer le document PDF créé ou manipulé dans un flux en utilisant les surcharges des méthodes `Save`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

Pour une explication plus détaillée, veuillez vous rendre à la section [Showcase](/pdf/fr/net/showcases/).

## Enregistrer au format PDF/A ou PDF/X

PDF/A est une version normalisée ISO du format de document portable (PDF) à utiliser dans l'archivage et la préservation à long terme des documents électroniques.
PDF/A diffère du PDF en ce qu'il interdit les fonctionnalités non adaptées à l'archivage à long terme, telles que le lien de police (par opposition à l'incorporation de police) et le cryptage. Les exigences ISO pour les visionneuses PDF/A incluent des directives de gestion des couleurs, un support des polices intégrées et une interface utilisateur pour lire les annotations intégrées.

PDF/X est un sous-ensemble de la norme ISO PDF. Le but de PDF/X est de faciliter l'échange graphique, et il a donc une série d'exigences liées à l'impression qui ne s'appliquent pas aux fichiers PDF standard.

Dans les deux cas, la méthode `Save` est utilisée pour stocker les documents, tandis que les documents doivent être préparés en utilisant la méthode `Convert`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```