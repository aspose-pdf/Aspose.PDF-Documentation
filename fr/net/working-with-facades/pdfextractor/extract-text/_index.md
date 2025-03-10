---
title: Extraire du texte d'un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/extract-text/
description: Cette section explique comment extraire du texte d'un PDF en utilisant la classe PdfExtractor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF File",
    "alternativeHeadline": "Effortless Text Extraction from PDF Files",
    "abstract": "La classe PdfExtractor permet une extraction efficace de texte à partir de fichiers PDF grâce à plusieurs méthodes, permettant aux utilisateurs de récupérer facilement du texte, des images et des pièces jointes. En utilisant des méthodes telles que ExtractText, GetText et GetNextPageText, les développeurs peuvent extraire et enregistrer sans effort le contenu textuel de pages individuelles ou de documents entiers, rationalisant ainsi les tâches de manipulation de PDF. Avec des modes d'extraction flexibles disponibles, cette fonctionnalité améliore le contrôle sur le format de sortie, en faisant un outil essentiel pour quiconque travaillant avec des données PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "441",
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
    "url": "/net/extract-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Dans cet article, nous examinerons les détails de l'extraction de texte d'un fichier PDF. Toutes ces fonctionnalités d'extraction sont fournies à un seul endroit, dans la classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Nous verrons comment utiliser ces fonctionnalités dans notre code.

La classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) fournit trois types de capacités d'extraction. Ces trois catégories sont Texte, Images et Pièces jointes. Afin d'effectuer l'extraction sous chacune de ces trois catégories, PdfExtractor fournit diverses méthodes qui fonctionnent ensemble pour vous donner le résultat final.

Par exemple, pour extraire du texte, vous pouvez utiliser trois méthodes, à savoir [ExtractText, GetText, HasNextPageText et GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index). Maintenant, pour commencer à extraire du texte, tout d'abord, vous devez appeler la méthode [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index) ; cela extraira le texte du fichier PDF et le stockera en mémoire. Après cela, la méthode [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) prendra ce texte extrait et l'enregistrera sur le disque à l'emplacement spécifié dans un fichier. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) vous aide à parcourir chaque page et à vérifier si la page suivante contient du texte ou non. Si elle contient du texte, alors [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) vous aidera à enregistrer le texte d'une page individuelle dans le fichier.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```

Pour extraire le mode d'extraction de texte, utilisez le code suivant :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextExtractonMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "ExtractTextExtractonMode.pdf");

        // ExtractText
        // pdfExtractor.ExtractTextMode = 0; // pure mode
        pdfExtractor.ExtractTextMode = 1; // raw mode
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "ExtractTextExtractonMode_out.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```