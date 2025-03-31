---
title: 자바스크립트 액션 추가 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/adding-javascript-actions/
description: Aspose.PDF를 사용하여 .NET에서 PDF에 버튼 클릭 또는 양식 제출과 같은 자바스크립트 액션을 추가하는 방법을 알아보세요.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Javascript actions PDF",
    "alternativeHeadline": "Enhance PDF with Interactive JavaScript Actions",
    "abstract": "Aspose.PDF for .NET PdfContentEditor 클래스를 사용하여 인터랙티브 자바스크립트 액션을 통합하여 PDF를 향상시키세요. 이 기능은 사용자가 동적 링크를 생성하고 특정 메뉴 항목 액션을 실행할 수 있게 하여, 문서 경험을 사용자 정의 인터랙티브 요소로 풍부하게 합니다. 사용자 상호작용에 원활하게 반응하는 이벤트 기반 액션을 추가하여 작업 흐름을 간소화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "216",
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
    "url": "/net/adding-javascript-actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-javascript-actions/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/PdfContentEditor) 클래스는 Aspose.Pdf.Facades 패키지에 포함되어 있으며 PDF 파일에 자바스크립트 액션을 추가할 수 있는 유연성을 제공합니다. PDF 뷰어에서 메뉴 항목을 실행하는 일련의 액션에 해당하는 링크를 생성할 수 있습니다. 이 클래스는 문서 이벤트에 대한 추가 액션을 생성하는 기능도 제공합니다.

우선, [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 객체가 그려지며, 우리의 예에서는 [Rectangle](https://reference.aspose.com/pdf/ko/net/aspose.pdf.drawing/rectangle)입니다. 그리고 Rectangle에 [createJavaScriptLink](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) 액션을 설정합니다. 이후 문서를 저장할 수 있습니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Create Javascript link
        var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

        var code = "app.alert('Welcome to Aspose!');";
        editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

        // Save PDF document
        editor.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");

    // Create Javascript link
    var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

    var code = "app.alert('Welcome to Aspose!');";
    editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

    // Save PDF document
    editor.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}