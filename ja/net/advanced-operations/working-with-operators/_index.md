---
title: オペレーターの使用
linktitle: オペレーターの使用
type: docs
weight: 170
url: /ja/net/operators/
description: Aspose.PDFでオペレーターを使用する方法について説明します。オペレータークラスは、PDF操作のための優れた機能を提供します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "オペレーターの使用",
    "alternativeHeadline": "PDFオペレーターの使用方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdf内のオペレーター, PDFオペレーターの使用",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDFでオペレーターを使用する方法について説明します。オペレータークラスは、PDF操作のための優れた機能を提供します。"
}
</script>

## PDFオペレーターとその使用法の紹介

オペレーターは、ページにグラフィカルな形状を描画するなど、実行されるべきいくつかのアクションを指定するPDFキーワードです。オペレーターキーワードは、初期のソリダス文字（2Fh）がないことで名前付きオブジェクトと区別されます。オペレーターはコンテンツストリーム内でのみ意味を持ちます。

コンテンツストリームは、ページに描画されるグラフィカル要素を記述する指示が含まれているPDFストリームオブジェクトです。PDFオペレーターの詳細については、[PDF仕様](https://opensource.adobe.com/dc-acrobat-sdk-docs/)で見ることができます。

### 実装の詳細

このトピックでは、Aspose.PDFでオペレーターを使用する方法について説明します。
このトピックでは、Aspose.PDFで演算子を使用する方法について説明します。

- **GSave** 演算子は、PDFの現在のグラフィカル状態を保存します。
- **ConcatenateMatrix** （連結行列）演算子は、画像がPDFページにどのように配置されるかを定義するために使用されます。
- **Do** 演算子は、ページ上に画像を描画します。
- **GRestore** 演算子は、グラフィカル状態を復元します。

PDFファイルに画像を追加するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトを作成し、入力PDFドキュメントを開きます。
1. 画像を追加する特定のページを取得します。
1. 画像をページのResourcesコレクションに追加します。
1. 演算子を使用してページに画像を配置します：
   - まず、GSave 演算子を使用して現在のグラフィカル状態を保存します。
   - 次に、ConcatenateMatrix 演算子を使用して画像が配置される位置を指定します。
   - Do 演算子を使用してページに画像を描画します。
1. 最後に、GRestore 演算子を使用して更新されたグラフィカル状態を保存します。

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。
以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリと一緒に使用できます。

以下のコードスニペットは、PDFオペレーターの使用方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// 座標を設定
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// 画像を追加するページを取得
Page page = pdfDocument.Pages[1];
// 画像をストリームにロード
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// ページリソースのイメージコレクションに画像を追加
page.Resources.Images.Add(imageStream);
// GSaveオペレーターを使用：このオペレーターは現在のグラフィックス状態を保存します
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// RectangleとMatrixオブジェクトを作成
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// ConcatenateMatrix（マトリックスの連結）オペレーターを使用：画像がどのように配置されるかを定義
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Doオペレーターを使用：このオペレーターは画像を描画します
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// GRestoreオペレーターを使用：このオペレーターはグラフィックス状態を復元します
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
```
## ページ上にXFormを描画するためのオペレーターの使用

このトピックでは、GSave/GRestoreオペレーター、ContatenateMatrixオペレーターを使用してxFormの位置を指定し、Doオペレーターを使用してページ上にxFormを描画する方法を示します。

以下のコードは、PDFファイルの既存の内容をGSave/GRestoreオペレーターペアでラップします。このアプローチは、既存の内容の最後で初期グラフィックス状態を取得するのに役立ちます。このアプローチがない場合、望ましくない変換が既存のオペレーターチェーンの最後に残る可能性があります。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // サンプルは以下を示しています
    // GSave/GRestoreオペレーターの使用
    // xFormの位置指定にContatenateMatrixオペレーターを使用
    // ページにxFormを描画するためにDoオペレーターを使用

    // 既存の内容をGSave/GRestoreオペレーターペアでラップ
    //        これは既存の内容の最後で初期グラフィックス状態を取得するためです
    //        それ以外の場合、望ましくない変換が既存のオペレーターチェーンの最後に残る可能性があります
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // 新しいコマンドの後でグラフィックス状態を適切にクリアするために、グラフィックス状態の保存オペレータを追加
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region create xForm

    // xFormを作成
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // 画像の幅と高さを定義
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // 画像をストリームに読み込む
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // 画像をXFormリソースの画像コレクションに追加
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Doオペレーターを使用: このオペレーターは画像を描画します
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // x=100 y=500の座標にフォームを配置
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Doオペレーターを使用してフォームを描画
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // x=100 y=300の座標にフォームを配置
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Doオペレーターを使用してフォームを描画
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore();

    // GSaveの後でグラフィックス状態をGRestoreで復元
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## オペレータクラスを使用してグラフィックオブジェクトを削除する

オペレータクラスは、PDF操作に優れた機能を提供します。PDFファイルに[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスの [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) メソッドを使用して削除できないグラフィックが含まれている場合、代わりにオペレータクラスを使用して削除できます。

次のコードスニペットは、グラフィックを削除する方法を示しています。PDFファイルにグラフィックのテキストラベルが含まれている場合、このアプローチを使用すると、PDFファイルにラベルが残る可能性があるため、そのような画像を削除する代替方法としてグラフィックオペレーターを探してください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// 使用されるパスペイントオペレータ
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
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

