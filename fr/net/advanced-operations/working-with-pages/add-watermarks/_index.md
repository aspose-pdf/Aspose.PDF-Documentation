---
title: Ajouter un filigrane à un PDF en utilisant C#
linktitle: Ajouter un filigrane
type: docs
weight: 90
url: /fr/net/add-watermarks/
description: Cet article explique les fonctionnalités de travail avec des artefacts et l'obtention de filigranes dans des PDF en utilisant C# de manière programmatique.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un filigrane à un PDF en utilisant C#",
    "alternativeHeadline": "Comment ajouter un filigrane à un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, ajouter un filigrane",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique les fonctionnalités de travail avec des artefacts et l'obtention de filigranes dans des PDF en utilisant C# de manière programmatique."
}
</script>
**Aspose.PDF pour .NET** permet d'ajouter des filigranes à votre document PDF à l'aide d'Artifacts. Veuillez consulter cet article pour résoudre votre tâche.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Un filigrane créé avec Adobe Acrobat est appelé un artefact (tel que décrit dans la section 14.8.2.2 Contenu Réel et Artefacts de la spécification PDF). Pour travailler avec les artefacts, Aspose.PDF dispose de deux classes : [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) et [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

Pour obtenir tous les artefacts sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) possède la propriété Artifacts. Ce sujet explique comment travailler avec les artefacts dans les fichiers PDF.

## Travailler avec les Artefacts

La classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) contient les propriétés suivantes :

**Artifact.Type** – obtient le type d'artefact (supporte les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
**Artifact.Type** – obtient le type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Arrière-plan, Mise en page, Page, Pagination et Indéfini).
**Artifact.Subtype** – obtient le sous-type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Arrière-plan, Pied de page, En-tête, Indéfini, Filigrane).

{{% alert color="primary" %}}

Veuillez noter que les filigranes créés avec Adobe Acrobat ont le type Pagination et le sous-type Filigrane.

{{% /alert %}}

**Artifact.Contents** – Obtient une collection d'opérateurs internes de l'artefact. Son type pris en charge est System.Collections.ICollection.
**Artifact.Form** – Obtient le XForm d'un artefact (si XForm est utilisé). Les artefacts de filigrane, d'en-tête et de pied de page contiennent XForm qui montre tous les contenus de l'artefact.
**Artifact.Image** – Obtient l'image d'un artefact (si une image est présente, sinon null).
**Artifact.Text** – Obtient le texte d'un artefact.
**Artifact.Rectangle** – Obtient la position d'un artefact sur la page.
**Artifact.Rotation** – Obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation dans le sens antihoraire).
**Artifact.Rotation** – Obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation dans le sens antihoraire).
**Artifact.Opacity** – Obtient l'opacité d'un artefact. Les valeurs possibles sont comprises entre 0 et 1, où 1 est complètement opaque.

## Exemples de programmation : Comment ajouter un filigrane sur des fichiers PDF

Le fragment de code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF avec C#.

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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

