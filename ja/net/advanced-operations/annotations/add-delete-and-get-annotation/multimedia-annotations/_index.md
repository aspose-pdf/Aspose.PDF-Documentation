---
title: C#を使用したPDFマルチメディア注釈
linktitle: マルチメディア注釈
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/multimedia-annotation/
description: Aspose.PDF for .NETは、PDFドキュメントにマルチメディア注釈を追加、取得、削除することを可能にします。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Multimedia Annotation using C#",
    "alternativeHeadline": "Enable Multimedia Annotations in PDF with C#",
    "abstract": "Aspose.PDF for .NETは、ユーザーがPDFドキュメントにさまざまなマルチメディアタイプをシームレスに追加、取得、削除できる高度なマルチメディア注釈機能を導入します。この機能は、画面、音声、リッチメディア注釈をサポートし、ドキュメントのインタラクティビティを向上させ、外部ビデオコンテンツ、音声ノート、埋め込みメディアの統合を可能にし、PDFドキュメントをよりダイナミックで魅力的にします。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF multimedia annotation, Aspose.PDF, C# PDF features, screen annotation, sound annotation, rich media annotation, widget annotations, 3D annotation, document navigation, multimedia file embedding",
    "wordcount": "2247",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

PDFドキュメントの注釈は、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトのAnnotationsコレクションに含まれています。このコレクションには、その個々のページのすべての注釈が含まれています：各ページには独自のAnnotationsコレクションがあります。特定のページに注釈を追加するには、そのページのAnnotationsコレクションにAddメソッドを使用して追加します。

PDFドキュメントにSWFファイルを注釈として含めるには、Aspose.PDF.InteractiveFeatures.Annotations名前空間の[ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation)クラスを使用します。画面注釈は、メディアクリップが再生されるページの領域を指定します。

PDFドキュメントに外部ビデオリンクを追加する必要がある場合は、[MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation)を使用できます。
ムービー注釈には、コンピュータの画面とスピーカーで表示されるアニメーショングラフィックスと音声が含まれます。

[Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation)は、テキスト注釈に類似していますが、テキストノートの代わりにコンピュータのマイクから録音された音声またはファイルからインポートされた音声が含まれています。注釈がアクティブになると、音声が再生されます。注釈は、ほとんどの点でテキスト注釈のように振る舞い、音声を表すことを示すために異なるアイコン（デフォルトではスピーカー）を持ちます。

ただし、PDFドキュメント内にメディアを埋め込む必要がある場合は、[RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation)を使用する必要があります。

RichMediaAnnotationクラスの以下のメソッド/プロパティを使用できます。

- Stream CustomPlayer { set; }: ビデオを再生するために使用されるプレーヤーを設定できます。
- string CustomFlashVariables { set; }: フラッシュアプリケーションに渡される変数を設定できます。この行は、「key=value」ペアのセットで、‘&’で区切られています。
- void AddCustomData(strig name, Stream data): プレーヤー用の追加データを追加します。例えば、source=video.mp4&autoPlay=true&scale=100。
- ActivationEvent ActivateOn { get; set}: プレーヤーをアクティブにするイベント；可能な値はClick、PageOpen、PageVisibleです。
- void SetContent(Stream stream, string name): 再生されるビデオ/音声データを設定します。
- void Update(): 注釈のデータ構造を作成します。このメソッドは最後に呼び出す必要があります。
- void SetPoster(Stream): プレーヤーがアクティブでないときに表示される画像、すなわちビデオのポスターを設定します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも機能します。

## 画面注釈を追加

