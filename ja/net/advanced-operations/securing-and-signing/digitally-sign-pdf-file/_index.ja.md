---
title: PDFにデジタル署名を追加またはデジタル署名する方法
linktitle: PDFにデジタル署名
type: docs
weight: 10
url: /net/digitally-sign-pdf-file/
description: C#またはVB.NETを使用してPDF文書にデジタル署名を行います。C#またはVB.NETを使用してデジタル署名されたPDFを検証または検証します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFにデジタル署名する方法",
    "alternativeHeadline": "デジタル署名付きPDFの扱い方",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文書生成",
    "keywords": "pdf, c#, デジタル署名pdf",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "C#またはVB.NETを使用してPDF文書にデジタル署名を行います。C#またはVB.NETを使用してデジタル署名されたPDFを検証または検証します。"
}
</script>
Aspose.PDF for .NETは、SignatureFieldクラスを使用してPDFファイルにデジタル署名を行う機能をサポートしています。PKCS12証明書を使用してPDFファイルを認証することもできます。[Adobe Acrobatでの署名とセキュリティの追加](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)に似ています。

PDFドキュメントに署名を使用する場合、基本的にその内容を「そのまま」確認することになります。したがって、その後に行われた他の変更は署名を無効にし、ドキュメントが変更されたかどうかを知ることができます。一方、ドキュメントを最初に認証することで、ユーザーが認証を無効にすることなくドキュメントに加えることができる変更を指定できます。

言い換えれば、ドキュメントは依然としてその完全性を保持していると考えられ、受信者は引き続きドキュメントを信頼できます。詳細については、PDFを認証および署名するをご覧ください。一般に、ドキュメントの認証は.NET実行可能ファイルのコード署名と比較できます。

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも動作します。

## Aspose.PDF for .NETの署名機能

PDF署名には以下のクラスとメソッドを使用できます

- クラス [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)
- 列挙型 [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)
- [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) クラスのプロパティ [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified)

## デジタル署名を使ってPDFに署名

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // PKCS7/PKCS7Detachedオブジェクトを使用
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // 出力PDFファイルを保存
            signature.Save(outFile);
        }
    }
}
```
## デジタル署名にタイムスタンプを追加

### PDFにタイムスタンプ付きでデジタル署名をする方法

Aspose.PDF for .NETは、タイムスタンプサーバーまたはWebサービスを用いてPDFにデジタル署名することをサポートしています。

この要件を達成するために、[TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) クラスがAspose.PDF名前空間に追加されました。以下のコードスニペットをご覧ください。これはタイムスタンプを取得し、PDFドキュメントに追加します：

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // ユーザー/パスワードは省略可能
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // 3つの署名タイプのいずれかを作成
            signature.Sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
            // 出力PDFファイルを保存
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

