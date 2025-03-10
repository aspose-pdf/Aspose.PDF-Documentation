---
title: PDF 문서를 프로그래밍 방식으로 저장하기
linktitle: PDF 저장
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/save-pdf-document/
description: C# Aspose.PDF for .NET PDF 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 배웁니다. PDF 문서를 파일 시스템, 스트림 및 웹 애플리케이션에 저장합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "개발자들이 Aspose.PDF for .NET을 사용하여 PDF 문서를 프로그래밍 방식으로 쉽게 저장하는 방법을 알아보세요. 이 기능은 파일 시스템, 스트림 및 웹 애플리케이션 내에서 PDF를 저장하는 것을 지원하여 다양한 사용 사례를 수용하며, 장기 보관 및 그래픽 교환을 위한 PDF/A 및 PDF/X 표준 준수를 보장합니다. 이 강력한 저장 메커니즘으로 PDF 처리 능력을 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

다음 코드 스니펫은 [Aspose.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 문서를 파일 시스템에 저장하기

`Document` 클래스의 `Save` 메서드를 사용하여 생성되거나 조작된 PDF 문서를 파일 시스템에 저장할 수 있습니다.
형식 유형(옵션)을 제공하지 않으면 문서는 Aspose.PDF v.1.7 (*.pdf) 형식으로 저장됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## PDF 문서를 스트림에 저장하기

`Save` 메서드의 오버로드를 사용하여 생성되거나 조작된 PDF 문서를 스트림에 저장할 수도 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

자세한 설명은 [Showcase](/pdf/ko/net/showcases/) 섹션을 참조하세요.

## PDF/A 또는 PDF/X 형식 저장하기

PDF/A는 전자 문서의 보관 및 장기 보존을 위해 사용되는 휴대용 문서 형식(PDF)의 ISO 표준화된 버전입니다.
PDF/A는 장기 보관에 적합하지 않은 기능(예: 글꼴 링크(글꼴 포함과 반대) 및 암호화)을 금지한다는 점에서 PDF와 다릅니다. PDF/A 뷰어에 대한 ISO 요구 사항에는 색상 관리 지침, 포함된 글꼴 지원 및 포함된 주석을 읽기 위한 사용자 인터페이스가 포함됩니다.

PDF/X는 PDF ISO 표준의 하위 집합입니다. PDF/X의 목적은 그래픽 교환을 용이하게 하는 것이며, 따라서 표준 PDF 파일에는 적용되지 않는 일련의 인쇄 관련 요구 사항이 있습니다.

두 경우 모두 `Save` 메서드를 사용하여 문서를 저장하며, 문서는 `Convert` 메서드를 사용하여 준비해야 합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```