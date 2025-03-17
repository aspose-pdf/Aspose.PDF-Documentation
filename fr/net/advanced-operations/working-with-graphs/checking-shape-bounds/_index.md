---
title: Vérifier les limites de forme dans la collection Shapes
type: docs
weight: 70
url: /fr/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Apprenez à vérifier les limites d'une forme lorsqu'elle est insérée dans la collection Shapes pour s'assurer qu'elle s'adapte à son conteneur parent.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "La nouvelle fonctionnalité de vérification des limites de Aspose.PDF for .NET dans la collection `Drawing.Graph.Shapes` valide automatiquement les dimensions des éléments par rapport aux conteneurs parents, empêchant le débordement de mise en page. Elle déclenche des exceptions lorsque les éléments dépassent les limites du conteneur, imposant des contraintes de taille strictes lors de l'insertion pour garantir un formatage PDF précis et rationaliser l'exactitude de la conception.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "849",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-03-17",
    "description": ""
}
</script>

## Introduction
Ce document fournit un guide détaillé sur l'utilisation de la fonctionnalité de vérification des limites dans la collection Shapes. Cette fonctionnalité garantit que les éléments s'adaptent à leur conteneur parent et peut être configurée pour déclencher une exception si le composant ne s'adapte pas. Nous allons passer en revue les étapes pour mettre en œuvre cette fonctionnalité et fournir un exemple complet.

## Prérequis
Vous aurez besoin des éléments suivants :
* Visual Studio 2019 ou version ultérieure
* Aspose.PDF for .NET 25.3 ou version ultérieure
* Un fichier PDF d'exemple contenant quelques pages

Vous pouvez télécharger la bibliothèque Aspose.PDF for .NET depuis le site officiel ou l'installer en utilisant le gestionnaire de packages NuGet dans Visual Studio.

## Étapes
Voici les étapes à suivre pour compléter la tâche :
1. Créer un document PDF.
2. Créer un objet `Graph` avec des dimensions spécifiées.
3. Créer un objet `Shape` avec des dimensions spécifiées.
4. Définir le `BoundsCheckMode` sur `ThrowExceptionIfDoesNotFit`.
5. Tenter d'ajouter la forme au graphique.

Voyons comment mettre en œuvre ces étapes dans le code C#.

### Étape 1 : Créer un document PDF
Tout d'abord, créez un nouveau document PDF et ajoutez-y une page.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### Étape 2 : Créer un objet Graph avec des dimensions spécifiées
Ensuite, créez un objet `Graph` avec une largeur et une hauteur de 100 unités. Positionnez le graphique à 10 unités du haut et à 15 unités de la gauche de la page. Ajoutez une bordure noire au graphique.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### Étape 3 : Créer un objet Shape (par exemple, Rectangle) avec des dimensions spécifiées
Créez un objet Rectangle avec une largeur et une hauteur de 50 unités. Positionnez le rectangle à (-1, 0), ce qui est en dehors des limites du graphique.

```csharp
var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### Étape 4 : Définir le BoundsCheckMode sur ThrowExceptionIfDoesNotFit
Définissez le `BoundsCheckMode` sur `ThrowExceptionIfDoesNotFit` pour garantir qu'une exception soit lancée si le rectangle ne s'adapte pas au graphique.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### Étape 5 : Ajouter le rectangle au graphique
Ajoutez le rectangle au graphique. Cela lancera une `Aspose.Pdf.BoundsOutOfRangeException` car le rectangle ne s'adapte pas aux dimensions du graphique.

```csharp
graph.Shapes.Add(rect);
```

## Sortie
Après l'exécution du code, la sortie attendue sera une `Aspose.Pdf.BoundsOutOfRangeException` avec le message :

```
Bounds not fit. Container dimensions: 100x100
```

## Dépannage
En cas de problèmes, voici quelques conseils :
* Assurez-vous que le `BoundsCheckMode` est correctement défini.
* Vérifiez que les dimensions de l'élément et du conteneur sont exactes.
* Vérifiez le positionnement de l'élément dans le conteneur.

## Exemple complet
Voici un exemple complet démontrant toutes les étapes combinées :

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using (var doc = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        
        // Create a Graph object with specified dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Shape object (for example, Rectangle) with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using var doc = new Aspose.Pdf.Document();
    
    // Add page
    var page = doc.Pages.Add();

    // Create a Graph object with specified dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## Conclusion
La fonctionnalité de vérification des limites dans la collection Shapes est un outil puissant pour garantir que les éléments s'adaptent aux conteneurs parents. Vous pouvez prévenir les problèmes de mise en page dans vos documents PDF en définissant le BoundsCheckMode sur ThrowExceptionIfDoesNotFit. Cette fonctionnalité est particulièrement utile dans les scénarios où le positionnement et la taille précis des éléments sont critiques. Pour plus de détails, visitez la [documentation officielle](https://docs.aspose.com/pdf/net/).