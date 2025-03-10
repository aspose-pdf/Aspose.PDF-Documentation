---
title: Travailler avec les couches PDF en utilisant C#
linktitle: Travailler avec les couches PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/work-with-pdf-layers/
description: La tâche suivante explique comment verrouiller une couche PDF, extraire des éléments de couche PDF, aplatir un PDF en couches et fusionner toutes les couches à l'intérieur d'un PDF en une seule.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "Découvrez une gestion améliorée des documents PDF avec la nouvelle fonctionnalité Aspose.PDF for .NET qui permet aux utilisateurs de travailler efficacement avec les couches PDF. Cette fonctionnalité permet de verrouiller et de déverrouiller des couches, d'extraire des éléments dans des fichiers séparés, d'aplatir le contenu en couches et de fusionner plusieurs couches en une seule, offrant un meilleur contrôle sur la visibilité et l'organisation des documents. Libérez le potentiel de vos documents PDF et rationalisez vos flux de travail avec ces outils puissants.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Les couches PDF permettent à un document PDF de contenir différents ensembles de contenu qui peuvent être visualisés ou masqués sélectivement. Chaque couche dans un PDF peut inclure du texte, des images ou des graphiques, et les utilisateurs peuvent activer ou désactiver ces couches, en fonction de leurs besoins. Les couches sont souvent utilisées dans des documents complexes où différents contenus doivent être organisés ou séparés.

## Verrouiller une couche PDF

Avec Aspose.PDF for .NET, vous pouvez ouvrir un PDF, verrouiller une couche spécifique sur la première page et enregistrer le document avec les modifications.

Depuis la version 24.5, cette fonctionnalité a été mise en œuvre.

Deux nouvelles méthodes et une propriété ont été ajoutées :

- Layer.Lock(); - Verrouille la couche.
- Layer.Unlock(); - Déverrouille la couche.
- Layer.Locked; - Propriété, indiquant l'état de verrouillage de la couche.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## Extraire les éléments de la couche PDF

La bibliothèque Aspose.PDF for .NET permet d'extraire chaque couche de la première page et d'enregistrer chaque couche dans un fichier séparé.

Pour créer un nouveau PDF à partir d'une couche, le code suivant peut être utilisé :

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

La version 24.9 a entraîné une mise à jour de cette fonctionnalité.

Il est possible d'extraire des éléments de couche PDF et de les enregistrer dans un nouveau flux de fichier PDF :

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## Aplatir un PDF en couches

La bibliothèque Aspose.PDF for .NET ouvre un PDF, itère à travers chaque couche sur la première page et aplatit chaque couche, la rendant permanente sur la page.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

La méthode 'Layer.Flatten(bool cleanupContentStream)' accepte le paramètre booléen qui spécifie s'il faut supprimer les marqueurs de groupe de contenu optionnels du flux de contenu. Définir le paramètre cleanupContentStream sur false accélère le processus d'aplatissement.

## Fusionner toutes les couches à l'intérieur du PDF en une seule

La bibliothèque Aspose.PDF for .NET permet de fusionner soit toutes les couches PDF, soit une couche spécifique sur la première page en une nouvelle couche et d'enregistrer le document mis à jour.

Deux méthodes ont été ajoutées pour fusionner toutes les couches sur la page :

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

Le deuxième paramètre permet de renommer le marqueur de groupe de contenu optionnel. La valeur par défaut est "oc1" (/OC /oc1 BDC).

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```