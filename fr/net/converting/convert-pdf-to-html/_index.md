---
title: Convertir PDF en HTML dans .NET
linktitle: Convertir PDF en format HTML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment convertir un fichier PDF en format HTML avec la bibliothèque Aspose.PDF C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "Présentation d'une nouvelle fonctionnalité puissante dans Aspose.PDF for .NET qui permet la conversion transparente de documents PDF en format HTML. Cette fonctionnalité prend en charge la sortie multi-page, la gestion des images SVG et des options pour le rendu de texte transparent, permettant aux développeurs de transformer facilement des PDF en contenu prêt pour le web avec seulement quelques lignes de code C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1650",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Aperçu

Cet article explique comment **convertir PDF en HTML en utilisant C#**. Il couvre ces sujets.

- [Convertir PDF en HTML](#csharp-pdf-to-html)

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Convertir PDF en HTML

**Aspose.PDF for .NET** offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie. Cet article traite de la manière de convertir un fichier PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for .NET offre la capacité de convertir des fichiers HTML en format PDF en utilisant l'approche InLineHtml. Nous avons reçu de nombreuses demandes pour une fonctionnalité qui convertit un fichier PDF en format HTML et avons fourni cette fonctionnalité. Veuillez noter que cette fonctionnalité prend également en charge XHTML 1.0.

**Aspose.PDF for .NET** prend en charge les fonctionnalités pour convertir un fichier PDF en HTML. Les principales tâches que vous pouvez accomplir avec la bibliothèque Aspose.PDF sont listées :

- Convertir PDF en HTML.
- Diviser la sortie en HTML multi-page.
- Spécifier le dossier pour stocker les fichiers SVG.
- Compresser les images SVG lors de la conversion.
- Enregistrer les images en tant qu'arrière-plan PNG.
- Spécifier le dossier des images.
- Créer des fichiers suivants avec uniquement le contenu du corps.
- Rendu de texte transparent.
- Rendu des couches de documents PDF.

{{% alert color="success" %}}
**Essayez de convertir PDF en HTML en ligne**

Aspose.PDF for .NET vous présente une application gratuite en ligne ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en HTML avec l'application gratuite](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET fournit un code de deux lignes pour transformer un fichier PDF source en HTML. L'[`énumération SaveFormat`](https://reference.aspose.com/pdf/fr/net/aspose.pdf/saveformat) contient la valeur Html qui vous permet d'enregistrer le fichier source au format HTML. Le code suivant montre le processus de conversion d'un fichier PDF en HTML.

<a name="csharp-pdf-to-html" id="cshart-pdf-to-html"><strong>Convertir PDF en HTML</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.Html** en appelant la méthode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### Diviser la sortie en HTML multi-page

Lors de la conversion d'un grand fichier PDF avec plusieurs pages en format HTML, la sortie apparaît comme une seule page HTML. Cela peut devenir très long. Pour contrôler la taille des pages, il est possible de diviser la sortie en plusieurs pages lors de la conversion de PDF en HTML. Veuillez essayer d'utiliser le code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### Spécifier le dossier pour stocker les fichiers SVG

Lors de la conversion de PDF en HTML, il est possible de spécifier le dossier dans lequel les images SVG doivent être enregistrées. Utilisez la [`classe HtmlSaveOption`](https://reference.aspose.com/pdf/fr/net/aspose.pdf/htmlsaveoptions) [`propriété SpecialFolderForSvgImages`](https://reference.aspose.com/pdf/fr/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages) pour spécifier un répertoire d'images SVG spécial. Cette propriété obtient ou définit le chemin vers le répertoire dans lequel les images SVG doivent être enregistrées lorsqu'elles sont rencontrées lors de la conversion. Si le paramètre est vide ou nul, alors tous les fichiers SVG sont enregistrés avec d'autres fichiers image.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### Compresser les images SVG lors de la conversion

Pour compresser les images SVG lors de la conversion de PDF en HTML, veuillez essayer d'utiliser le code suivant :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### Enregistrer les images en tant qu'arrière-plan PNG

Le format de sortie par défaut pour enregistrer les images est SVG. Lors de la conversion, certaines images du PDF sont transformées en images vectorielles SVG. Cela pourrait être lent. Au lieu de cela, les images pourraient être transformées en un fichier d'arrière-plan PNG pour chaque page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### Spécifier le dossier des images

Nous pouvons également spécifier le dossier dans lequel les images seront enregistrées lors de la conversion de PDF en HTML :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### Créer des fichiers suivants avec uniquement le contenu du corps

Récemment, on nous a demandé d'introduire une fonctionnalité où les fichiers PDF sont convertis en HTML et l'utilisateur peut obtenir uniquement le contenu de la balise `<body>` pour chaque page. Cela produirait un fichier avec des détails CSS, `<html>`, `<head>` et toutes les pages dans d'autres fichiers juste avec le contenu `<body>`.

Pour répondre à cette exigence, une nouvelle propriété, HtmlMarkupGenerationMode, a été introduite dans la classe HtmlSaveOptions.

Avec le code simple suivant, vous pouvez diviser la sortie HTML en pages. Dans les pages de sortie, tous les objets HTML doivent aller exactement là où ils vont maintenant (traitement et sortie des polices, création et sortie CSS, création et sortie des images), sauf que le HTML de sortie contiendra les contenus actuellement placés à l'intérieur des balises (maintenant les balises “body” seront omises). Cependant, lors de l'utilisation de cette approche, le lien vers le CSS est de la responsabilité de votre code, car des éléments comme seront supprimés. À cette fin, vous pouvez lire le CSS via File.ReadAllText() et l'envoyer via AJAX à une page web où il sera appliqué par jQuery.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### Rendu de texte transparent

Dans le cas où le fichier PDF source/d'entrée contient des textes transparents ombragés par des images de premier plan, il pourrait y avoir des problèmes de rendu de texte. Donc, pour répondre à de tels scénarios, les propriétés SaveShadowedTextsAsTransparentTexts et SaveTransparentTexts peuvent être utilisées.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### Rendu des couches de documents PDF

Nous pouvons rendre les couches de documents PDF dans un élément de type couche séparé lors de la conversion de PDF en HTML :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```