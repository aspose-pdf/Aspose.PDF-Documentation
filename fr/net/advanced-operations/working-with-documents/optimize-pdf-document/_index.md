---
title: Optimiser, Compresser ou Réduire la Taille d'un PDF en C#
linktitle: Optimiser PDF
type: docs
weight: 30
url: /fr/net/optimize-pdf/
description: Optimiser un fichier PDF, réduire toutes les images, diminuer la taille du PDF, désintégrer les polices, supprimer les objets inutilisés avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/changing-page-sizes-in-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimiser PDF avec C#",
    "alternativeHeadline": "Comment optimiser un PDF avec .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, optimiser pdf",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Optimiser un fichier PDF, réduire toutes les images, diminuer la taille du PDF, désintégrer les polices, supprimer les objets inutilisés avec C#."
}
</script>
Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert réseau et le stockage. Cela est particulièrement pratique pour la publication sur des pages web, le partage sur des réseaux sociaux, l'envoi par e-mail ou l'archivage dans un stockage. Nous pouvons utiliser plusieurs techniques pour optimiser un PDF :

- Optimiser le contenu de la page pour la navigation en ligne
- Réduire ou compresser toutes les images
- Activer la réutilisation du contenu de la page
- Fusionner les flux en double
- Désincorporer les polices
- Supprimer les objets inutilisés
- Supprimer les champs de formulaire aplatis
- Supprimer ou aplatir les annotations

{{% alert color="primary" %}}

 Une explication détaillée des méthodes d'optimisation peut être trouvée sur la page Aperçu des Méthodes d'Optimisation.

{{% /alert %}}

## Optimiser le document PDF pour le Web

L'optimisation, ou linéarisation pour le Web, fait référence au processus de rendu d'un fichier PDF adapté à la navigation en ligne utilisant un navigateur web. Pour optimiser un fichier pour l'affichage web :

1. Ouvrez le document source dans un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1.
1. Enregistrez le document optimisé en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Le code suivant montre comment optimiser un document PDF pour le web.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// Optimiser pour le web
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// Enregistrer le document de sortie
pdfDocument.Save(dataDir);
```

## Réduire la taille du PDF

La méthode [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) vous permet de réduire la taille du document en éliminant les informations inutiles.
La méthode [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) vous permet de réduire la taille du document en éliminant les informations inutiles.

- Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
- Les ressources identiques sont fusionnées en un seul objet
- Les objets inutilisés sont supprimés

Le fragment ci-dessous est un exemple. Notez cependant que cette méthode ne peut pas garantir la réduction de la taille du document.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// Optimiser le document PDF. Notez cependant que cette méthode ne peut pas garantir la réduction de la taille du document
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// Enregistrer le document mis à jour
pdfDocument.Save(dataDir);
```

## Gestion de la stratégie d'optimisation

Nous pouvons également personnaliser la stratégie d'optimisation.
Nous pouvons également personnaliser la stratégie d'optimisation.

### Réduire ou compresser toutes les images

Nous avons deux façons de travailler avec les images : réduire la qualité des images et/ou changer leur résolution. Dans tous les cas, [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions) doit être appliqué. Dans l'exemple suivant, nous réduisons les images en diminuant [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) à 50.

`ImageQuality` fonctionne de manière similaire à la qualité JPEG, où la valeur 0 est la plus basse et la valeur 100 est la plus élevée.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Initialiser OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Définir l'option CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Définir l'option ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
```
Une autre méthode consiste à redimensionner les images avec une résolution inférieure. Dans ce cas, nous devrions définir ResizeImages sur vrai et MaxResolution à la valeur appropriée.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Initialiser le Temps
var time = DateTime.Now.Ticks;
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// Initialiser OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Définir l'option CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Définir l'option ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Définir l'option ResizeImage
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// Définir l'option MaxResolution
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
```
Un autre problème important est le temps d'exécution. Mais encore une fois, nous pouvons également gérer ce paramètre. Actuellement, nous pouvons utiliser deux algorithmes - Standard et Rapide. Pour contrôler le temps d'exécution, nous devons définir une propriété [Version](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). Le fragment suivant montre l'algorithme Rapide :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Initialiser le Temps
var time = DateTime.Now.Ticks;
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Initialiser OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Définir l'option CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Définir l'option ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Définir la Version de Compression d'Image sur rapide
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### Suppression des objets inutilisés

