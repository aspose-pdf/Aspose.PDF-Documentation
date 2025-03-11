---
title: Работа с портфолио в формате PDF
linktitle: Портфолио
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/portfolio/
description: Как создать портфолио в формате PDF с помощью C#. Для создания портфолио в формате PDF следует использовать файл Microsoft Excel, документ Word и файл изображения.
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
    "abstract": "Откройте для себя инновационную функцию PDF Portfolio в Aspose.PDF, которая позволяет пользователям легко объединять несколько типов файлов, включая Microsoft Excel, документы Word и изображения, в единый PDF-документ. Эта функция не только сохраняет идентичность каждого отдельного файла, но и упрощает процесс управления, извлечения и изменения компонентов в портфеле, обеспечивая удобство работы с документами",
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
    "description": "Как создать портфолио в формате PDF на C#. Для создания портфолио в формате PDF следует использовать файл Microsoft Excel, документ Word и файл с изображением"
}
</script>

## Как создать портфолио PDF

Aspose.PDF позволяет создавать документы портфолио PDF с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Добавьте файл в объект Document.Collection после его получения с помощью класса [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Когда файлы будут добавлены, используйте метод Save класса Document для сохранения документа портфолио.

В следующем примере используется файл Microsoft Excel, документ Word и файл изображения для создания портфолио PDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

### Портфолио PDF, созданное с помощью Aspose.PDF

![Портфолио PDF, созданное с Aspose.PDF](working-with-pdf-portfolio_1.jpg)

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

## Извлечение файлов из портфолио PDF

Портфолио PDF позволяет объединить содержимое из различных источников (например, PDF, Word, Excel, файлы JPEG) в один унифицированный контейнер. Исходные файлы сохраняют свою индивидуальность, но собираются в файл портфолио PDF. Пользователи могут открывать, читать, редактировать и форматировать каждый компонентный файл независимо от других компонентных файлов.

Aspose.PDF позволяет создавать документы PDF Portfolio с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) и предлагает возможность извлекать файлы из PDF-портфолио.

Следующий фрагмент кода показывает, как извлечь файлы из PDF-портфолио.

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

![Извлечение файлов из PDF Portfolio](working-with-pdf-portfolio_2.jpg)

## Удаление файлов из портфолио PDF

Чтобы удалить файлы из портфолио PDF, попробуйте использовать следующие строки кода.

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