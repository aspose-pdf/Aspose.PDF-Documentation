---
title: PDF 파일에서 첨부 파일 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/extract-attachments/
description: Aspose.PDF를 사용하여 .NET에서 PDF 문서의 첨부 파일을 추출하고 관리하는 방법을 알아보세요.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "Aspose.PDF for .NET의 새로운 첨부 파일 추출 기능은 개발자가 PDF 문서 내에서 파일 첨부 파일을 쉽게 검색하고 관리할 수 있도록 합니다. PdfExtractor 클래스를 활용하여 사용자는 첨부 파일을 추출하고 첨부 파일 이름 및 세부 정보와 같은 필수 정보를 얻어 문서 처리 기능을 향상시킬 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 추출 기능 중 하나는 첨부 파일 추출입니다. 이 카테고리는 첨부 파일을 추출하는 데 도움이 되는 메서드 집합을 제공할 뿐만 아니라 첨부 파일 관련 정보를 제공하는 메서드도 제공합니다. 즉, [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) 및 [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) 메서드는 각각 첨부 파일 정보와 첨부 파일 이름을 제공합니다. 첨부 파일을 추출하고 가져오기 위해 [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) 및 [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment) 메서드를 사용합니다.

다음 코드 스니펫은 PdfExtractor 메서드를 사용하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Create the extractor
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "GetAlltheAttachments.pdf");

        // Extract attachments
        pdfExtractor.ExtractAttachment();

        // Get attachment names
        if (pdfExtractor.GetAttachNames().Count > 0)
        {
            Console.WriteLine("Extracting and storing...");

            // Get extracted attachments
            pdfExtractor.GetAttachment(dataDir + "GetAlltheAttachments_out.pdf");
        }
    }
}
```