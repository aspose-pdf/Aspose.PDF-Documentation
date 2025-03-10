---
title: PDF 파일에 북마크 추가하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/how-to-create-nested-bookmarks/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 중첩 북마크를 만드는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Bookmarks to PDF file",
    "alternativeHeadline": "Create Nested Bookmarks in PDF Documents Easily",
    "abstract": "Aspose.Pdf.Facades의 PdfContentEditor 클래스를 사용하여 새로운 중첩 북마크 기능으로 PDF 문서를 향상시키세요. 이 기능은 콘텐츠를 효과적으로 구성하는 계층적 북마크를 생성할 수 있게 하여 사용자가 PDF 내의 장과 관련 페이지를 쉽게 탐색할 수 있도록 합니다. 이 정교한 북마크 솔루션으로 문서 탐색을 간소화하고 사용자 경험을 향상시키세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "211",
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
    "url": "/net/how-to-create-nested-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-create-nested-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

북마크는 PDF 문서 내의 특정 페이지를 추적/링크할 수 있는 옵션을 제공합니다. [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) 클래스는 [Aspose.Pdf.Facades 네임스페이스](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)에서 기존 PDF 파일 내의 특정 페이지 또는 모든 페이지에 자신만의 북마크를 정교하면서도 직관적인 방식으로 생성할 수 있는 기능을 제공합니다.

## 구현 세부사항

단순 북마크 생성 외에도, 때때로 장의 형태로 북마크를 생성해야 할 필요가 있습니다. 여기서 개별 북마크를 장 북마크 안에 중첩시켜 + 기호를 클릭하면 북마크가 확장될 때 내부 페이지를 볼 수 있도록 합니다. 아래 그림과 같이요.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}