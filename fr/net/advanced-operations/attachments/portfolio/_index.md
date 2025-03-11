---
title: Travailler avec le Portfolio en PDF
linktitle: Portefeuille
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/portfolio/
description: Comment créer un portfolio PDF avec C#. Vous devez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Portfolio in PDF",
    "alternativeHeadline": "Create Dynamic PDF Portfolios from Multiple File Types",
    "abstract": "Découvrez la fonctionnalité innovante de Portfolio PDF dans Aspose.PDF, permettant aux utilisateurs de combiner facilement plusieurs types de fichiers, y compris Microsoft Excel, documents Word et images, en un PDF cohérent. Cette fonctionnalité préserve non seulement l'identité de chaque fichier individuel, mais simplifie également le processus de gestion, d'extraction et de modification des composants au sein du portfolio, garantissant une expérience utilisateur fluide pour la génération et la gestion de documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Portfolio, C# PDF creation, Aspose.PDF library, Document class, FileSpecification class, file extraction PDF, remove files PDF Portfolio, unified container PDF, embedded files collection, PDF manipulation .NET",
    "wordcount": "575",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2024-11-25",
    "description": "Comment créer un portfolio PDF avec C#. Vous devez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF."
}
</script>

## Comment créer un portfolio PDF

Aspose.PDF permet de créer des documents de portfolio PDF en utilisant la [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) classe. Ajoutez un fichier dans un objet Document.Collection après l'avoir obtenu avec la [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) classe. Lorsque les fichiers ont été ajoutés, utilisez la méthode Save de la classe Document pour enregistrer le document de portfolio.

L'exemple suivant utilise un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF.

Le code ci-dessous donne le portfolio suivant.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

### Portfolio PDF créé avec Aspose.PDF

![Un portfolio PDF créé avec Aspose.PDF for .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatePortfolio()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Instantiate document Collection object
        document.Collection = new Aspose.Pdf.Collection();

        // Get Files to add to Portfolio
        var excel = new Aspose.Pdf.FileSpecification(dataDir + "HelloWorld.xlsx");
        var word = new Aspose.Pdf.FileSpecification(dataDir + "HelloWorld.docx");
        var image = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg");

        // Provide description of the files
        excel.Description = "Excel File";
        word.Description = "Word File";
        image.Description = "Image File";

        // Add files to document collection
        document.Collection.Add(excel);
        document.Collection.Add(word);
        document.Collection.Add(image);

        // Save PDF document
        document.Save(dataDir + "CreatePortfolio_out.pdf");
    }
}
```

## Extraire des fichiers du portfolio PDF

Les portfolios PDF vous permettent de rassembler du contenu provenant de diverses sources (par exemple, fichiers PDF, Word, Excel, JPEG) dans un conteneur unifié. Les fichiers originaux conservent leur identité individuelle mais sont assemblés dans un fichier de portfolio PDF. Les utilisateurs peuvent ouvrir, lire, éditer et formater chaque fichier composant indépendamment des autres fichiers composants.

Aspose.PDF permet la création de documents de portfolio PDF en utilisant la [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) classe. Il offre également la possibilité d'extraire des fichiers d'un portfolio PDF.

Le code suivant montre les étapes pour extraire des fichiers d'un portfolio PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractPortfolioFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf"))
    {
        // Get collection of embedded files
        Aspose.Pdf.EmbeddedFileCollection embeddedFiles = document.EmbeddedFiles;
        // Iterate through individual file of Portfolio
        foreach (Aspose.Pdf.FileSpecification fileSpecification in embeddedFiles)
        {
            // Get the attachment and write to file or stream
            byte[] fileContent = new byte[fileSpecification.Contents.Length];
            fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
            string filename = Path.GetFileName(fileSpecification.Name);
            // Save the extracted file to some location
            using (FileStream fileStream = new FileStream(dataDir + filename + "_out", FileMode.Create))
            {
                fileStream.Write(fileContent, 0, fileContent.Length);
            }
        }
    }
}
```

![Extraire des fichiers du portfolio PDF](working-with-pdf-portfolio_2.jpg)

## Supprimer des fichiers du portfolio PDF

Pour supprimer des fichiers d'un portfolio PDF, essayez d'utiliser les lignes de code suivantes.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemovePortfolioFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf"))
    {
        document.Collection.Delete();
        // Save PDF document
        document.Save(dataDir + "NoPortFolio_out.pdf");
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