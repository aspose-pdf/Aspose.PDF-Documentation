---
title: 기존 PDF 파일에 주석 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/adding-annotations-to-existing-pdf-file/
description: Aspose.PDF를 사용하여 .NET에서 기존 PDF 문서에 댓글이나 강조와 같은 주석을 추가하는 방법을 알아보세요.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Annotations to existing PDF file",
    "alternativeHeadline": "Enhance PDF with Dynamic Annotation Capabilities",
    "abstract": "사용자가 자유 텍스트, 텍스트 및 선 주석을 포함한 다양한 유형의 주석을 원활하게 추가할 수 있도록 하는 새로운 주석 기능으로 PDF 문서를 향상시키십시오. PdfContentEditor를 활용하여 기존 PDF 파일을 쉽게 바인딩하고 주석 영역을 지정하여 몇 줄의 코드로 문서의 상호작용성과 명확성을 개선할 수 있습니다. 풍부한 주석을 PDF에 직접 통합하여 작업 흐름을 최적화하고 사용자 참여 및 이해도를 높이십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "621",
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
    "url": "/net/adding-annotations-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-annotations-to-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 기존 PDF 파일에 자유 텍스트 주석 추가 (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)를 사용하면 기존 PDF 파일에 다양한 유형의 주석을 추가할 수 있습니다. 특정 주석을 추가하기 위해 해당 메서드를 사용할 수 있습니다. 예를 들어, 다음 코드 스니펫에서는 [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메서드를 사용하여 [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 유형의 주석을 추가했습니다.

모든 유형의 주석은 동일한 방식으로 PDF 파일에 추가할 수 있습니다. 먼저, [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 유형의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 둘째, 주석 영역을 지정하기 위해 Rectangle 객체를 생성해야 합니다.

그 후, [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메서드를 호출하여 [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 주석을 추가하고, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 자유 텍스트 주석을 추가하는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Add annotation
        editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number

        // Save PDF document
        editor.Save(dataDir + "AddFreeTextAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    // Add annotation
    editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number

    // Save PDF document
    editor.Save(dataDir + "AddFreeTextAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 기존 PDF 파일에 텍스트 주석 추가 (facades)

이 예제에서도 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 유형의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 둘째, 주석 영역을 지정하기 위해 Rectangle 객체를 생성해야 합니다. 그 후, [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메서드를 호출하여 FreeText 주석을 추가하고, 주석의 제목과 주석이 위치한 페이지 번호를 생성할 수 있습니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Add annotation
        editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);

        // Save PDF document
        editor.Save(dataDir + "AddTextAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    // Add annotation
    editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);

    // Save PDF document
    editor.Save(dataDir + "AddTextAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 기존 PDF 파일에 선 주석 추가 (facades)

우리는 또한 Rectangle, 선의 시작 및 끝 좌표, 페이지 번호, 두께, 스타일 및 주석 프레임의 색상, 선 대시 유형, 선의 시작 및 끝 유형을 지정합니다.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Create Line Annotation
        editor.CreateLine(
            new System.Drawing.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 2,
            System.Drawing.Color.Red,
            "dash",
            new int[] { 1, 0, 3 },
            new[] { "Open", "Open" });

        // Save PDF document
        editor.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    // Create Line Annotation
    editor.CreateLine(
        new System.Drawing.Rectangle(550, 93, 562, 439),
        "Test",
        556, 99, 556, 443, 1, 2,
        System.Drawing.Color.Red,
        "dash",
        new int[] { 1, 0, 3 },
        new[] { "Open", "Open" });

    // Save PDF document
    editor.Save(dataDir + "AddLineAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}