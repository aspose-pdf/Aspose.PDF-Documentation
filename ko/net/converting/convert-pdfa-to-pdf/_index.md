---
title: PDF/A를 PDF 형식으로 변환
linktitle: PDF/A를 PDF 형식으로 변환
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ko/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: 이 주제는 Aspose.PDF가 .NET 라이브러리를 사용하여 PDF/A 파일을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF/A to PDF format",
    "alternativeHeadline": "Remove PDF/A Compliance for Enhanced Document Flexibility in C#",
    "abstract": "Aspose.PDF는 이제 .NET 라이브러리를 사용하여 PDF/A 파일을 표준 PDF 문서로 원활하게 변환하는 기능을 제공합니다. 이 기능은 사용자가 PDF/A 준수 제한을 제거할 수 있게 하여 PDF/A 표준에 의해 부과된 제한 없이 PDF 콘텐츠를 더 쉽게 편집하고 수정할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/convert-pdfa-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdfa-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF/A 문서를 PDF로 변환

PDF/A 문서를 PDF로 변환하는 것은 원본 문서에서 <abbr title="Portable Document Format Archive">PDF/A</abbr> 제한을 제거하는 것을 의미합니다. 클래스 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document)에는 입력/소스 파일에서 PDF 준수 정보를 제거하는 [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/removepdfacompliance) 메서드가 있습니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // Remove PDF/A compliance information
        document.RemovePdfaCompliance();
    
        // Save PDF document
        document.Save(dataDir + "PDFAToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf");

    // Remove PDF/A compliance information
    document.RemovePdfaCompliance();
    
    // Save PDF document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

문서에 변경 사항을 추가하면 PDF/A 준수도 제거될 수 있습니다(예: 페이지 추가). 다음 예제에서는 새 페이지가 추가된 후 출력 문서가 PDF/A 준수를 잃습니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // Adding a new (empty) page removes PDF/A compliance information.
        document.Pages.Add();

        // Save PDF document
        document.Save(dataDir + "PDFAToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf");

    // Adding a new (empty) page removes PDF/A compliance information.
    document.Pages.Add();

    // Save PDF document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}