---
title: Working with Portfolio in PDF
linktitle: Portfolio
type: docs
weight: 40
url: /net/portfolio/
description: How to Create a PDF Portfolio with C#. You should use a Microsoft Excel File, a Word document, and an image file to create a PDF Portfolio.
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
    "alternativeHeadline": "Create Portfolio in PDF document",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation in pdf",
    "keywords": "pdf, c#, portfolio",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "How to Create a PDF Portfolio with C#. You should use a Microsoft Excel File, a Word document, and an image file to create a PDF Portfolio."
}
</script>

## How to Create a PDF Portfolio

Aspose.PDF allows creating PDF Portfolio documents using the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class. Add a file into a Document.Collection object after getting it with the [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) class. When the files have been added, use the Document class' Save method to save the portfolio document.

The following example uses a Microsoft Excel File, a Word document and an image file to create a PDF Portfolio.

The code below results in the following portfolio.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

### A PDF Portfolio created with Aspose.PDF

![A PDF Portfolio created with Aspose.PDF for .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Instantiate Document Object
Document document = new Document();

// Instantiate document Collection object
document.Collection = new Collection();

// Get Files to add to Portfolio
FileSpecification excel = new FileSpecification(dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification(dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// Provide description of the files
excel.Description = "Excel File";
word.Description = "Word File";
image.Description = "Image File";

// Add files to document collection
document.Collection.Add(excel);
document.Collection.Add(word);
document.Collection.Add(image);

// Save Portfolio document
document.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```

## Extract files from PDF Portfolio

PDF Portfolios allow you to bring together content from a variety of sources (for example, PDF, Word, Excel, JPEG files) into one unified container. The original files retain their individual identities but are assembled into a PDF Portfolio file. Users can open, read, edit, and format each component file independently of the other component files.

Aspose.PDF allows the creation of PDF Portfolio documents using [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class. It also offers the capability to extract files from PDF portfolio.

The following code snippet shows you the steps to extract files from PDF portfolio.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Load source PDF Portfolio
Document document = new Document(dataDir + "PDFPortfolio.pdf");
// Get collection of embedded files
EmbeddedFileCollection embeddedFiles = document.EmbeddedFiles;
// Iterate through individual file of Portfolio
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // Get the attachment and write to file or stream
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // Save the extracted file to some location
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // Close the stream object
    fileStream.Close();
}
```

![Extract files from PDF Portfolio](working-with-pdf-portfolio_2.jpg)

## Remove Files from PDF Portfolio

In order to delete/remove files from PDF portfolio, try using the following code lines.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Load source PDF Portfolio
Document document = new Document(dataDir + "PDFPortfolio.pdf");
document.Collection.Delete();
document.Save(dataDir + "No_PortFolio_out.pdf");
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
