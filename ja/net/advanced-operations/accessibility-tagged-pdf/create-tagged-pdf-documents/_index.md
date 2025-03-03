---
title: C#を使用してタグ付きPDFを作成する
linktitle: タグ付きPDFを作成する
type: docs
weight: 10
url: /ja/net/create-tagged-pdf/
description: この記事では、Aspose.PDF for .NETを使用してプログラムでタグ付きPDFドキュメントの構造要素を作成する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してタグ付きPDFを作成する",
    "alternativeHeadline": "タグ付きPDFの作成方法",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "作成, タグ付け, PDF",
    "wordcount": "302",
    "proficiencyLevel": "初心者",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してプログラムでタグ付きPDFドキュメントの構造要素を作成する方法について説明します。"
}
</script>

タグ付きPDFを作成するとは、ドキュメントに特定の要素を追加（または作成）して、PDF/UA要件に従ってドキュメントを検証できるようにすることを意味します。これらの要素は、しばしば構造要素と呼ばれます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリとも連携します。

## タグ付きPDFの作成（シンプルなシナリオ）

タグ付きPDFドキュメントに構造要素を作成するために、Aspose.PDFは[ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) インターフェースを使用して構造要素を作成するメソッドを提供します。次のコードスニペットは、ヘッダーと段落の2つの要素を含むタグ付きPDFを作成する方法を示しています。

```csharp
private static void CreateTaggedPdfDocument01()
{
    // PDFドキュメントを作成
    var document = new Document();

    // タグ付きPdfで作業するためのコンテンツを取得
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // ドキュメントのタイトルと言語を設定
    taggedContent.SetTitle("タグ付きPDFドキュメント");
    taggedContent.SetLanguage("en-US");

    // メインヘッダーを作成
    HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("メインヘッダー");

    // 段落要素を作成
    ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
    "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
    "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
    "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
    "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
    "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
    "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
    "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
    "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    // ヘッダーと段落要素をルート要素に追加
    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // タグ付きPDFドキュメントを保存
    document.Save("C:\\Samples\\TaggedPDF\\Sample1.pdf");
}
```
フォローするドキュメントが作成されます:

![タグ付きPDFドキュメント、2つの要素を含む - ヘッダーとパラグラフ](taggedpdf-01.png)

## タグ付きPDFにネストされた要素を作成する（構造要素ツリーの作成）

場合によっては、より複雑な構造を作成する必要があります。例えば、パラグラフに引用を配置します。
構造要素ツリーを作成するには、[AppendChild](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild) メソッドを使用する必要があります。
次のコードスニペットは、タグ付きPDFドキュメントの構造要素ツリーを作成する方法を示しています:

```csharp
private static void CreateTaggedPdfDocument02()
{
    // PDFドキュメントを作成
    var document = new Document();

    // TaggedPdfで作業するためのコンテンツを取得
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // ドキュメントのタイトルと言語を設定
    taggedContent.SetTitle("タグ付きPDFドキュメント");
    taggedContent.SetLanguage("en-US");

    HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("ヘッダーレベル1");

    ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = FontRepository.FindFont("Calibri");
    // Adjust position
    paragraphWithQuotes.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
    {
        Margin = new Aspose.Pdf.MarginInfo(10, 5, 10, 5)
    });

    SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
    QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
    SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // タグ付きPDFドキュメントを保存
    document.Save("C:\\Samples\\TaggedPDF\\Sample2.pdf");
}
```
作成後のドキュメントは次のようになります:
![タグ付きPDFドキュメントにネストされた要素 - spanと引用符](taggedpdf-02.png)

## テキスト構造のスタイリング

タグ付きPDFドキュメントのテキスト構造をスタイルするために、Aspose.PDFは[StructureTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate)クラスの[Font](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font)、[FontSize](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize)、[FontStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle)、および[ForegroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor)プロパティを提供しています。次のコードスニペットは、タグ付きPDFドキュメントのテキスト構造をスタイルする方法を示しています:

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdfドキュメントを作成する
Document document = new Document();

// タグ付きPdfで作業するコンテンツを取得する
ITaggedContent taggedContent = document.TaggedContent;

// ドキュメントのタイトルと言語を設定する
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

ParagraphElement p = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(p);

// 開発中
p.StructureTextState.FontSize = 18F;
p.StructureTextState.ForegroundColor = Color.Red;
p.StructureTextState.FontStyle = FontStyles.Italic;

p.SetText("Red italic text.");

// タグ付きPdfドキュメントを保存する
document.Save(dataDir + "StyleTextStructure.pdf");
```
## 構造要素の説明

タグ付きPDFドキュメントの構造要素を説明するために、Aspose.PDFは[IllustrationElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement)クラスを提供しています。次のコードスニペットは、タグ付きPDFドキュメントで構造要素を説明する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdfドキュメントを作成する
Document document = new Document();

// TaggedPdfで作業するためのコンテンツを取得
ITaggedContent taggedContent = document.TaggedContent;

// ドキュメントのタイトルと言語を設定
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// 開発中
IllustrationElement figure1 = taggedContent.CreateFigureElement();
taggedContent.RootElement.AppendChild(figure1);
figure1.AlternativeText = "Figure One";
figure1.Title = "Image 1";
figure1.SetTag("Fig1");
figure1.SetImage("image.png");

// Tagged Pdfドキュメントを保存
document.Save(dataDir + "IllustrationStructureElements.pdf");

```

## タグ付きPDFの検証

Aspose.PDF for .NETは、PDF/UA タグ付きPDFドキュメントの検証機能を提供します。PDF/UA標準の検証は以下をサポートします:

- XObjectsのチェック
- アクションのチェック
- オプショナルコンテンツのチェック
- 埋め込みファイルのチェック
- Acroformフィールドのチェック（自然言語と代替名、デジタル署名の検証）
- XFAフォームフィールドのチェック
- セキュリティ設定のチェック
- ナビゲーションのチェック
- アノテーションのチェック

以下のコードスニペットは、タグ付きPDFドキュメントを検証する方法を示しています。対応する問題はXMLログレポートに表示されます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inputFileName = dataDir + "StructureElements.pdf";
string outputLogName = dataDir + "ua-20.xml";

using (var document = new Aspose.Pdf.Document(inputFileName))
{
    bool isValid = document.Validate(outputLogName, Aspose.Pdf.PdfFormat.PDF_UA_1);

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
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
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

