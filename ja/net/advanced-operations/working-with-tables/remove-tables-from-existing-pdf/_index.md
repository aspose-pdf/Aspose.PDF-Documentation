---
title: 既存のPDFからテーブルを削除する
linktitle: テーブルを削除する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/remove-tables-from-existing-pdf/
description: Aspose.PDF for .NETを使用してPDFドキュメントからテーブルを削除する方法を理解し、ドキュメントの明瞭さと構造を改善します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Tables from existing PDF",
    "alternativeHeadline": "Effortlessly Eliminate Tables from Existing PDF Files",
    "abstract": "Aspose.PDF for .NETのテーブル削除機能により、ユーザーはTableAbsorberクラスを使用して既存のPDFドキュメントからテーブルオブジェクトを効率的に排除できます。この機能は、テーブルを見つけて削除するための簡単なメソッドを提供することで、PDFコンテンツの管理プロセスを簡素化し、ドキュメント編集機能を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

Aspose.PDF for NETは、ゼロから生成されるPDFドキュメント内にテーブルを挿入/作成する機能を提供します。また、既存のPDFドキュメントにテーブルオブジェクトを追加することもできます。ただし、既存のPDF内のテーブルを操作する必要がある場合があります。[既存のPDF内のテーブルを操作する](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/)ことで、既存のテーブルセルの内容を更新できます。しかし、既存のPDFドキュメントからテーブルオブジェクトを削除する必要がある場合もあります。

{{% /alert %}}

テーブルを削除するには、[TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber)クラスを使用して既存のPDF内のテーブルを取得し、次に[Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove)を呼び出す必要があります。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## PDFドキュメントからテーブルを削除する

PDFドキュメントからテーブルを削除するために、既存のTableAbsorberクラスに新しい関数、すなわちRemove()を追加しました。アブソーバーがページ上のテーブルを正常に見つけると、それらを削除する能力を持つようになります。以下のコードスニペットは、PDFドキュメントからテーブルを削除する方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get first table on the page
        Aspose.Pdf.Text.AbsorbedTable table = absorber.TableList[0];

        // Remove the table
        absorber.Remove(table);

        // Save PDF document
        document.Save(dataDir + "RemoveTable_out.pdf");
    }
}
```

## PDFドキュメントから複数のテーブルを削除する

時には、PDFドキュメントに複数のテーブルが含まれている場合があり、複数のテーブルを削除する必要があるかもしれません。PDFドキュメントから複数のテーブルを削除するには、以下のコードスニペットを使用してください：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveMultipleTables()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input2.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit second page with absorber
        absorber.Visit(document.Pages[1]);

        // Get copy of table collection
        Aspose.Pdf.Text.AbsorbedTable[] tables = new Aspose.Pdf.Text.AbsorbedTable[absorber.TableList.Count];
        absorber.TableList.CopyTo(tables, 0);

        // Loop through the copy of collection and removing tables
        foreach (var table in tables)
        {
            absorber.Remove(table);
        }

        // Save PDF document
        document.Save(dataDir + "RemoveMultipleTables_out.pdf");
    }
}
```

{{% alert color="primary" %}}

テーブルを削除または置き換えると、TableListコレクションが変更されることに注意してください。したがって、ループ内でテーブルを削除/置き換える場合は、TableListコレクションのコピーが不可欠です。

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