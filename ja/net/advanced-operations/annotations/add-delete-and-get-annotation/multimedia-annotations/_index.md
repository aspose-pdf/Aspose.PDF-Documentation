---
title: C#を使用したPDFマルチメディア注釈
linktitle: マルチメディア注釈
type: docs
weight: 40
url: ja/net/multimedia-annotation/
description: Aspose.PDF for .NETを使用すると、PDFドキュメントからマルチメディア注釈を追加、取得、削除することができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用したPDFマルチメディア注釈",
    "alternativeHeadline": "PDFにマルチメディア注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, c#, マルチメディア注釈, スクリーン注釈, サウンド注釈, ウィジェット注釈, 3D注釈",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用すると、PDFドキュメントからマルチメディア注釈を追加、取得、削除することができます。"
}
</script>
PDFドキュメント内の注釈は、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトのAnnotationsコレクションに含まれています。このコレクションには、その個別ページのすべての注釈が含まれています。各ページには独自のAnnotationsコレクションがあります。特定のページに注釈を追加するには、そのページのAnnotationsコレクションにAddメソッドを使用して追加します。

Aspose.PDF.InteractiveFeatures.Annotations名前空間の[ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation)クラスを使用して、PDFドキュメントにSWFファイルを注釈として含めることができます。スクリーン注釈は、メディアクリップが再生されるページ上の領域を指定します。

PDFドキュメントに外部ビデオリンクを追加する必要がある場合は、[MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation)を使用できます。ムービー注釈には、コンピュータ画面とスピーカーを通じて提示されるアニメーショングラフィックとサウンドが含まれています。

[Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation)は、テキスト注釈と類似していますが、テキストノートの代わりに、コンピュータのマイクから録音された音声またはファイルからインポートされた音声が含まれています。
[音声アノテーション](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation)は、テキストメモの代わりにコンピュータのマイクから録音された音声またはファイルからインポートされた音声を含む点で、テキストアノテーションと類似しています。

しかし、PDFドキュメント内にメディアを埋め込む必要がある場合は、[RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation)を使用する必要があります。

以下のRichMediaAnnotationクラスのメソッド/プロパティを使用できます。

- Stream CustomPlayer { set; }: ビデオを再生するためのプレーヤーを設定します。
- string CustomFlashVariables { set; }: フラッシュアプリケーションに渡される変数を設定します。この行は「key=value」のペアであり、'&'で区切られます。
- void AddCustomData(strig name, Stream data): プレーヤーの追加データを追加します。例えば source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: プレーヤーがアクティブになるイベント；可能な値はClick, PageOpen, PageVisibleです
- void SetContent(Stream stream, string name): 再生されるビデオ/オーディオデータを設定します。
changefreq: "monthly"
type: docs
- void SetContent(Stream stream, string name): ビデオ/オーディオデータを再生するために設定します。
- void Update(): アノテーションのデータ構造を作成します。このメソッドは最後に呼び出すべきです。
- void SetPoster(Stream): ビデオのポスター、つまりプレイヤーが非アクティブの時に表示される画像を設定します。

