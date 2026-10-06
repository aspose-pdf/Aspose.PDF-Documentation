---
title: "Java での PDF の背景の追加"
linktitle: 背景の追加
type: docs
weight: 20
url: /ja/java/add-backgrounds/
description: Aspose.PDF と `BackgroundArtifact` を使用して、JavaでPDFページに背景画像または背景色を追加する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java で PDF に背景を追加する方法"
Abstract: "このページでは、Java で Aspose.PDF を使用して PDF ページの背景を追加または削除する方法を説明します。背景画像の追加、画像の不透明度の調整、背景色の適用、およびページから背景アーティファクトを削除する方法をカバーしています。"
---
背景アーティファクトを使用すると、論理的なドキュメントテキストを変更せずに、メインページコンテンツの背後に視覚的な要素を配置できます。

## PDF への背景画像の追加

ページに画像を背景アーティファクトとして表示する必要がある場合は、この例を使用してください。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) および画像入力ストリームで開いてください。
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) を作成し、画像ストリームを割り当ててください。
1. アーティファクトを対象ページに追加し、出力 PDF を保存してください。

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

## 不透明度付きの背景画像の追加

この例では、ページのコンテンツの背後に半透明の背景画像を配置します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) および画像ストリームで開いてください。
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) を作成し、画像を割り当て、不透明度を設定してください。
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

## PDF への背景色の追加

ページが画像ではなく単色の背景色を使用する場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) を作成し、背景色を割り当ててください。
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

## 背景のアーティファクトの削除

既存の背景アーティファクトをページから削除する必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページアーティファクトコレクションを逆順に反復処理してください。
1. タイプが pagination でサブタイプが background のアーティファクトを削除し、文書を保存してください。

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
