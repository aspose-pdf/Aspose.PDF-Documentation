---
title: 기존 PDF에서 페이지 나누기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/page-break-in-existing-pdf/
description: Aspose.PDF를 사용하여 .NET에서 기존 PDF 파일에 페이지 나누기를 삽입하는 방법을 알아보세요.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Page Break in existing PDF",
    "alternativeHeadline": "Insert Custom Page Breaks in PDF Files",
    "abstract": "PdfFileEditor 클래스에서 페이지 나누기 기능을 소개하여 사용자가 기존 PDF 문서의 레이아웃을 정밀하게 제어할 수 있도록 합니다. 이 기능은 문서 내 특정 위치에 페이지 나누기를 삽입할 수 있게 하여 사용자 정의를 향상시키고 콘텐츠의 전반적인 프레젠테이션을 개선합니다. 간단한 메서드 호출로 사용자는 특정 형식 요구 사항을 충족하도록 PDF를 쉽게 수정할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "369",
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
    "url": "/net/page-break-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-break-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

기본 레이아웃으로 PDF 파일 내의 내용은 왼쪽 상단에서 오른쪽 하단으로 추가됩니다. 내용이 페이지 하단 여백을 초과하면 페이지 나누기가 발생합니다. 그러나 요구 사항에 따라 페이지 나누기를 삽입해야 할 필요가 있을 수 있습니다. 이 요구 사항을 충족하기 위해 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스에 AddPageBreak(...) 메서드가 추가되었습니다.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1).
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2).
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/addpagebreak).

- src는 소스 문서/문서에 대한 경로/소스 문서가 있는 스트림입니다.
- dest는 문서가 저장될 목적지 문서/문서가 저장될 경로/스트림입니다.
- PageBreak는 페이지 나누기 객체의 배열입니다. 페이지 나누기를 배치해야 하는 페이지의 인덱스와 페이지에서 페이지 나누기의 수직 위치라는 두 가지 속성이 있습니다.

## 예제 1 (페이지 나누기 추가)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageBreak.pdf"))
    {
        // Create PDF document
        using (var dest = new Aspose.Pdf.Document())
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
            fileEditor.AddPageBreak(document, dest, new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
            {
                new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
            });
            // Save PDF document
            dest.Save(dataDir + "PageBreak_out.pdf");
        }
    }
}
```

## 예제 2

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Create PdfFileEditor object
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    fileEditor.AddPageBreak(dataDir + "PageBreak.pdf",
        dataDir + "PageBreakWithDestPath_out.pdf",
        new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
        {
            new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
        });
}
```

## 예제 3

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    using (var src = new FileStream(dataDir + "PageBreak.pdf", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

            // Add page break
            fileEditor.AddPageBreak(src, dest,
                new[]
                {
                    new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
                });
        }
    }
}
```