---
title: PDFをPDF/A形式に変換する
linktitle: PDFをPDF/A形式に変換する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ja/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Aspose.PDFを使用して、アーカイブ目的のためにPDFファイルをPDF/A形式に変換する方法を学びます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PDF/A formats",
    "alternativeHeadline": "Effortless PDF to PDF/A Conversion with Validation in C#",
    "abstract": "Aspose.PDF for .NETの機能により、標準PDFファイルをPDF/A-1b、PDF/A-2u、PDF/A-3aなどのさまざまなPDF/A準拠形式にシームレスに変換できます。この機能は、包括的な検証を通じてPDF/A基準への準拠を保証するだけでなく、追加ファイルの添付や欠落フォントの置き換えを可能にし、文書の整合性とアクセシビリティを向上させます。効率的で信頼性の高いPDF/A変換のためのAspose.PDFの強力な機能を探求してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1840",
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
    "url": "/net/convert-pdf-to-pdfa/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-pdfa/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

**Aspose.PDF for .NET**は、PDFファイルを<abbr title="Portable Document Format / A">PDF/A</abbr>準拠のPDFファイルに変換することを可能にします。その前に、ファイルを検証する必要があります。このトピックでは、その方法を説明します。

- [PDFをPDF/A-1bに変換](#csharp-convert-pdf-to-a1b)
- [PDFをPDF/A-3bに変換](#csharp-convert-pdf-to-a3b)
- [PDFをPDF/A-4に変換](#csharp-convert-pdf-to-a4)

{{% alert color="primary" %}}

私たちは、PDF/A準拠を検証するためにAdobe PreflightとveraPDFに従っています。市場に出回っているすべてのツールは、PDF/A準拠の「表現」を持っています。参考のためにPDF/A検証ツールに関するこの記事を確認してください。Aspose.PDFがPDFファイルを生成する方法を検証するためにAdobe製品を選択しました。なぜなら、AdobeはPDFに関連するすべての中心にいるからです。

{{% /alert %}}

DocumentクラスのConvertメソッドを使用してファイルを変換します。PDFをPDF/A準拠のファイルに変換する前に、Validateメソッドを使用してPDFを検証します。検証結果はXMLファイルに保存され、その結果もConvertメソッドに渡されます。また、ConvertErrorAction列挙体を使用して、変換できない要素のアクションを指定することもできます。

{{% alert color="success" %}}
**PDFをPDF/Aにオンラインで変換してみる**

Aspose.PDF for .NETは、機能と品質を調査するために試すことができるオンライン無料アプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しています。

[![Aspose.PDF PDFからPDF/Aへの変換を無料アプリで](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## サポートされている標準
私たちは、次の標準をサポートしています：PDF/A-1b、PDF/A-1a、PDF/A-2b、PDF/A-2u、PDF/A-2a、PDF/A-3b、PDF/A-3u、PDF/A-3a、PDF/A-4、PDF/A-4e、PDF/A-4f。

## PDFファイルをPDF/A-1bに変換

<a name="csharp-convert-pdf-to-a1b" id="csharp-convert-pdf-to-a1b"><strong>PDFをPDF/A-1bに変換</strong></a>

次のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        document.Convert(dataDir + "PDFA1bConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_1B, Aspose.Pdf.ConvertErrorAction.Delete);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFA_out.pdf");
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
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Convert to PDF/A compliant document
    // During conversion process, the validation is also performed
    document.Convert(dataDir + "PDFA1bConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_1B, Aspose.Pdf.ConvertErrorAction.Delete);
    
    // Save PDF document
    document.Save(dataDir + "PDFToPDFA_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

検証のみを行うには、次のコード行を使用します：

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidatePdfAStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "ValidationResultA1b.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidatePdfAStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf");

    // Validate PDF for PDF/A-1a
    document.Validate(dataDir + "ValidationResultA1b.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
}
```
{{< /tab >}}
{{< /tabs >}}

## PDFファイルをPDF/A-3bに変換

<a name="csharp-convert-pdf-to-a3b" id="csharp-convert-pdf-to-a3b"><strong>PDFをPDF/A-3bに変換</strong></a>

Aspose.PDF for .NETは、PDFファイルをPDF/A-3b形式に変換する機能もサポートしています。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA3b()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Convert to PDF/A compliant document, log file is omitted
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.PDF_A_3B, Aspose.Pdf.ConvertErrorAction.Delete);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFA3b_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA3b()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Convert to PDF/A compliant document, log file is omitted
    document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.PDF_A_3B, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "PDFToPDFA3b_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## PDFファイルをPDF/A-4に変換

<a name="csharp-convert-pdf-to-a4" id="csharp-convert-pdf-to-a4"><strong>PDFをPDF/A-4に変換</strong></a>

Aspose.PDF for .NETは、PDFファイルをPDF/A-4形式に変換する機能もサポートしています。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);
    
        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
    document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

    // Convert to the PDF/A-4 format
    document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "PDFToPDFA4_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## PDF/Aファイルに添付ファイルを追加

PDF/A準拠の文書にファイルを添付する必要がある場合は、Aspose.PDF.PdfFormat列挙体からPDF_A_3A値を使用することをお勧めします。
PDF/A-3aは、PDF/A準拠のファイルに任意のファイル形式を添付する機能を提供する形式です。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachmentToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Setup new file to be added as attachment
        using (var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg", "Large Image file"))
        {
            // Add attachment to document's attachment collection
            document.EmbeddedFiles.Add(fileSpecification);

            // Perform conversion to PDF/A-3a, so that the attachment is included in the resultant file
            document.Convert(dataDir + "PDFA3aConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_3A, Aspose.Pdf.ConvertErrorAction.Delete);

            // Save PDF document
            document.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachmentToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Setup new file to be added as attachment
    using var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg", "Large Image file");

    // Add attachment to document's attachment collection
    document.EmbeddedFiles.Add(fileSpecification);

    // Perform conversion to PDF/A-3a, so that the attachment is included in the resultant file
    document.Convert(dataDir + "PDFA3aConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_3A, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 欠落フォントを代替フォントで置き換える

PDF/A基準に従って、フォントはPDF/A文書に埋め込む必要があります。しかし、ソース文書にフォントが埋め込まれておらず、マシンに存在しない場合、PDF/A変換は失敗します。この場合、欠落フォントをマシンに存在する代替フォントで置き換える必要があります。欠落フォントは、PDFからPDF/Aへの変換中にSimpleFontSubsitutionクラスを使用して置き換えることができます。

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceMissingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    try
    {
        // Check whether a font, used in the source document, is installed in the system
        Aspose.Pdf.Text.FontRepository.FindFont("AgencyFB");
    }
    catch (Aspose.Pdf.FontNotFoundException)
    {
        // Font is missing on the destination machine. Replace it with the Arial font installed in the system
        var fontSubstitution = new Aspose.Pdf.Text.SimpleFontSubstitution("AgencyFB", "Arial");
        Aspose.Pdf.Text.FontRepository.Substitutions.Add(fontSubstitution);
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // During the conversion, the missing font will be replaced with the substitution one
        document.Convert(dataDir + "ReplaceMissingFonts.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "ReplaceMissingFonts_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceMissingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    try
    {
        // Check whether a font, used in the source document, is installed in the system
        Aspose.Pdf.Text.FontRepository.FindFont("AgencyFB");
    }
    catch (Aspose.Pdf.FontNotFoundException)
    {
        // Font is missing on the destination machine. Replace it with the Arial font installed in the system
        var fontSubstitution = new Aspose.Pdf.Text.SimpleFontSubstitution("AgencyFB", "Arial");
        Aspose.Pdf.Text.FontRepository.Substitutions.Add(fontSubstitution);
    }

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // During the conversion, the missing font will be replaced with the substitution one
    document.Convert(dataDir + "ReplaceMissingFonts.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "ReplaceMissingFonts_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## ドキュメントの論理構造タグを自動的に作成

PDF文書には、アクセシビリティと組織を向上させるために論理構造タグを含めることができます。これらのタグは、文書の内容をセクション、段落などの論理的な部分に分割することによって構造化します。文書がPDF/Aに変換されると、Aspose.PDFは基本的な論理構造マークアップを自動的に生成できます。ユーザーはその後、この構造を手動で洗練させ、文書の内容に関するさらなる洞察を追加できます。

論理文書構造を生成するには、[Aspose.Pdf.AutoTaggingSettings](https://reference.aspose.com/pdf/ja/net/aspose.pdf/autotaggingsettings/)クラスのインスタンスを作成し、その[AutoTaggingSettings.EnableAutoTagging](https://reference.aspose.com/pdf/ja/net/aspose.pdf/autotaggingsettings/enableautotagging/)を`true`に設定し、[PdfFormatConversionOptions.AutoTaggingSettings](https://reference.aspose.com/pdf/ja/net/aspose.pdf/pdfformatconversionoptions/autotaggingsettings/)プロパティに割り当てます。

{{% alert color="warning" %}}
文書にすでに論理構造タグがある場合、オートタグ付けを有効にすると既存の論理構造が破壊され、新しいものが生成されます。
{{% /alert %}}

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertToPdfAWithAutomaticTagging()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Create conversion options
        Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(dataDir + "ConvertToPdfAWithAutomaticTagging.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Create auto-tagging settings
        // Aspose.Pdf.AutoTaggingSettings.Default may be used to set the same settings as given below
        Aspose.Pdf.AutoTaggingSettings autoTaggingSettings = new Aspose.Pdf.AutoTaggingSettings();

        // Enable auto-tagging during the conversion process
        autoTaggingSettings.EnableAutoTagging = true;

        // Use the heading recognition strategy that's optimal for the given document structure
        autoTaggingSettings.HeadingRecognitionStrategy = Aspose.Pdf.HeadingRecognitionStrategy.Auto;

        // Assign auto-tagging settings to be used during the conversion process
        options.AutoTaggingSettings = autoTaggingSettings;

        // During the conversion, the document logical structure will be automatically created
        document.Convert(options);

        // Save PDF document
        document.Save(dataDir + "ConvertToPdfAWithAutomaticTagging_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertToPdfAWithAutomaticTagging()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Create conversion options
    Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(dataDir + "ConvertToPdfAWithAutomaticTagging.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

    // Create auto-tagging settings
    // Aspose.Pdf.AutoTaggingSettings.Default may be used to set the same settings as given below
    Aspose.Pdf.AutoTaggingSettings autoTaggingSettings = new Aspose.Pdf.AutoTaggingSettings
    {
        // Enable auto-tagging during the conversion process
        EnableAutoTagging = true,

        // Use the heading recognition strategy that's optimal for the given document structure
        HeadingRecognitionStrategy = Aspose.Pdf.HeadingRecognitionStrategy.Auto
    };

    // Assign auto-tagging settings to be used during the conversion process
    options.AutoTaggingSettings = autoTaggingSettings;

    // During the conversion, the document logical structure will be automatically created
    document.Convert(options);

    // Save PDF document
    document.Save(dataDir + "ConvertToPdfAWithAutomaticTagging_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}