---
title: PDF/3-A準拠のPDFを作成し、C#でZUGFeRD請求書を添付する
linktitle: PDFにZUGFeRDを添付する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/attach-zugferd/
description: ZUGFeRDを使用してPDF文書を生成する方法を学ぶ
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "開発者がPDF/A-3Bに準拠したPDF文書を生成し、C#を使用してZUGFeRD請求書をシームレスに添付できる新機能を発見してください。この機能は、PDFファイルに請求書メタデータを埋め込むプロセスを簡素化し、長期的な文書保存と電子請求書基準への準拠を確保します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFにZUGFeRDを添付する

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

ZUGFeRDをPDFに添付するための手順をお勧めします：

* 入力および出力PDFファイルがあるフォルダーを指すパス変数を定義します。
* パスから既存のPDFファイル（例："ZUGFeRD-test.pdf"）を読み込んでドキュメントオブジェクトを作成します。
* ZUGFeRD標準に準拠した請求書メタデータを含む別のファイル"factur-x.xml"のパスと説明を提供して、[FileSpecification](https://reference.aspose.com/pdf/ja/net/aspose.pdf/filespecification/)オブジェクトを作成します。
* ファイル仕様オブジェクトに、説明、MIMEタイプ、AF関係などのプロパティを追加します。AF関係は、埋め込まれたファイルがPDF文書にどのように関連しているかを示します。この場合、埋め込まれたファイルはPDFコンテンツの代替表現であるため、"Alternative"に設定されています。
* ファイル仕様オブジェクトをドキュメントの埋め込みファイルコレクションに追加します。ファイル名はZUGFeRD標準に従って指定する必要があります（例："factur-x.xml"）。
* ドキュメントをPDF/A-3B形式に変換します。これは、電子文書の長期保存を確保するPDFのサブセットです。PDF/A-3Bは、PDF文書に任意の形式のファイルを埋め込むことを許可します。
* 変換されたドキュメントを新しいPDFファイル（例："ZUGFeRD-res.pdf"）として保存します。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

convertメソッドは、ストリーム、PDF形式、および変換エラーアクションをパラメーターとして受け取ります。ストリームパラメーターは、変換ログを保存するために使用できます。変換エラーアクションパラメーターは、変換中にエラーが発生した場合に何をするかを指定します。この場合、"Delete"に設定されており、PDF/A-3B形式に準拠していない要素はドキュメントから削除されます。