以下のコードスニペットは、PDFファイルに画面注釈を追加する方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddScreenAnnotationWithMedia()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (cument = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Path to the media file (SWF)
        var mediaFile = dataDir + "input.swf";

        // Create Screen Annotation
        var screenAnnotation = new Aspose.Pdf.Annotations.ScreenAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(170, 190, 470, 380),
            mediaFile);

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(screenAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddScreenAnnotationWithMedia_out.pdf");
    }
}
```

## 音声注釈を追加

以下のコードスニペットは、PDFファイルに音声注釈を追加する方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSoundAnnotation()
{
    // Open PDF document
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        var mediaFile = dataDir + "file_example_WAV_1MG.wav";

        // Create Sound Annotation
        var soundAnnotation = new Aspose.Pdf.Annotations.SoundAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(20, 700, 60, 740),
            mediaFile)
        {
            Color = Aspose.Pdf.Color.Blue,
            Title = "John Smith",
            Subject = "Sound Annotation demo",
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(20, 700, 60, 740))
        };

        document.Pages[1].Annotations.Add(soundAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddSoundAnnotation_out.pdf");
    }
}
```

## RichMediaAnnotationを追加

以下のコードスニペットは、PDFファイルにRichMediaAnnotationを追加する方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRichMediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
        Page page = document.Pages.Add();

        // Define video and poster names
        const string videoName = "file_example_MP4_480_1_5MG.mp4";
        const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        string skinName = "SkinOverAllNoFullNoCaption.swf";

        // Create RichMediaAnnotation
        var rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600));

        // Specify the stream containing the video player code
        rma.CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp, "Players", "Videoplayer.swf"), FileMode.Open, FileAccess.Read);

        // Compose flash variables line for the player
        rma.CustomFlashVariables = $"source={videoName}&skin={skinName}";

        // Add skin code
        rma.AddCustomData(skinName, new FileStream(Path.Combine(pathToAdobeApp, skinName), FileMode.Open, FileAccess.Read));

        // Set poster for the video
        rma.SetPoster(new FileStream(Path.Combine(dataDir, posterName), FileMode.Open, FileAccess.Read));

        // Set video content
        using (Stream fs = new FileStream(Path.Combine(dataDir, videoName), FileMode.Open, FileAccess.Read))
        {
            rma.SetContent(videoName, fs);
        }

        // Set type of the content (video)
        rma.Type = RichMediaAnnotation.ContentType.Video;

        // Activate player by click
        rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

        // Update annotation data
        rma.Update();

        // Add annotation to the page
        page.Annotations.Add(rma);

        // Save PDF document
        document.Save(dataDir + "RichMediaAnnotation_out.pdf");
    }
}
```

### マルチメディア注釈を取得

以下のコードスニペットを使用して、PDFドキュメントからマルチメディア注釈を取得してみてください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMultimediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get multimedia annotations (Screen, Sound, RichMedia)
        var mediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Screen
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Sound
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.Annotation>();

        // Iterate through the annotations and print their details
        foreach (var ma in mediaAnnotations)
        {
            Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
        }
    }
}
```

### マルチメディア注釈を削除

