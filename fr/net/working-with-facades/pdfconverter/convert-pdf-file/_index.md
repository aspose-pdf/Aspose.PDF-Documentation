---
title: Convertir un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/convert-pdf-file/
description: Apprenez à convertir un fichier PDF en divers formats dans .NET en utilisant Aspose.PDF pour une gestion flexible des documents.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF File",
    "alternativeHeadline": "Convert PDF Pages to Image Formats Efficiently",
    "abstract": "Débloquez la puissance de Aspose.PDF for .NET Facades pour convertir sans effort des pages PDF en divers formats d'image tels que JPEG, GIF et PNG avec la classe PdfConverter. Cette fonctionnalité permet un contrôle détaillé sur le processus de conversion, vous permettant de spécifier des paramètres tels que la résolution, le type de coordonnées et la plage de pages pour une sortie personnalisée. Améliorez vos capacités de gestion de documents en intégrant des conversions PDF en image sans faille dans vos applications.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "561",
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
    "url": "/net/convert-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Convertir des pages PDF en différents formats d'image (Facades)

Pour convertir des pages PDF en différents formats d'image, vous devez créer un objet [PdfConverter](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter) et ouvrir le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez appeler la méthode [DoConvert](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter/methods/doconvert) pour les tâches d'initialisation. Ensuite, vous pouvez parcourir toutes les pages en utilisant les méthodes [HasNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). La méthode [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) vous permet de créer une image d'une page particulière. Vous devez également passer ImageFormat à cette méthode afin de créer une image d'un type spécifique, c'est-à-dire JPEG, GIF ou PNG, etc. Enfin, appelez la méthode [Close](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter/methods/close) de la classe [PdfConverter](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter). Le code suivant vous montre comment convertir des pages PDF en images.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

Dans le prochain extrait de code, nous allons montrer comment vous pouvez changer certains paramètres. Avec [CoordinateType](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype), nous définissons le cadre 'CropBox'. De plus, nous pouvons changer la [Resolution](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter/properties/resolution) en spécifiant le nombre de points par pouce. Le suivant [FormPresentationMode](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - mode de présentation du formulaire. Ensuite, nous indiquons le [StartPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfconverter/properties/startpage) avec lequel le numéro de page du début de la conversion est défini. Nous pouvons également spécifier la dernière page en définissant une plage.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Set additional conversion settings
        converter.CoordinateType = Aspose.Pdf.PageCoordinateType.CropBox;
        converter.Resolution = new Aspose.Pdf.Devices.Resolution(600);
        converter.FormPresentationMode = Aspose.Pdf.Devices.FormPresentationMode.Production;
        converter.StartPage = 2;

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

## Convertir des pages PDF en formats d'image avec substitution de police personnalisée

Dans le code suivant, nous démontrons comment appliquer une substitution de police personnalisée lors du processus de conversion PDF-en-image. Nous utilisons la collection FontRepository.Substitutions pour enregistrer une règle de substitution personnalisée. Dans cet exemple, lorsque la police "Helvetica" est rencontrée, elle est remplacée par "Arial".

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using var converter = new Aspose.Pdf.Facades.PdfConverter();
    
    // Bind PDF document
    converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

    // Initialize the converting process
    converter.DoConvert();

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
    {
        // Generate output file name with '_out' suffix
        var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
        // Convert the page to image and save it
        converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Voir aussi

Aspose.PDF for .NET permet de convertir des documents PDF en divers formats et également de convertir d'autres formats en PDF. De plus, vous pouvez vérifier la qualité de la conversion Aspose.PDF et visualiser les résultats en ligne avec l'application de conversion Aspose.PDF. Apprenez la section [Conversion](/pdf/fr/net/converting/) pour résoudre vos tâches.