---
title: 페이지 속성 조작
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/manipulate-page-properties/
description: 이 섹션에서는 PdfPageEditor 클래스를 사용하여 Aspose.PDF Facades로 페이지 속성을 조작하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "PdfPageEditor 클래스를 소개합니다. 이는 PDF 페이지 속성을 관리하기 위한 강력한 도구입니다. 이 기능은 개발자가 회전, 확대/축소 수준 및 페이지 치수와 같은 필수 페이지 속성을 검색하고 수정할 수 있게 하여 PDF 콘텐츠 프레젠테이션에 대한 세밀한 제어를 제공합니다. 속성을 가져오고 설정하는 간단한 방법을 통해 특정 페이지 콘텐츠의 크기를 조정할 수 있는 기능을 포함하여 PDF 문서를 향상시키는 것이 그 어느 때보다 쉬워졌습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 기존 PDF 파일에서 PDF 페이지 속성 가져오기

[PdfPageEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor)는 PDF 파일의 개별 페이지와 작업할 수 있게 해줍니다. 이를 통해 다양한 페이지 박스 크기, 페이지 회전, 페이지 확대/축소 등과 같은 개별 페이지의 속성을 가져올 수 있습니다. 이러한 속성을 가져오기 위해서는 [PdfPageEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [GetPageRotation](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) 등과 같은 다양한 메서드를 사용하여 페이지 속성을 가져올 수 있습니다.

다음 코드 스니펫은 기존 PDF 파일에서 PDF 페이지 속성을 가져오는 방법을 보여줍니다.


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## 기존 PDF 파일에서 PDF 페이지 속성 설정하기

페이지 회전, 확대/축소 또는 원점과 같은 페이지 속성을 설정하려면 [PdfPageEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor) 클래스를 사용해야 합니다. 이 클래스는 이러한 페이지 속성을 설정하기 위한 다양한 메서드와 속성을 제공합니다. 우선, [PdfPageEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, 이러한 메서드와 속성을 사용하여 페이지 속성을 설정할 수 있습니다. 마지막으로, [Save](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에서 PDF 페이지 속성을 설정하는 방법을 보여줍니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## PDF 파일의 특정 페이지 콘텐츠 크기 조정

[PdfPageEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor) 클래스의 ResizeContents 메서드는 PDF 파일의 페이지 콘텐츠 크기를 조정할 수 있게 해줍니다. [ContentsResizeParameters](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) 클래스는 페이지를 크기 조정하는 데 사용할 매개변수를 지정하는 데 사용됩니다. 예를 들어, 비율 또는 단위로 여백을 설정할 수 있습니다. 모든 페이지의 크기를 조정하거나 ResizeContents 메서드를 사용하여 크기를 조정할 페이지 배열을 지정할 수 있습니다.

다음 코드 스니펫은 PDF 파일의 특정 페이지 콘텐츠 크기를 조정하는 방법을 보여줍니다.



```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```