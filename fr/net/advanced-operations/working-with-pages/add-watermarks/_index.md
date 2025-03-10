---
title: Ajouter un filigrane à un PDF en utilisant C#
linktitle: Ajouter un filigrane
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /fr/net/add-watermarks/
description: Cet article explique les fonctionnalités de travail avec des artefacts et l'obtention de filigranes dans des PDF en utilisant programmatique le C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "La nouvelle fonctionnalité dans Aspose.PDF for .NET permet aux développeurs d'ajouter programmatique des filigranes personnalisables aux documents PDF en utilisant la fonctionnalité d'artefact. Cette fonctionnalité améliore la gestion des documents en prenant en charge diverses propriétés d'artefact, y compris le type, l'opacité, la rotation et la personnalisation du texte, permettant aux utilisateurs de créer facilement des fichiers PDF professionnels et identifiables.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "Cet article explique les fonctionnalités de travail avec des artefacts et l'obtention de filigranes dans des PDF en utilisant programmatique le C#."
}
</script>

**Aspose.PDF for .NET** permet d'ajouter des filigranes à votre document PDF en utilisant des artefacts. Veuillez consulter cet article pour résoudre votre tâche.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Un filigrane créé avec Adobe Acrobat est appelé un artefact (comme décrit dans 14.8.2.2 Contenu réel et artefacts de la spécification PDF). Afin de travailler avec des artefacts, Aspose.PDF a deux classes : [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) et [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

Pour obtenir tous les artefacts sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la propriété Artifacts. Ce sujet explique comment travailler avec des artefacts dans des fichiers PDF.

## Travailler avec des artefacts

La classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) contient les propriétés suivantes :

- **Artifact.Type** : obtient le type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
- **Artifact.Subtype** : obtient le sous-type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Veuillez noter que les filigranes créés avec Adobe Acrobat ont le type Pagination et le sous-type Watermark.

{{% /alert %}}

- **Artifact.Contents** : Obtient une collection des opérateurs internes de l'artefact. Son type pris en charge est System.Collections.ICollection.
- **Artifact.Form** : Obtient un XForm d'un artefact (si XForm est utilisé). Les filigranes, en-têtes et pieds de page contiennent un XForm qui montre tous les contenus de l'artefact.
- **Artifact.Image** : Obtient l'image d'un artefact (si une image est présente, sinon null).
- **Artifact.Text** : Obtient le texte d'un artefact.
- **Artifact.Rectangle** : Obtient la position d'un artefact sur la page.
- **Artifact.Rotation** : Obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation dans le sens inverse des aiguilles d'une montre).
- **Artifact.Opacity** : Obtient l'opacité d'un artefact. Les valeurs possibles sont dans la plage 0…1, où 1 est complètement opaque.

## Comment ajouter un filigrane sur des fichiers PDF

Le code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>