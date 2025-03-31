---
title: PDF 파일의 XMP 메타데이터 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/get-xmp-metadata-of-an-existing-pdf-file/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 기존 PDF의 XMP 메타데이터를 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get XMP Metadata of PDF File",
    "alternativeHeadline": "Extract XMP Metadata from PDF Files Easily",
    "abstract": "새로운 XMP 메타데이터 기능을 통해 PDF 파일에서 자세한 통찰력을 얻으세요. 이 기능은 특정 XMP 메타데이터 속성을 손쉽게 추출할 수 있게 하여 문서의 관리 및 분류를 개선합니다. 워크플로를 간소화하고 정확한 메타데이터 추출로 PDF의 유용성을 향상시키세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "213",
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
    "url": "/net/get-xmp-metadata-of-an-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-xmp-metadata-of-an-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

PDF 파일에서 XMP 메타데이터를 가져오려면 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 특정 XMP 메타데이터 속성을 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 객체에 전달하여 해당 값을 가져올 수 있습니다. 다음 코드 스니펫은 PDF 파일에서 XMP 메타데이터를 가져오는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using (var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata())
    {
        // Bind PDF document
        xmpMetaData.BindPdf(dataDir + "GetXMPMetadata.pdf");

        // Get XMP Meta Data properties
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate].ToString());
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate].ToString());
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool].ToString());
        Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

        Console.ReadLine();
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Bind PDF document
    xmpMetaData.BindPdf(dataDir + "GetXMPMetadata.pdf");

    // Get XMP Meta Data properties
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate].ToString());
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate].ToString());
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool].ToString());
    Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

    Console.ReadLine();
}
```
{{< /tab >}}
{{< /tabs >}}