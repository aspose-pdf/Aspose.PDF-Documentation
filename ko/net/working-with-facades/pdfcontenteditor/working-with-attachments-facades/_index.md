---
title: 첨부파일 작업 - 파사드
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/working-with-attachments-facades/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 첨부파일 작업 - 파사드에 대해 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "Aspose.PDF for .NET의 첨부파일 작업 - 파사드 기능은 사용자가 PDF 문서 내에서 파일 첨부파일을 쉽게 관리할 수 있도록 합니다. PdfContentEditor 클래스를 사용하여 다양한 파일 유형을 프로그래밍 방식으로 추가, 검색 및 제거하는 기능을 통해 이 기능은 첨부파일을 원활하게 통합하여 PDF 상호작용을 향상시키는 프로세스를 간소화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "589",
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
    "url": "/net/working-with-attachments-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-attachments-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

이 섹션에서는 Aspose.PDF for .NET 파사드를 사용하여 PDF에서 첨부파일 작업을 수행하는 방법을 설명합니다. 첨부파일은 부모 문서에 첨부된 추가 파일로, pdf, word, 이미지 또는 기타 파일과 같은 다양한 파일 유형일 수 있습니다. PDF에 첨부파일을 추가하고, 첨부파일의 정보를 가져오고, 파일로 저장하고, C#을 사용하여 PDF에서 첨부파일을 프로그래밍 방식으로 삭제하는 방법을 배우게 됩니다.

## 기존 PDF에서 파일로 첨부파일 추가

[PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스를 사용하여 기존 PDF 파일에 첨부파일을 추가할 수 있습니다. 첨부파일은 디스크의 파일 경로를 사용하여 추가할 수 있습니다. [AddDocumentAttachment](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 메서드를 사용하여 첨부파일을 추가할 수 있습니다. 이 메서드는 두 개의 인수를 사용합니다: 파일 경로와 첨부파일 설명. 먼저 기존 PDF 파일을 열고 그 안에 첨부파일을 추가해야 합니다. 그런 다음 [PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor)의 [Save](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 출력 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 파일에서 첨부파일을 추가하는 방법을 보여줍니다. 예를 들어, MP3 파일을 추가해 보겠습니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor =  new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));
    editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 기존 PDF에서 스트림으로 첨부파일 추가

첨부파일은 [AddDocumentAttachment](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 메서드를 사용하여 스트림 - FileStream에서 PDF 파일에 추가할 수 있습니다. 이 메서드는 세 개의 인수를 사용합니다: 스트림, 첨부파일 이름 및 첨부파일 설명. 첨부파일을 추가하려면 [PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [AddDocumentAttachment](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 메서드를 호출하여 첨부파일을 추가할 수 있습니다. 마지막으로, 업데이트된 PDF 파일을 저장하기 위해 Save 메서드를 호출할 수 있습니다. 다음 코드 스니펫은 스트림에서 첨부파일을 추가하는 방법을 보여줍니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
        editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));

    var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
    editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 기존 PDF 파일에서 모든 첨부파일 삭제

[PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [DeleteAttachments](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 메서드를 사용하면 기존 PDF 파일에서 모든 첨부파일을 삭제할 수 있습니다. [DeleteAttachments](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 메서드를 호출합니다. 마지막으로, 업데이트된 PDF 파일을 저장하기 위해 [Save](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save/index) 메서드를 호출해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 모든 첨부파일을 삭제하는 방법을 보여줍니다.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf")))
    {
        editor.DeleteAttachments();

        // Save PDF document
        editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"));
    editor.DeleteAttachments();

    // Save PDF document
    editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}