---
title: Travailler avec des graphiques vectoriels
linktitle: Travailler avec des graphiques vectoriels
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /fr/net/working-with-vector-graphics/
description: Cet article décrit les fonctionnalités de travail avec l'outil GraphicsAbsorber en utilisant C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics",
    "alternativeHeadline": "Enhance PDF Graphics Manipulation with С№",
    "abstract": "Découvrez les capacités avancées de l'outil GraphicsAbsorber dans Aspose.PDF for .NET, permettant aux développeurs de manipuler sans effort des graphiques vectoriels dans des documents PDF. Cette fonctionnalité permet une extraction, un déplacement et une suppression précis des graphiques, ainsi que la possibilité de les ajouter à différentes pages, améliorant ainsi votre flux de travail de manipulation PDF avec plus de flexibilité et de contrôle.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "889",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "Cette section décrit les fonctionnalités de travail avec le fichier PDF GraphicsAbsorber en utilisant la bibliothèque C#."
}
</script>

Dans ce chapitre, nous allons explorer comment utiliser la puissante classe `GraphicsAbsorber` pour interagir avec des graphiques vectoriels dans des documents PDF. Que vous ayez besoin de déplacer, de supprimer ou d'ajouter des graphiques, ce guide vous montrera comment effectuer ces tâches efficacement.

## Introduction<a name="introduction"></a>

Les graphiques vectoriels sont un élément crucial de nombreux documents PDF, utilisés pour représenter des images, des formes et d'autres éléments graphiques. Aspose.PDF fournit la classe `GraphicsAbsorber`, qui permet aux développeurs d'accéder et de manipuler ces graphiques par programmation. En utilisant la méthode `Visit` de `GraphicsAbsorber`, vous pouvez extraire des graphiques vectoriels d'une page spécifiée et effectuer diverses opérations, telles que les déplacer, les supprimer ou les copier sur d'autres pages.

## Extraction de graphiques avec `GraphicsAbsorber`<a name="extracting-graphics"></a>

La première étape pour travailler avec des graphiques vectoriels consiste à les extraire d'un document PDF. Voici comment vous pouvez le faire en utilisant la classe `GraphicsAbsorber` :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Step 5: Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

1. **Créer un objet Document** : Un nouvel objet `Document` est instancié avec le chemin vers le fichier PDF cible.
2. **Créer une instance de `GraphicsAbsorber`** : Cette classe capture tous les éléments graphiques d'une page spécifiée.
3. **Méthode Visit** : La méthode `Visit` est appelée sur la première page, permettant à `GraphicsAbsorber` d'absorber les graphiques vectoriels.
4. **Itérer à travers les éléments extraits** : Le code boucle à travers chaque élément extrait, imprimant des informations telles que le numéro de page, la position et le nombre d'opérateurs de dessin impliqués.

## Déplacement de graphiques<a name="moving-graphics"></a>

Une fois que vous avez extrait les graphiques, vous pouvez les déplacer à une position différente sur la même page. Voici comment vous pouvez y parvenir :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveGraphics()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber instance 
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Loop through each extracted graphic element and shift its position
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                // Move graphics by shifting its X and Y coordinates
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate** : Cette méthode suspend temporairement les mises à jour pour améliorer les performances lors de plusieurs modifications.
- **ResumeUpdate** : Cette méthode reprend les mises à jour et applique les modifications apportées aux positions des graphiques.
- **Positionnement des éléments** : La position de chaque graphique est ajustée en modifiant ses coordonnées `X` et `Y`.

## Suppression de graphiques<a name="removing-graphics"></a>

Il existe des scénarios où vous pourriez vouloir supprimer des graphiques spécifiques d'une page. Aspose.PDF propose deux méthodes pour y parvenir :

### Méthode 1 : Utiliser la limite de rectangle

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suspend updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove elements inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                // Check if the graphic's position falls within the rectangle
                if (rectangle.Contains(element.Position))
                {
                    // Remove the graphic element
                    element.Remove();
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### Méthode 2 : Utiliser une collection d'éléments supprimés

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection for the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Add elements within the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the selected graphic elements
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **Limite de rectangle** : Définissez une zone rectangulaire pour spécifier quels graphiques supprimer.
- **Suspendre et reprendre les mises à jour** : Assurez-vous d'une suppression efficace sans rendu intermédiaire.

## Ajout de graphiques à une autre page<a name="adding-graphics"></a>

Les graphiques absorbés d'une page peuvent être ajoutés à une autre page dans le même document. Voici deux méthodes pour y parvenir :

### Méthode 1 : Ajouter des graphiques individuellement

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element from the first page to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page.
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### Méthode 2 : Ajouter des graphiques en tant que collection

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics at once from the first page to the second page
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate et ResumeUpdate** : Ces méthodes aident à maintenir les performances lors de modifications en masse.
- **AddOnPage vs. AddGraphics** : Utilisez `AddOnPage` pour des ajouts individuels et `AddGraphics` pour des ajouts en masse.

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