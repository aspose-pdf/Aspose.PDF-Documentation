---
title: C#を使用して図形注釈を追加する
linktitle: 図形注釈
type: docs
weight: 30
url: /ja/net/figures-annotation/
description: この記事では、Aspose.PDF for .NETを使用してPDFドキュメントから図形注釈を追加、取得、削除する方法について説明します。
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用して図形注釈を追加する",
    "alternativeHeadline": "PDFに図形注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, 図形注釈, 多角形注釈, 線注釈, 正方形注釈, 円注釈",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFドキュメントから図形注釈を追加、取得、削除する方法について説明します。"
}
</script>

PDFドキュメント管理アプリは、ドキュメントに注釈を付けるためのさまざまなツールを提供します。PDFの内部構造の観点からこれらのツールは注釈です。次の種類の描画ツールをサポートしています。

* Line Annotation - 線と矢印を描画するためのツール
* Square Annotation - 四角と長方形を描画するためのツール
* Circle Annotation - 楕円と円を描画するためのツール
* FreeText Annotation - コールアウトコメントのためのツール
* Polygon Annotation - 多角形と雲形を描画するためのツール
* Polyline Annotation - 連結された線を描画するためのツール

## ページに形と図形を追加する

注釈を追加するアプローチは、どれも典型的です。

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)を利用してPDFファイルをロードするか新規作成する。
1. 新しい注釈を作成し、パラメータを設定する（新しいRectangle、新しいPoint、タイトル、色、幅など）。
1. リンクポップアップアノテーションを元のものと関連付けます。
1. ページに注釈を追加します。

## 線または矢印の追加

線の注釈の目的は、ページ上に直線または矢印を表示することです。
線を作成するために、新しいLineAnnotationオブジェクトが必要です。
LineAnnotationクラスのコンストラクタは四つのパラメータを取ります：

* 注釈が追加されるページ、
* 注釈の境界を定義する矩形、
* 線の開始と終了を定義する二つの点。

また、いくつかのプロパティを初期化する必要があります：

* `Title` - 通常は、このコメントを作成したユーザーの名前です
* `Subject` - 任意の文字列にできますが、一般的には注釈の名前です

線をスタイルするために、色、幅、開始スタイル、終了スタイルを設定する必要があります。
私たちのラインをスタイリングするためには、色、幅、開始スタイル、および終了スタイルを設定する必要があります。

次のコードスニペットは、PDFファイルに線注釈を追加する方法を示しています：

```csharp
// PDFファイルをロードする
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// 線注釈を作成する
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// ページに注釈を追加する
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## 四角または円の追加

[四角](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) と [円](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) の注釈は、ページ上に長方形または楕円を表示します。
[Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) と [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) 注釈は、ページに四角形または楕円を表示します。

### 円注釈の追加

新しい円または楕円注釈を描画するには、新しい CircleAnnotation オブジェクトを作成する必要があります。`CircleAnnotation` クラスのコンストラクタは以下の二つのパラメータを取ります：

* 注釈が追加されるページ，
* 注釈の境界を定義する矩形

また、`CircleAnnotation` オブジェクトのいくつかのプロパティを設定できます。これらのプロパティは、PDFビューアでの注釈の見た目と振る舞いを制御します。ここで、そして Square でさらに `InteriorColor` 色は塗りつぶし色、`Color` は境界色です。

### 四角注釈の追加

四角を描画することは、円を描画することと同じです。
長方形を描くことは、円を描くことと同じです。

```csharp
var dataDir = "<path-to-file>";
// PDFファイルを読み込む
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// 円のアノテーションを作成
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Circle",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// 四角のアノテーションを作成
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Rectangle",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// ページにアノテーションを追加
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
例として、PDFドキュメントにSquareとCircleの注釈を追加した結果を以下に示します：

![Circle and Square Annotation demo](circle_demo.png)

## ポリゴンとポリラインの注釈を追加する

Poly-ツールを使用して、ドキュメント上に任意の数の側面を持つ形状と輪郭を作成できます。

