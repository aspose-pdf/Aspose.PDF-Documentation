---
title: 获取 PDF 文件信息
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/get-pdf-file-information/
description: 本节解释如何使用 Aspose.PDF Facades 获取 PDF 文件信息。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get PDF file information",
    "alternativeHeadline": "Retrieve Detailed Information from PDF Files",
    "abstract": "通过利用 PdfFileInfo 类的新功能解锁基本的 PDF 元数据。此功能使开发人员能够轻松访问和检索重要的文件特定详细信息，如主题、标题、关键字和创建者，从而增强文档管理和分析过程。通过利用这个强大的工具来简化 PDF 交互，以全面检索文件信息",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "285",
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
    "url": "/net/get-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

为了获取 PDF 文件的特定信息，您需要创建一个 [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 类的对象。之后，您可以获取各个属性的值，如主题、标题、关键字和创建者等。

以下代码片段向您展示如何获取 PDF 文件信息。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfInfo()
{
    // Define the directory for input files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Get and display PDF information
        Console.WriteLine("Subject: {0}", fileInfo.Subject);
        Console.WriteLine("Title: {0}", fileInfo.Title);
        Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
        Console.WriteLine("Creator: {0}", fileInfo.Creator);
        Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
        Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);

        // Check if the file is a valid PDF and if it is encrypted
        Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
        Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

        // Get dimensions of the first page
        Console.WriteLine("Page width: {0}", fileInfo.GetPageWidth(1));
        Console.WriteLine("Page height: {0}", fileInfo.GetPageHeight(1));
    }
}
```

## 获取元信息

为了获取信息，我们使用 [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header) 属性。通过 'Hashtable' 我们获取所有可能的值。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMetaInfo()
{
    // Define the directory for input files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "SetMetaInfo_out.pdf"))
    {
        // Retrieve all existing custom attributes
        var hashTable = new System.Collections.Hashtable(fileInfo.Header);

        // Enumerate and display all custom attributes
        var enumerator = hashTable.GetEnumerator();
        while (enumerator.MoveNext())
        {
            string output = $"{enumerator.Key} {enumerator.Value}";
            Console.WriteLine(output);
        }

        // Retrieve and display a specific custom attribute
        Console.WriteLine("Reviewer: " + fileInfo.GetMetaInfo("Reviewer"));
    }
}
```