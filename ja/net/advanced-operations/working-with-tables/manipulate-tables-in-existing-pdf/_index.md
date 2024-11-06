---
title: 既存のPDFで表を操作する
linktitle: 表の操作
type: docs
weight: 40
url: ja/net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "既存のPDFで表を操作する",
    "alternativeHeadline": "既存のPDFで表の内容を更新する方法",
    "author": {
        "@type": "Person",
        "name":"アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "PDF、C#、表の操作",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>

## 既存のPDF内のテーブルを操作する

Aspose.PDF for .NETがサポートする最も初期の機能の一つは、テーブルの操作であり、スクラッチから生成されるPDFファイルや既存のPDFファイルにテーブルを追加するための大きなサポートを提供します。また、データベースの内容に基づいて動的なテーブルを作成するために、データベース（DOM）とテーブルを統合する機能も利用できます。この新しいリリースで、PDFドキュメントのページに既に存在する簡単なテーブルを検索して解析する新機能を実装しました。**Aspose.PDF.Text.TableAbsorber** という新しいクラスがこれらの機能を提供します。TableAbsorberの使用方法は、既存のTextFragmentAbsorberクラスに非常に似ています。次のコードスニペットは、特定のテーブルセルの内容を更新する手順を示しています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも連携します。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 既存のPDFファイルをロード
Document pdfDocument = new Document(dataDir + "input.pdf");
// テーブルを見つけるためのTableAbsorberオブジェクトを作成
TableAbsorber absorber = new TableAbsorber();

// absorberを使用して最初のページを訪れる
absorber.Visit(pdfDocument.Pages[1]);

// ページ上の最初のテーブルにアクセスし、その最初のセルとその中のテキストフラグメントを取得
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// セル内の最初のテキストフラグメントのテキストを変更
fragment.Text = "こんにちは世界";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## PDFドキュメント内の古いテーブルを新しいテーブルに置き換える

特定のテーブルを見つけて所望のテーブルに置き換える必要がある場合、[TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) クラスの Replace() メソッドを使用できます。次の例は、PDFドキュメント内のテーブルを置き換える機能を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 既存のPDFドキュメントを読み込む
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// テーブルを見つけるための TableAbsorber オブジェクトを作成する
TableAbsorber absorber = new TableAbsorber();

// absorber で最初のページを訪れる
absorber.Visit(pdfDocument.Pages[1]);

// ページ上の最初のテーブルを取得する
AbsorbedTable table = absorber.TableList[0];

// 新しいテーブルを作成する
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Col 1");
row.Cells.Add("Col 2");
row.Cells.Add("Col 3");

// 新しいテーブルで既存のテーブルを置き換える
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// ドキュメントを保存する
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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
    "applicationCategory": "PDF操作ライブラリ for .NET",
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

