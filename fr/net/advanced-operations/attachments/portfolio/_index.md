---
title: Travailler avec un Portfolio en PDF
linktitle: Portfolio
type: docs
weight: 40
url: fr/net/portfolio/
description: Comment créer un Portfolio PDF avec C#. Vous devriez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un Portfolio PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec un Portfolio en PDF",
    "alternativeHeadline": "Créer un Portfolio dans un document PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF en PDF",
    "keywords": "pdf, c#, portfolio",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "Comment créer un Portfolio PDF avec C#. Vous devriez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un Portfolio PDF."
}
</script>
## Comment créer un portfolio PDF

Aspose.PDF permet de créer des documents de portfolio PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Ajoutez un fichier dans un objet Document.Collection après l'avoir obtenu avec la classe [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Lorsque les fichiers ont été ajoutés, utilisez la méthode Save de la classe Document pour enregistrer le document de portfolio.

L'exemple suivant utilise un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF.

Le code ci-dessous aboutit au portfolio suivant.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

### Un portfolio PDF créé avec Aspose.PDF

![Un portfolio PDF créé avec Aspose.PDF pour .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Instancier l'objet Document
Document doc = new Document();

// Instancier l'objet de collection de documents
doc.Collection = new Collection();

// Obtenir les fichiers à ajouter au Portfolio
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// Fournir une description des fichiers
excel.Description = "Fichier Excel";
word.Description = "Fichier Word";
image.Description = "Fichier Image";

// Ajouter les fichiers à la collection de documents
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// Enregistrer le document de portfolio
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## Extraire des fichiers d'un Portfolio PDF

Les Portfolios PDF vous permettent de rassembler des contenus provenant de diverses sources (par exemple, des fichiers PDF, Word, Excel, JPEG) dans un conteneur unifié. Les fichiers originaux conservent leur identité individuelle mais sont assemblés dans un fichier Portfolio PDF. Les utilisateurs peuvent ouvrir, lire, modifier et formater chaque fichier composant indépendamment des autres fichiers du portefeuille.

Aspose.PDF permet la création de documents Portfolio PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Il offre également la capacité d'extraire des fichiers d'un portfolio PDF.

Le fragment de code suivant vous montre les étapes pour extraire des fichiers d'un portfolio PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Charger le PDF Portfolio source
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// Obtenir la collection de fichiers intégrés
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// Itérer à travers chaque fichier du Portfolio
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // Obtenir la pièce jointe et écrire dans un fichier ou un flux
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // Sauvegarder le fichier extrait à un certain emplacement
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // Fermer l'objet stream
    fileStream.Close();
}
```
![Extract files from PDF Portfolio](working-with-pdf-portfolio_2.jpg)

## Supprimer des fichiers d'un portfolio PDF

Pour supprimer des fichiers d'un portfolio PDF, essayez d'utiliser les lignes de code suivantes.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Charger le portfolio PDF source
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
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


