---
title: 既存のPDFからテーブルを削除する
linktitle: テーブルを削除
type: docs
weight: 50
url: /ja/net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "既存のPDFからテーブルを削除する",
    "alternativeHeadline": "PDFからテーブルを削除する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, テーブルを削除, テーブルを削除する",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF for NETでは、PDFドキュメントをゼロから生成する際にテーブルを挿入/作成する機能を提供しています。また、既存のPDFドキュメントにテーブルオブジェクトを追加することもできます。しかし、[既存のPDFでテーブルを操作する](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/)必要があるかもしれません。ここでは、既存のテーブルセルの内容を更新できます。さらに、既存のPDFドキュメントからテーブルオブジェクトを削除する必要が生じることがあります。

{{% /alert %}}

テーブルを削除するためには、既存のPDF内のテーブルを掴むために[TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber)クラスを使用してから、[Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove)を呼び出す必要があります。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリとも動作します。

## PDF文書からテーブルを削除する

新しい関数を追加しました。
新しい関数を追加しました。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 既存のPDFドキュメントを読み込みます
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// テーブルを見つけるためのTableAbsorberオブジェクトを作成します
TableAbsorber absorber = new TableAbsorber();

// absorberで最初のページを訪れます
absorber.Visit(pdfDocument.Pages[1]);

// ページ上の最初のテーブルを取得します
AbsorbedTable table = absorber.TableList[0];

// テーブルを削除します
absorber.Remove(table);

// PDFを保存します
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## PDFドキュメントから複数のテーブルを削除する

時々、PDFドキュメントには複数のテーブルが含まれている場合があり、それらを削除する必要が生じるかもしれません。PDFドキュメントから複数のテーブルを削除するには、以下のコードスニペットを使用してください：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 既存のPDFドキュメントを読み込みます
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// テーブルを見つけるためのTableAbsorberオブジェクトを作成します
TableAbsorber absorber = new TableAbsorber();

// absorberで2ページ目を訪れます
absorber.Visit(pdfDocument.Pages[1]);

// テーブルコレクションのコピーを取得します
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// コレクションのコピーをループしてテーブルを削除します
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// ドキュメントを保存します
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}
テーブルの削除や置換はTableListコレクションに影響を与えることを考慮してください。したがって、ループ内でテーブルを削除/置換する場合は、TableListコレクションのコピーが不可欠です。
{{% /alert %}}

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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

