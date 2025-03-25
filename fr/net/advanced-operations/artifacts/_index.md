---
title: Travailler avec les artefacts dans .NET
linktitle: Travailler avec les artefacts
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /fr/net/artifacts/
description: Aspose.PDF for .NET vous permet d’ajouter une image d’arrière-plan aux pages PDF, et d’obtenir chaque filigrane en utilisant la classe Artifact.
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
    "alternativeHeadline": "Enhance PDF Documents with Artifacts Management",
    "abstract": "Aspose.PDF pour .NET introduit la classe Artifact, permettant aux développeurs de gérer facilement les éléments non liés au contenu tels que les images de fond et les filigranes dans les documents PDF. Cette fonctionnalité améliore l'accessibilité et les performances des documents en permettant aux technologies d'assistance d'ignorer les éléments décoratifs, tout en offrant des options personnalisables pour divers types et propriétés d'artefacts.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2501",
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
    "dateModified": "2025-03-12",
    "description": "Aspose.PDF pour .NET vous permet d'ajouter une image de fond aux pages PDF et d'obtenir chaque filigrane en utilisant la classe Artifact."
}
</script>

Les artefacts dans PDF sont des objets graphiques ou d’autres éléments qui ne font pas partie du contenu réel du document. Ils sont généralement utilisés pour la décoration, la mise en page ou comme arrière-plan. Des exemples d’artefacts incluent les en-têtes de page, les pieds de page, les séparateurs ou des images qui ne véhiculent aucune signification.

L’objectif des artefacts dans PDF est de permettre la distinction entre les éléments de contenu et les éléments non liés au contenu. Cela est important pour l’accessibilité, car les lecteurs d’écran et autres technologies d’assistance peuvent ignorer les artefacts et se concentrer sur le contenu pertinent. Les artefacts peuvent également améliorer la performance et la qualité des documents PDF, puisqu’ils peuvent être omis lors de l’impression, de la recherche ou de la copie.

Pour créer un élément en tant qu’artefact dans un PDF, vous devez utiliser la classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Il contient les propriétés utiles suivantes:

