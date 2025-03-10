---
title: Optimiser, compresser ou réduire la taille d'un PDF en C#
linktitle: Optimiser PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/optimize-pdf/
description: Optimiser un fichier PDF, réduire toutes les images, réduire la taille du PDF, désincorporer les polices, supprimer les objets inutilisés avec C#.
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
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "La nouvelle fonctionnalité d'optimisation des PDF en C# permet aux développeurs de réduire considérablement la taille des fichiers PDF en utilisant plusieurs stratégies, telles que la compression des images, la désincorporation des polices et la suppression des objets inutilisés. Cette amélioration améliore l'efficacité pour la publication sur le web, le partage par e-mail et le stockage, fournissant une solution efficace pour gérer de grands documents PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2282",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Optimiser un fichier PDF, réduire toutes les images, réduire la taille du PDF, désincorporer les polices, supprimer les objets inutilisés avec C#."
}
</script>

Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert et le stockage sur le réseau. Cela est particulièrement utile pour la publication sur des pages web, le partage sur les réseaux sociaux, l'envoi par e-mail ou l'archivage dans le stockage. Nous pouvons utiliser plusieurs techniques pour optimiser un PDF :

- Optimiser le contenu des pages pour la navigation en ligne.
- Réduire ou compresser toutes les images.
- Activer la réutilisation du contenu des pages.
- Fusionner les flux dupliqués.
- Désincorporer les polices.
- Supprimer les objets inutilisés.
- Supprimer les champs de formulaire aplatis.
- Supprimer ou aplatir les annotations.

{{% alert color="primary" %}}

 Une explication détaillée des méthodes d'optimisation peut être trouvée sur la page Vue d'ensemble des méthodes d'optimisation.

{{% /alert %}}

## Optimiser le document PDF pour le web

L'optimisation, ou linéarisation pour le web, fait référence au processus de rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur web. Pour optimiser un fichier pour l'affichage web :

1. Ouvrez le document d'entrée dans un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Utilisez la méthode [Optimize](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimize).
1. Enregistrez le document optimisé en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le code suivant montre comment optimiser un document PDF pour le web.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## Réduire la taille du PDF

La méthode [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) vous permet de réduire la taille du document en éliminant les informations inutiles. Par défaut, cette méthode fonctionne comme suit :

- Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées.
- Les ressources égales sont regroupées en un seul objet.
- Les objets inutilisés sont supprimés.

Le snippet ci-dessous est un exemple. Notez cependant que cette méthode ne peut pas garantir la réduction de la taille du document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## Gestion de la stratégie d'optimisation

Nous pouvons également personnaliser la stratégie d'optimisation. Actuellement, la méthode [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf.document/optimizeresources/methods/1) utilise 5 techniques. Ces techniques peuvent être appliquées en utilisant la méthode OptimizeResources() avec le paramètre [OptimizationOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions).

### Réduction ou compression de toutes les images

Nous avons deux façons de travailler avec les images : réduire la qualité de l'image et/ou changer leur résolution. Dans tous les cas, les [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions) doivent être appliquées. Dans l'exemple suivant, nous réduisons les images en abaissant la [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) à 50.

`ImageQuality` fonctionne de manière similaire à la qualité JPEG, où la valeur 0 est la plus basse et la valeur 100 est la plus élevée.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

Une autre façon est de redimensionner les images avec une résolution plus basse. Dans ce cas, nous devrions définir ResizeImages sur true et MaxResolution sur la valeur appropriée.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

Un autre point important est le temps d'exécution. Mais encore une fois, nous pouvons gérer ce paramètre aussi. Actuellement, nous pouvons utiliser deux algorithmes - Standard et Rapide. Pour contrôler le temps d'exécution, nous devrions définir une propriété [Version](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). Le snippet suivant démontre l'algorithme Rapide :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### Suppression des objets inutilisés

Un document PDF contient parfois des objets PDF qui ne sont référencés par aucun autre objet dans le document. Cela peut se produire, par exemple, lorsqu'une page est supprimée de l'arbre des pages du document mais que l'objet de la page lui-même n'est pas supprimé. La suppression de ces objets ne rend pas le document invalide mais le réduit plutôt.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Suppression des flux inutilisés

