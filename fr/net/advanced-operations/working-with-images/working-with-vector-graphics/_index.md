---
title: Travailler avec les Graphiques Vectoriels
linktitle: Travailler avec les Graphiques Vectoriels
type: docs
weight: 120
url: /fr/net/working-with-vector-graphics/
description: Cet article décrit les fonctionnalités de l'outil GraphicsAbsorber en utilisant C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec GraphicsAbsorber",
    "alternativeHeadline": "Comment obtenir la position d'une image dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, c#, GraphicsAbsorber dans pdf",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section décrit les fonctionnalités de travail avec le fichier PDF GraphicsAbsorber en utilisant la bibliothèque C#."
}
</script>
```
Dans ce chapitre, nous allons explorer comment utiliser la puissante classe `GraphicsAbsorber` pour interagir avec les graphiques vectoriels au sein des documents PDF. Que vous ayez besoin de déplacer, de supprimer ou d'ajouter des graphiques, ce guide vous montrera comment réaliser ces tâches efficacement. Commençons !

## Introduction<a name="introduction"></a>

Les graphiques vectoriels sont un composant crucial de nombreux documents PDF, utilisés pour représenter des images, des formes et d'autres éléments graphiques. Aspose.PDF fournit la classe `GraphicsAbsorber`, qui permet aux développeurs d'accéder et de manipuler ces graphiques de manière programmatique. En utilisant la méthode `Visit` de `GraphicsAbsorber`, vous pouvez extraire les graphiques vectoriels d'une page spécifiée et effectuer diverses opérations, telles que les déplacer, les supprimer ou les copier sur d'autres pages.

## 1. Extraire les graphiques avec `GraphicsAbsorber`<a name="extracting-graphics"></a>

La première étape pour travailler avec des graphiques vectoriels est de les extraire d'un document PDF. Voici comment vous pouvez le faire en utilisant la classe `GraphicsAbsorber` :

```csharp
public static void UsingGraphicsAbsorber()
{
    // Étape 1 : Créer un objet Document.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // Étape 2 : Créer une instance de GraphicsAbsorber.
    var graphicsAbsorber = new GraphicsAbsorber();

    // Sélectionner la première page du document.
    var page = document.Pages[1];

    // Étape 3 : Utiliser la méthode `Visit` pour extraire les graphiques de la page.
    graphicsAbsorber.Visit(page);

    // Afficher des informations sur les éléments extraits.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"Numéro de page : {element.SourcePage.Number}");
        Console.WriteLine($"Position : ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"Nombre d'opérateurs : {element.Operators.Count}");
    }
}
```
### Explication :

1. **Créer un objet Document** : Un nouvel objet `Document` est instancié avec le chemin vers le fichier PDF cible.
2. **Créer une instance de `GraphicsAbsorber`** : Cette classe capture tous les éléments graphiques d'une page spécifiée.
3. **Méthode Visit** : La méthode `Visit` est appelée sur la première page, permettant à `GraphicsAbsorber` d'absorber les graphiques vectoriels.
4. **Itérer à travers les éléments extraits** : Le code boucle à travers chaque élément extrait, imprimant des informations telles que le numéro de page, la position et le nombre d'opérateurs de dessin impliqués.

## 2. Déplacer les graphiques<a name="moving-graphics"></a>

Une fois que vous avez extrait les graphiques, vous pouvez les déplacer vers une position différente sur la même page. Voici comment vous pouvez y parvenir :

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // Suspendre temporairement les mises à jour pour améliorer les performances.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // Déplacer les graphiques en décalant ses coordonnées X et Y.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // Reprendre les mises à jour et appliquer les changements.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Points clés :

- **SuppressUpdate** : Cette méthode suspend temporairement les mises à jour pour améliorer les performances lors de multiples modifications.
- **ResumeUpdate** : Cette méthode reprend les mises à jour et applique les modifications faites aux positions des graphiques.
- **Positionnement des éléments** : La position de chaque graphique est ajustée en modifiant ses coordonnées `X` et `Y`.

## 3. Suppression de graphiques<a name="removing-graphics"></a>

Il existe des scénarios où vous pourriez vouloir supprimer des graphiques spécifiques d'une page. Aspose.PDF offre deux méthodes pour y parvenir :

### Méthode 1 : Utilisation de la limite rectangulaire

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // Vérifiez si la position du graphique se trouve dans le rectangle.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // Supprime l'élément graphique.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Méthode 2 : Utilisation d'une collection d'éléments supprimés

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Explication :

- **Limite du rectangle** : Définir une zone rectangulaire pour spécifier quels graphiques supprimer.
- **Supprimer et reprendre les mises à jour** : Assure une suppression efficace sans rendu intermédiaire.

## 4. Ajout de graphiques à une autre page<a name="adding-graphics"></a>

Les graphiques absorbés d'une page peuvent être ajoutés à une autre page du même document.
Les graphiques absorbés d'une page peuvent être ajoutés à une autre page dans le même document.

### Méthode 1 : Ajouter des graphiques individuellement

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // Ajouter chaque élément graphique à la deuxième page.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Méthode 2 : Ajouter des graphiques en tant que collection

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // Ajouter tous les graphiques en une seule fois.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Points Clés :

- **SuppressUpdate et ResumeUpdate** : Ces méthodes aident à maintenir la performance lors de modifications en masse.
- **AddOnPage vs. AddGraphics** : Utilisez `AddOnPage` pour des ajouts individuels et `AddGraphics` pour des ajouts en masse.

## Conclusion

Dans ce chapitre, nous avons exploré comment utiliser la classe `GraphicsAbsorber` pour extraire, déplacer, supprimer et ajouter des graphiques vectoriels dans des documents PDF en utilisant Aspose.PDF. En maîtrisant ces techniques, vous pouvez améliorer significativement la présentation visuelle de vos PDFs et créer des documents dynamiques et visuellement attrayants.

N'hésitez pas à expérimenter avec les exemples de code et à les adapter à vos cas d'utilisation spécifiques. Bon codage !

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

