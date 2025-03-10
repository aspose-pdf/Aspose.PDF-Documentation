---
title: PDF에서 포트폴리오 작업하기
linktitle: 포트폴리오
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/portfolio/
description: C#으로 PDF 포트폴리오를 만드는 방법. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성해야 합니다.
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
    "abstract": "Aspose.PDF의 혁신적인 PDF 포트폴리오 기능을 발견하여 사용자가 Microsoft Excel, Word 문서 및 이미지를 포함한 여러 파일 형식을 손쉽게 결합하여 일관된 PDF로 만들 수 있도록 합니다. 이 기능은 각 개별 파일의 정체성을 유지할 뿐만 아니라 포트폴리오 내에서 구성 요소를 관리, 추출 및 수정하는 과정을 단순화하여 문서 생성 및 관리에 대한 원활한 사용자 경험을 보장합니다.",
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
    "description": "C#으로 PDF 포트폴리오를 만드는 방법. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성해야 합니다."
}
</script>

## PDF 포트폴리오 만들기

Aspose.PDF는 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있습니다. [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 클래스를 사용하여 파일을 가져온 후 Document.Collection 객체에 파일을 추가합니다. 파일이 추가되면 Document 클래스의 Save 메서드를 사용하여 포트폴리오 문서를 저장합니다.

다음 예제는 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성합니다.

아래 코드는 다음과 같은 포트폴리오를 생성합니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

### Aspose.PDF로 생성된 PDF 포트폴리오

![Aspose.PDF for .NET로 생성된 PDF 포트폴리오](working-with-pdf-portfolio_1.jpg)

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

## PDF 포트폴리오에서 파일 추출하기

PDF 포트폴리오는 다양한 출처(예: PDF, Word, Excel, JPEG 파일)의 콘텐츠를 하나의 통합 컨테이너로 모을 수 있게 해줍니다. 원본 파일은 개별 정체성을 유지하지만 PDF 포트폴리오 파일로 조립됩니다. 사용자는 각 구성 요소 파일을 다른 구성 요소 파일과 독립적으로 열고, 읽고, 편집하고, 형식을 지정할 수 있습니다.

Aspose.PDF는 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있습니다. 또한 PDF 포트폴리오에서 파일을 추출하는 기능도 제공합니다.

다음 코드 조각은 PDF 포트폴리오에서 파일을 추출하는 단계를 보여줍니다.

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

![PDF 포트폴리오에서 파일 추출하기](working-with-pdf-portfolio_2.jpg)

## PDF 포트폴리오에서 파일 제거하기

PDF 포트폴리오에서 파일을 삭제/제거하려면 다음 코드 줄을 사용해 보십시오.

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