Parfois, le document contient des flux de ressources inutilisés. Ces flux ne sont pas des "objets inutilisés" car ils sont référencés à partir d'un dictionnaire de ressources de page. Ainsi, ils ne sont pas supprimés avec la méthode "supprimer les objets inutilisés". Mais ces flux ne sont jamais utilisés avec le contenu de la page. Cela peut se produire dans les cas où une image a été supprimée de la page mais pas des ressources de la page. De plus, cette situation se produit souvent lorsque des pages sont extraites du document et que les pages du document ont des ressources "communes", c'est-à-dire le même objet Resources. Le contenu des pages est analysé afin de déterminer si un flux de ressources est utilisé ou non. Les flux inutilisés sont supprimés. Cela diminue parfois la taille du document. L'utilisation de cette technique est similaire à l'étape précédente :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Lien des flux dupliqués

Certains documents peuvent contenir plusieurs flux de ressources identiques (comme des images, par exemple). Cela peut se produire, par exemple, lorsqu'un document est concaténé avec lui-même. Le document de sortie contient deux copies indépendantes du même flux de ressources. Nous analysons tous les flux de ressources et les comparons. Si des flux sont dupliqués, ils sont fusionnés, c'est-à-dire qu'une seule copie est conservée. Les références sont modifiées en conséquence, et les copies de l'objet sont supprimées. Dans certains cas, cela aide à diminuer la taille du document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

De plus, nous pouvons utiliser les paramètres [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent). Si cette propriété est définie sur true, le contenu de la page sera réutilisé lors de l'optimisation du document pour des pages identiques.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### Désincorporation des polices

Si le document utilise des polices incorporées, cela signifie que toutes les données de police sont stockées dans le document. L'avantage est que le document est consultable, peu importe si la police est installée sur la machine de l'utilisateur ou non. Mais l'incorporation des polices rend le document plus volumineux. La méthode de désincorporation des polices supprime toutes les polices incorporées. Ainsi, la taille du document diminue mais le document lui-même peut devenir illisible si la police correcte n'est pas installée.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

Les ressources d'optimisation appliquent ces méthodes au document. Si l'une de ces méthodes est appliquée, la taille du document diminuera très probablement. Si aucune de ces méthodes n'est appliquée, la taille du document ne changera pas, ce qui est évident.

## Autres moyens de réduire la taille du document PDF

### Suppression ou aplatissage des annotations

Les annotations peuvent être supprimées lorsqu'elles ne sont pas nécessaires. Lorsqu'elles sont nécessaires mais ne nécessitent pas d'édition supplémentaire, elles peuvent être aplaties. Ces deux techniques réduiront la taille du fichier.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Suppression des champs de formulaire

Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

### Convertir un PDF de l'espace colorimétrique RVB en niveaux de gris

Un fichier PDF comprend du texte, des images, des pièces jointes, des annotations, des graphiques et d'autres objets. Vous pouvez rencontrer un besoin de convertir un PDF de l'espace colorimétrique RVB en niveaux de gris afin qu'il soit plus rapide lors de l'impression de ces fichiers PDF. De plus, lorsque le fichier est converti en niveaux de gris, la taille du document est également réduite, mais cela peut également entraîner une diminution de la qualité du document. Cette fonctionnalité est actuellement prise en charge par la fonctionnalité Pre-Flight d'Adobe Acrobat, mais en ce qui concerne l'automatisation de bureau, Aspose.PDF est une solution ultime pour fournir de tels leviers pour les manipulations de documents. Afin de répondre à cette exigence, le code suivant peut être utilisé.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### Compression FlateDecode

{{% alert color="primary" %}}

Cette fonctionnalité est prise en charge par la version 18.12 ou supérieure.

{{% /alert %}}

Aspose.PDF for .NET fournit un support de compression FlateDecode pour la fonctionnalité d'optimisation PDF. Le code suivant montre comment utiliser l'option dans l'optimisation pour stocker des images avec une compression **FlateDecode** :

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### Stocker l'image dans XImageCollection

Aspose.PDF for .NET offre la possibilité de stocker de nouvelles images dans **XImageCollection** avec compression FlateDecode. Pour activer cette option, vous pouvez utiliser le drapeau **ImageFilterType.Flate**. Le code suivant montre comment utiliser cette fonctionnalité :

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
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