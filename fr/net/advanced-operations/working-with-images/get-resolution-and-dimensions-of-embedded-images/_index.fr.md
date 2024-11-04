---
title: Obtenir la Résolution et les Dimensions des Images
linktitle: Obtenir la Résolution et les Dimensions
type: docs
weight: 40
url: /net/get-resolution-and-dimensions-of-embedded-images/
description: Cette section présente les détails pour obtenir la résolution et les dimensions des Images Intégrées
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtenir la Résolution et les Dimensions des Images",
    "alternativeHeadline": "Comment obtenir la Résolution et les Dimensions des Images Intégrées",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, obtenir résolution, obtenir dimensions",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de Documentation Aspose.PDF",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section présente les détails pour obtenir la résolution et les dimensions des Images Intégrées"
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Ce sujet explique comment utiliser les classes d'opérateurs dans l'espace de noms Aspose.PDF qui fournissent la capacité d'obtenir des informations sur la résolution et les dimensions des images sans avoir à les extraire.

Il existe différentes manières d'atteindre cet objectif. Cet article explique comment utiliser une `arraylist` et [les classes de placement d'images](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. D'abord, chargez le fichier PDF source (contenant des images).
1. Ensuite, créez un objet ArrayList pour contenir les noms de toutes les images dans le document.
1. Obtenez les images en utilisant la propriété Page.Resources.Images.
1. Créez un objet stack pour contenir l'état graphique de l'image et utilisez-le pour suivre les différents états des images.
1.
1. Étant donné que nous pouvons modifier la matrice avec ConcatenateMatrix, nous pourrions également avoir besoin de revenir à l'état original de l'image. Utilisez les opérateurs GSave et GRestore. Ces opérateurs sont appariés et doivent donc être appelés ensemble. Par exemple, si vous effectuez un travail graphique avec des transformations complexes et que finalement vous revenez aux transformations initiales, l'approche sera la suivante :

```csharp
// Dessiner du texte
GSave

ConcatenateMatrix  // tourner le contenu après l'opérateur

// Un travail graphique

ConcatenateMatrix // mettre à l'échelle (avec la rotation précédente) le contenu après l'opérateur

// Un autre travail graphique

GRestore

// Dessiner du texte
```

En conséquence, le texte est dessiné sous forme régulière mais certaines transformations sont effectuées entre les opérateurs de texte. Pour afficher l'image ou pour dessiner des formes et des images, nous devons utiliser l'opérateur Do.

Nous avons également une classe nommée XImage qui offre deux propriétés, Width et Height, qui peuvent être utilisées pour obtenir les dimensions de l'image.

1.
1.
1. Afficher les informations dans une invite de commande avec le nom de l'image.

Le code suivant vous montre comment obtenir les dimensions et la résolution d'une image sans extraire l'image du document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Charger le fichier PDF source
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// Définir la résolution par défaut pour l'image
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// Définir un objet liste qui contiendra les noms des images
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// Insérer un objet dans la pile
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// Obtenir tous les opérateurs de la première page du document
foreach (Operator op in doc.Pages[1].Contents)
{
    // Utiliser les opérateurs GSave/GRestore pour rétablir les transformations précédemment définies
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // Instancier l'objet ConcatenateMatrix car il définit la matrice de transformation actuelle.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // Créer l'opérateur Do qui dessine des objets à partir des ressources. Il dessine des objets Form et des objets Image
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // Sauvegarder l'état précédent et pousser l'état actuel au sommet de la pile
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // Jeter l'état actuel et restaurer l'état précédent
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // Multiplier la matrice actuelle avec la matrice d'état
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // Dans le cas où il s'agit d'un opérateur de dessin d'image
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // Créer un objet XImage pour contenir les images de la première page du PDF
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // Obtenir les dimensions de l'image
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // Obtenir les informations de hauteur et de largeur de l'image
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // Calculer la résolution à partir des informations ci-dessus
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // Afficher les informations de dimension et de résolution de chaque image
            Console.Out.WriteLine(
                    string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
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

