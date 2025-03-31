---
title: 페이지 회전 작업
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/working-with-page-rotation/
description: 이 섹션에서는 PdfPageEditor 클래스를 사용하여 페이지 회전 작업을 수행하는 방법을 설명합니다.
lastmod: "2021-07-07"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Page Rotation",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with PdfPageEditor",
    "abstract": "PdfPageEditor 클래스의 강력한 페이지 회전 기능을 발견하여 사용자 정의 가능한 회전 각도를 통해 문서 페이지를 정밀하게 조작할 수 있습니다. 개별 페이지 회전을 지정하거나 선택한 페이지에 균일한 회전을 적용하는 옵션을 통해 이 기능은 PDF 편집 기능을 향상시켜 사용자에게 더 큰 유연성과 제어를 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "202",
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
    "url": "/net/working-with-page-rotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-page-rotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

[PdfPageEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor) 클래스는 페이지를 회전할 수 있는 기능을 제공합니다.

{{% /alert %}}

## PageRotations를 사용하여 페이지 회전

문서에서 페이지를 회전하려면 [PageRotations](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations)를 사용할 수 있습니다.
`PageRotations`는 페이지 번호와 회전 각도를 포함하며, 키는 페이지 번호를 나타내고, 키의 값은 각도에서의 회전을 나타냅니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void RotatePages1()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "sample.pdf");

         // Specify the page rotation dictionary
         editor.PageRotations = new System.Collections.Generic.Dictionary<int, int>
         {
             { 1, 90 },
             { 2, 180 },
             { 3, 270 }
         };

         // Save PDF document
         editor.Save(dataDir + "sample-rotate-a.pdf");
     }
 }
```

## Rotation을 사용하여 페이지 회전

[Rotation](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfpageeditor/properties/rotation) 속성도 사용할 수 있습니다. 회전은 0, 90, 180 또는 270이어야 합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotatePages2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Specify the pages to rotate and the rotation angle
        editor.ProcessPages = new int[] { 1, 3 };
        editor.Rotation = 90;

        // Save PDF document
        editor.Save(dataDir + "sample-rotate-a.pdf");
    }
}
```