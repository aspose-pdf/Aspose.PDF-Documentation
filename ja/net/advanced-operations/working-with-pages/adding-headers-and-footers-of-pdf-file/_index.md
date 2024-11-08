---
title: PDFにヘッダーとフッターを追加
linktitle: PDFにヘッダーとフッターを追加
type: docs
weight: 70
url: /ja/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NETを使用して、TextStampクラスを使用してPDFファイルにヘッダーとフッターを追加できます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFにヘッダーとフッターを追加",
    "alternativeHeadline": "PDFファイルにヘッダーとフッターを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, ヘッダー追加, PDFにフッター追加",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用して、TextStampクラスを使用してPDFファイルにヘッダーとフッターを追加できます。"
}
</script>
**Aspose.PDF for .NET** では、既存のPDFファイルにヘッダーとフッターを追加することができます。PDFドキュメントに画像やテキストを追加することもできます。また、C#を使用して1つのPDFファイルに異なるヘッダーを追加することも試みてください。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリとも動作します。

## PDFファイルのヘッダーにテキストを追加

[TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) クラスを使用して、PDFファイルのヘッダーにテキストを追加できます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーにテキストを追加するには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、PDFのヘッダーにテキストを追加するためにPageのAddStampメソッドを呼び出すことができます。

TopMarginプロパティを設定して、PDFのヘッダーエリアにテキストが調整されるようにする必要があります。また、HorizontalAlignmentをCenter、VerticalAlignmentをTopに設定する必要があります。

次のコードスニペットは、C#を使用してPDFファイルのヘッダーにテキストを追加する方法を示しています。
以下のコードスニペットは、C#を使用してPDFファイルのヘッダーにテキストを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// ヘッダーを作成
TextStamp textStamp = new TextStamp("ヘッダーテキスト");
// スタンプのプロパティを設定
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// すべてのページにヘッダーを追加
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## PDFファイルのフッターにテキストを追加する

PDFファイルのフッターにテキストを追加するには、TextStampクラスを使用できます。
TextStamp クラスを使用して、PDFファイルのフッターにテキストを追加できます。

{{% alert color="primary" %}}

PDFのフッターエリアにテキストを調整するように、Bottom Margin プロパティを設定する必要があります。また、HorizontalAlignment を Center に、VerticalAlignment を Bottom に設定する必要があります。

{{% /alert %}}

以下のコードスニペットは、C#を使用してPDFファイルのフッターにテキストを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// フッターを作成
TextStamp textStamp = new TextStamp("Footer Text");
// スタンプのプロパティを設定
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// すべてのページにフッターを追加
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// 出力ファイルを保存
doc.Save(dataDir + "TextinFooter_out.pdf");
```
## PDFファイルのヘッダーに画像を追加

[ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) クラスを使用して、PDFファイルのヘッダーに画像を追加できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォント色など、画像ベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PDFのヘッダーに画像を追加するために、Pageの[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)メソッドを呼び出すことができます。

{{% alert color="primary" %}}
TopMarginプロパティを設定する必要があります。これにより、PDFのヘッダーエリアに画像が調整されます。また、HorizontalAlignmentをCenter、VerticalAlignmentをTopに設定する必要があります。
{{% /alert %}}

以下のコードスニペットは、C#を使用してPDFファイルのヘッダーに画像を追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// ヘッダーを作成
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// スタンプのプロパティを設定
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// すべてのページにヘッダーを追加
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// 出力ファイルを保存
pdfDocument.Save(dataDir + "ImageinHeader_out.pdf");
```
## PDFファイルのフッターに画像を追加する

PDFファイルのフッターに画像を追加するには、Image Stampクラスを使用できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、画像ベースのスタンプを作成するために必要なプロパティを提供します。フッターに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、ページのAddStampメソッドを呼び出して、PDFのフッターに画像を追加できます。

{{% alert color="primary" %}}

[BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) プロパティを設定して、画像がPDFのフッターエリアに合うように調整する必要があります。また、[HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) を `Center` に、[VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) を `Bottom` に設定する必要があります。

{{% /alert %}}

以下のコードスニペットは、C#でPDFファイルのフッターに画像を追加する方法を示しています。
次のコードスニペットは、C#を使用してPDFファイルのフッターに画像を追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ImageInFooter.pdf");
// フッターを作成
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
// スタンプのプロパティを設定
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// すべてのページにフッターを追加
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// 出力ファイルを保存
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## PDFファイルで異なるヘッダーを追加する

ドキュメントのヘッダー/フッターセクションにTextStampを追加する場合、TopMarginやBottomMarginプロパティを使用しますが、単一のPDFドキュメントに複数のヘッダー/フッターを追加する必要がある場合もあります。
ヘッダー/フッターセクションにTextStampを追加するには、TopMarginまたはBottomMarginプロパティを使用しますが、時には1つのPDFドキュメントに複数のヘッダー/フッターを追加する必要がある場合があります。

この要件を達成するために、個々のTextStampオブジェクト（オブジェクトの数は必要なヘッダー/フッターの数に依存します）を作成し、PDFドキュメントに追加します。また、個々のスタンプオブジェクトに対して異なる書式情報を指定することもできます。次の例では、Documentオブジェクトと3つのTextStampオブジェクトを作成し、PDFのヘッダーセクションにテキストを追加するためにPageの[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)メソッドを使用しました。次のコードスニペットは、Aspose.PDF for .NETを使用してPDFファイルのフッターに画像を追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ソースドキュメントを開く
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// 三つのスタンプを作成する
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Header 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Header 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Header 3");

// スタンプの配置を設定（ページの上部、水平方向に中央）
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// フォントスタイルをBoldとして指定
stamp1.TextState.FontStyle = FontStyles.Bold;
// テキストの前景色情報を赤として設定
stamp1.TextState.ForegroundColor = Color.Red;
// フォントサイズを14として指定
stamp1.TextState.FontSize = 14;

// 2番目のスタンプオブジェクトの垂直配置をTopとして設定する必要がある
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// スタンプの水平配置情報を中央揃えとして設定
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// スタンプオブジェクトのズームファクターを設定
stamp2.Zoom = 10;

// 3番目のスタンプオブジェクトの書式を設定
// スタンプオブジェクトの垂直配置情報をTOPとして指定
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// スタンプオブジェクトの水平配置情報を中央揃えとして設定
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// スタンプオブジェクトの回転角度を設定
stamp3.RotateAngle = 35;
// スタンプの背景色としてピンクを設定
stamp3.TextState.BackgroundColor = Color.Pink;
// スタンプのフォントフェイス情報をVerdanaに変更
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// 最初のスタンプは最初のページに追加される;
doc.Pages[1].AddStamp(stamp1);
// 二番目のスタンプは二ページ目に追加される;
doc.Pages[2].AddStamp(stamp2);
// 三番目のスタンプは三ページ目に追加される。
doc.Pages[3].AddStamp(stamp3);
// 更新されたドキュメントを保存する
doc.Save(dataDir + "MultiHeader_out.pdf");
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