Un document PDF contient parfois des objets PDF qui ne sont référencés par aucun autre objet dans le document. Cela peut arriver, par exemple, lorsqu'une page est retirée de l'arborescence des pages du document mais que l'objet page lui-même n'est pas supprimé. La suppression de ces objets ne rend pas le document invalide mais le réduit plutôt.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Définir l'option RemoveUsedObject
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Enregistrer le document mis à jour
pdfDocument.Save(dataDir);
```

### Suppression des flux inutilisés

Parfois, le document contient des flux de ressources inutilisés.
Parfois, le document contient des flux de ressources inutilisés.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Définir l'option RemoveUsedStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
```

### Liaison de flux dupliqués

Certains documents peuvent contenir plusieurs flux de ressources identiques (comme des images, par exemple).
Certains documents peuvent contenir plusieurs flux de ressources identiques (comme des images, par exemple).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Définir l'option LinkDuplcateStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
```

De plus, nous pouvons utiliser les paramètres [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).
De plus, nous pouvons utiliser les paramètres [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Définir l'option AllowReusePageContent
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("Début");
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Terminé");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Taille du fichier original : {0}. Taille du fichier réduit : {1}", fi1.Length, fi2.Length);
```
### Désincorporer les Polices

Si le document utilise des polices incorporées, cela signifie que toutes les données de la police sont stockées dans le document. L'avantage est que le document peut être visualisé indépendamment du fait que la police soit installée sur la machine de l'utilisateur ou non. Cependant, incorporer des polices augmente la taille du document. La méthode de désincorporation des polices supprime toutes les polices incorporées. Ainsi, la taille du document diminue mais le document peut devenir illisible si la police correcte n'est pas installée.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Définir l'option UnembedFonts
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Début");
// Optimiser le document PDF en utilisant OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Enregistrer le document mis à jour
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Terminé");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Taille du fichier original : {0}. Taille du fichier réduite : {1}", fi1.Length, fi2.Length);
```
Les ressources d'optimisation appliquent ces méthodes au document. Si l'une de ces méthodes est appliquée, la taille du document diminuera très probablement. Si aucune de ces méthodes n'est appliquée, la taille du document ne changera pas, ce qui est évident.

## Autres moyens de réduire la taille du document PDF

### Suppression ou aplatissement des annotations

Les annotations peuvent être supprimées lorsqu'elles sont inutiles. Lorsqu'elles sont nécessaires mais ne nécessitent pas de modification supplémentaire, elles peuvent être aplaties. Ces deux techniques réduiront la taille du fichier.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Ouvrir le document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Aplatir les annotations
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### Suppression des champs de formulaire

Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Charger le formulaire PDF source
Document doc = new Document(dataDir + "input.pdf");

// Aplatir les formulaires
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Enregistrer le document mis à jour
doc.Save(dataDir);
```

### Convertir un PDF de l'espace colorimétrique RVB en niveaux de gris

Un fichier PDF comprend du Texte, des Images, des Pièces jointes, des Annotations, des Graphiques et d'autres objets.
Un fichier PDF comprend du Texte, des Images, des Pièces jointes, des Annotations, des Graphiques et d'autres objets.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Charger le fichier PDF source
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // Obtenir une instance de la page particulière dans le PDF
        Page page = document.Pages[idxPage];
        // Convertir l'image en espace de couleurs RGB vers un espace de couleurs en niveaux de gris
        strategy.Convert(page);
    }
    // Sauvegarder le fichier résultant
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### Compression FlateDecode

{{% alert color="primary" %}}

Cette fonctionnalité est prise en charge par la version 18.12 ou supérieure.

{{% /alert %}}

Aspose.PDF pour .NET prend en charge la compression FlateDecode pour la fonctionnalité d'optimisation des PDF.
Aspose.PDF pour .NET prend en charge la compression FlateDecode pour la fonctionnalité d'optimisation PDF.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **Stocker l'image dans XImageCollection**

Aspose.PDF pour .NET permet de stocker de nouvelles images dans **XImageCollection** avec compression FlateDecode. Pour activer cette option, vous pouvez utiliser le drapeau **ImageFilterType.Flate**. Le fragment de code suivant montre comment utiliser cette fonctionnalité :

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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


