---
title: C#로 PDF 파일에 링크 만들기
linktitle: 링크 만들기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/create-links/
description: 이 섹션에서는 C#으로 PDF 문서에 링크를 만드는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Links in PDF file with C#",
    "alternativeHeadline": "Create Interactive Links in PDFs Using C#",
    "abstract": "이 새로운 기능은 개발자가 C#을 사용하여 PDF 문서 내에서 대화형 링크를 원활하게 생성할 수 있도록 합니다. 이 기능은 외부 애플리케이션이나 다른 PDF 파일에 링크를 연결하여 사용자 참여를 향상시키며, 보다 동적이고 기능이 풍부한 문서 경험을 가능하게 합니다. 튜토리얼 및 사용자 안내에 이상적이며, 이 통합은 사용자가 콘텐츠를 효과적으로 연결할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Create Links, PDF document, C#, LinkAnnotation, LaunchAction, GoToRemoteAction, Aspose.PDF, Document object, PDF manipulation, External link",
    "wordcount": "690",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2024-11-25",
    "description": "이 섹션에서는 C#으로 PDF 문서에 링크를 만드는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 링크 만들기

문서에 애플리케이션 링크를 추가하면 문서에서 애플리케이션에 링크할 수 있습니다. 이는 독자가 튜토리얼의 특정 지점에서 특정 작업을 수행하도록 하거나 기능이 풍부한 문서를 만들고자 할 때 유용합니다. 애플리케이션 링크를 만들려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 링크를 추가할 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 가져옵니다.
1. Page 및 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 생성합니다.
1. [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 사용하여 링크 속성을 설정합니다.
1. 또한 [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) 객체의 Action 속성을 설정합니다.
1. [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) 객체를 생성할 때 시작할 애플리케이션을 지정합니다.
1. 링크를 Page 객체의 [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) 속성에 추가합니다.
1. 마지막으로 Document 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 애플리케이션에 링크를 만드는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateApplicationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateApplicationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### PDF 파일에서 PDF 문서 링크 만들기

Aspose.PDF for .NET은 외부 PDF 파일에 링크를 추가하여 여러 문서를 연결할 수 있도록 합니다. PDF 문서 링크를 만들려면:

1. 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 그런 다음 링크를 추가할 특정 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 가져옵니다.
1. Page 및 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 생성합니다.
1. [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 사용하여 링크 속성을 설정합니다.
1. Action 속성을 [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction) 객체로 설정합니다.
1. GoToRemoteAction 객체를 생성할 때 시작해야 할 PDF 파일과 열어야 할 페이지 번호를 지정합니다.
1. 링크를 Page 객체의 Annotations 컬렉션에 추가합니다.
1. Document 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 PDF 문서 링크를 만드는 방법을 보여줍니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateDocumentLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateDocumentLink_out.pdf");
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