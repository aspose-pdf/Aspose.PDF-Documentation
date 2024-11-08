---
title: C#を使用したPDFツールチップ
linktitle: PDFツールチップ
type: docs
weight: 20
url: /ja/net/pdf-tooltip/
description: C#とAspose.PDFを使用してPDFのテキストフラグメントにツールチップを追加する方法を学ぶ
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用したPDFツールチップ",
    "alternativeHeadline": "テキストにPDFツールチップを追加",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, add pdf tooltip",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "C#とAspose.PDFを使用してPDFのテキストフラグメントにツールチップを追加する方法を学ぶ"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

## 検索したテキストに見えないボタンを追加してツールチップを追加する

PDFドキュメントにフレーズや特定の単語に詳細をツールチップとして追加することがよく求められます。これにより、ユーザーがマウスカーソルをテキスト上にホバーしたときにポップアップが表示されます。Aspose.PDF for .NETは、検索されたテキストの上に見えないボタンを追加することでツールチップを作成する機能を提供します。次のコードスニペットは、この機能を実現する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// テキストを含むサンプルドキュメントを作成する
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("マウスカーソルをここに移動してツールチップを表示します"));
doc.Pages[1].Paragraphs.Add(new TextFragment("マウスカーソルをここに移動して非常に長いツールチップを表示します"));
doc.Save(outputFile);

// テキストを含むドキュメントを開く
Document document = new Document(outputFile);
// すべてのフレーズを見つけるためのTextAbsorberオブジェクトを作成する
TextFragmentAbsorber absorber = new TextFragmentAbsorber("マウスカーソルをここに移動してツールチップを表示します");
// ドキュメントページでabsorberを受け入れる
document.Pages.Accept(absorber);
// 抽出されたテキストフラグメントを取得する
TextFragmentCollection textFragments = absorber.TextFragments;

// フラグメントをループする
foreach (TextFragment fragment in textFragments)
{
    // テキストフラグメントの位置に見えないボタンを作成する
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // AlternateNameの値がビューアーアプリケーションによってツールチップとして表示される
    field.AlternateName = "テキストのためのツールチップ。";
    // ドキュメントにボタンフィールドを追加する
    document.Form.Add(field);
}

// 次に非常に長いツールチップのサンプルが続きます
absorber = new TextFragmentAbsorber("マウスカーソルをここに移動して非常に長いツールチップを表示します");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // 非常に長いテキストを設定する
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// ドキュメントを保存する
document.Save(outputFile);
```
{{% alert color="primary" %}}

ツールチップの長さに関して、ツールチップテキストはPDFドキュメント内のPDF文字列タイプとしてコンテンツストリームの外に含まれています。PDFファイルではこのような文字列に効果的な制限はありません（PDFリファレンス付録Cを参照）。ただし、特定のプロセッサーおよび特定の運用環境で実行される準拠リーダー（例：Adobe Acrobat）にはそのような制限があります。PDFリーダーアプリケーションのドキュメントを参照してください。

{{% /alert %}}

## マウスオーバーで表示される隠しテキストブロックを作成する

Aspose.PDFでは、テキストボックスフィールド（またはその他のタイプの注釈）を隠す/表示するアクションを割り当てるために、Aspose.Pdf.Annotations.HideAction クラスが使用されます。以下のコードスニペットを使用して、マウスの入力/退出時にテキストブロックを表示/非表示にしてください。

PDFドキュメント内のPDFアクションは、準拠しているリーダー（例：Adobe Acrobat）で問題なく動作します。
PDFドキュメントでの動作が適合するリーダーで正常に機能することを考慮してください。

- Internet Explorer v.11.0でのPDFドキュメントの隠すアクションの全実装は問題なく機能します。
- Opera v.12.14でも隠すアクションの全実装は機能しますが、ドキュメントを初めて開いたときに少し反応が遅れることがあります。
- Google Chrome v.61.0でドキュメントを閲覧する場合、フィールド名を受け入れるHideActionコンストラクタを使用する実装のみが機能します。Google Chromeでの閲覧が重要な場合は、対応するコンストラクタを使用してください：

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// テキストを含むサンプルドキュメントを作成する
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("マウスカーソルをここに移動して浮動テキストを表示"));
doc.Save(outputFile);

// テキストを含むドキュメントを開く
Document document = new Document(outputFile);
// すべてのフレーズを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber absorber = new TextFragmentAbsorber("マウスカーソルをここに移動して浮動テキストを表示");
// ドキュメントページのためにabsorberを受け入れる
document.Pages.Accept(absorber);
// 最初に抽出されたテキストフラグメントを取得
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// ページの指定された矩形に浮動テキストの非表示テキストフィールドを作成
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// フィールド値として表示されるテキストを設定
floatingField.Value = "これは「浮動テキストフィールド」です。";
// このシナリオではフィールドを'readonly'にすることをお勧めします
floatingField.ReadOnly = true;
// ドキュメントを開いたときにフィールドを見えなくするために'hidden'フラグを設定
floatingField.Flags |= AnnotationFlags.Hidden;

// フィールド名を一意に設定する必要はありませんが、許可されています
floatingField.PartialName = "FloatingField_1";

// フィールドの外観特性を設定する必要はありませんが、それによりより良くなります
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// ドキュメントにテキストフィールドを追加
document.Form.Add(floatingField);

// テキストフラグメントの位置に見えないボタンを作成
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// 指定されたフィールド（アノテーション）および不可視フラグの新しい隠すアクションを作成。
// （上記で名前を指定した場合、浮動フィールドを名前で参照することもできます。）
// 見えないボタンフィールドでマウスが入る/出るときのアクションを追加
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// ドキュメントにボタンフィールドを追加
document.Form.Add(buttonField);

// ドキュメントを保存
document.Save(outputFile);
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

