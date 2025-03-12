---
title: PDF 파일 정보 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/get-pdf-file-information/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일 정보를 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get PDF file information",
    "alternativeHeadline": "Retrieve Detailed Information from PDF Files",
    "abstract": "Aspose.PDF for .NET Facades의 PdfFileInfo 클래스를 활용하여 필수 PDF 메타데이터를 잠금 해제하는 새로운 기능입니다. 이 기능은 개발자가 주제, 제목, 키워드 및 작성자와 같은 중요한 파일별 세부정보에 쉽게 접근하고 검색할 수 있도록 하여 문서 관리 및 분석 프로세스를 향상시킵니다. 포괄적인 파일 정보 검색을 위한 이 강력한 도구를 활용하여 PDF 상호작용을 간소화하세요.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

PDF 파일의 특정 정보를 얻으려면 [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 클래스의 객체를 생성해야 합니다. 그 후, 주제, 제목, 키워드 및 작성자와 같은 개별 속성의 값을 가져올 수 있습니다.

다음 코드 스니펫은 PDF 파일 정보를 가져오는 방법을 보여줍니다.

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

## 메타 정보 가져오기

정보를 얻기 위해 [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header) 속성을 사용합니다. 'Hashtable'을 사용하여 가능한 모든 값을 가져옵니다.

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