---
title: 기존 PDF의 XMP 메타데이터 설정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/set-xmp-metadata-of-an-existing-pdf/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 기존 PDF의 XMP 메타데이터를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set XMP Metadata of an existing PDF",
    "alternativeHeadline": "Set XMP Metadata for Existing PDF Files",
    "abstract": "기존 PDF 파일에 대해 XMP 메타데이터를 설정할 수 있는 강력한 기능을 소개합니다. 이 기능은 사용자가 PDF 문서를 쉽게 바인딩하고 필수 메타데이터 속성을 사용자 정의할 수 있도록 하여 문서 관리 및 정보 검색 기능을 향상시킵니다. 메타데이터를 추가, 수정 및 저장하는 간단한 방법을 통해 사용자는 PDF 파일을 더 나은 조직 및 준수를 위해 최적화할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "317",
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
    "url": "/net/set-xmp-metadata-of-an-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-xmp-metadata-of-an-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

PDF 파일에 XMP 메타데이터를 설정하려면 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 클래스의 [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) 메서드를 사용하여 다양한 속성을 추가할 수 있습니다. 마지막으로 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 호출합니다. 다음 코드 스니펫은 PDF 파일에 XMP 메타데이터를 추가하는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using (var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata())
    {
        // Bind PDF document
        xmpMetaData.BindPdf(dataDir + "SetXMPMetadata.pdf");

        // Add create date
        xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

        // Change meta data date
        xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate] = DateTime.Now.ToString();

        // Add creator tool
        xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator tool name");

        // Remove modify date
        xmpMetaData.Remove(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate);

        // Add user defined property
        // Register namespace prefix and URI
        xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");

        // Add user property with the prefix
        xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

        // Change user defined property
        xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

        // Save PDF document
        xmpMetaData.Save(dataDir + "SetXMPMetadata_out.pdf");
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
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Bind PDF document
    xmpMetaData.BindPdf(dataDir + "SetXMPMetadata.pdf");

    // Add create date
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Change meta data date
    xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate] = DateTime.Now.ToString();

    // Add creator tool
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator tool name");

    // Remove modify date
    xmpMetaData.Remove(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate);

    // Add user defined property
    // register namespace prefix and URI
    xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");

    // Add user property with the prefix
    xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

    // Change user defined property
    xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

    // Save PDF document
    xmpMetaData.Save(dataDir + "SetXMPMetadata_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}