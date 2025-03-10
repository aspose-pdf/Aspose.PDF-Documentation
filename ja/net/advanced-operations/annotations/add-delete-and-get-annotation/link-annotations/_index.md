---
title: PDFでのリンク注釈の使用
linktitle: リンク注釈
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/link-annotations/
description: Aspose.PDF for .NETを使用すると、PDFドキュメントからリンク注釈を追加、取得、削除できます。
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Link Annotation for PDF",
    "alternativeHeadline": "How to add Link Annotation in PDF",
    "abstract": "Aspose.PDF for .NETは、PDFドキュメント内のリンク注釈を管理するための強力な機能を提供し、ユーザーがハイパーリンクをシームレスに追加、取得、削除できるようにします。この機能により、特定のページ、外部ファイル、またはWeb URLを開くリンクをカスタマイズ可能なさまざまなスタイルとアクションで作成することで、ドキュメントのインタラクティビティが向上します。この強力な注釈機能を使用して、PDFのナビゲーションとユーザーエンゲージメントの新しい可能性を開きましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, text annotation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用すると、PDFドキュメントからテキスト注釈を追加、取得、削除できます。"
}
</script>

## 既存のPDFファイルにリンク注釈を追加する

> 次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

[リンク注釈](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)は、ハイパーリンク、他の場所への宛先、およびドキュメントを表します。PDF標準によれば、リンク注釈は次の3つのケースで使用できます：ページビューを開く、ファイルを開く、Webページを開く。

### ページビューを開くためのリンク注釈の使用

注釈を作成するために、いくつかの追加手順が実行されました。デモ用にフラグメントを見つけるために2つのTextFragmentAbsorberを使用しました。最初のものはリンク注釈テキスト用で、2番目のものはドキュメント内のいくつかの場所を示します。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Link Annotation Demo.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define regular expressions for text fragments
        var regEx1 = new Regex(@"Link Annotation Demo \d");
        var regEx2 = new Regex(@"Sample text \d");

        // Create TextFragmentAbsorber for the first regular expression
        var textFragmentAbsorber1 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx1);
        textFragmentAbsorber1.Visit(document);

        // Create TextFragmentAbsorber for the second regular expression
        var textFragmentAbsorber2 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx2);
        textFragmentAbsorber2.Visit(document);

        // Get the text fragments for both absorbers
        var linkFragments = textFragmentAbsorber1.TextFragments;
        var sampleTextFragments = textFragmentAbsorber2.TextFragments;

        // Create a LinkAnnotation
        var linkAnnotation1 = new Aspose.Pdf.Annotations.LinkAnnotation(page, linkFragments[1].Rectangle)
        {
            Action = new Aspose.Pdf.Annotations.GoToAction(
                new Aspose.Pdf.Annotations.XYZExplicitDestination(
                    sampleTextFragments[1].Page,
                    sampleTextFragments[1].Rectangle.LLX,
                    sampleTextFragments[1].Rectangle.URX, 1.5))
        };

        // Add the link annotation to the page
        page.Annotations.Add(linkAnnotation1);

        // Save PDF document
        document.Save(dataDir + "AddLinkAnnotation_out.pdf");
    }
}
```

注釈を作成するために、次の手順に従いました：

1. `LinkAnnotation`を作成し、ページオブジェクトと注釈に対応するテキストフラグメントの矩形を渡します。
1. `Action`を`GoToAction`として設定し、`XYZExplicitDestination`を目的地として渡します。ページ、左および上の座標、ズームに基づいて`XYZExplicitDestination`を作成しました。
1. 注釈をページの注釈コレクションに追加します。
1. ドキュメントを保存します。

### 名前付き宛先を使用したリンク注釈の使用

さまざまなドキュメントを処理しているとき、入力しているときに注釈がどこを指すかわからない状況が発生します。
この場合、特別な（名前付き）宛先を使用でき、コードは次のようになります：

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

別の場所で名前付き宛先を作成できます。

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```

### ファイルを開くためのリンク注釈の使用

ファイルを開くための注釈を作成する際には、上記の例と同じアプローチが使用されます。

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

違いは、`GoToAction`の代わりに`GoToRemoteAction`を使用することです。GoToRemoteActionのコンストラクタは、ファイル名とページ番号の2つのパラメータを受け取ります。
別の形式を使用してファイル名といくつかの宛先を渡すこともできます。明らかに、使用する前にそのような宛先を作成する必要があります。

### Webページを開くためのリンク注釈の使用

Webページを開くには、`Action`を`GoToURIAction`オブジェクトで設定します。
ハイパーリンクをコンストラクタパラメータとして渡すことも、他の種類のURIを渡すこともできます。たとえば、電話番号を呼び出すアクションを実装するために`callto`を使用できます。

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```

## 装飾されたリンク注釈の追加

ボーダーを使用してリンク注釈をカスタマイズできます。以下の例では、幅3ptの青い破線のボーダーを作成します。

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

別の例では、ブラウザスタイルをシミュレートし、リンクに下線を使用する方法を示します。

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### リンク注釈の取得

次のコードスニペットを使用して、PDFドキュメントからLinkAnnotationを取得してみてください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Get all Link annotations from the first page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        // Iterate through each Link annotation
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);

            // Create a TextAbsorber to extract text within the annotation's rectangle
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;

            // Accept the absorber for the first page
            document.Pages[1].Accept(absorber);

            // Extract and print the text associated with the hyperlink
            string extractedText = absorber.Text;
            Console.WriteLine(extractedText);
        }
    }
}
```

### リンク注釈の削除

次のコードスニペットは、PDFファイルからリンク注釈を削除する方法を示しています。これには、1ページ目のすべてのリンク注釈を見つけて削除する必要があります。その後、削除された注釈でドキュメントを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Find and delete all link annotations on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        foreach (var la in linkAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLinkAnnotations_out.pdf");
    }
}
```