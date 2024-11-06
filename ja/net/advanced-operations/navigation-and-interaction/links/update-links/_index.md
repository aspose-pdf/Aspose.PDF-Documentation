---
title: PDF内のリンクを更新する
linktitle: リンクを更新
type: docs
weight: 20
url: ja/net/update-links/
description: PDF内のリンクをプログラムで更新する方法についてのガイドです。このガイドは、C#言語でPDF内のリンクを更新する方法について説明しています。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内のリンクを更新する",
    "alternativeHeadline": "PDF内のリンクを更新する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdf内のリンクを更新",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "PDF内のリンクをプログラムで更新する方法についてのガイドです。このガイドは、C#言語でPDF内のリンクを更新する方法について説明しています。"
}
</script>
次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## PDFファイル内のリンクを更新する

PDFファイルにハイパーリンクを追加する場合の議論として、「[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)」クラスを使用してPDFファイルにリンクを追加することができます。PDFファイル内の既存のリンクを取得するために使用される類似のクラスもあります。既存のリンクを更新する必要がある場合はこれを使用します。既存のリンクを更新するには：

1. PDFファイルを読み込みます。
1. PDFファイルの特定のページに移動します。
1. [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) オブジェクトのDestinationプロパティを使用してリンク先を指定します。
1. 目的地のページは、[XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) コンストラクタを使用して指定されます。

### リンクターゲットを同じドキュメントのページに設定する

次のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットをドキュメントの2ページ目に設定する方法を示しています。
以下のコードスニペットは、PDFファイルのリンクを更新し、そのターゲットをドキュメントの2ページ目に設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDFファイルを読み込む
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// ドキュメントの最初のページから最初のリンク注釈を取得する
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// リンクの変更：リンク先を変更する
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// リンクオブジェクトの目的地を指定する
// 第一パラメータはドキュメントオブジェクト、第二は目的地のページ番号です。
// 5番目の引数は、該当ページを表示する際のズームファクターです。2を使用すると、ページが200％のズームで表示されます
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// 更新されたリンクを含むドキュメントを保存する
doc.Save(dataDir);
```
### ウェブアドレスへのリンク先を設定する

ウェブアドレスを指すようにハイパーリンクを更新するには、[GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) オブジェクトをインスタンス化して、LinkAnnotationのActionプロパティに渡します。以下のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットをウェブアドレスに設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDFファイルをロードする
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// ドキュメントの最初のページから最初のリンク注釈を取得する
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// リンクの変更: リンクアクションを変更し、ターゲットをウェブアドレスに設定する
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// リンクを更新したドキュメントを保存する
doc.Save(dataDir);
```
### PDFファイルへのリンクターゲットを設定

次のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットを別のPDFファイルに設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDFファイルをロードする
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// 次の行は目的地を更新しますが、ファイルは更新しません
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// 次の行はファイルを更新します
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// 更新されたリンクでドキュメントを保存
document.Save(dataDir);
```

### LinkAnnotationのテキスト色を更新

リンク注釈にはテキストが含まれていません。
リンク注釈にテキストが含まれていません。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDFファイルを読み込む
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // 注釈の下のテキストを検索する
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // テキストの色を変更する。
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// リンクを更新したドキュメントを保存する
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NETライブラリ",
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
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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

