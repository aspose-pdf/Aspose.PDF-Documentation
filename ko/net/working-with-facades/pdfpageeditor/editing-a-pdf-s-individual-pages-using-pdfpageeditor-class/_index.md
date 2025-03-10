---
title: PDF의 개별 페이지 편집
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: 이 섹션에서는 PdfPageEditor 클래스를 사용하여 PDF의 개별 페이지를 편집하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Editing PDF individual pages",
    "alternativeHeadline": "Edit Individual Pages of PDF Easily with PdfPageEditor",
    "abstract": "PdfPageEditor 클래스는 사용자가 회전, 정렬 및 전환 효과와 같은 기능을 통해 PDF 파일의 개별 페이지를 효율적으로 조작할 수 있는 기능을 제공합니다. 이 전문 도구는 페이지 표시 및 형식에 대한 제어를 향상시켜 PDF 콘텐츠의 맞춤형 프레젠테이션을 가능하게 합니다. 각 페이지가 어떻게 표시되고 상호작용되는지를 최적화하기 위한 원활한 편집 기능을 경험해 보세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "593",
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
    "url": "/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

Aspose.Pdf.Facades 네임스페이스는 [Aspose.PDF for .NET](/pdf/net/)에서 PDF 파일의 개별 페이지를 조작할 수 있게 해줍니다. 이 기능은 페이지 표시, 정렬 및 전환 등을 작업하는 데 도움이 됩니다. PdfPageEditor 클래스는 이 기능을 달성하는 데 도움을 줍니다. 이 기사에서는 이 클래스에서 제공하는 속성과 메서드 및 이러한 메서드의 작동 방식에 대해 살펴보겠습니다.

{{% /alert %}}

## 설명

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 및 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스와 다릅니다. 먼저 차이점을 이해해야 하며, 그러면 PdfPageEditor 클래스를 더 잘 이해할 수 있습니다. PdfFileEditor 클래스는 페이지 추가, 삭제 또는 연결과 같은 파일의 모든 페이지를 조작할 수 있게 해주며, PdfContentEditor 클래스는 페이지의 내용, 즉 텍스트 및 기타 객체를 조작하는 데 도움을 줍니다. 반면, PdfPageEditor 클래스는 개별 페이지 자체와만 작업하며 회전, 확대 및 정렬 등을 수행합니다.

이 클래스에서 제공하는 기능은 크게 세 가지 범주로 나눌 수 있습니다: 전환, 정렬 및 표시. 아래에서 이러한 범주에 대해 논의하겠습니다.

### 전환

이 클래스에는 전환과 관련된 두 가지 속성인 [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) 및 [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration)가 포함되어 있습니다. TransitionType은 프레젠테이션 중 다른 페이지에서 이 페이지로 이동할 때 사용할 전환 스타일을 지정합니다. TransitionDuration은 페이지의 표시 지속 시간을 지정합니다.

### 정렬

PdfPageEditor 클래스는 수평 및 수직 정렬을 모두 지원합니다. 이를 위해 두 가지 속성인 [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) 및 [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment)를 제공합니다. Alignment 속성은 내용을 수평으로 정렬하는 데 사용됩니다. Alignment 속성은 Center, Left 및 Right의 세 가지 옵션을 포함하는 AlignmentType 값을 취합니다. VerticalAlignment 속성은 Bottom, Center 및 Top의 세 가지 옵션을 포함하는 VerticalAlignmentType 값을 취합니다.

### 표시

표시 범주에는 PageSize, Rotation, Zoom 및 DisplayDuration과 같은 속성을 포함할 수 있습니다. PageSize 속성은 파일 내 개별 페이지의 크기를 지정합니다. 이 속성은 A0, A1, A2, A3, A4, A5, A6, B5, Letter, Ledger 및 P11x17과 같은 미리 정의된 페이지 크기를 캡슐화하는 PageSize 객체를 입력으로 받습니다. Rotation 속성은 개별 페이지의 회전을 설정하는 데 사용됩니다. 이 속성은 0, 90, 180 또는 270의 값을 취할 수 있습니다. Zoom 속성은 페이지의 확대 계수를 설정하며, float 값을 입력으로 받습니다. 이 클래스는 또한 파일 내 개별 페이지의 페이지 크기 및 페이지 회전을 가져오는 메서드를 제공합니다.

위에서 언급한 메서드의 샘플은 아래의 코드 스니펫에서 확인할 수 있습니다:



```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EditPdfPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create a new instance of PdfPageEditor class
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Specify an array of pages which need to be manipulated (pages can be multiple, here we have specified only one page)
        pdfPageEditor.ProcessPages = new int[] { 1 };

        // Alignment related code
        pdfPageEditor.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;

        // Specify transition type for the pages
        pdfPageEditor.TransitionType = 2;
        // Specify transition duration
        pdfPageEditor.TransitionDuration = 5;

        // Display related code

        // Select a page size from the enumeration and assign to property
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLedger;

        // Assign page rotation
        pdfPageEditor.Rotation = 90;

        // Specify zoom factor for the page
        pdfPageEditor.Zoom = 100;

        // Assign display duration for the page
        pdfPageEditor.DisplayDuration = 5;

        // Fetching methods

        // Methods provided by the class, page rotation specified already
        var rotation = pdfPageEditor.GetPageRotation(1);

        // Already specified page can be fetched
        var pageSize = pdfPageEditor.GetPageSize(1);

        // This method gets the page count
        var totalPages = pdfPageEditor.GetPages();

        // This method changes the origin from (0,0) to specified number
        pdfPageEditor.MovePosition(100, 100);

        // Save PDF document
        pdfPageEditor.Save(dataDir + "EditPdfPages_out.pdf");
    }
}
```

## 결론

{{% alert color="primary" %}}
이 기사에서는 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스에 대해 자세히 살펴보았습니다. 이 클래스에서 제공하는 속성과 메서드를 설명했습니다. 개별 페이지를 조작하는 작업을 매우 쉽고 간단하게 만들어 줍니다.
{{% /alert %}}