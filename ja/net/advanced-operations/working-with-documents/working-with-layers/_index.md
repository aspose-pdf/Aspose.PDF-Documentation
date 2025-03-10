---
title: C#を使用してPDFレイヤーを操作する
linktitle: PDFレイヤーを操作する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/work-with-pdf-layers/
description: 次のタスクでは、PDFレイヤーをロックし、PDFレイヤー要素を抽出し、レイヤー付きPDFをフラット化し、PDF内のすべてのレイヤーを1つにマージする方法を説明します。
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "新しいAspose.PDF for .NET機能を使用して、ユーザーがPDFレイヤーを効果的に操作できるように、PDFドキュメント管理が向上します。この機能により、レイヤーのロックとアンロック、要素を別々のファイルに抽出、レイヤー付きコンテンツのフラット化、複数のレイヤーを1つにマージすることができ、ドキュメントの可視性と整理に対する制御が強化されます。PDFドキュメントの可能性を引き出し、これらの強力なツールでワークフローを効率化しましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

PDFレイヤーは、PDFドキュメントが異なるコンテンツセットを含むことを可能にし、それらを選択的に表示または非表示にできます。PDF内の各レイヤーには、テキスト、画像、またはグラフィックスが含まれており、ユーザーはニーズに応じてこれらのレイヤーをオンまたはオフに切り替えることができます。レイヤーは、異なるコンテンツを整理または分離する必要がある複雑なドキュメントでよく使用されます。

## PDFレイヤーをロックする

Aspose.PDF for .NETを使用すると、PDFを開き、最初のページの特定のレイヤーをロックし、変更を加えたドキュメントを保存できます。

この機能は、24.5リリース以降に実装されました。

新しいメソッドが2つ追加され、1つのプロパティが追加されました：

- Layer.Lock(); - レイヤーをロックします。
- Layer.Unlock(); - レイヤーのロックを解除します。
- Layer.Locked; - レイヤーのロック状態を示すプロパティです。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## PDFレイヤー要素を抽出する

Aspose.PDF for .NETライブラリは、最初のページから各レイヤーを抽出し、各レイヤーを別々のファイルに保存することを可能にします。

レイヤーから新しいPDFを作成するには、次のコードスニペットを使用できます：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

24.9リリースにより、この機能が更新されました。

PDFレイヤー要素を抽出し、新しいPDFファイルストリームに保存することが可能です：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## レイヤー付きPDFをフラット化する

Aspose.PDF for .NETライブラリは、PDFを開き、最初のページの各レイヤーを反復処理し、各レイヤーをフラット化してページ上に永続化します。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

'Layer.Flatten(bool cleanupContentStream)'メソッドは、コンテンツストリームからオプショナルコンテンツグループマーカーを削除するかどうかを指定するブールパラメータを受け入れます。cleanupContentStreamパラメータをfalseに設定すると、フラット化のプロセスが高速化されます。

## PDF内のすべてのレイヤーを1つにマージする

Aspose.PDF for .NETライブラリは、すべてのPDFレイヤーまたは最初のページの特定のレイヤーを新しいレイヤーにマージし、更新されたドキュメントを保存することを可能にします。

ページ上のすべてのレイヤーをマージするために2つのメソッドが追加されました：

- void MergeLayers(string newLayerName)。
- void MergeLayers(string newLayerName, string newOptionalContentGroupId)。

2番目のパラメータは、オプショナルコンテンツグループマーカーの名前を変更することを可能にします。デフォルト値は"oc1" (/OC /oc1 BDC)です。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```