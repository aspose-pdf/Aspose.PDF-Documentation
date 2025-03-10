---
title: PDFをPDF/X交換形式に変換
linktitle: PDFをPDF/X交換形式に変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ja/net/convert-pdf-to-pdfx/
lastmod: "2025-01-16"
description: Aspose.PDF for .NETを使用して、グラフィックス交換および印刷目的のためにPDFファイルをPDF/X形式に変換する方法を学びます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PDF/X exchange format",
    "alternativeHeadline": "Effortless PDF to PDF/X Conversion in C#",
    "abstract": "Aspose.PDF for .NETのPDF/Xサポートにより、標準PDFファイルをさまざまなPDF/X準拠形式に簡単に変換できます。この機能は、包括的な検証を通じてPDF/X標準への準拠を保証するだけでなく、カスタムICCプロファイルを使用して、すべての環境で適切なグラフィックス交換を確保することも可能にします。効率的で信頼性の高いPDF/X変換のためのAspose.PDFの強力な機能を探求してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1064",
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
    "url": "/net/convert-pdf-to-pdfx/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-pdfx/"
    },
    "dateModified": "2025-01-16",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーや開発者向けの情報を確認してください。"
}
</script>

**Aspose.PDF for .NET**は、PDFファイルを<abbr title="Portable Document Format eXchange">PDF/X</abbr>準拠のPDFファイルに変換することを可能にします。この文書では、その方法を説明します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## サポートされている標準
**Aspose.PDF for .NET**は、以下の標準をサポートしています: PDF/X-1a:2001、PDF/X-1a:2003、PDF/X-3:2003、PDF/X-4。

## 外部ICCプロファイルを使用してPDFファイルをPDF/X-4に変換

以下のコードスニペットは、PDFファイルをPDF/X-4準拠のPDFに変換し、適切な色再現を確保するために外部ICCプロファイルを提供する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfX()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFX.pdf"))
    {
        // Set up the desired PDF/X format with PdfFormatConversionOptions
        Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Provide the name of the external ICC profile file (optional)
        options.IccProfileFileName = dataDir + "ISOcoated_v2_eci.icc";

        // Provide an output condition identifier and other necessary OutputIntent properties (optional)
        options.OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39");

        // Convert to PDF/X compliant document
        document.Convert(options);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFX4_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFX.pdf");

    // Set up the desired PDF/X format with PdfFormatConversionOptions
    Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_4, Aspose.Pdf.ConvertErrorAction.Delete);

    // Provide the name of the external ICC profile file (optional)
    options.IccProfileFileName = dataDir + "ISOcoated_v2_eci.icc";

    // Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39");

    // Convert to PDF/X compliant document
    document.Convert(options);
    
    // Save PDF document
    document.Save(dataDir + "PDFToPDFX4_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}