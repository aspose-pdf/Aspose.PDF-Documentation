---
title: "Java を使用したセキュリティ注釈"
linktitle: "セキュリティ注釈"
type: docs
weight: 75
url: /ja/java/security-annotations/
description: "Aspose.PDF for Java を使用して、PDF 内のテキストを墨消し対象としてマークし、墨消し注釈を適用し、選択したページ領域の墨消しを行う方法を説明します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java でのセキュリティ注釈による機密 PDF コンテンツの墨消し"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメントの墨消し注釈を操作する方法を説明します。一致するテキストを墨消し注釈でマークする方法、墨消しを恒久的に適用する方法、および検出した画像配置の矩形に基づいて選択領域の墨消しを行う方法を示します。"
---
このセクションでは、セキュリティ注釈を使用して機密性の高い PDF コンテンツの墨消しを準備し、適用するワークフローを説明します。

## 墨消し注釈によるテキストのマーク

墨消しを恒久的に適用する前に、一致するテキストを墨消し注釈で覆う必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象テキストを検索し、一致箇所ごとに [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) を作成してください。
1. 墨消し注釈の外観を設定し、ドキュメントを保存してください。

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

## 既存の墨消し注釈の適用

この例では、ページに既に存在する墨消し注釈を恒久的に適用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 型が [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction` の注釈を収集してください。
1. 収集した各注釈で `redact()` を呼び出し、更新したファイルを保存してください。

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

## 選択したページ領域の墨消し

対象コンテンツがテキストの一致ではなく位置で特定される場合に、このアプローチを使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ上の対象矩形を検出してください。たとえば、画像の配置から取得してください。
1. 対象領域に [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) を作成し、ドキュメントを保存してください。

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