以下のコードスニペットは、PDFファイルからマルチメディア注釈を削除する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolyAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get RichMedia annotations
        var richMediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.RichMediaAnnotation>();

        // Delete each RichMedia annotation
        foreach (var rma in richMediaAnnotations)
        {
            document.Pages[1].Annotations.Delete(rma);
        }

        // Save PDF document
        document.Save(dataDir + "DeletePolyAnnotation_out.pdf");
    }
}
```

## ウィジェット注釈を追加

インタラクティブフォームは、[Widget Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation)を使用してフィールドの外観を表現し、ユーザーのインタラクションを管理します。
これらのフォーム要素をPDFに追加して、情報の入力、送信、または他のユーザーインタラクションを容易にします。

ウィジェット注釈は、特定のページ上のフォームフィールドのグラフィカルな表現であるため、注釈として直接作成することはできません。

各ウィジェット注釈は、そのタイプに応じた適切なグラフィックス（外観）を持ちます。作成後、ボーダースタイルや背景色など、特定の視覚的側面を変更できます。
テキストカラーやフォントなどの他のプロパティは、フィールドに添付されると変更できます。

場合によっては、フィールドが複数のページに表示され、同じ値を繰り返すことを望むことがあります。その場合、通常は1つのウィジェットしか持たないフィールドに複数のウィジェットが添付されることがあります：TextField、ListBox、ComboBox、CheckBoxは通常1つだけですが、RadioGroupは各ラジオボタンに対して複数のウィジェットを持ちます。
フォームに記入する人は、これらのウィジェットのいずれかを使用してフィールドの値を更新でき、これは他のすべてのウィジェットにも反映されます。

ドキュメント内の各場所の各フォームフィールドは、1つのウィジェット注釈を表します。ウィジェット注釈の位置特有のデータは、特定のページに追加されます。各フォームフィールドにはいくつかのバリエーションがあります。ボタンはラジオボタン、チェックボックス、またはプッシュボタンである可能性があります。選択ウィジェットはリストボックスまたはコンボボックスである可能性があります。

このサンプルでは、ドキュメント内のナビゲーション用のプッシュボタンを追加する方法を学びます。

### ドキュメントにボタンを追加

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPrintButton()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Define the rectangle for the button
        var rect = new Aspose.Pdf.Rectangle(72, 748, 164, 768);

        // Create a button field
        var printButton = new Aspose.Pdf.Forms.ButtonField(page, rect)
        {
            AlternateName = "Print current document",
            Color = Aspose.Pdf.Color.Black,
            PartialName = "printBtn1",
            NormalCaption = "Print Document"
        };

        // Set the border style for the button
        var border = new Aspose.Pdf.Annotations.Border(printButton)
        {
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
            Width = 2
        };
        printButton.Border = border;

        // Set the border and background color characteristics
        printButton.Characteristics.Border = System.Drawing.Color.FromArgb(255, 0, 0, 255);
        printButton.Characteristics.Background = System.Drawing.Color.FromArgb(255, 0, 191, 255);

        // Add the button to the form
        document.Form.Add(printButton);

        // Save PDF document
        document.Save(dataDir + "PrintButton_out.pdf");
    }
}
```

このボタンにはボーダーがあり、背景が設定されています。また、ボタン名（Name）、ツールチップ（AlternateName）、ラベル（NormalCaption）、およびラベルテキストの色（Color）を設定します。

### ドキュメントナビゲーションアクションの使用

ウィジェット注釈の使用のより複雑な例が存在します - PDFドキュメント内のドキュメントナビゲーションです。これはPDFドキュメントプレゼンテーションを準備するために必要になることがあります。

