---
title: Comment créer un PDF en utilisant C#
linktitle: Créer un document PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/create-pdf-document/
description: Créer et formater le document PDF avec Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "La nouvelle fonctionnalité dans Aspose.PDF for .NET permet aux développeurs de créer et de formater facilement des documents PDF en utilisant C#. Avec cette API intuitive, les utilisateurs peuvent générer des PDF consultables, manipuler du contenu étiqueté pour l'accessibilité et intégrer sans effort la génération de PDF dans diverses applications .NET, améliorant ainsi la productivité et rationalisant les flux de travail.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Créer et formater le document PDF avec Aspose.PDF for .NET."
}
</script>

Nous cherchons toujours un moyen de générer des documents PDF et de travailler avec eux dans des projets C# de manière plus précise, exacte et efficace. Avoir des fonctions faciles à utiliser d'une bibliothèque nous permet de nous concentrer davantage sur le travail, et moins sur les détails chronophages de la génération de PDF, que ce soit dans .NET.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Créer (ou générer) un document PDF en utilisant le langage C#

L'API Aspose.PDF for .NET vous permet de créer et de lire des fichiers PDF en utilisant C# et VB.NET. L'API peut être utilisée dans une variété d'applications .NET, y compris WinForms, ASP.NET et plusieurs autres. Dans cet article, nous allons montrer comment utiliser l'API Aspose.PDF for .NET pour générer et lire facilement des fichiers PDF dans des applications .NET.

### Comment créer un fichier PDF simple

Pour créer un fichier PDF en utilisant C#, les étapes suivantes peuvent être utilisées.

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à la collection [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) de l'objet Document.
1. Ajoutez [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) à la collection [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la page.
1. Enregistrez le document PDF résultant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHelloWorldDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

### Comment créer un document PDF consultable

Aspose.PDF for .NET fournit la fonctionnalité de créer ainsi que de manipuler des documents PDF existants. Lors de l'ajout d'éléments de texte dans un fichier PDF, le PDF résultant est consultable. Cependant, si nous convertissons une image contenant du texte en fichier PDF, le contenu à l'intérieur du PDF n'est pas consultable. Cependant, en tant que solution de contournement, nous pouvons utiliser l'OCR sur le fichier résultant, afin qu'il devienne consultable.

Cette logique spécifiée ci-dessous reconnaît le texte pour les images PDF. Pour la reconnaissance, vous pouvez utiliser des supports OCR externes conformes à la norme HOCR. À des fins de test, nous avons utilisé un OCR Google Tesseract gratuit. Par conséquent, vous devez d'abord installer Tesseract-OCR sur votre système, et vous aurez l'application console Tesseract.

Voici le code complet pour accomplir cette exigence :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateSearchableDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchableDocument.pdf"))
    {
        document.Convert(CallBackGetHocr);

        // Save PDF document
        document.Save(dataDir + "SearchableDocument_out.pdf");
    }
}

private static string CallBackGetHocr(System.Drawing.Image img)
{
    var tmpFile = Path.GetTempFileName();
    try
    {
        using (var bmp = new System.Drawing.Bitmap(img))
        {
            bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        }

        var inputFile = string.Concat('"', tmpFile, '"');
        var outputFile = string.Concat('"', tmpFile, '"');
        var arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        var tesseractProcessName = RunExamples.GetTesseractExePath();

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
            CreateNoWindow = true,
            WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
            WorkingDirectory = Path.GetDirectoryName(tesseractProcessName)
        };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### Comment créer un PDF accessible en utilisant des fonctions de bas niveau

Ce code fonctionne avec un document PDF et son contenu étiqueté, en utilisant une bibliothèque Aspose.PDF pour le traiter.

L'exemple crée un nouvel élément span dans le contenu étiqueté de la première page d'un PDF, trouve tous les éléments BDC et les associe au span. Le document modifié est ensuite enregistré.

Vous pouvez créer une déclaration bdc en spécifiant mcid, lang et le texte d'expansion en utilisant l'objet BDCProperties :

```cs
var bdc = new Aspose.Pdf.Operators.BDC("P", new Aspose.Pdf.Facades.BDCProperties(1, "de", "Hallo, welt!"));
```

Après avoir créé l'arbre de structure, il est possible de lier l'opérateur BDC à l'élément spécifié de la structure avec la méthode Tag sur l'objet élément :

```cs
Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

Étapes pour créer un PDF accessible :

1. Chargez le document PDF.
1. Accédez au contenu étiqueté.
1. Créez un élément Span.
1. Ajoutez le Span à l'élément racine.
1. Itérez sur le contenu de la page.
1. Vérifiez les éléments BDC et étiquetez-les.
1. Enregistrez le document modifié.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create a span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

Ce code modifie un PDF en créant un élément span dans le contenu étiqueté du document et en étiquetant un contenu spécifique (opérations BDC) de la première page avec ce span. Le PDF modifié est ensuite enregistré dans un nouveau fichier.

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