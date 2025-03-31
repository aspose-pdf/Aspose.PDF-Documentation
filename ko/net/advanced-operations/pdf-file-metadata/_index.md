---
title: C#에서 PDF 파일 메타데이터 작업하기
linktitle: PDF 파일 메타데이터
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 200
url: /ko/net/pdf-file-metadata/
description: Aspose.PDF를 사용하여 .NET에서 저자 및 제목과 같은 PDF 메타데이터를 추출하고 관리하는 방법을 탐색합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF File Metadata in C#",
    "alternativeHeadline": "Extracting and Managing PDF Metadata in C#",
    "abstract": "C# 개발자를 위한 새로운 기능으로 PDF 파일 관리의 힘을 활용하여 PDF 파일 메타데이터에 원활하게 접근할 수 있습니다. 파일 속성에 대한 통찰력을 얻고, XMP 메타데이터를 추출하며, 문서 정보를 쉽게 업데이트하여 문서 처리 프로세스를 간소화합니다. PDF 메타데이터를 효율적으로 유지하고 조작하기 위한 향상된 기능을 경험하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF file metadata, C# PDF manipulation, get PDF file information, set PDF file information, XMP metadata, Aspose.PDF for .NET, document properties, PDF metadata management",
    "wordcount": "834",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2024-11-25",
    "description": "이 섹션에서는 PDF 파일 정보를 가져오는 방법, PDF 파일에서 XMP 메타데이터를 가져오는 방법, PDF 파일 정보를 설정하는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 파일 정보 가져오기

PDF 파일의 특정 정보를 가져오려면 먼저 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 객체의 [Info](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/properties/info) 속성을 사용하여 [DocumentInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf/documentinfo) 객체를 가져와야 합니다. [DocumentInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf/documentinfo) 객체를 가져온 후에는 개별 속성의 값을 가져올 수 있습니다. 다음 코드 스니펫은 PDF 파일 정보를 가져오는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;

        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;
        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## PDF 파일 정보 설정하기

Aspose.PDF for .NET은 저자, 생성 날짜, 주제 및 제목과 같은 PDF에 대한 파일 특정 정보를 설정할 수 있게 해줍니다. 이 정보를 설정하려면:

1. [DocumentInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf/documentinfo) 객체를 생성합니다.
1. 속성의 값을 설정합니다.
1. Document 클래스의 Save 메서드를 사용하여 업데이트된 문서를 저장합니다.

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";
        docInfo.Producer = "Custom producer";
        docInfo.Creator = "Custom creator";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";
        docInfo.Producer = "Custom producer";
        docInfo.Creator = "Custom creator";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## PDF 파일에서 XMP 메타데이터 가져오기

Aspose.PDF는 PDF 파일의 XMP 메타데이터에 접근할 수 있게 해줍니다. PDF 파일의 메타데이터를 가져오려면:

1. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 객체를 생성하고 입력 PDF 파일을 엽니다.
1. [Metadata](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/properties/metadata) 속성을 사용하여 파일의 메타데이터를 가져옵니다.

다음 코드 스니펫은 PDF 파일에서 메타데이터를 가져오는 방법을 보여줍니다.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## PDF 파일에 XMP 메타데이터 설정하기

Aspose.PDF는 PDF 파일에 메타데이터를 설정할 수 있게 해줍니다. 메타데이터를 설정하려면:

1. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 객체를 생성합니다.
1. [Metadata](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/properties/metadata) 속성을 사용하여 메타데이터 값을 설정합니다.
1. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 문서를 저장합니다.

다음 코드 스니펫은 PDF 파일에 메타데이터를 설정하는 방법을 보여줍니다.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## 접두사가 있는 메타데이터 삽입하기

일부 개발자는 접두사가 있는 새로운 메타데이터 네임스페이스를 생성해야 합니다. 다음 코드 스니펫은 접두사가 있는 메타데이터를 삽입하는 방법을 보여줍니다.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}
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