以下のコードスニペットは [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも連携して動作します。

## スクリーンアノテーションの追加

以下のコードスニペットは、PDFファイルにスクリーンアノテーションを追加する方法を示しています：

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;


namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // ドキュメントディレクトリへのパス。
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // PDFファイルをロード
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // スクリーンアノテーションを作成
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## 音声注釈の追加

次のコードスニペットは、PDFファイルに音声注釈を追加する方法を示しています：

```csharp
        public static void AddSoundAnnotation()
        {
            // PDFファイルを読み込む
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // 音声注釈を作成する
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "音声注釈デモ",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## RichMediaAnnotationの追加

次のコードスニペットは、PDFファイルにRichMediaAnnotationを追加する方法を示しています：
以下のコードスニペットは、PDFファイルにRichMediaAnnotationを追加する方法を示しています：

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //ビデオデータに名前を付けます。このデータはこの名前でドキュメントに埋め込まれ、この名前でフラッシュ変数から参照されます。
            //videoNameはファイルへのパスを含むべきではありません。これはPDFドキュメント内のデータにアクセスするための「キー」です。
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //ビデオプレーヤーのスキンも使用します
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //ここではビデオプレーヤーのコードを含むストリームを指定する必要があります
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //プレーヤーのフラッシュ変数行を構成します。異なるプレーヤーはフラッシュ変数行の異なるフォーマットを持つ可能性があることに注意してください。使用しているプレーヤーのドキュメントを参照してください。
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //スキンコードを追加します。
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //ビデオのポスターを設定します
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //ビデオコンテンツを設定します
            rma.SetContent(videoName, fs);

            //コンテンツのタイプを設定します（ビデオ）
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //クリックによるプレーヤーの活性化
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //注釈データを更新します。このメソッドは、すべての割り当て/設定の後に呼び出す必要があります。このメソッドは注釈のデータ構造を初期化し、必要なデータを埋め込みます。
            rma.Update();

            //ページに注釈を追加します。
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### マルチメディア注釈の取得

以下のコードスニペットを使用して、PDFドキュメントからマルチメディア注釈を取得してください。

```csharp
        public static void GetMultimediaAnnotation()
        {
            // PDFファイルを読み込む
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### マルチメディア注釈の削除

以下のコードスニペットは、PDFファイルからマルチメディア注釈を削除する方法を示しています。

```csharp
        public static void DeletePolyAnnotation()
        {
            // PDFファイルを読み込む
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## ウィジェット注釈の追加

対話式フォームは、フィールドの外観を表現し、ユーザーの操作を管理するために[ウィジェット注釈](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation)を使用します。
PDFに追加するこれらのフォーム要素を使用して、情報の入力、提出、またはその他のユーザー操作を容易にします。

ウィジェット注釈は特定のページにフォームフィールドのグラフィカルな表現なので、直接注釈として作成することはできません。

各ウィジェット注釈には、そのタイプに応じた適切なグラフィック（外観）があります。作成後、境界線のスタイルや背景色など、特定の視覚的側面を変更できます。
テキストの色やフォントなどの他のプロパティは、フィールドに添付された後に変更できます。

場合によっては、同じ値を繰り返して、複数のページにフィールドを表示させたいことがあります。
場合によっては、同じ値を繰り返して複数のページにフィールドを表示させたいことがあります。
フォームを記入する人は、いずれかのウィジェットを使用してフィールドの値を更新でき、これが他のすべてのウィジェットにも反映されます。

ドキュメントの各場所の各フォームフィールドは、1つのウィジェット注釈を表します。ウィジェット注釈の場所固有のデータは特定のページに追加されます。各フォームフィールドにはいくつかのバリエーションがあります。ボタンはラジオボタン、チェックボックス、またはプッシュボタンにすることができます。選択ウィジェットはリストボックスまたはコンボボックスにすることができます。

このサンプルでは、ドキュメントのナビゲーション用のプッシュボタンを追加する方法を学びます。

### ドキュメントにボタンを追加する

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "現在のドキュメントを印刷する",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "ドキュメントを印刷"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
このボタンには境界線があり、背景が設定されています。また、ボタン名（名前）、ツールチップ（代替名）、ラベル（通常キャプション）、ラベルテキストの色（色）も設定します。

### ドキュメントナビゲーションアクションの使用

ウィジェットアノテーションの使用例がもっと複雑です - PDFドキュメントのドキュメントナビゲーションです。これは、PDFドキュメントプレゼンテーションを準備するために必要になるかもしれません。

この例では、4つのボタンを作成する方法を示しています：

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "先頭のページに移動", "前のページに移動", "次のページに移動", "最後のページに移動" };
var normalCaptions = new[] { "先頭", "前", "次", "最後" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

ページに添付せずにボタンを作成する必要があります。
ページにアタッチせずにボタンを作成する必要があります。

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

このボタンの配列をドキュメントの各ページに複製する必要があります。

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

[Form.Add method](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) を以下のパラメータで呼び出します：field、name、およびこのフィールドが追加されるページのインデックス。
以下のパラメータを持つ [Form.Add メソッド](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) を呼び出します：フィールド、名前、そしてこのフィールドが追加されるページのインデックス。

そして完全な結果を得るために、最初のページの「First」と「Prev」ボタンと、最後のページの「Next」と「Last」ボタンを無効にする必要があります。

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

この機能の詳細な情報と可能性については、[フォームの操作](/pdf/net/acroforms/)も参照してください。

PDFドキュメントでは、3D CADや3Dモデリングソフトウェアで作成された高品質の3Dコンテンツを表示および管理でき、PDFドキュメントに埋め込まれます。手に持っているかのように全方向に3D要素を回転させることができます。

なぜそもそも画像の3D表示が必要なのでしょうか？

過去数年間で、テクノロジーは3Dプリンティングのおかげであらゆる分野で大きな進歩を遂げました。
過去数年間に、技術は3Dプリントのおかげであらゆる分野で大きな進歩を遂げました。

3Dモデリングの主な任務は、将来のオブジェクトや物体のアイデアです。なぜなら、物体を製造するためには、その設計特徴をすべての詳細にわたって理解し、産業設計や建築で次々と再生産することが必要だからです。

## 3Dアノテーションの追加

3Dアノテーションは、U3D形式で作成されたモデルを使用して追加されます。

1. 新しい[ドキュメント](https://reference.aspose.com/pdf/net/aspose.pdf/document)を作成する
1. 望ましい3Dモデルのデータ（この場合は"Ring.u3d"）を読み込んで、[PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)を作成する
1. [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork)オブジェクトを作成して、ドキュメントと3DContentにリンクする
1. pdf3dArtWorkオブジェクトを調整する：

    - 3DLightingScheme - （例では`CAD`を設定します）
    - 3DRenderMode - （例では`Solid`を設定します）
    - `ViewArray`を入力し、少なくとも1つの[3Dビュー](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview)を作成して配列に追加する。
- `ViewArray` を埋め、少なくとも1つの[3Dビュー](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview)を作成して配列に追加してください。

1. アノテーションの3つの基本パラメーターを設定します：
    - アノテーションが配置される `page`、
    - アノテーションが内包される `rectangle`、
    - `3dArtWork` オブジェクト。
1. 3Dオブジェクトのより良いプレゼンテーションのために、枠線を設定します。
1. デフォルトビューを設定します（例 - TOP）
1. 追加のパラメーターをいくつか追加します：名前、プレビューポスターなど。
1. アノテーションを[ページ](https://reference.aspose.com/pdf/net/aspose.pdf/page)に追加します。
1. 結果を保存します。

### 例

以下のコードスニペットを確認して、3Dアノテーションを追加してください。

```csharp
    public static void Add3dAnnotation()
    {
    // PDFファイルをロード
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    //必要に応じてプレビュー画像を設定
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
このコード例は、このようなモデルを示しています：

![3D Annotation demo](3d_demo.png)

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
    "applicationCategory": "PDF操作ライブラリー for .NET",
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

