---
title: PDFマルチメディア注釈 
linktitle: マルチメディア注釈
type: docs
weight: 40
url: /java/multimedia-annotation/
description: Aspose.PDF for Javaを使用すると、PDFドキュメントからマルチメディア注釈を追加、取得、削除できます。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメント内の注釈は、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)オブジェクトのAnnotationsコレクションに含まれています。このコレクションには、その個々のページのすべての注釈が含まれています。各ページには独自のAnnotationsコレクションがあります。特定のページに注釈を追加するには、そのページのAnnotationsコレクションにAddメソッドを使用して追加します。

PDFドキュメントにSWFファイルを注釈として含めるには、Aspose.PDF.InteractiveFeatures.Annotations名前空間の[ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation)クラスを使用します。
 A screen annotationは、メディアクリップを再生するページの領域を指定します。

PDFドキュメントに外部ビデオリンクを追加する必要がある場合は、[MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation)を使用できます。Movie Annotationは、コンピュータの画面やスピーカーを通じて表示されるアニメーション画像と音声を含みます。

[Sound Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation)は、テキストノートの代わりにコンピュータのマイクから録音された音声やファイルからインポートされた音声を含む点で、テキスト注釈と類似しています。注釈がアクティブになると、音声が再生されます。注釈はほとんどの面でテキスト注釈のように振る舞い、異なるアイコン（デフォルトではスピーカー）を持ち、音声を表していることを示します。

しかし、PDFドキュメント内にメディアを埋め込む必要がある場合は、[RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation)を使用する必要があります。
以下のRichMediaAnnotationクラスのメソッド/プロパティが使用できます。

- Stream CustomPlayer { set; }: ビデオを再生するために使用されるプレイヤーを設定します。
- string CustomFlashVariables { set; }: フラッシュアプリケーションに渡される変数を設定します。この行は「key=value」ペアのセットで、「&」で区切られています。
- void AddCustomData(strig name, Stream data): プレイヤーに追加データを追加します。例えば、source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: プレイヤーをアクティブにするイベント。可能な値はClick、PageOpen、PageVisibleです。
- void SetContent(Stream stream, string name): 再生するビデオ/オーディオデータを設定します。
- void Update(): 注釈のデータ構造を作成します。このメソッドは最後に呼び出す必要があります。
- void SetPoster(Stream): プレイヤーがアクティブでないときに表示される画像、つまりビデオのポスターを設定します。

## 画面注釈を追加する

次のコードスニペットは、PDFファイルに画面注釈を追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // ドキュメントディレクトリへのパス
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // PDFファイルを読み込みます
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // 画面注釈を作成します
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## サウンド注釈を追加

次のコードスニペットは、PDFファイルにサウンド注釈を追加する方法を示しています:

