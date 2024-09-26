---
title: PDFでのリンク注釈の使用
linktitle: リンク注釈
type: docs
weight: 70
url: /net/link-annotations/
description: Aspose.PDF for .NETは、PDFドキュメントからリンク注釈を追加、取得、削除することができます。
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFにリンク注釈を使用する",
    "alternativeHeadline": "PDFにリンク注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, テキスト注釈",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETは、PDFドキュメントからテキスト注釈を追加、取得、削除することができます。"
}
</script>
## 既存のPDFファイルにリンク注釈を追加する

> 次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

[リンク注釈](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)は、ハイパーリンク、他の場所へのリンク、または文書を表します。PDF標準によると、リンク注釈は三つのケースで使用できます：ページビューを開く、ファイルを開く、ウェブページを開く。

### ページビューを開くためのリンク注釈の使用

注釈を作成するためにいくつかの追加ステップが実行されました。デモにフラグメントを見つけるために2つのTextFragmentAbsorbersを使用しました。最初のものはリンク注釈テキスト用で、二つ目は文書の中のいくつかの場所を示します。

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
注釈を作成するために、以下の手順に従いました：

1. `LinkAnnotation`を作成し、ページオブジェクトと注釈に対応するテキストフラグメントの矩形を渡します。
1. `Action`を`GoToAction`に設定し、目的の目的地として`XYZExplicitDestination`を渡します。`XYZExplicitDestination`はページ、左座標、上座標、ズームに基づいて作成されました。
1. ページ注釈コレクションに注釈を追加します。
1. 文書を保存します。

### 名前付き目的地を使用したリンク注釈

さまざまな文書を処理する際に、注釈が指す場所がわからない状況が生じます。
この場合、特別な（名前付き）目的地を使用でき、コードはここに示すようになります：

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

別の場所で名前付き目的地を作成できます。

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### ファイルを開くためのリンクアノテーションの使用

上記の例と同じアプローチが、ファイルを開くためのアノテーションを作成する際に使用されます。

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

違いは、`GoToAction`の代わりに`GoToRemoteAction`を使用することです。GoToRemoteActionのコンストラクターは、ファイル名とページ番号の2つのパラメーターを取得します。
また、ファイル名とある目的地を渡す別の形式を使用することもできます。明らかに、それを使用する前にそのような目的地を作成する必要があります。

### ウェブページを開くためのリンクアノテーションの使用

ウェブページを開くには、`GoToURIAction`オブジェクトで`Action`を設定します。
コンストラクターパラメーターとしてハイパーリンクを渡すことも、他の種類のURIを使用することもできます。たとえば、電話番号を呼び出すアクションを実装するために`callto`を使用することができます。

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // 電話番号を呼び出すアクションを設定してリンクアノテーションを作成する
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## リンクアノテーションに装飾を追加する

リンクアノテーションをカスタマイズするために、境界線を使用できます。以下の例では、幅3ptの青い破線の境界線を作成します。

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

別の例では、ブラウザスタイルを模倣してリンクに下線を使用する方法を示します。

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

### リンクアノテーションを取得する

PDFドキュメントからLinkAnnotationを取得するには、以下のコードスニペットを使用してみてください。

```csharp
class ExampleLinkAnnotations
{
    // ドキュメントディレクトリへのパス。
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // PDFファイルをロードする
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // 各リンクアノテーションのURLを印刷する
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // ハイパーリンクに関連付けられたテキストを印刷する
            Console.WriteLine(extractedText);
        }
    }
}
```
### リンク注釈の削除

次のコードスニペットは、PDFファイルからリンク注釈を削除する方法を示しています。これには、最初のページのすべてのリンク注釈を見つけて削除する必要があります。その後、注釈を削除したドキュメントを保存します。

```csharp
class ExampleLinkAnnotations
{
    // ドキュメントディレクトリへのパス
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // PDFファイルを読み込む
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // 最初のページのすべてのリンク注釈を見つけて削除する
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // 注釈を削除したドキュメントを保存する
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
