---
title: PDFでのアクションの操作
linktitle: アクション
type: docs
weight: 20
url: /net/actions/
description: このセクションでは、C#を使用してドキュメントとフォームフィールドにプログラムでアクションを追加する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFでのアクションの操作",
    "alternativeHeadline": "PDFにアクションを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, PDF内のアクション",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、C#を使用してドキュメントとフォームフィールドにプログラムでアクションを追加する方法について説明します。"
}
</script>
次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

## PDFファイルにハイパーリンクを追加する

PDFファイルにハイパーリンクを追加することが可能です。これにより、読者がPDFの他の部分や外部コンテンツにナビゲートできるようになります。

PDFドキュメントにWebハイパーリンクを追加するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスオブジェクトを作成します。
1. リンクを追加したい[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスを取得します。
1. Pageと[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) オブジェクトを使用して、[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) オブジェクトを作成します。Rectangleオブジェクトは、ページ上でリンクを追加する場所を指定するために使用されます。
1. Actionプロパティを[GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) オブジェクトに設定します。これはリモートURIの場所を指定します。
1. フリーテキストを追加するには：

- [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) オブジェクトをインスタンス化します。これはPageオブジェクトとRectangleオブジェクトも引数として受け入れるため、LinkAnnotationコンストラクタに対して指定された値と同じ値を提供することができます。
- [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) オブジェクトのContentsプロパティを使用して、出力PDFに表示されるべき文字列を指定します。
- オプションで、[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) およびFreeTextAnnotationオブジェクトの境界線の幅を0に設定して、PDFドキュメントに表示されないようにします。
- [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) および [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) オブジェクトが定義されたら、これらのリンクを [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) オブジェクトのAnnotationsコレクションに追加します。
- [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトと[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)オブジェクトが定義されたら、これらのリンクを[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトのAnnotationsコレクションに追加します。
- 最後に、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFを保存します。

次のコードスニペットは、PDFファイルにハイパーリンクを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// ドキュメントを開く
Document document = new Document(dataDir + "AddHyperlink.pdf");
// リンクを作成
Page page = document.Pages[1];
// リンク注釈オブジェクトを作成
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// LinkAnnotationのためのボーダーオブジェクトを作成
Border border = new Border(link);
// ボーダーの幅を0に設定
border.Width = 0;
// LinkAnnotationのボーダーを設定
link.Border = border;
// リンクタイプをリモートURIとして指定
link.Action = new GoToURIAction("www.aspose.com");
// リンク注釈をPDFファイルの最初のページの注釈コレクションに追加
page.Annotations.Add(link);

// フリーテキスト注釈を作成
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// フリーテキストとして追加される文字列
textAnnotation.Contents = "Link to Aspose website";
// フリーテキスト注釈のボーダーを設定
textAnnotation.Border = border;
// フリーテキスト注釈をドキュメントの最初のページの注釈コレクションに追加
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// 更新されたドキュメントを保存
document.Save(dataDir);
```
## 同じPDF内のページへのハイパーリンクを作成する

Aspose.PDF for .NETはPDFの作成だけでなく、操作するための優れた機能を提供しています。また、PDFページへのリンクを追加する機能も提供しており、リンクは別のPDFファイルのページ、Web URL、アプリケーションの起動、または同じPDFファイル内のページへのリンクを指示することができます。同じPDFファイル内のページへのローカルハイパーリンクを追加するために、Aspose.PDF名前空間に[LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink)というクラスが追加され、このクラスにはTargetPageNumberというプロパティがあり、ハイパーリンクの対象/目的のページを指定するために使用されます。

ローカルハイパーリンクを追加するためには、リンクをテキストフラグメントに関連付けることができるように、TextFragmentを作成する必要があります。[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)クラスには、LocalHyperlinkインスタンスを関連付けるために使用されるHyperlinkというプロパティがあります。次のコードスニペットは、この要件を達成するための手順を示しています。

```csharp
```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Documentインスタンスを作成します
Document doc = new Document();
// PDFファイルのページコレクションにページを追加します
Page page = doc.Pages.Add();
// Text Fragmentインスタンスを作成します
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("ページ7へのリンクページ番号テスト");
// ローカルハイパーリンクインスタンスを作成します
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// リンクインスタンスのターゲットページを設定します
link.TargetPageNumber = 7;
// TextFragmentのハイパーリンクを設定します
text.Hyperlink = link;
// ページの段落コレクションにテキストを追加します
page.Paragraphs.Add(text);
// 新しいTextFragmentインスタンスを作成します
text = new TextFragment("ページ1へのリンクページ番号テスト");
// TextFragmentは新しいページに追加する必要があります
text.IsInNewPage = true;
// 別のローカルハイパーリンクインスタンスを作成します
link = new LocalHyperlink();
// 2番目のハイパーリンクのターゲットページを設定します
link.TargetPageNumber = 1;
// 2番目のTextFragmentのリンクを設定します
text.Hyperlink = link;
// ページオブジェクトの段落コレクションにテキストを追加します
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// 更新されたドキュメントを保存します
doc.Save(dataDir);
```
## PDFハイパーリンクの宛先（URL）を取得する

リンクはPDFファイル内の注釈として表され、追加、更新、または削除することができます。Aspose.PDF for .NETは、PDFファイル内のハイパーリンクの宛先（URL）を取得することもサポートしています。

リンクのURLを取得するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトを作成します。
1. リンクを抽出する[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)を取得します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) クラスを使用して、指定されたページからすべての[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを抽出します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector)オブジェクトを[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトのAcceptメソッドに渡します。
1.
1. 最終的に、LinkAnnotation アクションを GoToURIAction として抽出します。

次のコードスニペットは、PDFファイルからハイパーリンクの宛先（URL）を取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDFファイルを読み込む
Document document = new Document(dataDir + "input.pdf");

// PDFの全ページを通して走査する
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // 特定のページからリンクアノテーションを取得する
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // 全てのリンクを保持するリストを作成する
    IList<Annotation> list = selector.Selected;
    // リスト内の個々のアイテムを反復処理する
    foreach (LinkAnnotation a in list)
    {
        // 宛先のURLを出力する
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## ハイパーリンクテキストを取得

ハイパーリンクには二つの部分があります：ドキュメントに表示されるテキストと、目的地のURLです。場合によっては、URLよりテキストが必要になります。

PDFファイルのテキストと注釈/アクションは異なるエンティティによって表されます。ページ上のテキストは単なる単語と文字のセットですが、注釈はハイパーリンクに固有のようなインタラクティビティをもたらします。

URLの内容を見つけるためには、注釈とテキストの両方を扱う必要があります。[Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation)オブジェクト自体はテキストを持っていませんが、ページ上のテキストの下に位置しています。したがって、テキストを取得するために、AnnotationはURLの境界を提供し、TextオブジェクトはURLの内容を提供します。以下のコードスニペットをご覧ください。

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // 文書ディレクトリへのパス。
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // PDFファイルを読み込む
                Document document = new Document(dataDir + "input.pdf");
                // PDFの各ページを繰り返し処理
                foreach (Page page in document.Pages)
                {
                    // リンク注釈を表示
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // 各リンク注釈のURLを印刷
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // ハイパーリンクに関連付けられたテキストを印刷
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## PDFファイルからドキュメントオープンアクションを削除する

[PDFページを指定する方法](#how-to-specify-pdf-page-when-viewing-document) では、最初のページ以外でドキュメントを開く方法を説明しました。複数のドキュメントを結合するとき、1つ以上のドキュメントにGoToアクションが設定されている場合、それらを削除することが望ましいかもしれません。たとえば、2つのドキュメントを組み合わせ、2番目のドキュメントに2ページ目に移動するGoToアクションがある場合、出力ドキュメントは組み合わせたドキュメントの最初のページではなく、2番目のドキュメントの2ページ目で開かれます。この動作を避けるために、オープンアクションコマンドを削除します。

オープンアクションを削除するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトの [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) プロパティをnullに設定します。
1. Documentオブジェクトの [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFを保存します。

次のコードスニペットは、PDFファイルからドキュメントオープンアクションを削除する方法を示しています。
次のコードスニペットは、PDFファイルからドキュメントオープンアクションを削除する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// ドキュメントを開く
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// ドキュメントオープンアクションを削除
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// 更新されたドキュメントを保存
document.Save(dataDir);
```

## PDFページを指定する方法 {#how-to-specify-pdf-page-when-viewing-document}

Adobe ReaderなどのPDFビューアでPDFファイルを表示するとき、通常は最初のページが開きます。しかし、異なるページでファイルを開くように設定することが可能です。

[XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) クラスを使用して、開きたいPDFファイルのページを指定できます。
[XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) クラスを使用すると、PDFファイル内で開きたいページを指定できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// PDFファイルをロードします
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// ドキュメントの2ページ目のインスタンスを取得します
Page page2 = doc.Pages[2];
// ターゲットページのズーム係数を設定する変数を作成します
double zoom = 1;
// GoToActionインスタンスを作成します
GoToAction action = new GoToAction(doc.Pages[2]);
// 2ページ目に移動します
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// ドキュメントのオープンアクションを設定します
doc.OpenAction = action;
// 更新されたドキュメントを保存します
doc.Save(dataDir + "goto2page_out.pdf");
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