- **Artifact.Type** – renvoie le type d’artefact (prend en charge les valeurs de l’énumération Artifact.ArtifactType, où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
- **Artifact.Subtype** – renvoie le sous-type d’artefact (prend en charge les valeurs de l’énumération Artifact.ArtifactSubtype, dont les valeurs incluent Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – renvoie l’image d’un artefact (si une image est présente, sinon null).
- **Artifact.Text** – renvoie le texte d’un artefact.
- **Artifact.Contents** – renvoie une collection des opérateurs internes de l’artefact. Son type supporté est System.Collections.ICollection.
- **Artifact.Form** – renvoie le XForm d’un artefact (si le XForm est utilisé). Les artefacts de filigrane, d’en-tête et de pied de page contiennent un XForm qui affiche tous les contenus de l’artefact.
- **Artifact.Rectangle** – renvoie la position d’un artefact sur la page.
- **Artifact.Rotation** – renvoie la rotation d’un artefact (en degrés, une valeur positive indiquant une rotation dans le sens antihoraire).
- **Artifact.Opacity** – renvoie l’opacité d’un artefact. Les valeurs possibles se situent dans l’intervalle 0...1, où 1 signifie totalement opaque.

Les classes suivantes peuvent également être utiles pour travailler avec des artefacts:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Travailler avec les filigranes existants

Un filigrane créé avec Adobe Acrobat est appelé un artefact (tel que décrit dans la section 14.8.2.2 Contenu réel et artefacts de la spécification PDF).

Pour obtenir tous les filigranes d'une page particulière, la classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) possède la propriété Artifacts.

L'extrait de code suivant montre comment obtenir tous les filigranes sur la première page d'un fichier PDF.

_Note:_ Ce code fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

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

## Travailler avec les arrière-plans en tant qu’artefacts

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane ou un autre design subtil aux documents. Dans Aspose.PDF for .NET, chaque document PDF est une collection de pages et chaque page contient une collection d’artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

L'extrait de code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact.

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

Si vous souhaitez, pour une raison quelconque, utiliser un arrière-plan de couleur unie, veuillez modifier le code précédent de la manière suivante:

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

Pour calculer le nombre total d’artefacts d’un type particulier (par exemple, le nombre total de filigranes), utilisez le code suivant:

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

## Ajout d'un artefact de numérotation Bates

Pour ajouter un artefact de numérotation Bates à un document, appelez la méthode d'extension ```AddBatesNumbering(BatesNArtifact batesNArtifact)``` sur le ```PageCollection```, en passant l'objet ```BatesNArtifact``` en paramètre:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddBatesNumbering(new BatesNArtifact
        {
            // These properties are set to their default values, as if they were not specified
            StartPage = 1,
            EndPage = 0,
            Subset = Subset.All,
            NumberOfDigits = 6,
            StartNumber = 1,
            Prefix = "",
            Suffix = "",
            ArtifactVerticalAlignment = VerticalAlignment.Bottom,
            ArtifactHorizontalAlignment = HorizontalAlignment.Right,
            RightMargin = 72,
            LeftMargin = 72,
            TopMargin = 36,
            BottomMargin = 36
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// The path to the documents directory
var dataDir = RunExamples.GetDataDir_AsposePdf();

// Create or open PDF document
using var document = new Aspose.Pdf.Document();

// Add 10 pages
for (int i = 0; i < 10; i++)
{
    document.Pages.Add();
}

// Add Bates numbering to all pages
document.Pages.AddBatesNumbering(new BatesNArtifact
{
    // These properties are set to their default values, as if they were not specified
    StartPage = 1,
    EndPage = 0,
    Subset = Subset.All,
    NumberOfDigits = 6,
    StartNumber = 1,
    Prefix = "",
    Suffix = "",
    ArtifactVerticalAlignment = VerticalAlignment.Bottom,
    ArtifactHorizontalAlignment = HorizontalAlignment.Right,
    RightMargin = 72,
    LeftMargin = 72,
    TopMargin = 36,
    BottomMargin = 36
});

// Save PDF document
document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
```
{{< /tab >}}
{{< /tabs >}}

Ou, vous pouvez passer une collection de ```PaginationArtifacts```:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddPagination(new List<Aspose.Pdf.PaginationArtifact>
        {
            new Aspose.Pdf.BatesNArtifact
            {
                // These properties are set to their default values, as if they were not specified
                StartPage = 1,
                EndPage = 0,
                Subset = Subset.All,
                NumberOfDigits = 6,
                StartNumber = 1,
                Prefix = "",
                Suffix = "",
                ArtifactVerticalAlignment = VerticalAlignment.Bottom,
                ArtifactHorizontalAlignment = HorizontalAlignment.Right,
                RightMargin = 72,
                LeftMargin = 72,
                TopMargin = 36,
                BottomMargin = 36
            }
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using var document = new Aspose.Pdf.Document();

    // Add 10 pages
    for (int i = 0; i < 10; i++)
    {
        document.Pages.Add();
    }

    // Add Bates numbering to all pages
    document.Pages.AddPagination(new List<Aspose.Pdf.PaginationArtifact>
    {
        new Aspose.Pdf.BatesNArtifact
        {
            // These properties are set to their default values, as if they were not specified
            StartPage = 1,
            EndPage = 0,
            Subset = Subset.All,
            NumberOfDigits = 6,
            StartNumber = 1,
            Prefix = "",
            Suffix = "",
            ArtifactVerticalAlignment = VerticalAlignment.Bottom,
            ArtifactHorizontalAlignment = HorizontalAlignment.Right,
            RightMargin = 72,
            LeftMargin = 72,
            TopMargin = 36,
            BottomMargin = 36
        }
    });

    // Save PDF document
    document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Alternativement, vous pouvez ajouter un artefact de numérotation Bates à l'aide d'un délégué d'action:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddBatesNumbering(batesN =>
        {
            // These properties are set to their default values, as if they were not specified
            batesN.StartPage = 1;
            batesN.EndPage = 0;
            batesN.Subset = Subset.All;
            batesN.NumberOfDigits = 6;
            batesN.StartNumber = 1;
            batesN.Prefix = "";
            batesN.Suffix = "";
            batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
            batesN.ArtifactHorizontalAlignment = HorizontalAlignment.Right;
            batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
            batesN.RightMargin = 72;
            batesN.LeftMargin = 72;
            batesN.TopMargin = 36;
            batesN.BottomMargin = 36;
            batesN.TextState.FontSize = 10;
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using var document = new Aspose.Pdf.Document();

    // Add 10 pages
    for (int i = 0; i < 10; i++)
    {
        document.Pages.Add();
    }

    // Add Bates numbering to all pages
    document.Pages.AddBatesNumbering(batesN =>
    {
        // These properties are set to their default values, as if they were not specified
        batesN.StartPage = 1;
        batesN.EndPage = 0;
        batesN.Subset = Subset.All;
        batesN.NumberOfDigits = 6;
        batesN.StartNumber = 1;
        batesN.Prefix = "";
        batesN.Suffix = "";
        batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
        batesN.ArtifactHorizontalAlignment = HorizontalAlignment.Right;
        batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
        batesN.RightMargin = 72;
        batesN.LeftMargin = 72;
        batesN.TopMargin = 36;
        batesN.BottomMargin = 36;
        batesN.TextState.FontSize = 10;
    });

    // Save PDF document
    document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Pour supprimer la numérotation Bates, utilisez le code suivant:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBatesNArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SampleBatesNArtifact_out.pdf"))
    {
        // Delete Bates numbering from all pages
        document.Pages.DeleteBatesNumbering();

        //Save PDF document
        document.Save(dataDir + "DeleteBatesNArtifacts_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBatesNArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SampleBatesNArtifact_out.pdf");

    // Delete Bates numbering from all pages
    document.Pages.DeleteBatesNumbering();

    //Save PDF document
    document.Save(dataDir + "DeleteBatesNArtifacts_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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