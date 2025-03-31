---
title: 확장 가능한 메타데이터 플랫폼 - XMP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/working-with-extensible-metadata-platform-xmp/
description: 이 섹션에서는 PdfXmpMetadata 클래스를 사용하여 확장 가능한 메타데이터 플랫폼 - XMP와 작업하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extensible Metadata Platform - XMP",
    "alternativeHeadline": "Enhanced PDF Metadata Management with XMP Integration",
    "abstract": "확장 가능한 메타데이터 플랫폼(XMP) 기능은 사용자가 PDF 파일 내에서 표준화된 메타데이터와 독점 메타데이터를 효율적으로 삽입하고 조작할 수 있도록 합니다. PdfXmpMetadata 클래스를 활용하여 이 기능은 변경 사항을 추적하고 PDF 문서의 의미론적 기능을 향상시키는 과정을 단순화하여 고급 메타데이터 관리 통합을 원하는 개발자에게 유용한 도구가 됩니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "412",
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
    "url": "/net/working-with-extensible-metadata-platform-xmp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-extensible-metadata-platform-xmp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

확장 가능한 메타데이터 플랫폼(XMP)은 Adobe Systems Inc.에서 만든 표준입니다. 이 표준은 표준화된 메타데이터와 독점 메타데이터를 처리하고 저장하기 위해 개발되었습니다. 이 메타데이터는 다양한 파일 형식에 삽입될 수 있지만, 이 기사에서는 PDF 파일 형식에만 집중하겠습니다. Aspose.Pdf.Facades 네임스페이스를 사용하여 PDF 파일에 메타데이터를 삽입하는 방법을 살펴보겠습니다. PDF 문서에서 XMP를 조작하기 위해 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 클래스를 사용할 것입니다.

{{% /alert %}}

## 배경

PDF 파일은 생애 주기 동안 여러 단계를 거칩니다. 우리는 PDF 문서를 만들고, 그 후 다른 사람이나 부서에 전달하여 추가 처리를 진행합니다. 그러나 이 과정에서 우리는 변경 사항의 다양한 측면을 추적해야 합니다. XMP는 파일 내 데이터에 대한 변경 사항이나 기타 정보를 추적하는 역할을 합니다.

## 설명

Aspose.Pdf.Facades를 사용하여 XMP를 조작하기 위해 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 클래스를 사용할 것입니다. 이 클래스를 사용하여 미리 정의된 메타데이터 속성을 조작합니다. [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 클래스는 이러한 속성을 PDF 파일에 추가합니다. 또한 메타데이터를 추가하는 PDF 파일을 열고 저장하는 데 도움을 줍니다. 따라서 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 클래스를 사용하면 PDF 파일에서 XMP를 쉽게 조작할 수 있습니다.
다음 코드 스니펫은 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 클래스를 사용하여 XMP와 작업하는 방법을 이해하는 데 도움이 될 것입니다:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using (var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open))
    {
        using (var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create))
        {
            // Bind PDF document
            xmpMetaData.BindPdf(input);

            // Add base URL property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

            // Add creation date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

            // Add Metadata Date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

            // Add Creator Tool property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

            // Add Modify Date to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

            // Add Nick Name to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

            // Save PDF document
            xmpMetaData.Save(output);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open);

    using var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create);

    // Bind PDF document
    xmpMetaData.BindPdf(input);

    // Add base URL property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

    // Add creation date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Add Metadata Date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

    // Add Creator Tool property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

    // Add Modify Date to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

    // Add Nick Name to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

    // Save PDF document
    xmpMetaData.Save(output);
}
```
{{< /tab >}}
{{< /tabs >}}

## 결론

{{% alert color="primary" %}}
이 기사에서는 Aspose.Pdf.Facades를 사용하여 XMP와 작업하는 방법을 살펴보았습니다. 이 기사에서 사용된 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 클래스는 사용자가 PDF 문서에서 메타데이터를 조작하는 것을 매우 쉽게 만들어 줍니다. [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 클래스를 제대로 사용하면 PDF 파일에 지능을 통합하는 것이 매우 쉬워지며, 의미론적 웹을 실현하는 데 한 걸음 더 다가갈 수 있습니다.
{{% /alert %}}