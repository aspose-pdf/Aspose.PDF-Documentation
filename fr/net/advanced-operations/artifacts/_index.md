---
title: Travailler avec des artefacts dans .NET
linktitle: Travailler avec des artefacts
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /fr/net/artifacts/
description: Aspose.PDF for .NET vous permet d'ajouter une image de fond aux pages PDF et d'obtenir chaque filigrane en utilisant la classe Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NET introduit la classe Artifact, permettant aux développeurs de gérer efficacement des éléments non liés au contenu comme des images de fond et des filigranes dans des documents PDF. Cette fonctionnalité améliore la structure du document tout en améliorant l'accessibilité et les performances, car les artefacts peuvent être ignorés par les technologies d'assistance. Avec des options personnalisables pour les types et les propriétés, les utilisateurs peuvent facilement manipuler ces éléments pour créer des PDF visuellement attrayants.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET vous permet d'ajouter une image de fond aux pages PDF et d'obtenir chaque filigrane en utilisant la classe Artifact."
}
</script>

Les artefacts dans un PDF sont des objets graphiques ou d'autres éléments qui ne font pas partie du contenu réel du document. Ils sont généralement utilisés à des fins de décoration, de mise en page ou de fond. Des exemples d'artefacts incluent les en-têtes de page, les pieds de page, les séparateurs ou les images qui ne transmettent aucune signification.

Le but des artefacts dans un PDF est de permettre la distinction entre les éléments de contenu et les éléments non liés au contenu. Cela est important pour l'accessibilité, car les lecteurs d'écran et d'autres technologies d'assistance peuvent ignorer les artefacts et se concentrer sur le contenu pertinent. Les artefacts peuvent également améliorer les performances et la qualité des documents PDF, car ils peuvent être omis lors de l'impression, de la recherche ou de la copie.

Pour créer un élément en tant qu'artefact dans un PDF, vous devez utiliser la classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Elle contient les propriétés utiles suivantes :

- **Artifact.Type** – obtient le type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
- **Artifact.Subtype** – obtient le sous-type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – obtient l'image d'un artefact (si une image est présente, sinon null).
- **Artifact.Text** – obtient le texte d'un artefact.
- **Artifact.Contents** – obtient une collection des opérateurs internes de l'artefact. Son type pris en charge est System.Collections.ICollection.
- **Artifact.Form** – obtient le XForm d'un artefact (si XForm est utilisé). Les artefacts de filigrane, d'en-tête et de pied de page contiennent un XForm qui montre tous les contenus de l'artefact.
- **Artifact.Rectangle** – obtient la position d'un artefact sur la page.
- **Artifact.Rotation** – obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation dans le sens inverse des aiguilles d'une montre).
- **Artifact.Opacity** – obtient l'opacité d'un artefact. Les valeurs possibles sont dans la plage 0...1, où 1 est complètement opaque.

Les classes suivantes peuvent également être utiles pour travailler avec des artefacts :

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Travailler avec des filigranes existants

Un filigrane créé avec Adobe Acrobat est appelé un artefact (comme décrit dans 14.8.2.2 Contenu réel et artefacts de la spécification PDF).

Pour obtenir tous les filigranes sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la propriété Artifacts.

Le code suivant montre comment obtenir tous les filigranes sur la première page d'un fichier PDF.

_Remarque :_ Ce code fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## Travailler avec des arrière-plans en tant qu'artefacts

Les images de fond peuvent être utilisées pour ajouter un filigrane ou un autre design subtil aux documents. Dans Aspose.PDF for .NET, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) peut être utilisée pour ajouter une image de fond à un objet page.

Le code suivant montre comment ajouter une image de fond aux pages PDF en utilisant l'objet BackgroundArtifact.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

Si vous souhaitez, pour une raison quelconque, utiliser un fond de couleur unie, veuillez modifier le code précédent de la manière suivante :

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## Compter les artefacts d'un type particulier

Pour calculer le nombre total d'artefacts d'un type particulier (par exemple, le nombre total de filigranes), utilisez le code suivant :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
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