**ポリゴン注釈**はページ上のポリゴンを表します。任意の数の頂点が直線で接続されています。
**ポリライン注釈**もポリゴンに似ていますが、最初と最後の頂点が暗黙的に接続されていない点が異なります。

### ポリゴン注釈の追加

PolygonAnnotationはポリゴン注釈を担当します。PolygonAnnotationクラスのコンストラクタは三つのパラメータを取ります：

* 注釈が追加されるページ、
* 注釈の境界を定義する矩形、
* ポリゴンの頂点を定義する点の配列。

`Color`と`InteriorColor`はそれぞれ境界線と塗りつぶしの色に使用されます。

### ポリライン注釈の追加
### ポリライン注釈の追加

PolygonAnnotationは、ポリゴン注釈を担当します。PolygonAnnotationクラスのコンストラクタは3つのパラメータを取ります：

* 注釈が追加されるページ、
* 注釈の境界を定義する矩形、
* ポリゴンの頂点を定義する点の配列。

`PolygonAnnotation`ではこの形状を塗りつぶすことができませんので、`InteriorColor`を使用する必要はありません。

次のコードスニペットは、PDFファイルにポリゴンとポリライン注釈を追加する方法を示しています：

```csharp
// PDFファイルをロード
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// ポリゴン注釈を作成
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// ポリライン注釈を作成
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// ページに注釈を追加
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## 図形の取得

すべての注釈は`Annotations`コレクションに保存されます。どの注釈も`AnnotationType`プロパティを通じてそのタイプを示すことができます。したがって、望ましい注釈をフィルタリングするためにLINQクエリを作成することができます。

### 線の注釈の取得

以下の例は、PDFドキュメントの最初のページからすべての線の注釈を取得する方法を説明しています。

```csharp
// PDFファイルをロード
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### 円の注釈の取得

以下の例は、PDFドキュメントの最初のページからすべてのポリライン注釈を取得する方法を説明しています。

```csharp
// PDFファイルをロード
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### 四角注釈の取得

以下の例は、PDFドキュメントの最初のページからすべての四角注釈を取得する方法を説明しています。

```csharp
// PDFファイルを読み込む
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### 折れ線注釈の取得

以下の例は、PDFドキュメントの最初のページからすべての折れ線注釈を取得する方法を説明しています。

```csharp
// PDFファイルを読み込む
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### 多角形注釈の取得
以下の例は、PDFドキュメントの最初のページからすべてのポリゴンアノテーションを取得する方法を説明しています。

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## 図形の削除

PDFからアノテーションを削除する方法は非常にシンプルです：

* 削除するアノテーションを選択（いくつかのコレクションを作成）
* コレクションをforeachループを使用して反復処理し、Deleteメソッドを使用してアノテーションコレクションから各アノテーションを削除します。

### 線のアノテーションの削除

```csharp
// PDFファイルを読み込む
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### 円と四角の注釈を削除

```csharp
// PDFファイルを読み込む
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### 多角形と折れ線の注釈を削除

PDFファイルから多角形と折れ線の注釈を削除する方法を示すコードスニペットです。

```csharp
// PDFファイルを読み込む
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## PDFファイルにインク注釈を追加する方法

インク注釈は、一つまたは複数の非連続パスで構成される自由形式の「落書き」を表します。開かれたとき、関連するノートのテキストを含むポップアップウィンドウが表示される必要があります。

[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) は、一つまたは複数の非連続点で構成される自由形式の落書きを表します。以下のコードスニペットを使用してPDFドキュメントにInkAnnotationを追加してみてください。

```csharp
// PDFファイルをロードする
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// 出力ファイルを保存する
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### InkAnnotationの線幅を設定する

[InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) の線幅は、LineInfoおよびBorderオブジェクトを使用して変更できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 文書ディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "テスト";
a1.Title = "タイトル";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// 出力ファイルを保存する
doc.Save(dataDir);
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
### 円注釈を削除

次のコードスニペットは、PDFファイルから円注釈を削除する方法を示しています。

```csharp
public static void DeleteCircleAnnotation()
{
    // PDFファイルを読み込む
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
