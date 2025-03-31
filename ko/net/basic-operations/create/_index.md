---
title: 프로그래밍 방식으로 PDF 문서 만들기
linktitle: PDF 만들기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/create-document/
description: 이 페이지에서는 Aspose.PDF 라이브러리를 사용하여 처음부터 PDF 문서를 만드는 방법을 설명합니다.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 개발자가 C# 및 VB.NET을 사용하여 프로그래밍 방식으로 PDF 문서를 생성할 수 있도록 하여 WinForms 및 ASP.NET과 같은 다양한 .NET 애플리케이션의 프로세스를 간소화합니다. 페이지와 텍스트를 추가하는 간단한 방법으로 사용자는 처음부터 사용자 지정 PDF 파일을 쉽게 생성하여 애플리케이션 기능과 사용자 경험을 향상시킬 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

Aspose.PDF for .NET API를 사용하면 C# 및 VB.NET을 사용하여 PDF 파일을 생성하고 읽을 수 있습니다. 이 API는 WinForms, ASP.NET 및 여러 다른 .NET 애플리케이션에서 사용할 수 있습니다. 이 기사에서는 Aspose.PDF for .NET API를 사용하여 .NET 애플리케이션에서 PDF 파일을 쉽게 생성하고 읽는 방법을 보여줍니다.

## C#을 사용하여 PDF 파일 만들기

C#을 사용하여 PDF 파일을 만들기 위해 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스의 객체를 생성합니다.
1. Document 객체의 [Pages](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/properties/pages) 컬렉션에 [Page](https://reference.aspose.com/pdf/ko/net/aspose.pdf/page) 객체를 추가합니다.
1. 페이지의 [Paragraphs](https://reference.aspose.com/pdf/ko/net/aspose.pdf/page/properties/paragraphs) 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textfragment)를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

다음 코드 스니펫은 [Aspose.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

이 경우, 우리는 A4 페이지 크기와 세로 방향의 PDF 한 페이지 문서를 생성합니다. 우리의 페이지에는 페이지의 왼쪽 상단 부분에 "Hello, World"가 포함됩니다.