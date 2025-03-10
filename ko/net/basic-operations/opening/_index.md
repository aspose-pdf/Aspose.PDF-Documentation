---
title: 프로그래밍 방식으로 PDF 문서 열기
linktitle: PDF 열기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/open-pdf-document/
description: C# Aspose.PDF for .NET PDF 라이브러리에서 PDF 파일을 여는 방법을 알아보세요. 기존 PDF, 스트림에서 문서 및 암호화된 PDF 문서를 열 수 있습니다.
aliases:
    - /net/opening-a-pdf-document/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Open PDF document programmatically",
    "alternativeHeadline": "Programmatically Open and Access Various PDF Documents with C#",
    "abstract": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서를 여는 방법을 알아보세요. 이 기능은 개발자가 기존 PDF에 원활하게 접근하고, 스트림에서 문서를 로드하며, 암호화된 파일을 쉽게 처리할 수 있도록 하여 작업 효율성을 높이고 C#에서 PDF 조작의 기능을 확장합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "238",
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
    "url": "/net/open-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/open-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 기존 PDF 문서 열기

문서를 여는 방법에는 여러 가지가 있습니다. 가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        Console.WriteLine("Pages " + document.Pages.Count);
    }
}
```

## 스트림에서 기존 PDF 문서 열기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocumentStream()
{
    var fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Create a new WebClient instance
    var webClient = new System.Net.WebClient();
    // Concatenate the domain with the Web resource filename
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine("Pages " + document.Pages.Count);
    }
}
```

## 암호화된 PDF 문서 열기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocumentWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    const string password = "Aspose2020";
    try
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "DocSite.pdf", password))
        {
            Console.WriteLine("Pages " + document.Pages.Count);
        }
    }
    catch (Aspose.Pdf.InvalidPasswordException e)
    {
        Console.WriteLine(e);
    }
}
```