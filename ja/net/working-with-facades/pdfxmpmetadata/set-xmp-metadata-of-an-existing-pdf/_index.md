---
title: 既存のPDFのXMPメタデータを設定する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/set-xmp-metadata-of-an-existing-pdf/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFのXMPメタデータを設定する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set XMP Metadata of an existing PDF",
    "alternativeHeadline": "Set XMP Metadata for Existing PDF Files",
    "abstract": "Aspose.PDF for .NET Facadesを使用して既存のPDFファイルのXMPメタデータを設定する強力な機能を紹介します。この機能により、ユーザーはPDFドキュメントを簡単にバインドし、重要なメタデータプロパティをカスタマイズでき、ドキュメント管理と情報検索機能が向上します。メタデータの追加、変更、保存のための簡単なメソッドを使用することで、ユーザーはPDFファイルをより良い整理とコンプライアンスのために最適化できます。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

PDFファイルにXMPメタデータを設定するには、[PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用してPDFファイルをバインドする必要があります。[PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata)クラスの[Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index)メソッドを使用して、さまざまなプロパティを追加できます。最後に、[PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata)クラスの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドを呼び出します。以下のコードスニペットは、PDFファイルにXMPメタデータを追加する方法を示しています。

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
        // Step #1: register namespace prefix and URI
        xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");

        // Step #2: add user property with the prefix
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
    // Step #1: register namespace prefix and URI
    xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");

    // Step #2: add user property with the prefix
    xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

    // Change user defined property
    xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

    // Save PDF document
    xmpMetaData.Save(dataDir + "SetXMPMetadata_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}