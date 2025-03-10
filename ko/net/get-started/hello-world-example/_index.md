---
title: C# 언어를 사용한 Hello World 예제
linktitle: Hello World 예제
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/hello-world-example/
description: 이 샘플은 Aspose.PDF를 사용하여 "Hello World"라는 텍스트가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using C# language",
    "alternativeHeadline": "Aspose.PDF C# example",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2024-11-26",
    "description": "이 샘플은 Aspose.PDF를 사용하여 'Hello World'라는 텍스트가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.",
    "articleBody": "A \"Hello World\" example is traditionally used to introduce features of a programming language or software with a simple use case.\nAspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text \"Hello World!\". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.\nBelow code snippet follows these steps:\n1. // Create PDF document\n2. Add a Page to document object\n3. Create a TextFragment\n4. Add TextFragment to Paragraph collection of the page\n5. Save resultant PDF document\nFollowing code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API."
}
</script>

"Hello World" 예제는 전통적으로 프로그래밍 언어나 소프트웨어의 기능을 간단한 사용 사례로 소개하는 데 사용됩니다.

Aspose.PDF for .NET는 개발자가 .NET 애플리케이션에 PDF 문서 생성, 조작 및 변환 기능을 포함할 수 있도록 하는 기능이 풍부한 PDF API입니다. PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX 및 이미지 파일 형식을 포함한 많은 인기 있는 파일 형식과 함께 작업하는 것을 지원합니다. 이 기사에서는 "Hello World!"라는 텍스트가 포함된 PDF 문서를 생성합니다. 환경에 Aspose.PDF for .NET를 설치한 후 아래 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

다음 코드 스니펫은 다음 단계를 따릅니다:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 인스턴스화합니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 추가합니다.
1. [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) 객체를 생성합니다.
1. 페이지의 [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) 컬렉션에 TextFragment를 추가합니다.
1. 결과 PDF 문서를 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)합니다.

다음 코드 스니펫은 Aspose.PDF for .NET API의 작동을 보여주는 Hello World 프로그램입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

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