---
title: 내부 및 외부 필드 복사
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/copy-inner-and-outer-field/
description: 이 섹션에서는 FormEditor 클래스를 사용하여 Aspose.PDF Facades로 내부 및 외부 필드를 복사하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "Aspose.PDF for .NET의 내부 및 외부 필드 복사 기능은 사용자가 동일한 PDF 내에서 필드를 복제하거나 외부 PDF 파일에서 필드를 전송할 수 있도록 하여 양식 편집을 향상시킵니다. FormEditor 클래스에서 제공하는 사용하기 쉬운 CopyInnerField 및 CopyOuterField 메서드를 통해 사용자는 양식 필드를 효율적으로 관리하여 일관성을 보장하고 문서 준비 시간을 절약할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[CopyInnerField](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) 메서드는 동일한 파일에서 동일한 좌표에 있는 필드를 복사할 수 있도록 합니다. 이 메서드는 복사할 필드 이름, 새 필드 이름 및 필드를 복사해야 하는 페이지 번호가 필요합니다. [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스에서 이 메서드를 제공합니다. 다음 코드 스니펫은 동일한 파일에서 동일한 위치에 필드를 복사하는 방법을 보여줍니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## 기존 PDF 파일에서 외부 필드 복사

[CopyOuterField](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) 메서드는 외부 PDF 파일에서 양식 필드를 복사한 다음 입력 PDF 파일의 동일한 위치와 지정된 페이지 번호에 추가할 수 있도록 합니다. 이 메서드는 필드를 복사해야 하는 PDF 파일, 필드 이름 및 필드를 복사해야 하는 페이지 번호가 필요합니다. 이 메서드는 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스에서 제공됩니다. 다음 코드 스니펫은 외부 PDF 파일에서 필드를 복사하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```