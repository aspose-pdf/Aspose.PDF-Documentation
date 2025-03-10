---
title: PDFドキュメントをプログラムで保存
linktitle: PDFを保存
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/save-pdf-document/
description: C# Aspose.PDF for .NET PDFライブラリを使用してPDFファイルを保存する方法を学びます。PDFドキュメントをファイルシステム、ストリーム、およびWebアプリケーションに保存します。
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
    "abstract": "開発者がAspose.PDF for .NETを使用してPDFドキュメントを簡単にプログラムで保存する方法を発見してください。この機能は、ファイルシステム、ストリーム、およびWebアプリケーション内で直接PDFを保存することをサポートし、さまざまなユースケースに対応しながら、長期保存およびグラフィックス交換のためのPDF/AおよびPDF/X標準への準拠を確保します。この堅牢な保存メカニズムでPDF処理能力を最適化してください。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

次のコードスニペットは、[Aspose.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## PDFドキュメントをファイルシステムに保存

`Document`クラスの`Save`メソッドを使用して、作成または操作されたPDFドキュメントをファイルシステムに保存できます。
フォーマットタイプ（オプション）を指定しない場合、ドキュメントはAspose.PDF v.1.7（*.pdf）形式で保存されます。

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

## PDFドキュメントをストリームに保存

`Save`メソッドのオーバーロードを使用して、作成または操作されたPDFドキュメントをストリームに保存することもできます。

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

詳細な説明については、[Showcase](/pdf/ja/net/showcases/)セクションをご覧ください。

## PDF/AまたはPDF/X形式で保存

PDF/Aは、電子文書のアーカイブおよび長期保存のために使用されるポータブルドキュメントフォーマット（PDF）のISO標準化されたバージョンです。
PDF/Aは、フォントリンク（フォント埋め込みとは対照的）や暗号化など、長期保存に適さない機能を禁止している点でPDFとは異なります。PDF/AビューアのISO要件には、カラー管理ガイドライン、埋め込まれたフォントのサポート、および埋め込まれた注釈を読むためのユーザーインターフェースが含まれます。

PDF/XはPDF ISO標準のサブセットです。PDF/Xの目的はグラフィックス交換を促進することであり、そのため、標準PDFファイルには適用されない一連の印刷関連の要件があります。

いずれの場合も、`Save`メソッドを使用してドキュメントを保存し、ドキュメントは`Convert`メソッドを使用して準備する必要があります。

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