```java
          public static void AddSoundAnnotation() {
        // PDFファイルをロードする
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // サウンド注釈を作成する
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("サウンド注釈デモ");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## リッチメディア注釈を追加

次のコードスニペットは、PDFファイルにリッチメディア注釈を追加する方法を示しています:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // ビデオデータに名前を付ける。このデータはこの名前でドキュメントに埋め込まれ、
        // フラッシュ変数からこの名前で参照されます。
        // videoNameにはファイルへのパスを含めないでください; これはむしろPDFドキュメント内の
        // データにアクセスするための「キー」です。

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // また、ビデオプレイヤーのスキンを使用します
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // ここでビデオプレイヤーのコードを含むストリームを指定する必要があります
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // プレイヤーのためにフラッシュ変数の行を作成します。異なるプレイヤーによっては
        // フラッシュ変数の行の形式が異なるかもしれません。
        // プレイヤーのドキュメントを参照してください。
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // スキンコードを追加します。
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // ビデオのポスターを設定します
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // ビデオコンテンツを設定します
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // コンテンツのタイプを設定します（ビデオ）
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // クリックでプレイヤーをアクティブ化します
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // 注釈データを更新します。このメソッドは全ての
        // 割り当て/設定の後に呼び出される必要があります。このメソッドは注釈のデータ構造を
        // 初期化し、必要なデータを埋め込みます。
        rma.update();

        // ページに注釈を追加します。
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## Get MultimediaAnnotation

PDFドキュメントからMultimediaAnnotationを取得するには、以下のコードスニペットを使用してください。

```java
public static void GetMultimediaAnnotation() {
        // PDFファイルをロード
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }
```

## Delete MultimediaAnnotation

PDFファイルからMultimediaAnnotationを削除する方法を以下のコードスニペットに示します。

```java
    public static void DeletePolyAnnotation() {
        // PDFファイルをロード
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
```


## ウィジェット注釈の追加

インタラクティブなフォームは、フィールドの外観を表現し、ユーザーの操作を管理するために[ウィジェット注釈](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation)を使用します。
PDFに追加されるこれらのフォーム要素を利用して、情報の入力や送信、その他のユーザー操作を容易にします。

ウィジェット注釈は特定のページ上のフォームフィールドのグラフィカルな表現であり、注釈として直接作成することはできません。

各ウィジェット注釈は、そのタイプに応じた適切なグラフィック（外観）を持ちます。作成後、境界スタイルや背景色などの特定の視覚的側面を変更することができます。
テキストの色やフォントなどの他のプロパティは、フィールドに接続された後に変更することができます。

場合によっては、フィールドを複数のページに表示し、同じ値を繰り返すことを望むかもしれません。
 その場合、通常は1つのウィジェットしか持たないフィールドに複数のウィジェットが添付されることがあります。TextField、ListBox、ComboBox、および CheckBox は通常1つしか持たないのに対し、RadioGroup は複数のウィジェットを持ち、それぞれのラジオボタンに1つずつ付いています。
フォームに入力する人は、これらのウィジェットのいずれかを使用してフィールドの値を更新することができ、これは他のすべてのウィジェットにも反映されます。

文書中の各場所に対応する各フォームフィールドは、1つのウィジェット注釈を表します。ウィジェット注釈の場所固有のデータは、特定のページに追加されます。各フォームフィールドにはいくつかのバリエーションがあります。ボタンはラジオボタン、チェックボックス、またはプッシュボタンにすることができます。選択ウィジェットは、リストボックスまたはコンボボックスにすることができます。

このサンプルでは、文書内のナビゲーションのためのプッシュボタンの追加方法を学びます。

## 文書にボタンを追加

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // PDFファイルをロード
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("現在の文書を印刷");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("文書を印刷");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);

        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

このボタンには境界線があり、背景が設定されています。また、ボタン名（Name）、ツールチップ（AlternateName）、ラベル（NormalCaption）、およびラベルテキストの色（Color）を設定します。

## ドキュメントナビゲーションアクションの使用

ウィジェット注釈の使用法のより複雑な例として、PDFドキュメント内のドキュメントナビゲーションがあります。これは、PDFドキュメントのプレゼンテーションを準備する必要がある場合に必要になることがあります。

この例では、4つのボタンを作成する方法を示します:

```java
public static void AddDocumentNavigationActions() {
// PDFファイルをロード
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "最初のページに移動", "前のページに移動", "次のページに移動", "最後のページに移動" };
String[] normalCaptions = { "最初", "前", "次", "最後" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```


## ウィジェット注釈を削除する方法

Aspose.PDF for Java には、ファイルから注釈を削除するためのルールがあります。

```java
public static void DeleteWidgetAnnotation() {
        // PDFファイルをロードする
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // AnnotationSelectorを使用して注釈をフィルタリングする
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // 注釈を削除する
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

PDFドキュメントでは、3D CADまたは3Dモデリングソフトウェアで作成され、PDFドキュメントに埋め込まれた高品質の3Dコンテンツを表示および管理できます。
 3D要素を手に持っているかのように、すべての方向に回転させることができます。

なぜ画像の3D表示が必要なのですか？

ここ数年、3Dプリンティングのおかげで、技術はすべての分野で大きな進歩を遂げました。3Dプリンティング技術は、建設、機械工学、デザインの技術スキルを教えるための主要なツールとして適用できます。これらの技術は、個人用印刷デバイスの出現のおかげで、教育プロセスの新しい形態の導入、動機づけの向上、卒業生および教師の必要な能力の形成に貢献できます。

3Dモデリングの主なタスクは、将来のオブジェクトまたはオブジェクトのアイデアです。なぜなら、オブジェクトをリリースするためには、産業デザインや建築の中で連続再生を行うための設計上の特徴をすべて詳細に理解する必要があるからです。

## 3Dアノテーションを追加

3Dアノテーションは、Aspose.PDF for Javaを使用してU3D形式で作成されたモデルを使用して追加されます。
1. 新しい[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)を作成します。
1. 必要な3Dモデル（この場合は"Ring.u3d"）のデータをロードして、[PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)を作成します。
1. [3dArtWork](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork)オブジェクトを作成し、ドキュメントおよび3DContentにリンクします。
1. pdf3dArtWorkオブジェクトを調整します：

    - 3DLightingScheme - （例では`CAD`を設定します）
    - 3DRenderMode - （例では`Solid`を設定します）
    - `ViewArray`を埋め、少なくとも1つの[3D View](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView)を作成し、配列に追加します。

1. 注釈に3つの基本パラメータを設定します：
    - 注釈が配置される`page`、
    - 注釈が存在する`rectangle`、
    - および`3dArtWork`オブジェクト。
1. 3Dオブジェクトのより良いプレゼンテーションのために、ボーダーフレームを設定します。
1. デフォルトビューを設定します（例 - TOP）。

1. いくつかの追加パラメータを追加します: 名前、プレビューポスターなど。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) に注釈を追加します。
1. 結果を保存します。

## 例

3D注釈を追加するための以下のコードスニペットを確認してください。

```java
    public class Example3DAnnotation
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // PDFファイルを読み込みます
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
    pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
    pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.getPages().add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
    pdf3dAnnotation.setDefaultViewIndex(1);
    pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
    pdf3dAnnotation.setName("Ring.u3d");
    //必要に応じてプレビュー画像を設定します
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}
```


このコード例はそのようなモデルを示しました:

![3D Annotation demo](3d_demo.png)