---
title: Java を使用したセキュリティ アノテーション
linktitle: セキュリティ アノテーション
type: docs
weight: 75
url: /ja/java/security-annotations/
description: Aspose.PDF for Java を使用して、PDF ファイル内のテキストを編集対象としてマークし、編集アノテーションを適用し、選択したページ領域を編集する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java でセキュリティ アノテーションを使用して、機密 PDF コンテンツを編集します。
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントで赤塗り注釈を操作する方法を説明します。マッチしたテキストを赤塗り注釈でマークする方法、赤塗りを永続的に適用する方法、検出された画像配置矩形に基づいて選択領域を赤塗りする方法について概説しています。
---
このセクションのセキュリティ注釈ワークフローは、機密性の高い PDF コンテンツに対して赤塗りを準備し、適用することに重点を置いています。

## テキストを赤塗り注釈でマークする

赤塗りが永続的に適用される前に、マッチするテキストを赤塗り注釈で覆う必要がある場合にこの例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象テキストを検索して作成する [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) 各マッチについて。
1. レダクションの外観を設定し、ドキュメントを保存してください。

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## 既存のリダクションを適用する

この例では、ページに既に存在するリダクション注釈を永続的に適用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイプの注釈を収集する [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. 呼び出し `redact()` 各収集された注釈に対して、更新されたファイルを保存してください。

```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## 選択したページ領域を赤塗りする

対象コンテンツがテキストの一致ではなく位置で特定される場合に、このアプローチを使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ上の対象矩形を検出します。たとえば、画像の配置から取得します。
1. 作成 [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) その領域のために文書を保存してください。

```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## 関連する注釈トピック

- [インタラクティブ注釈](/pdf/ja/java/interactive-annotations/)
- [マークアップ注釈](/pdf/ja/java/markup-annotations/)
- [シェイプ注釈](/pdf/ja/java/shape-annotations/)
- [テキスト注釈](/pdf/ja/java/text-based-annotations/)
- [透かし注釈](/pdf/ja/java/watermark-annotations/)
- [注釈のインポートとエクスポート](/pdf/ja/java/import-export-annotations/)
