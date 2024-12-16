---
title: PDFマルチメディア注釈をC++で使用
linktitle: マルチメディア注釈
type: docs
weight: 40
url: /ja/cpp/multimedia-annotation/
description: Aspose.PDF for C++を使用すると、PDFドキュメントにマルチメディア注釈を追加、取得、削除できます。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

ビデオ、オーディオ、およびインタラクティブなコンテンツを追加することで、PDFが多次元のコミュニケーションツールとなり、ドキュメントへの関心とエンゲージメントが高まります。このようなPDF形式ファイル内のコンテンツは、マルチメディア注釈と呼ばれます。

PDFドキュメントの注釈は、[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)オブジェクトのAnnotationsコレクションに含まれています。このコレクションには、その個々のページに対するすべての注釈が含まれています。各ページは独自のAnnotationsコレクションを持っています。特定のページに注釈を追加するには、そのページのAnnotationsコレクションにAddメソッドを使用して追加します。

代わりに、Aspose.PDF.InteractiveFeatures.Annotations名前空間の[ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation)クラスを使用して、PDFドキュメントにSWFファイルを注釈として含めます。 A screen annotation specifies a region of a page upon which media clips may be played.

PDF ドキュメントに外部ビデオリンクを追加する必要がある場合、[MovieAnnotaiton](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation) を使用できます。ムービー注釈には、コンピュータの画面およびスピーカーを通じて表示されるアニメーション グラフィックとサウンドが含まれています。

[サウンド注釈](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) は、テキストノートの代わりにコンピュータのマイクから録音された音声やファイルからインポートされた音声を含むことを除いて、テキスト注釈に類似しています。注釈がアクティブ化されると、音声が再生されます。注釈はほとんどの点でテキスト注釈のように振る舞いますが、サウンドを表していることを示すために異なるアイコン（デフォルトではスピーカー）が使用されます。

しかし、PDF ドキュメント内にメディアを埋め込む必要がある場合、[RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation) を使用する必要があります。
## スクリーン注釈を追加

次のコードスニペットは、PDF ファイルにスクリーン注釈を追加する方法を示しています：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // PDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // スクリーン注釈を作成
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## サウンド注釈を追加

次のコードスニペットは、PDF ファイルにサウンド注釈を追加する方法を示しています：

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // PDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // サウンド注釈を作成
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Sound Annotation demo");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}

```

## リッチメディアアノテーションを追加する

次のコードスニペットは、PDFファイルにリッチメディアアノテーションを追加する方法を示しています:

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // ビデオデータに名前を付けます。このデータはこの名前でドキュメントに埋め込まれ、
    // この名前でフラッシュ変数から参照されます。
    // videoNameはファイルへのパスを含めるべきではありません。これはむしろPDFドキュメント内の
    // データにアクセスするための「キー」です。

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // また、ビデオプレーヤーのスキンを使用します
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // ここでビデオプレーヤーのコードを含むストリームを指定する必要があります
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // プレーヤーのフラッシュ変数ラインを構成します。異なるプレーヤーが
    // 異なる形式のフラッシュ変数ラインを持つことがあることに注意してください。
    // 自分のプレーヤーのドキュメントを参照してください。
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // スキンコードを追加します。
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // ビデオのポスターを設定します
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // ビデオコンテンツを設定します
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // コンテンツのタイプを設定します（ビデオ）
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // クリックでプレーヤーをアクティブ化
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // アノテーションデータを更新します。このメソッドはすべての
    // 割り当て/セットアップの後に呼び出されるべきです。このメソッドはアノテーションのデータ構造を初期化し、
    // 必要なデータを埋め込みます。
    rma->Update();

    // ページにアノテーションを追加します。
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### Get MultimediaAnnotation

PDFドキュメントからMultimediaAnnotationを取得するために、以下のコードスニペットを使用してください。

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### Delete MultimediaAnnotation

PDFファイルからMultimediaAnnotationを削除する方法を示す以下のコードスニペットを参照してください。

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## 3D注釈を追加

今日、PDFファイルには、単純なテキストやグラフィック以外にも、論理構造や注釈やフォームフィールドなどのインタラクティブな要素、レイヤー、マルチメディア（ビデオコンテンツを含む）、3Dオブジェクトなど、さまざまなコンテンツを含めることができます。

このような3Dコンテンツは、PDFファイル内で3D注釈を使用して表示することができます。

このセクションでは、Aspose.PDFのC++ライブラリを使用してPDFドキュメントに3D注釈を作成する基本的な手順を示します。

3D注釈は、U3Dフォーマットで作成されたモデルを使用して追加されます。

1. 新しい[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)を作成する
1. 目的の3Dモデル（この場合「Ring.u3d」）のデータを読み込み、[PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)を作成する
1. [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/)オブジェクトを作成し、ドキュメントと3DContentにリンクする
1. pdf3dArtWorkオブジェクトを調整する:

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // PDFファイルを読み込む
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //必要に応じてプレビュー画像を設定する
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

このコード例は、このようなモデルを示しました：

![3D Annotation demo](3d_demo.png)

## ウィジェット注釈を追加する

ウィジェット注釈は、インタラクティブなPDFフォーム内のフォームフィールドの外観を表します。

PDF v 1.2以降、ウィジェット注釈を使用できます。これらはインタラクティブなフォーム要素であり、PDFに追加することで、ユーザーが情報を入力、送信、または他のアクションを実行しやすくします。ウィジェットは特別なタイプの注釈ですが、ウィジェット注釈は、特定のページにおけるフォームフィールドのグラフィカルな表現であるため、注釈として直接作成することはできません。

ドキュメントの各場所に対する各フォームフィールドは、一つの注釈ウィジェットを表します。ウィジェットの位置固有の注釈データは、特定のページに追加されます。各フォームフィールドにはいくつかのオプションがあります。ボタンはトグル、チェックボックス、またはボタンにすることができます。選択ウィジェットは、リストボックスまたはコンボボックスにすることができます。

Aspose.PDF for C++は、[Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/)クラスを使用してこの注釈を追加することができます。

ページにボタンを追加するには、次のコードスニペットを使用する必要があります。

### ドキュメントナビゲーションアクションの使用

この例では、4つのボタンを作成する方法を示します：

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"最初のページへ移動", u"前のページへ移動", u"次のページへ移動", u"最後のページへ移動" });
    auto normalCaptions = MakeArray<String>({ u"最初", u"前", u"次", u"最後" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// ページに添付せずにボタンを作成する必要があります。

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// このボタンの配列をドキュメント内の各ページに複製する必要があります。

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### ウィジェット注釈の削除

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // 注釈を削除する
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```