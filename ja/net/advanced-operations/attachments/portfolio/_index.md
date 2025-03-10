---
title: PDFポートフォリオの操作
linktitle: ポートフォリオ
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/portfolio/
description: C#を使用してPDFポートフォリオを作成する方法。Microsoft Excelファイル、Word文書、および画像ファイルを使用してPDFポートフォリオを作成する必要があります。
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
    "abstract": "Aspose.PDFの革新的なPDFポートフォリオ機能を発見し、ユーザーがMicrosoft Excel、Word文書、画像などの複数のファイルタイプを簡単に統合して一貫したPDFにすることを可能にします。この機能は、各個別ファイルのアイデンティティを保持するだけでなく、ポートフォリオ内のコンポーネントの管理、抽出、修正のプロセスを簡素化し、文書生成と管理のための効率的なユーザー体験を保証します。",
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
    "description": "C#を使用してPDFポートフォリオを作成する方法。Microsoft Excelファイル、Word文書、および画像ファイルを使用してPDFポートフォリオを作成する必要があります。"
}
</script>

## PDFポートフォリオの作成方法

Aspose.PDFを使用すると、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスを使用してPDFポートフォリオ文書を作成できます。[FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification)クラスを使用してファイルを取得した後、Document.Collectionオブジェクトにファイルを追加します。ファイルが追加されたら、DocumentクラスのSaveメソッドを使用してポートフォリオ文書を保存します。

以下の例では、Microsoft Excelファイル、Word文書、および画像ファイルを使用してPDFポートフォリオを作成します。

以下のコードは、次のポートフォリオを生成します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

### Aspose.PDFで作成されたPDFポートフォリオ

![Aspose.PDF for .NETで作成されたPDFポートフォリオ](working-with-pdf-portfolio_1.jpg)

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

## PDFポートフォリオからファイルを抽出する

PDFポートフォリオを使用すると、さまざまなソース（たとえば、PDF、Word、Excel、JPEGファイル）からのコンテンツを1つの統一コンテナにまとめることができます。元のファイルはそれぞれのアイデンティティを保持しながら、PDFポートフォリオファイルに組み込まれます。ユーザーは、他のコンポーネントファイルとは独立して、各コンポーネントファイルを開いて、読み取り、編集、フォーマットできます。

Aspose.PDFを使用すると、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスを使用してPDFポートフォリオ文書を作成できます。また、PDFポートフォリオからファイルを抽出する機能も提供しています。

以下のコードスニペットは、PDFポートフォリオからファイルを抽出する手順を示しています。

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

![PDFポートフォリオからファイルを抽出する](working-with-pdf-portfolio_2.jpg)

## PDFポートフォリオからファイルを削除する

PDFポートフォリオからファイルを削除するには、以下のコード行を使用してみてください。

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