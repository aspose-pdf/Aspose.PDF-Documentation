---
title: PDFドキュメントへの添付ファイルの追加
linktitle: PDFドキュメントへの添付ファイルの追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-attachment-to-pdf-document/
description: このページでは、Aspose.PDF for .NETライブラリを使用してPDFファイルに添付ファイルを追加する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Attachment to a PDF document",
    "alternativeHeadline": "Easily Attach Files to Your PDF Documents",
    "abstract": "Aspose.PDF for .NETは、ユーザーがテキストファイルや画像を含むさまざまな添付ファイルをシームレスに追加できる効率的な方法を提供します。この機能により、PDF内に追加情報を埋め込むプロセスが簡素化され、重要なデータがドキュメント内で簡単にアクセスできるようになります。この強力な機能を使用してドキュメント管理を最適化し、関連リソースを一緒に保つことでユーザーエクスペリエンスを向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Adding attachments to PDF, PDF file types, Aspose.PDF for .NET, FileSpecification object, Document object, EmbeddedFiles collection, PDF document manipulation, C# PDF library, PDF attachment functionality, Aspose.Drawing integration",
    "wordcount": "309",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "このページでは、Aspose.PDF for .NETライブラリを使用してPDFファイルに添付ファイルを追加する方法について説明します。"
}
</script>

添付ファイルにはさまざまな情報を含めることができ、さまざまなファイルタイプが使用できます。この記事では、PDFファイルに添付ファイルを追加する方法について説明します。

次のコードスニペットは、[Aspose.Drawing](/pdf/net/drawing/)ライブラリでも機能します。

1. 新しいC#プロジェクトを作成します。
1. Aspose.PDF DLLへの参照を追加します。
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成します。
1. 追加するファイルとファイルの説明を持つ[FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification)オブジェクトを作成します。
1. [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification)オブジェクトを[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection)コレクションに、コレクションのAddメソッドを使用して追加します。

[EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection)コレクションには、PDFファイル内のすべての添付ファイルが含まれています。次のコードスニペットは、PDFドキュメントに添付ファイルを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddEmbeddedFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"))
    {
        // Setup new file to be added as attachment
        Aspose.Pdf.FileSpecification fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "test.txt", "Sample text file");

        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);

        // Save PDF document
        document.Save(dataDir + "AddAnnotations_out.pdf");
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