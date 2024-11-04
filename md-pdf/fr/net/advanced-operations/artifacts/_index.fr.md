---
title: Travailler avec les artefacts en .NET
linktitle: Travailler avec les artefacts
type: docs
weight: 110
url: /net/artifacts/
description: Aspose.PDF pour .NET vous permet d'ajouter une image de fond aux pages PDF, et d'obtenir chaque filigrane en utilisant la classe Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec les artefacts en .NET",
    "alternativeHeadline": "Artefacts dans le document PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, artefacts dans pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET vous permet d'ajouter une image de fond aux pages PDF, et d'obtenir chaque filigrane en utilisant la classe Artifact."
}
</script>
Les artefacts dans les PDF sont des objets graphiques ou d'autres éléments qui ne font pas partie du contenu réel du document. Ils sont généralement utilisés à des fins de décoration, de mise en page ou de fond. Les exemples d'artefacts incluent les en-têtes de page, les pieds de page, les séparateurs ou les images qui ne transmettent aucune signification.

Le but des artefacts dans les PDF est de permettre la distinction entre les éléments de contenu et les éléments non-contenu. Cela est important pour l'accessibilité, car les lecteurs d'écran et autres technologies d'assistance peuvent ignorer les artefacts et se concentrer sur le contenu pertinent. Les artefacts peuvent également améliorer la performance et la qualité des documents PDF, car ils peuvent être omis lors de l'impression, de la recherche ou de la copie.

Pour créer un élément comme un artefact dans un PDF, vous devez utiliser la classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Elle contient les propriétés utiles suivantes :

- **Artifact.Type** – obtient le type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
- **Artifact.Type** – Obtient le type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
- **Artifact.Subtype** – Obtient le sous-type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Obtient une image d'artefact (si une image est présente, sinon null).
- **Artifact.Text** – Obtient le texte d'un artefact.
- **Artifact.Contents** – Obtient une collection d'opérateurs internes à l'artefact. Son type pris en charge est System.Collections.ICollection.
- **Artifact.Form** – Obtient un XForm d'artefact (si un XForm est utilisé). Les artefacts de watermark, d'en-tête et de pied de page contiennent un XForm qui montre tout le contenu de l'artefact.
- **Artifact.Rectangle** – Obtient la position d'un artefact sur la page.
- **Artifact.Rotation** – Obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation antihoraire).
- **Artifact.Opacity** – Obtient l'opacité d'un artefact.
- **Artifact.Opacity** – Obtient l'opacité d'un artefact.

Les classes suivantes peuvent également être utiles pour travailler avec des artefacts :

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Travailler avec des filigranes existants

Un filigrane créé avec Adobe Acrobat est appelé un artefact (comme décrit dans le 14.8.2.2 Contenu réel et artefacts de la spécification PDF).

Pour obtenir tous les filigranes sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) possède la propriété Artifacts.

Le snippet de code suivant montre comment obtenir tous les filigranes sur la première page d'un fichier PDF.

_Note :_ Ce code fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).
_Note :_ Ce code fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## Travailler avec les arrière-plans comme artefacts

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane, ou un autre design subtil, aux documents. Dans Aspose.PDF pour .NET, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Le code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
Si vous souhaitez, pour une raison quelconque, utiliser un fond de couleur unie, veuillez modifier le code précédent de la manière suivante :

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## Compter les artefacts d'un type particulier

Pour calculer le nombre total d'artefacts d'un type particulier (par exemple, le nombre total de filigranes), utilisez le code suivant :

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Filigranes : {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Fonds : {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("En-têtes : {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Pieds de page : {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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
```

