---
title: JavaでPDFの背景を追加する
linktitle: 背景を追加する
type: docs
weight: 20
url: /ja/java/add-backgrounds/
description: JavaでPDFページに画像および単色の背景を追加し、画像の不透明度を調整する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで背景を追加する
Abstract: JavaでPDFページに画像および単色の背景を追加し、画像の不透明度を調整する。
---
バックグラウンドアーティファクトを使用すると、論理的なドキュメントテキストを変更せずに、メインページコンテンツの背後にコンテンツではない視覚要素を配置できます。

## PDF にバックグラウンド画像を追加する

ページに画像をバックグラウンドアーティファクトとして表示させる場合は、この例を使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開き、画像ストリームを開いてください。
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) オブジェクトを作成し、画像ストリームを設定してください。
1. アーティファクトを対象ページに追加し、出力 PDFを保存してください。

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## 不透明度を設定した背景画像を追加する

この例は、ページコンテンツの背後に半透明の背景画像を配置します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開き、画像ストリームを開いてください。
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) オブジェクトを作成し、画像と不透明度を設定してください。
1. アーティファクトをページに追加し、ドキュメントを保存してください。

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## PDF に背景色を追加する

ページが画像の代わりに単色の背景色を使用すべき場合に、この例を使用してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で元の PDF を開いてください。
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) オブジェクトを作成し、背景色を設定してください。
1. アーティファクトをページに追加し、出力ファイルを保存してください。

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## 関連トピック

- [背景を削除](/pdf/ja/java/remove-backgrounds/)
- [Java で PDF アーティファクトを操作する](/pdf/ja/java/artifacts/)
