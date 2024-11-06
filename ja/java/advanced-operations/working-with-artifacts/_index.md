---
title: アーティファクトの操作 
linktitle: アーティファクトの操作
type: docs
weight: 110
url: ja/java/artifacts/
description: このページでは、Aspose.PDF for Java を使用してアーティファクトクラスを操作する方法について説明します。コードスニペットは、PDF ページに背景画像を追加する方法と、PDF ファイルの最初のページにある各透かしを取得する方法を示しています。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

アーティファクトは、一般的に作成されたコンテンツの一部ではないグラフィックスオブジェクトやその他のマーキングです。PDF のアーティファクトの例には、異なる情報が含まれます。ページのヘッダーやフッター、ページのセクションを分ける線やその他のグラフィックス、装飾的な画像などがあります。

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) クラスには以下が含まれます：

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – アーティファクトのタイプを取得します（Artifact.ArtifactType 列挙の値をサポートし、値には Background, Layout, Page, Pagination, Undefined が含まれます）。
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – アーティファクトのサブタイプを取得します（Background、Footer、Header、Undefined、Watermark を含む Artifact.ArtifactSubtype 列挙の値をサポートします）。

Adobe Acrobat で作成されたウォーターマークはアーティファクトと呼ばれます（PDF 仕様の 14.8.2.2 の Real Content and Artifacts に記載されています）。アーティファクトを操作するために、Aspose.PDF には [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) クラスと [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection) クラスの 2 つがあります。

特定のページ上のすべてのアーティファクトを取得するために、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスには Artifacts プロパティがあります。このトピックでは、PDF ファイル内のアーティファクトを操作する方法を説明します。

次のコードスニペットは、PDF ファイルの最初のページにウォーターマークを設定する方法を示しています。

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


背景画像は、ドキュメントに透かしや他の控えめなデザインを追加するために使用できます。Aspose.PDF for Javaでは、各PDFドキュメントはページのコレクションであり、各ページにはアーティファクトのコレクションが含まれています。[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact)クラスは、ページオブジェクトに背景画像を追加するために使用できます。

次のコードスニペットは、BackgroundArtifactオブジェクトを使用してPDFページに背景画像を追加する方法を示しています。

```java

    public static void SetBackground() throws FileNotFoundException {

        // ドキュメントを開く
        Document pdfDocument = new Document();
                
        // ドキュメントオブジェクトに新しいページを追加
        Page page = pdfDocument.getPages().add();

        // Background Artifactオブジェクトを作成
        BackgroundArtifact background = new BackgroundArtifact();

        // backgroundartifactオブジェクトの画像を指定
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // ページのアーティファクトコレクションにBackgroundArtifactを追加
        page.getArtifacts().add(background);

        // 変更されたPDFを保存
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## プログラミングサンプル: ウォーターマークを取得する

以下のコードスニペットは、PDFファイルの最初のページにある各ウォーターマークを取得する方法を示しています。

```java
    public static void GettingWatermarks() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // アーティファクトのサブタイプ、テキスト、位置を取得して反復処理
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## プログラミングサンプル: 特定のタイプのアーティファクトをカウントする

特定のタイプのアーティファクトの総数を計算するには（例えば、ウォーターマークの総数）、以下のコードを使用します。

```java
    public static void CountingArtifacts() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // アーティファクトのタイプがウォーターマークである場合、カウンターを増やす
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("ページには " + count + " 個のウォーターマークが含まれています");
    }
```