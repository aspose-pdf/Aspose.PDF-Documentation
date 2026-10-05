---
title: "PDF のメディア注釈"
linktitle: メディア注釈
type: docs
weight: 40
url: /ja/java/media-annotations/
description: "Java でサウンド、スクリーン、リッチメディア、3D PDF 注釈 API の操作方法を学び、一般的なマルチメディアワークフローのためのステップバイステップのガイダンスをご提供します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Java におけるメディア関連の PDF 注釈ワークフロー"
Abstract: このページでは、Aspose.PDF for Java における一般的なメディア注釈ワークフロー（サウンド、スクリーン、リッチメディア、3D、削除、検査シナリオ）について説明します。現在のリポジトリには、専用の `workingwithannotations` メディアサンプルクラスが含まれていないため、本稿では Java API パターンを直接、ステップバイステップのガイダンスとして文書化しています。
---
PDF のメディア注釈は、通常、サウンドクリップ、スクリーン再生領域、リッチメディアコンテナ、3D モデルなどの埋め込みまたはリンクされたマルチメディアコンテンツを含みます。

## リッチメディア注釈の追加

PDF ページがカスタムプレーヤー、ポスター画像、スキンを備えた埋め込み動画コンテンツをホストすべき場合に、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/) を作成し、プレーヤー資産、ポスター、およびコンテンツストリームを構成してください。
1. ページに注釈を追加し、出力ドキュメントを保存してください。

```java
public static void richMediaAnnotationsAdd(Path mediaDir, Path outputFile) throws Exception {
    String pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";

    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation richMediaAnnotation = new RichMediaAnnotation(
                page,
                new Rectangle(100, 500, 300, 600, true));

        String playerPath = pathToAdobeApp + "\\Players\\Videoplayer.swf";
        richMediaAnnotation.setCustomPlayer(new FileInputStream(playerPath));
        richMediaAnnotation.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        String skinPath = pathToAdobeApp + "\\" + skinName;
        richMediaAnnotation.addCustomData(skinName, new FileInputStream(skinPath));

        Path posterPath = mediaDir.resolve(posterName);
        richMediaAnnotation.setPoster(new FileInputStream(posterPath.toString()));

        Path videoPath = mediaDir.resolve(videoName);
        try (FileInputStream videoStream = new FileInputStream(videoPath.toString())) {
            richMediaAnnotation.setContent(videoName, videoStream);
        }

        richMediaAnnotation.setType(RichMediaAnnotation.ContentType.Video);
        richMediaAnnotation.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);
        richMediaAnnotation.update();

        page.getAnnotations().add(richMediaAnnotation);
        document.save(outputFile.toString());
    }
}
```

## リッチメディア注釈の削除

この例では、ページから既存のリッチメディア注釈を削除します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 型が [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia` の注釈を収集してください。
1. 収集された注釈を削除し、更新されたドキュメントを保存してください。

```java
public static void richMediaAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.RichMedia) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## マルチメディア注釈の取得

この例を使用して、ページ上に既に存在するスクリーン、サウンド、リッチメディアの注釈を検査します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 検出したいマルチメディア注釈タイプのセットを定義してください。
1. ページの注釈を反復処理し、各一致項目のタイプと矩形を出力してください。

```java
public static void multimediaAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Set<AnnotationType> targetTypes = Set.of(
                AnnotationType.Screen,
                AnnotationType.Sound,
                AnnotationType.RichMedia);

        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (targetTypes.contains(annotation.getAnnotationType())) {
                System.out.println(annotation.getAnnotationType() + " [" + annotation.getRect() + "]");
            }
        }
    }
}
```

## 3Dアノテーションの追加

この例では、事前定義された視点とレンダリングオプションを備えたインタラクティブな3Dモデルビューを追加します。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. モデルを [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) にロードし、[PDF3DArtwork](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/) を構成してください。
1. [PDF3DAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/) を作成し、ページに追加してドキュメントを保存してください。

```java
public static void annotation3dAdd(Path modelFile, Path outputFile) {
    try (Document document = new Document()) {
        PDF3DContent pdf3dContent = new PDF3DContent(modelFile.toString());
        PDF3DArtwork pdf3dArtwork = new PDF3DArtwork(document, pdf3dContent);
        pdf3dArtwork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtwork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        Matrix3D topMatrix = new Matrix3D(
                1, 0, 0,
                0, -1, 0,
                0, 0, -1,
                0.10271, 0.08184, 0.273836);

        Matrix3D frontMatrix = new Matrix3D(
                0, -1, 0,
                0, 0, 1,
                -1, 0, 0,
                0.332652, 0.08184, 0.085273);

        pdf3dArtwork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top"));
        pdf3dArtwork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left"));

        Page page = document.getPages().add();

        PDF3DAnnotation pdf3dAnnotation = new PDF3DAnnotation(
                page,
                new Rectangle(100, 500, 300, 700, true),
                pdf3dArtwork);

        pdf3dAnnotation.setBorder(new com.aspose.pdf.Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName(modelFile.getFileName().toString());

        page.getAnnotations().add(pdf3dAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 画面注釈の追加

ページがスクリーン再生領域を介してメディアファイルを参照する場合は、この例を使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) オブジェクトを、メディアファイルおよび対象矩形用に作成してください。
1. ページに注釈を追加し、ドキュメントを保存してください。

```java
public static void screenAnnotationWithMediaAdd(Path mediaFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ScreenAnnotation screenAnnotation = new ScreenAnnotation(
                page,
                new Rectangle(170, 190, 470, 380, true),
                mediaFile.toString());

        page.getAnnotations().add(screenAnnotation);
        document.save(outputFile.toString());
    }
}
```

## サウンド注釈の追加

この例では、ページにサウンド注釈を配置し、WAV ファイルに関連付けます。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [SoundAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) オブジェクトを、対象のオーディオファイル用に作成し、そのメタデータを設定してください。
1. ページに注釈を追加し、出力ドキュメントを保存してください。

```java
public static void soundAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Path mediaFile = inputFile.getParent().resolve("file_example_WAV_1MG.wav");

        SoundAnnotation soundAnnotation = new SoundAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true),
                mediaFile.toString());

        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Sound Annotation demo");

        soundAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true)));

        page.getAnnotations().add(soundAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 関連する注釈トピック

- [インタラクティブ注釈](/pdf/ja/java/interactive-annotations/)
- [マークアップ注釈](/pdf/ja/java/markup-annotations/)
- [セキュリティ注釈](/pdf/ja/java/security-annotations/)
- [形状注釈](/pdf/ja/java/shape-annotations/)
- [テキストアノテーション](/pdf/ja/java/text-based-annotations/)
- [透かしアノテーション](/pdf/ja/java/watermark-annotations/)
- [注釈のインポートとエクスポート](/pdf/ja/java/import-export-annotations/)