この例では、4つのボタンを作成する方法を示します：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNavigationButtons()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "JSON Fundamenals.pdf"))
    {
        // Create an array of button fields
        var buttons = new Aspose.Pdf.Forms.ButtonField[4];

        // Define alternate names and normal captions for the buttons
        var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
        var normalCaptions = new[] { "First", "Prev", "Next", "Last" };

        // Define predefined actions for the buttons
        PredefinedAction[] actions = {
            PredefinedAction.FirstPage,
            PredefinedAction.PrevPage,
            PredefinedAction.NextPage,
            PredefinedAction.LastPage
        };

        // Define border and background colors
        var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
        var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);

        // We should create the buttons without attaching them to the page.
        for (var i = 0; i < 4; i++)
        {
            buttons[i] = new Aspose.Pdf.Forms.ButtonField(document, new Aspose.Pdf.Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
            {
                AlternateName = alternateNames[i],
                Color = Aspose.Pdf.Color.White,
                NormalCaption = normalCaptions[i],
                OnActivated = new Aspose.Pdf.Annotations.NamedAction(actions[i])
            };

            // Set the border style for the button
            buttons[i].Border = new Aspose.Pdf.Annotations.Border(buttons[i])
            {
                Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
                Width = 2
            };

            // Set the border and background color characteristics
            buttons[i].Characteristics.Border = clrBorder;
            buttons[i].Characteristics.Background = clrBackGround;
        }

        // Duplicate the array of buttons on each page in the document
        for (var pageIndex = 1; pageIndex <= document.Pages.Count; pageIndex++)
        {
            for (var i = 0; i < 4; i++)
            {
                document.Form.Add(buttons[i], $"btn{pageIndex}_{i + 1}", pageIndex);
            }
        }

        // Save PDF document
        document.Save(dataDir + "NavigationButtons_out.pdf");

        // We call Form.Add method with the following parameters: field, name, and the index of the pages that this field will be added to.
        // And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

        document.Form["btn1_1"].ReadOnly = true;
        document.Form["btn1_2"].ReadOnly = true;

        document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
        document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
    }
}
```

この機能の詳細情報と可能性については、[フォームの操作](/pdf/ja/net/acroforms/)も参照してください。

PDFドキュメントでは、3D CADまたは3Dモデリングソフトウェアで作成された高品質の3Dコンテンツを表示および管理でき、PDFドキュメントに埋め込まれています。3D要素をすべての方向に回転させることができ、まるで手に持っているかのように操作できます。

なぜ3D画像の表示が必要なのでしょうか？

過去数年間、技術は3D印刷のおかげであらゆる分野で大きな進歩を遂げました。3D印刷技術は、建設、機械工学、デザインの技術スキルを教えるための主要なツールとして適用できます。これらの技術は、個人印刷デバイスの出現のおかげで、教育プロセスの新しい形態の導入、動機の向上、卒業生と教師の必要な能力の形成に寄与することができます。

3Dモデリングの主な目的は、未来のオブジェクトや物体のアイデアです。なぜなら、オブジェクトをリリースするためには、その設計の特徴をすべて詳細に理解する必要があるからです。これは、工業デザインや建築における連続的な再生のためです。

## 3D注釈を追加

3D注釈は、U3D形式で作成されたモデルを使用して追加されます。

1. 新しい[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)を作成します。
1. 必要な3Dモデル（この場合は「Ring.u3d」）のデータを読み込み、[PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)を作成します。
1. [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork)オブジェクトを作成し、ドキュメントと3DContentにリンクします。
1. pdf3dArtWorkオブジェクトを調整します：

    - 3DLightingScheme - （例では`CAD`を設定します）
    - 3DRenderMode - （例では`Solid`を設定します）
    - Fill `ViewArray`、少なくとも1つの[3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview)を作成し、配列に追加します。

1. 注釈の3つの基本パラメータを設定します：
    - 注釈が配置される`page`。
    - 注釈が配置される`rectangle`。
    - `3dArtWork`オブジェクト。
1. 3Dオブジェクトのより良いプレゼンテーションのために、ボーダーフレームを設定します。
1. デフォルトビューを設定します（例 - TOP）。
1. 追加のパラメータを設定します：名前、プレビューのポスターなど。
1. [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)に注釈を追加します。
1. 結果を保存します。

### 例

以下のコードスニペットを確認して、3D注釈を追加します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Add3dAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Load 3D content
        var pdf3DContent = new Aspose.Pdf.Annotations.PDF3DContent(dataDir + "Ring.u3d");

        // Create 3D artwork
        var pdf3dArtWork = new Aspose.Pdf.Annotations.PDF3DArtwork(document, pdf3DContent)
        {
            LightingScheme = new Aspose.Pdf.Annotations.PDF3DLightingScheme(Aspose.Pdf.Annotations.LightingSchemeType.CAD),
            RenderMode = new Aspose.Pdf.Annotations.PDF3DRenderMode(Aspose.Pdf.Annotations.RenderModeType.Solid),
        };

        // Define matrices for different views
        var topMatrix = new Aspose.Pdf.Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Aspose.Pdf.Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);

        // Add views to the 3D artwork
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        // Add page
        var page = document.Pages.Add();

        // Create a 3D annotation
        var pdf3dAnnotation = new Aspose.Pdf.Annotations.PDF3DAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.Border = new Aspose.Pdf.Annotations.Border(pdf3dAnnotation);
        pdf3dAnnotation.SetDefaultViewIndex(1);
        pdf3dAnnotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.NoZoom;
        pdf3dAnnotation.Name = "Ring.u3d";

        // Set preview image if needed
        // pdf3dAnnotation.SetImagePreview(dataDir + "sample_3d.png");

        // Add the 3D annotation to the page
        document.Pages[1].Annotations.Add(pdf3dAnnotation);

        // Save PDF document
        document.Save(dataDir + "Add3dAnnotation_out.pdf");
    }
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